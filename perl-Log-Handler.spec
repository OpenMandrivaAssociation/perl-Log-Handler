%define upstream_name    Log-Handler
%define upstream_version 0.69

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    A simple log file handler
Url:        http://search.cpan.org/dist/%{realname}
Source0:    http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Devel::Backtrace)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(UNIVERSAL::require)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is just a simple object oriented log file handler and very easy to
use.  It's possible to define a log level for your programs and control the
amount of informations that will be logged to the log file. In addition it's
possible to configure how you wish to open the log file - transient or
permanent - and lock and unlock the log file by each write operation. If you
wish you can assign the handler to check the inode of the log file (not on
Windows). That could be very useful if a rotate mechanism moves and zip the log
file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc META.yml ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*


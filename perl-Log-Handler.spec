%define upstream_name    Log-Handler
%define upstream_version 0.78

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.78
Release:	1

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	A simple log file handler
Url:		http://search.cpan.org/dist/%{realname}
Source0:	http://www.cpan.org/modules/by-module/Log/Log-Handler-0.78.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Devel::Backtrace)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc META.yml ChangeLog README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.710.0-2mdv2011.0
+ Revision: 657447
- rebuild for updated spec-helper

* Sat Feb 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.710.0-1
+ Revision: 637369
- update to new version 0.71

* Sat Jan 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.700.0-1mdv2011.0
+ Revision: 630622
- update to new version 0.70

* Sat Dec 18 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.690.0-1mdv2011.0
+ Revision: 622844
- update to new version 0.69

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.680.0-1mdv2011.0
+ Revision: 601900
- update to new version 0.68

* Sat Nov 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.670.0-1mdv2011.0
+ Revision: 597075
- new version

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.650.0-1mdv2011.0
+ Revision: 569938
- update to 0.65

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 0.640.0-1mdv2011.0
+ Revision: 498979
- update to 0.64

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.630.0-1mdv2010.1
+ Revision: 470465
- update to 0.63

* Sat Nov 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.620.0-1mdv2010.1
+ Revision: 462130
- update to 0.62

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.600.0-1mdv2010.1
+ Revision: 461324
- update to 0.60

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.560.0-1mdv2010.0
+ Revision: 392896
- update to 0.56

* Thu May 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.540.0-1mdv2010.0
+ Revision: 380350
- update to 0.54
- using %%perl_convert_version
- fixed license

* Mon May 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.52-1mdv2010.0
+ Revision: 379519
- update to new version 0.52

* Sun Mar 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.51-1mdv2009.1
+ Revision: 352844
- update to new version 0.51

* Fri Nov 28 2008 Jérôme Quelin <jquelin@mandriva.org> 0.50-1mdv2009.1
+ Revision: 307363
- update to new version 0.50

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.49-1mdv2009.1
+ Revision: 305736
- update to new version 0.49

* Fri Oct 31 2008 Jérôme Quelin <jquelin@mandriva.org> 0.48-1mdv2009.1
+ Revision: 298867
- update to new version 0.48

* Fri Sep 05 2008 Jérôme Quelin <jquelin@mandriva.org> 0.47-1mdv2009.0
+ Revision: 281096
- update to new version 0.47

* Tue Jul 29 2008 Jérôme Quelin <jquelin@mandriva.org> 0.46-1mdv2009.0
+ Revision: 252492
- update to new version 0.46

* Thu Jun 05 2008 Jérôme Quelin <jquelin@mandriva.org> 0.44-1mdv2009.0
+ Revision: 215753
- update to new version 0.44

* Thu May 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.43-1mdv2009.0
+ Revision: 209989
- update to new version 0.43

* Sat May 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.41-1mdv2009.0
+ Revision: 205402
- update to new version 0.41

* Tue May 06 2008 Jérôme Quelin <jquelin@mandriva.org> 0.40-1mdv2009.0
+ Revision: 201834
- adding missing prereq
- update to new version 0.40

* Mon May 05 2008 Jérôme Quelin <jquelin@mandriva.org> 0.38-2mdv2009.0
+ Revision: 201387
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long

* Wed Feb 06 2008 Jérôme Quelin <jquelin@mandriva.org> 0.38-1mdv2008.1
+ Revision: 163048
- import perl-Log-Handler




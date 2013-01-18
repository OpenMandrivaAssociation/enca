%define major 		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	A program that can detect and convert between character sets
Name:		enca
Version:	1.14
Release:	1
License:	GPLv2+
Group:		Text tools
Source0:	http://dl.cihar.com/%{name}/%{name}-%{version}.tar.gz
URL:		http://gitorious.org/enca
BuildRequires:	recode-devel

%description
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings using
either a built-in converter or external libraries and tools like libiconv,
librecode, or cstocs.

Currently, it has support for Belarussian, Bulgarian, Croatian, Czech,
Estonian, Latvian, Lithuanian, Polish, Russian, Slovak, Slovene, and
Ukrainian and some multibyte encodings (mostly variants of Unicode)
independently on the language.

Install Enca if you need to cope with text files of dubious origin
and unknown encoding and convert them to some reasonable encoding.

%package -n %{libname}
Summary:	A library detecting encoding of text files
Group:		System/Libraries

%description -n %{libname}
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings using
either a built-in converter or external libraries and tools like libiconv,
librecode, or cstocs.

Currently, it has support for Belarussian, Bulgarian, Croatian, Czech,
Estonian, Latvian, Lithuanian, Polish, Russian, Slovak, Slovene, and
Ukrainian and some multibyte encodings (mostly variants of Unicode)
independently on the language.

This package contains shared Enca library other programs can make use of.

%package -n %{develname}
Summary:	Header files and libraries for Enca development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libenca-devel = %{version}-%{release}
Provides:	enca-devel = %{version}-%{release}

%description -n %{develname}
This package contains the static libraries and header files for writing
programs using the Extremely Naive Charset Analyser library, and its API
documentation.

Install it if you are going to create applications using the Enca library.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall HTML_DIR=%{buildroot}%{_datadir}/gtk-doc/html

%files
%doc AUTHORS ChangeLog ChangeLog.prelib FAQ README README.devel THANKS TODO
%{_bindir}/enca
%{_bindir}/enconv
%{_libexecdir}/%{name}/extconv/*
%dir %{_libexecdir}/%{name}/extconv
%dir %{_libexecdir}/%{name}
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libenca.so.%{major}*

%files -n %{develname}
%{_includedir}/enca.h
%{_libdir}/pkgconfig/enca.pc
%{_libdir}/libenca.so
%doc %{_datadir}/gtk-doc/html/libenca/*
%doc %dir %{_datadir}/gtk-doc/html/libenca

%changelog
* Mon Jun 20 2011 Oden Eriksson <oeriksson@mandriva.com> 1.13-4mdv2011.0
+ Revision: 686309
- avoid pulling 32 bit libraries on 64 bit arch

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.13-3
+ Revision: 664145
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.13-2mdv2011.0
+ Revision: 605103
- rebuild

* Wed Feb 10 2010 Götz Waschk <waschk@mandriva.org> 1.13-1mdv2010.1
+ Revision: 503769
- update to new version 1.13

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 1.12-1mdv2010.1
+ Revision: 460847
- update to new version 1.12

* Fri Sep 25 2009 Frederik Himpe <fhimpe@mandriva.org> 1.11-1mdv2010.0
+ Revision: 449201
- update to new version 1.11

* Tue Aug 25 2009 Frederik Himpe <fhimpe@mandriva.org> 1.10-1mdv2010.0
+ Revision: 421243
- Update to new version 1.10

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.9-7mdv2009.0
+ Revision: 220724
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.9-6mdv2008.1
+ Revision: 149697
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 1.9-5mdv2008.0
+ Revision: 90163
- rebuild for 2008
- man pages aren't docs
- drop ancient conditionals
- new devel policy
- new license policy
- spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - s/Mandrake/Mandriva/


* Sun Jan 28 2007 Götz Waschk <waschk@mandriva.org> 1.9-4mdv2007.0
+ Revision: 114690
- Import enca

* Sun Jan 28 2007 Götz Waschk <waschk@mandriva.org> 1.9-4mdv2007.1
- Rebuild

* Mon May 15 2006 Stefan van der Eijk <stefan@eijk.nu> 1.9-3mdk
- rebuild for sparc

* Wed Feb 01 2006 Eskild Hustvedt <eskild@mandriva.org> 1.9-2mdk
- Rebuild for missing package
- Made the spec prettier

* Mon Dec 19 2005 Götz Waschk <waschk@mandriva.org> 1.9-1mdk
- New release 1.9
- use mkrel

* Fri Nov 25 2005 Götz Waschk <waschk@mandriva.org> 1.8-1mdk
- New release 1.8

* Wed Mar 02 2005 G�tz Waschk <waschk@linux-mandrake.com> 1.7-1mdk
- New release 1.7

* Thu Aug 05 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.5-2mdk
- rebuild to fix missing source package

* Tue Jul 27 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.5-1mdk
- initial mdk package

* Tue May 18 2004 David Necas (Yeti) <yeti@physics.muni.cz>
- doubled percents in changelog


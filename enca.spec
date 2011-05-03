%define name 		enca
%define major 		0
%define	libname		%mklibname %name %major
%define develname	%mklibname %name -d

Summary:		A program that can detect and convert between character sets
Name: 			enca
Version: 		1.13
Release: 		%mkrel 3
License: 		GPLv2+
Group: 			Text tools
Source: 		http://dl.cihar.com/%{name}/%{name}-%{version}.tar.lzma
URL: 			http://gitorious.org/enca
BuildRoot: 		%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: 		recode-devel

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

%package -n %libname
Summary: A library detecting encoding of text files
Group: System/Libraries

%description -n %libname
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings using
either a built-in converter or external libraries and tools like libiconv,
librecode, or cstocs.

Currently, it has support for Belarussian, Bulgarian, Croatian, Czech,
Estonian, Latvian, Lithuanian, Polish, Russian, Slovak, Slovene, and
Ukrainian and some multibyte encodings (mostly variants of Unicode)
independently on the language.

This package contains shared Enca library other programs can make use of.


%package -n %develname
Summary: Header files and libraries for Enca development
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: libenca-devel = %{version}-%{release}
Provides: enca-devel = %{version}-%{release}
Obsoletes: %{mklibname enca 0 -d}

%description -n %develname
The %develname package contains the static libraries and header files
for writing programs using the Extremely Naive Charset Analyser library,
and its API documentation.

Install %develname if you are going to create applications using the Enca
library.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall HTML_DIR=$RPM_BUILD_ROOT/%{_datadir}/gtk-doc/html

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root)
%doc AUTHORS ChangeLog ChangeLog.prelib FAQ README README.devel THANKS TODO
%{_bindir}/enca
%{_bindir}/enconv
%{_libexecdir}/%{name}/extconv/*
%dir %{_libexecdir}/%{name}/extconv
%dir %{_libexecdir}/%{name}
%{_mandir}/man1/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libenca.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_includedir}/enca.h
%{_libdir}/pkgconfig/enca.pc
%{_libdir}/libenca.a
%{_libdir}/libenca.la
%{_libdir}/libenca.so
%doc %{_datadir}/gtk-doc/html/libenca/*
%doc %dir %{_datadir}/gtk-doc/html/libenca


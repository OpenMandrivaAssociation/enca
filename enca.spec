%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Summary:	A program that can detect and convert between character sets
Name:		enca
Version:	1.14
Release:	9
License:	GPLv2+
Group:		Text tools
Url:		http://gitorious.org/enca
Source0:	http://dl.cihar.com/%{name}/%{name}-%{version}.tar.gz
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
This package contains shared Enca library other programs can make use of.

%package -n %{devname}
Summary:	Header files and libraries for Enca development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development libraries and header files for writing
programs using the Extremely Naive Charset Analyser library, and its API
documentation.

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

%files -n %{devname}
%{_includedir}/enca.h
%{_libdir}/pkgconfig/enca.pc
%{_libdir}/libenca.so
%doc %{_datadir}/gtk-doc/html/libenca/*
%doc %dir %{_datadir}/gtk-doc/html/libenca


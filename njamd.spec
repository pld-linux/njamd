Summary:	A debugger which detects memory allocation violations.
Name:		njamd
Version:	0.8.1
Release:	2
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://prdownloads.sourceforge.net/njamd/%{name}-%{version}.tar.gz
Patch0:		%{name}-ia64.patch
Patch1:		%{name}-0.8.0-nogui.patch
Patch2:		%{name}-0.8.1-64.patch
URL:		http://sourceforge.net/projects/njamd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NJAMD is a malloc debugger which protects against all common dynamic
memory bugs (including overflow, underflow, writes to freed memory,
and memory leaks) without recompiling or even relinking your
executable. NJAMD is able to trace memory leaks even through arbitrary
library functions that wrap malloc(3), such as strdup(3), GUI widget
allocators, and even C++ new and delete.

NJAMD is fast enough for everyday use, and light enough to debug most
applications. Large applications will require more RAM for comfortable
debugging.

%prep
%setup -q
%ifarch ia64
%patch0 -p1 -b .ia64
autoconf
%endif
%patch1 -p1 -b .nogui
%patch2 -p1 -b .64
%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS NOTES README TODO 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_libdir}/*

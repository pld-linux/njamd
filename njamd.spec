Summary:	A debugger which detects memory allocation violations
Summary(pl):	Odpluskwiacz wykrywaj±cy naruszenia alokacji pamiêci
Name:		njamd
Version:	0.8.1
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://prdownloads.sourceforge.net/njamd/%{name}-%{version}.tar.gz
Patch0:		%{name}-ia64.patch
Patch1:		%{name}-0.8.0-nogui.patch
Patch2:		%{name}-0.8.1-64.patch
URL:		http://sourceforge.net/projects/njamd
%ifarch ia64
BuildRequires:	autoconf
%endif
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

%description -l pl
NJAMD jest debuggerem malloca, zabezpieczaj±cym przed wszystkimi
popularnymi b³êdami zwi±zanymi ze zmiennymi dynamicznymi
(przekroczenie zakresu w górê i w dó³, zapisy do zwolnionej pamiêci,
wycieki pamiêci) bez rekompilacji ani nawet relinkowania binarki.
NAJMD mo¿e ¶ledziæ wycieki pamiêci nawet przez dowolne funkcje
biblioteczne u¿ywaj±ce malloc(3), takie jak strdup(3), alokacje
widgetów GUI, a tak¿e new i delete z C++.

NAJMD jest wystarczaj±co szybki do codziennego u¿ytku i wystarczaj±co
lekki by ¶ledziæ wiêkszo¶æ aplikacji. Du¿e aplikacje bêd± potrzebowa³y
wiêcej RAM-u do wygodnego odpluskwiania.

%prep
%setup -q
%ifarch ia64
%patch0 -p1
autoconf
%endif
%patch1 -p1
%patch2 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf %{buildroot}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS NOTES README TODO 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_libdir}/*

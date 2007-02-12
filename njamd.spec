Summary:	A debugger which detects memory allocation violations
Summary(pl.UTF-8):   Odpluskwiacz wykrywający naruszenia alokacji pamięci
Name:		njamd
Version:	0.8.1
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/njamd/%{name}-%{version}.tar.gz
# Source0-md5:	16b934472154fecc2dcc75089dcbc2fa
Patch0:		%{name}-ia64.patch
Patch1:		%{name}-0.8.0-nogui.patch
Patch2:		%{name}-0.8.1-64.patch
URL:		http://sourceforge.net/projects/njamd/
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

%description -l pl.UTF-8
NJAMD jest debuggerem malloca, zabezpieczającym przed wszystkimi
popularnymi błędami związanymi ze zmiennymi dynamicznymi
(przekroczenie zakresu w górę i w dół, zapisy do zwolnionej pamięci,
wycieki pamięci) bez rekompilacji ani nawet ponownej konsolidacji
binarki. NAJMD może śledzić wycieki pamięci nawet przez dowolne
funkcje biblioteczne używające malloc(3), takie jak strdup(3),
alokacje widgetów GUI, a także new i delete z C++.

NAJMD jest wystarczająco szybki do codziennego użytku i wystarczająco
lekki by śledzić większość aplikacji. Duże aplikacje będą potrzebowały
więcej RAM-u do wygodnego odpluskwiania.

%prep
%setup -q
%ifarch ia64
%patch0 -p1
%{__autoconf}
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
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS NOTES README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_libdir}/*

Summary: A debugger which detects memory allocation violations.
Name: njamd
Version: 0.8.1
Release: 2
License: GPL
Group: Development/Tools
Source: http://prdownloads.sourceforge.net/njamd/%{name}-%{version}.tar.gz
Patch0: njamd-ia64.patch
Patch1: njamd-0.8.0-nogui.patch
Patch2: njamd-0.8.1-64.patch
URL: http://sourceforge.net/projects/njamd
BuildRoot: %{_tmppath}/%{name}-root

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
%makeinstall

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS NOTES README TODO 
/usr/bin/*
%{_mandir}/man1/*
%{_mandir}/man3/*
/usr/lib/*

%changelog
* Thu Aug 16 2001 Bill Nottingham <notting@redhat.com>
- print 64-bit address pointers on 64 bit platforms
- don't warn about freeing null pointers

* Mon Jun 25 2001 Preston Brown <pbrown@redhat.com>
- 0.8.1 stable release

* Thu Feb  1 2001 Preston Brown <pbrown@redhat.com>
- removed tests from documentation bundle; they don't belong here (#15834)

* Wed Jan 31 2001 Preston Brown <pbrown@redhat.com>
- there is no gui mode yet; fix command line option list (#12453)

* Mon Dec 11 2000 Preston Brown <pbrown@redhat.com>
- 0.8.0

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun  2 2000 Bill Nottingham <notting@redhat.com>
- hardcode alignment on ia64

* Wed May 24 2000 Preston Brown <pbrown@redhat.com>
- initial package, to replace ElectricFence.

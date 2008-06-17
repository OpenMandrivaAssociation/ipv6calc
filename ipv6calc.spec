%define name ipv6calc
%define version 0.71.0
%define release %mkrel 5

Summary: Utility to manipulate IPv6 addresses
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0:	 ipv6calc-0.70.0-getopt.patch
License: GPL
Group: System/Base
Url: http://www.deepspace6.net/projects/ipv6calc.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ipv6calc is a small but powerful utility written in the C programming
language to manipulate (not only) IPv6 addresses. ipv6calc allows the
users to convert a given IPv6 address to the compressed format or to
the format used by /proc/net/if_inet6. ipv6calc is also the
replacement of the old ip6_int Perl program.

%prep
%setup -q
%patch0 -p1 -b .getopt

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%make installonly root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CREDITS README TODO USAGE doc/ipv6calc.html
%{_bindir}/ipv6*
%{_mandir}/man8/*.8*

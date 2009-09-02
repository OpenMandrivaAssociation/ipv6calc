Summary:	Utility to manipulate IPv6 addresses
Name:		ipv6calc
Version:	0.72.0
Release:	%mkrel 2
License:	GPLv2
Group:		System/Base
URL:		http://www.deepspace6.net/projects/ipv6calc.html
Source0:	ftp://ftp.bieringer.de/pub/linux/IPv6/ipv6calc/%{name}-%{version}.tar.gz
Patch0:		ipv6calc-0.70.0-getopt.patch
Patch1:		ipv6calc-0.72.0-optflags.diff
Patch2:		ipv6calc-0.72.0-format_not_a_string_literal_and_no_format_arguments.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ipv6calc is a small but powerful utility written in the C programming language
to manipulate (not only) IPv6 addresses. ipv6calc allows the users to convert a
given IPv6 address to the compressed format or to the format used by
/proc/net/if_inet6. ipv6calc is also the replacement of the old ip6_int Perl
program.

%prep

%setup -q
%patch0 -p1 -b .getopt
%patch1 -p1 -b .optflags
%patch2 -p1 -b .format_not_a_string_literal_and_no_format_arguments

%build
%configure2_5x

make RPM_OPT_FLAGS="%{optflags}"

%install
rm -rf %{buildroot}

%make install root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CREDITS README TODO USAGE doc/ipv6calc.html
%{_bindir}/ipv6*
%{_mandir}/man8/*.8*

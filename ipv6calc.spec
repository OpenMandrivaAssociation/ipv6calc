%define _disable_ld_no_undefined 1
%define _disable_lto 1

Summary:	Utility to manipulate IPv6 addresses
Name:		ipv6calc
Version:	4.1.0
Release:	1
License:	GPLv2
Group:		System/Base
URL:		https://www.deepspace6.net/projects/ipv6calc.html
Source0:	ftp://ftp.bieringer.de/pub/linux/IPv6/ipv6calc/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.bieringer.de/pub/linux/IPv6/ipv6calc/%{name}-%{version}.tar.gz.asc
BuildRequires:	wget
# BuildRequires:	aggregate
BuildRequires:	GeoIP-devel
BuildRequires:	perl-XML-Simple
#BuildRequires:	ip2location-devel ?
Requires:	geoip

%description
ipv6calc is a small but powerful utility written in the C programming language
to manipulate (not only) IPv6 addresses. ipv6calc allows the users to convert a
given IPv6 address to the compressed format or to the format used by
/proc/net/if_inet6. ipv6calc is also the replacement of the old ip6_int Perl
program.

%prep

%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition 
export CFLAGS=-Wno-error

%configure2_5x \
	--enable-geoip \
	--with-geoip-ipv4-default-file=%{_datadir}/GeoIP/GeoIP.dat

%make

%install
%makeinstall_std

## Install examples and helper files to temporary dir
## to be tagged as docs
mkdir -p installed-docs

# ipv6logconv
mkdir -p installed-docs/ipv6logconv
cp -r examples/analog/* installed-docs/ipv6logconv

# ipv6loganon
mkdir -p installed-docs/ipv6loganon
cp ipv6loganon/README installed-docs/ipv6loganon/

# ipv6logstats
mkdir -p installed-docs/ipv6logstats
cp ipv6logstats/example_* ipv6logstats/collect_ipv6logstats.pl README installed-docs/ipv6logstats/
cp -r ipv6logstats/examples-data ipv6logstats/examples-gri installed-docs/ipv6logstats/

# ipv6calcweb
mkdir -p installed-docs/ipv6calcweb
cp ipv6calcweb/USAGE ipv6calcweb/ipv6calcweb.cgi installed-docs/ipv6calcweb

%check
#make test

%files
%doc CREDITS README TODO USAGE doc/ipv6calc.html installed-docs/*
%{_bindir}/ipv6*
%{_mandir}/man8/*.8*
%{_datadir}/ipv6calc

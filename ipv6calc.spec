Summary:	Utility to manipulate IPv6 addresses
Name:		ipv6calc
Version:	0.82.1
Release:	%mkrel 2
License:	GPLv2
Group:		System/Base
URL:		http://www.deepspace6.net/projects/ipv6calc.html
Source0:	ftp://ftp.bieringer.de/pub/linux/IPv6/ipv6calc/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.bieringer.de/pub/linux/IPv6/ipv6calc/%{name}-%{version}.tar.gz.asc
Patch0:		ipv6calc-0.72.0-fix-str-fmt.patch
#BuildRequires:	ip2location-devel ?
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ipv6calc is a small but powerful utility written in the C programming language
to manipulate (not only) IPv6 addresses. ipv6calc allows the users to convert a
given IPv6 address to the compressed format or to the format used by
/proc/net/if_inet6. ipv6calc is also the replacement of the old ip6_int Perl
program.

%prep

%setup -q
%patch0 -p1 -b .format_not_a_string_literal_and_no_format_arguments

%build
%configure2_5x
make RPM_OPT_FLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CREDITS README TODO USAGE doc/ipv6calc.html
%{_bindir}/ipv6*
%{_mandir}/man8/*.8*


%changelog
* Sun May 15 2011 Oden Eriksson <oeriksson@mandriva.com> 0.82.1-1mdv2011.0
+ Revision: 674883
- 0.82.1

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-2
+ Revision: 665521
- mass rebuild

* Sun Jan 23 2011 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-1
+ Revision: 632426
- add the sig file...
- package the correct sig file
- 0.80.0

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.73.0-2mdv2011.0
+ Revision: 605981
- rebuild

* Sun Mar 07 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.73.0-1mdv2010.1
+ Revision: 515307
- drop old patches applied upstream
- use %%makeinstall
- update to 0.73
- rediff patch

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.72.0-2mdv2010.0
+ Revision: 425375
- rebuild

* Fri Dec 19 2008 Oden Eriksson <oeriksson@mandriva.com> 0.72.0-1mdv2009.1
+ Revision: 316240
- 0.72.0
- really make it use %%optflags
- fix build with -Werror=format-security

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.71.0-5mdv2009.0
+ Revision: 221641
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.71.0-4mdv2008.1
+ Revision: 150321
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.71.0-3mdv2008.0
+ Revision: 81031
- bump release

* Thu Aug 23 2007 Olivier Blin <oblin@mandriva.com> 0.71.0-2mdv2008.0
+ Revision: 69316
+ rebuild (emptylog)

* Thu Aug 02 2007 Olivier Blin <oblin@mandriva.com> 0.71.0-1mdv2008.0
+ Revision: 58038
- 0.71.0

* Fri Apr 20 2007 Olivier Blin <oblin@mandriva.com> 0.70.0-2mdv2008.0
+ Revision: 16227
- add html doc

* Fri Apr 20 2007 Olivier Blin <oblin@mandriva.com> 0.70.0-1mdv2008.0
+ Revision: 16198
- initial Mandriva release (an obsolete copy was previously bundled in iputils)
- Create ipv6calc


Name:           arp-scan
Version:        1.10.0
Release:        1%{?dist}
Summary:        Scanning and fingerprinting tool

# Includes getopt, which is LGPLv2+, but the whole is GPLv2+.
License:        GPLv2+
Source0:        https://github.com/royhills/arp-scan/releases/download/%{version}/%{name}-%{version}.tar.gz
# source code moved to github at https://github.com/royhills/arp-scan
BuildRequires:  libpcap-devel
# BuildRequires:  libcap-devel  #uncomment to enable POSIX.1e support
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  automake autoconf
BuildRequires:  make
Requires:       perl(LWP::Simple)
Requires:       libpcap
# Requires:       libcap  #uncomment to enable POSIX.1e support


%description
arp-scan is a command-line tool that uses the ARP protocol to discover and
fingerprint IP hosts on the local network.

%global debug_package %{nil}

%prep
%setup -q

%build
autoreconf --install
#install to sbindir
%configure --bindir=%{_sbindir}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS ChangeLog COPYING README TODO 
%{_sbindir}/*
%config(noreplace,missingok) %{_sysconfdir}/arp-scan
%{_datadir}/arp-scan
%{_mandir}/man?/*

%post
setcap cap_net_raw=ep %{_sbindir}/arp-scan


%changelog
* Sat Dec 17 2022 sonikbhoom <sonik.bhoom@bell.net> - 1.10.0
- updated spec build with arp-scan-1.10.0 RC1

* Thu Dec 15 2022 sonikbhoom <sonik.bhoom@bell.net> - 1.10.0
- initial spec build with arp-scan-1.10.0 RC1

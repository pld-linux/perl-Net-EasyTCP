#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	EasyTCP
Summary:	Net::EasyTCP Perl module - easily create TCP/IP clients and servers
Summary(pl):	Modu³ Perla Net::EasyTCP - pomocny przy tworzeniu klientów i serwerów TCP/IP
Name:		perl-Net-EasyTCP
Version:	0.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	c8ff3f221bcdb358ed9dfa8c6b098b35
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Storable
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::EasyTCP Perl module - easily create TCP/IP clients and servers.
Features:
- one easy module to create both clients and servers
- Object Oriented interface
- event-based callbacks in server mode
- internal protocol to take care of all the common transport problems
- transparent encryption
- transparent compression.

%description -l pl
Modu³ Perla Net::EasyTCP - pomocny przy tworzeniu klientów i serwerów
TCP/IP. Cechy:
- jeden ³atwy w u¿yciu modu³ do tworzenia klientów i serwerów
- obiektowo zorientowany interfejs
- funkcje callback sterowane zdarzeniami w trybie serwera
- wewnêtrzny protokó³ rozwi±zuj±cy g³ówne problemy z transportem
- prze¼roczyste szyfrowanie
- prze¼roczysta kompresja.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Net/EasyTCP.pm
#%dir %{perl_vendorlib}/auto/Net/EasyTCP
#%{perl_vendorlib}/auto/Net/EasyTCP/autosplit.ix
#%{perl_vendorlib}/auto/Net/EasyTCP/*.al
%{_mandir}/man3/*

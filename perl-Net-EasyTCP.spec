#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	EasyTCP
Summary:	Net::EasyTCP Perl module - easily create TCP/IP clients and servers
Summary(pl):	Modu� Perla Net::EasyTCP - pomocny przy tworzeniu klient�w i serwer�w TCP/IP
Name:		perl-Net-EasyTCP
Version:	0.19
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Storable
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
Modu� Perla Net::EasyTCP - pomocny przy tworzeniu klient�w i serwer�w
TCP/IP. Cechy:
- jeden �atwy w u�yciu modu� do tworzenia klient�w i serwer�w
- obiektowo zorientowany interfejs
- funkcje callback sterowane zdarzeniami w trybie serwera
- wewn�trzny protok� rozwi�zuj�cy g��wne problemy z transportem
- prze�roczyste szyfrowanie
- prze�roczysta kompresja.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Net/EasyTCP.pm
%dir %{perl_sitelib}/auto/Net/EasyTCP
%{perl_sitelib}/auto/Net/EasyTCP/autosplit.ix
%{perl_sitelib}/auto/Net/EasyTCP/*.al
%{_mandir}/man3/*

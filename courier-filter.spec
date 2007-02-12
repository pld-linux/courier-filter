%include	/usr/lib/rpm/macros.perl
Summary:	Purely Perl-based mail filter framework for the Courier
Summary(pl.UTF-8):   Oparty na czystym Perlu szkielet filtra pocztowego dla Couriera
Name:		courier-filter
Version:	0.16
Release:	0.1
License:	GPL and Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JM/JMEHNLE/courier-filter/Courier-Filter-%{version}.tar.gz
# Source0-md5:	de6c5d645f2b6e56c0fd15e0ec6b005f
URL:		http://search.cpan.org/dist/Courier-Filter/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	courier
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Courier::Filter implements the courierfilter interface as a framework
for mail filter modules that frees modules from the duties of creating
and handling the UNIX domain sockets, waiting for connections from
Courier, and reading and parsing message and control files.

%description -l pl.UTF-8
Courier::Filter implementuje interfejs courierfilter jako szkielet dla
modułów filtrujących pocztę uwalniający moduły od konieczności
tworzenia i obsługi gniazd uniksowych, oczekiwania na połączenia z
Couriera oraz czytania i przetwarzania wiadomości i plików
kontrolnych.

%prep
%setup -q -n Courier-Filter-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

./Build	install \
	destdir=$RPM_BUILD_ROOT

install bin/pureperlfilter $RPM_BUILD_ROOT%{_bindir}/pureperlfilter
install -d $RPM_BUILD_ROOT%{_sysconfdir}/courier/filters
install examples/pureperlfilter.conf $RPM_BUILD_ROOT%{_sysconfdir}/courier/filters

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/pureperlfilter
%attr(755,root,root) %{_bindir}/test-filter-module
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/courier/filters/*
%{_datadir}/courier-filter-perl
%{_mandir}/man1/*
%{_mandir}/man3/*

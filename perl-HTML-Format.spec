%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Format
Summary:	HTML::Formatter - Base class for HTML formatters
Summary(pl):	HTML::Formatter - bazowa klasa dla klas formatuj±cych HTML
Name:		perl-HTML-Format
Version:	2.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl-Font-AFM
# do not change to BuildRequires
Requires:	perl-HTML-Tree >= 3.15
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML formatters are able to format a HTML syntax tree into various
printable formats.  Different formatters produce output for different
output media.  Common for all formatters are that they will return the
formatted output when the format() method is called.  Format() takes a
HTML::Element as parameter.

%description -l pl
Klasy formatuj±ce HTML mog± sformatowaæ drzewo sk³adni HTML do ró¿nych
drukowalnych formatów. Ró¿ne klasy formatuj±ce daj± wyj¶cie dla
ró¿nych mediów. Wspólne dla wszystkich klas formatuj±cych jest to, ¿e
zwracaj± sformatowane wyj¶cie po wywo³aniu metody format(). format()
przyjmuje HTML::Element jako parametr.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/HTML/*.pm
%{_mandir}/man3/*

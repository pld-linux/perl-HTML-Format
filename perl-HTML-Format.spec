%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Format
Summary:	HTML::Formatter - base class for HTML formatters
Summary(pl):	HTML::Formatter - bazowa klasa dla klas formatuj±cych HTML
Name:		perl-HTML-Format
Version:	2.03
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2d12c10f26ea44a3b17709d4671b8e5
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Font-AFM
# do not change to BuildRequires
Requires:	perl-HTML-Tree >= 3.15
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(UNIVERSAL)'

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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/*.pm
%{_mandir}/man3/*

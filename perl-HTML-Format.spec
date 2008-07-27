#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Format
Summary:	HTML::Formatter - base class for HTML formatters
Summary(pl.UTF-8):	HTML::Formatter - bazowa klasa dla klas formatujących HTML
Name:		perl-HTML-Format
Version:	2.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2d287392b77c959f06397371116c2d7e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Font-AFM
BuildRequires:	perl-HTML-Element-Extended
%endif
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

%description -l pl.UTF-8
Klasy formatujące HTML mogą sformatować drzewo składni HTML do różnych
drukowalnych formatów. Różne klasy formatujące dają wyjście dla
różnych mediów. Wspólne dla wszystkich klas formatujących jest to, że
zwracają sformatowane wyjście po wywołaniu metody format(). format()
przyjmuje HTML::Element jako parametr.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%{perl_vendorlib}/HTML/*.pm
%{_mandir}/man3/*

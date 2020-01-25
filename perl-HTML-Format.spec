#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	Format
Summary:	HTML::Formatter - base class for HTML formatters
Summary(pl.UTF-8):	HTML::Formatter - bazowa klasa dla klas formatujących HTML
Name:		perl-HTML-Format
Version:	2.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	34831ec506eaa8a7ad5da698224cf58d
URL:		http://search.cpan.org/dist/HTML-Format/
BuildRequires:	perl-Module-Build >= 0.3601
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-Font-AFM
BuildRequires:	perl-HTML-Element-Extended
BuildRequires:	perl-HTML-Tree >= 3.15
BuildRequires:	perl-Test-Simple >= 0.96
%endif
Requires:	perl-Font-AFM
Requires:	perl-HTML-Tree >= 3.15
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
HTML formatters are able to format a HTML syntax tree into various
printable formats. Different formatters produce output for different
output media. Common for all formatters are that they will return the
formatted output when the format() method is called. Format() takes a
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
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/Format*.pm
%{_mandir}/man3/HTML::Format*.3pm*

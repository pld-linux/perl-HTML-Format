%include	/usr/lib/rpm/macros.perl
Summary:	HTML-Format perl module
Summary(pl):	Modu³ perla HTML-Format
Name:		perl-HTML-Format
Version:	1.23
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Format-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Font-AFM
BuildRequires:	perl >= 5.6
# do not change to BuildRequires
Requires:	perl-HTML-Tree >= 0.62
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-Format perl module.

%description -l pl
Modu³ perla HTML-Format.

%prep
%setup -q -n HTML-Format-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTML/FormatPS.pm
%{perl_sitelib}/HTML/FormatText.pm
%{perl_sitelib}/HTML/Formatter.pm
%{_mandir}/man3/*

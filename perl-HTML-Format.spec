%include	/usr/lib/rpm/macros.perl
Summary:	HTML-Format perl module
Summary(pl):	Modu� perla HTML-Format
Name:		perl-HTML-Format
Version:	1.23
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Format-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Font-AFM
BuildRequires:	perl-HTML-Tree >= 0.62
%requires_eq	perl
Requires:	%{perl_sitearch}
# do not change to BuildRequires
Requires:	perl-HTML-Tree >= 0.62
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-Format perl module

%description -l pl
Modu� perla HTML-Format

%prep
%setup -q -n HTML-Format-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML-Format
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/HTML/FormatPS.pm
%{perl_sitelib}/HTML/FormatText.pm
%{perl_sitelib}/HTML/Formatter.pm
%{perl_sitearch}/auto/HTML-Format

%{_mandir}/man3/*

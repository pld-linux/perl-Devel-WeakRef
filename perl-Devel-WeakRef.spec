%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	WeakRef
Summary:	Devel::WeakRef perl module
Summary(pl):	Modu³ perla Devel::WeakRef
Name:		perl-Devel-WeakRef
Version:	0.003
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-perl-5.6.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Test-Helper
Requires:	perl-Test-Helper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::WeakRef perl module allows you to use weak references to any
reference-valued variable (not reference-counted), dereferenced with a
method call, with a normal scalar dereference, or as part of a hash
lookup.

%description -l pl
Modu³ perla Devel::WeakRef.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Devel/WeakRef.pm
%dir %{perl_sitearch}/auto/Devel/WeakRef
%{perl_sitearch}/auto/Devel/WeakRef/WeakRef.bs
%attr(755,root,root) %{perl_sitearch}/auto/Devel/WeakRef/WeakRef.so
%{_mandir}/man3/*

%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	WeakRef
Summary:	Devel::WeakRef - weak references (not reference-counted)
Summary(pl):	Devel::WeakRef - s�abe odwo�ania (nie zliczane przez licznik odwo�a�)
Name:		perl-Devel-WeakRef
Version:	0.003
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	090bd51f8be8d0ce9b466f03cb538bed
Patch0:		%{name}-perl-5.6.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Test-Helper
Requires:	perl-Test-Helper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::WeakRef Perl module allows you to use weak references to any
reference-valued variable (not reference-counted), dereferenced with a
method call, with a normal scalar dereference, or as part of a hash
lookup.

%description -l pl
Modu� Perla Devel::WeakRef umo�liwia s�abe odwo�ania do dowolnych
zmiennych o warto�ciach referencyjnych (nie s� one zliczane przez
licznik odwo�a�). Wy�uskiwanie odbywa si� poprzez wywo�anie metody ze
zwy�ym skalarnym wy�uskaniem. S�abe odwo�ania mog� te� by� u�ywane
jako cz�� przeszukiwania hasha.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
%doc README TODO CHANGES
%{perl_vendorarch}/Devel/WeakRef.pm
%dir %{perl_vendorarch}/auto/Devel/WeakRef
%{perl_vendorarch}/auto/Devel/WeakRef/WeakRef.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/WeakRef/WeakRef.so
%{_mandir}/man3/*

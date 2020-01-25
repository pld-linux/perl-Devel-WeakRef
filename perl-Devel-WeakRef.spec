#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Devel
%define		pnam	WeakRef
Summary:	Devel::WeakRef - weak references (not reference-counted)
Summary(pl.UTF-8):	Devel::WeakRef - słabe odwołania (nie zliczane przez licznik odwołań)
Name:		perl-Devel-WeakRef
Version:	0.003
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	090bd51f8be8d0ce9b466f03cb538bed
Patch0:		%{name}-perl-5.6.patch
URL:		http://search.cpan.org/dist/Devel-WeakRef/
BuildRequires:	perl-Test-Helper
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Test-Helper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::WeakRef Perl module allows you to use weak references to any
reference-valued variable (not reference-counted), dereferenced with a
method call, with a normal scalar dereference, or as part of a hash
lookup.

%description -l pl.UTF-8
Moduł Perla Devel::WeakRef umożliwia słabe odwołania do dowolnych
zmiennych o wartościach referencyjnych (nie są one zliczane przez
licznik odwołań). Wyłuskiwanie odbywa się poprzez wywołanie metody ze
zwykłym skalarnym wyłuskaniem. Słabe odwołania mogą też być używane
jako część przeszukiwania hasha.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
%doc README TODO CHANGES
%{perl_vendorarch}/Devel/WeakRef.pm
%dir %{perl_vendorarch}/auto/Devel/WeakRef
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/WeakRef/WeakRef.so
%{_mandir}/man3/*

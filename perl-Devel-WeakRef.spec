%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	WeakRef
Summary:	Devel::WeakRef perl module
Summary(pl):	Modu³ perla Devel::WeakRef
Name:		perl-Devel-WeakRef
Version:	0.003
Release:	8
License:	GPL
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

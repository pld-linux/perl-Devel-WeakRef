%include	/usr/lib/rpm/macros.perl
Summary:	Devel-WeakRef perl module
Summary(pl):	Modu³ perla Devel-WeakRef
Name:		perl-Devel-WeakRef
Version:	0.003
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-WeakRef-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Test-Helper
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-Test-Helper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-WeakRef perl module allows you to use weak references to any
reference-valued variable (not reference-counted), dereferenced with a
method call, with a normal scalar dereference, or as part of a hash
lookup.

%description -l pl
Modu³ perla Devel-WeakRef.

%prep
%setup -q -n Devel-WeakRef-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Devel/WeakRef/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Devel/WeakRef
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README TODO CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,CHANGES}.gz

%{perl_sitearch}/Devel/WeakRef.pm

%dir %{perl_sitearch}/auto/Devel/WeakRef
%{perl_sitearch}/auto/Devel/WeakRef/.packlist
%{perl_sitearch}/auto/Devel/WeakRef/WeakRef.bs
%attr(755,root,root) %{perl_sitearch}/auto/Devel/WeakRef/WeakRef.so

%{_mandir}/man3/*

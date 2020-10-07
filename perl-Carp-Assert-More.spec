#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Carp-Assert-More
Version  : 1.24
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Carp-Assert-More-1.24.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Carp-Assert-More-1.24.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libc/libcarp-assert-more-perl/libcarp-assert-more-perl_1.16-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Carp-Assert-More-license = %{version}-%{release}
Requires: perl-Carp-Assert-More-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Carp::Assert)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)

%description
# Carp::Assert::More
[![Build Status](https://travis-ci.org/petdance/carp-assert-more.svg?branch=dev)](https://travis-ci.org/petdance/carp-assert-more)

%package dev
Summary: dev components for the perl-Carp-Assert-More package.
Group: Development
Provides: perl-Carp-Assert-More-devel = %{version}-%{release}
Requires: perl-Carp-Assert-More = %{version}-%{release}

%description dev
dev components for the perl-Carp-Assert-More package.


%package license
Summary: license components for the perl-Carp-Assert-More package.
Group: Default

%description license
license components for the perl-Carp-Assert-More package.


%package perl
Summary: perl components for the perl-Carp-Assert-More package.
Group: Default
Requires: perl-Carp-Assert-More = %{version}-%{release}

%description perl
perl components for the perl-Carp-Assert-More package.


%prep
%setup -q -n Carp-Assert-More-1.24
cd %{_builddir}
tar xf %{_sourcedir}/libcarp-assert-more-perl_1.16-1.debian.tar.xz
cd %{_builddir}/Carp-Assert-More-1.24
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Carp-Assert-More-1.24/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Carp-Assert-More
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Carp-Assert-More/1c54c26afbf89c84daacb0c7815c9c47d5a3918c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Carp::Assert::More.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Carp-Assert-More/1c54c26afbf89c84daacb0c7815c9c47d5a3918c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Carp/Assert/More.pm

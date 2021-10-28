#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : applaunchservices
Version  : 0.2.1
Release  : 15
URL      : https://files.pythonhosted.org/packages/d7/55/d355acc279722b00b4c4baa002d84f142dfd7ff32336fcb3921cd1fc348f/applaunchservices-0.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/d7/55/d355acc279722b00b4c4baa002d84f142dfd7ff32336fcb3921cd1fc348f/applaunchservices-0.2.1.tar.gz
Summary  : Simple package for registering an app with apple Launch Services to handle UTI and URL
Group    : Development/Tools
License  : MIT
Requires: applaunchservices-license = %{version}-%{release}
Requires: applaunchservices-python = %{version}-%{release}
Requires: applaunchservices-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Patch1: deps.patch

%description
# applaunchservices
Simple package for registering an app with apple Launch Services to handle UTI and URL. See Apple documentations for details.

%package license
Summary: license components for the applaunchservices package.
Group: Default

%description license
license components for the applaunchservices package.


%package python
Summary: python components for the applaunchservices package.
Group: Default
Requires: applaunchservices-python3 = %{version}-%{release}

%description python
python components for the applaunchservices package.


%package python3
Summary: python3 components for the applaunchservices package.
Group: Default
Requires: python3-core

%description python3
python3 components for the applaunchservices package.


%prep
%setup -q -n applaunchservices-0.2.1
cd %{_builddir}/applaunchservices-0.2.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585321526
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/applaunchservices
cp %{_builddir}/applaunchservices-0.2.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/applaunchservices/f79ba2890ff36ba2c90773a0b62d6eddcab61b30
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/applaunchservices/f79ba2890ff36ba2c90773a0b62d6eddcab61b30

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

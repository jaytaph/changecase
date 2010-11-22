Summary: NoxLogic Case Changer
Vendor: NoxLogic
Name: changecase
Version: 1.0
Release: 1
Source0: changecase-%{version}.tar.gz
License: GPL
Group: NoxLogic
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: coreutils
%description
This is a simple script that will change the case of the input.

%prep

%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/noxlogic/bin
cp bin/changecase $RPM_BUILD_ROOT/usr/local/noxlogic/bin
cp man/changecase.1 $RPM_BUILD_ROOT/usr/share/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%doc doc/*
%dir /usr/local
%dir /usr/local/noxlogic
%dir /usr/local/noxlogic/bin
/usr/share/man/man1/changecase.1
/usr/local/noxlogic/bin/changecase

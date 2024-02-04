Name:		px4_drv-dkms
Summary:	px4_drv-dkms
Version:	0.4.2
Release:	1%{?dist}
License:	GPL2	
BuildArch:	x86_64
Requires:       dkms

BuildRequires: dkms
%global debug_package %{nil}
Source0: https://github.com/kahenteikou/px4_drv_rpm/archive/refs/tags/v0.4.2.tar.gz
%description
px4_drv-dkms
%prep
rm -rf %{buildroot}

%setup -n px4_drv_rpm-%{version}
%build
%install
mkdir -p ${RPM_BUILD_ROOT}%{_usrsrc}/px4_drv-%{version}
cp -fr * ${RPM_BUILD_ROOT}%{_usrsrc}/px4_drv-%{version}/

%files
%{_usrsrc}/px4_drv-%{version}

%changelog
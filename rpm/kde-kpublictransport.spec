%global pkgnameo kpublictransport
%global kde_version 25.08.2
%global kf_version 6.18.0

Name:           kde-kpublictransport
Version:        25.08.2
Release:        0%{?dist}
Summary:        Library to assist with accessing public transport timetables and other data
License:        BSD and CC0-1.0 and LGPLv2+ and MIT and ODbL-1.0
URL:            https://invent.kde.org/libraries/kpublictransport
Source0:        %{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: kf6-extra-cmake-modules >= %{kf_version}

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qttools

BuildRequires: kf6-ki18n-devel

BuildRequires: zlib-devel
BuildRequires: protobuf-devel

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kpublictransport

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kpublictransport.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*categories
%{_libdir}/libKPublicTransport.so.*
%{_libdir}/libKPublicTransportOnboard.so.*
%{_kf6_qmldir}/org/kde/kpublictransport/

%files devel
%{_includedir}/KPublicTransport/
%{_libdir}/cmake/KPublicTransport/
%{_libdir}/libKPublicTransport.so
%{_libdir}/libKPublicTransportOnboard.so


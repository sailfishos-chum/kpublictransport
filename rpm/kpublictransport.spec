Name:           opt-kpublictransport
Version:        23.07.90
Release:        1%{?dist}
License:        BSD and CC0-1.0 and LGPLv2+ and MIT and ODbL-1.0
Summary:        Library to assist with accessing public transport timetables and other data
Url:            https://invent.kde.org/libraries/kpublictransport
Source0: %{name}-%{version}.tar.bz2

%global __requires_exclude ^libKPublicTransport.*$
%{?opt_kf5_default_filter}

BuildRequires: opt-extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: opt-kf5-rpm-macros
BuildRequires: zlib-devel
BuildRequires: protobuf-devel

BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qtdeclarative-devel

BuildRequires: opt-kf5-ki18n-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtdeclarative
Requires: opt-kf5-ki18n


%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%files
%{_opt_kf5_datadir}/qlogging-categories5/org_kde_kpublictransport.categories

%{_opt_kf5_libdir}/libKPublicTransport.so.1
%{_opt_kf5_libdir}/libKPublicTransport.so.%{version}
%{_opt_kf5_libdir}/libKPublicTransportOnboard.so.1
%{_opt_kf5_libdir}/libKPublicTransportOnboard.so.%{version}

%{_opt_kf5_qmldir}/org/kde/kpublictransport/*
%{_opt_kf5_datadir}/qlogging-categories5/org_kde_kpublictransport_onboard.categories

%package devel
Summary: Development files for %{name}
License: BSD and CC0-1.0 and LGPLv2+ and MIT and ODbL-1.0
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%files devel
%{_opt_kf5_includedir}/*

%{_opt_kf5_libdir}/cmake/*
%{_opt_kf5_libdir}/*.so


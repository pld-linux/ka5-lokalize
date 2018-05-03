%define		kdeappsver	18.04.0
%define		qtver		5.3.2
%define		kaname		lokalize
Summary:	lokalize
Name:		ka5-%{kaname}
Version:	18.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a56400b08e282aaac734fca32c54d009
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lokalize.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lokalize
%{_desktopdir}/org.kde.lokalize.desktop
%{_datadir}/config.kcfg/lokalize.kcfg
%{_iconsdir}/hicolor/128x128/apps/lokalize.png
%{_iconsdir}/hicolor/32x32/apps/lokalize.png
%{_iconsdir}/hicolor/64x64/apps/lokalize.png
%{_iconsdir}/hicolor/scalable/apps/lokalize.svgz
%{_datadir}/knotifications5/lokalize.notifyrc
%{_datadir}/kxmlgui5/lokalize
%{_datadir}/lokalize
%{_datadir}/metainfo/org.kde.lokalize.appdata.xml

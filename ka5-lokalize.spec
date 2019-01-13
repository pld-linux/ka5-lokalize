%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		lokalize
Summary:	lokalize
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	eb987cdf4bf03219c321980f232b1f13
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	hunspell-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.14.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.14.0
BuildRequires:	kf5-kcrash-devel >= 5.14.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.14.0
BuildRequires:	kf5-kdoctools-devel >= 5.14.0
BuildRequires:	kf5-ki18n-devel >= 5.14.0
BuildRequires:	kf5-kio-devel >= 5.14.0
BuildRequires:	kf5-knotifications-devel >= 5.14.0
BuildRequires:	kf5-kross-devel >= 5.14.0
BuildRequires:	kf5-kxmlgui-devel >= 5.14.0
BuildRequires:	kf5-sonnet-devel >= 5.14.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lokalize is a computer-aided translation system that focuses on
productivity and quality assurance. It is targeted for software
translation and also integrates external conversion tools for
freelance office document translation.

Features

• Project management overview • Translation merging (synchronization)
• Translation memory • Glossary • Spell-checking

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/lokalize.categories
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

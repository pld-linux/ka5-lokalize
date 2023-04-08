#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		lokalize
Summary:	Lokalize - computer-aided translation system
Summary(pl.UTF-8):	Lokalize - system komputerowo wspomaganego tłumaczenia
Name:		ka5-%{kaname}
Version:	22.12.3
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1d956c12ea8b22e66449e9048422a6c7
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
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kross-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-sonnet-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lokalize is a computer-aided translation system that focuses on
productivity and quality assurance. It is targeted for software
translation and also integrates external conversion tools for
freelance office document translation.

Features:
- Project management overview
- Translation merging (synchronization)
- Translation memory
- Glossary
- Spell-checking

%description -l pl.UTF-8
Lokalize to system komputerowo wspomaganego tłumaczenia, skupiający
się na produktywności i zapewnieniu jakości. Głównym zastosowaniem
jest tłumaczenie oprogramowania; zawiera także narzędzia do
zewnętrznej konwersji do tłumaczenia dokumentów biurowych.

Możliwości:
- widok ogólny zarządzania projektem
- łączenie tłumaczeń (synchronizacja)
- pamięć tłumaczeń
- słownik pojęć
- sprawdzanie pisowni

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake .. \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kaname} --with-kde

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
%{_datadir}/qlogging-categories5/lokalize.categories

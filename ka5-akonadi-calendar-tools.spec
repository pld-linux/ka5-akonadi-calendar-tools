%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		akonadi-calendar-tools
Summary:	Akonadi Calendar Tools
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a59425e38bcd91461e093a41ffd44ed0
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-calendar-devel >= 18.12.0
BuildRequires:	ka5-akonadi-devel >= 18.12.0
BuildRequires:	ka5-calendarsupport-devel >= 18.12.0
BuildRequires:	ka5-kcalcore-devel >= 18.12.0
BuildRequires:	ka5-kcalutils-devel
BuildRequires:	ka5-libkdepim-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-kdelibs4support-devel >= 5.53.0
BuildRequires:	kf5-kdoctools-devel >= 5.53.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Console applications and utilities for managing calendars in Akonadi.

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
/etc/xdg/console.categories
/etc/xdg/console.renamecategories
%attr(755,root,root) %{_bindir}/calendarjanitor
%attr(755,root,root) %{_bindir}/konsolekalendar
%{_desktopdir}/konsolekalendar.desktop
%{_iconsdir}/hicolor/128x128/apps/konsolekalendar.png
%{_iconsdir}/hicolor/16x16/apps/konsolekalendar.png
%{_iconsdir}/hicolor/22x22/apps/konsolekalendar.png
%{_iconsdir}/hicolor/32x32/apps/konsolekalendar.png
%{_iconsdir}/hicolor/48x48/apps/konsolekalendar.png

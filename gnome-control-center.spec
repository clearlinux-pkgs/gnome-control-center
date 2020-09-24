#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-control-center
Version  : 3.38.0
Release  : 54
URL      : https://download.gnome.org/sources/gnome-control-center/3.38/gnome-control-center-3.38.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-control-center/3.38/gnome-control-center-3.38.0.tar.xz
Summary  : A library full of GTK widgets for mobile phones
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 LGPL-2.1+ MIT
Requires: gnome-control-center-bin = %{version}-%{release}
Requires: gnome-control-center-data = %{version}-%{release}
Requires: gnome-control-center-libexec = %{version}-%{release}
Requires: gnome-control-center-license = %{version}-%{release}
Requires: gnome-control-center-locales = %{version}-%{release}
Requires: gnome-control-center-man = %{version}-%{release}
Requires: glibc-locale
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : colord
BuildRequires : colord-gtk-dev
BuildRequires : cups-dev
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : glibc-locale
BuildRequires : gsettings-desktop-schemas-dev
BuildRequires : gsound-dev
BuildRequires : intltool
BuildRequires : krb5-dev
BuildRequires : libgtop-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(accountsservice)
BuildRequires : pkgconfig(cheese-gtk)
BuildRequires : pkgconfig(colord-gtk)
BuildRequires : pkgconfig(gnome-bluetooth-1.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gnome-settings-daemon)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(grilo-0.3)
BuildRequires : pkgconfig(gsound)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libgtop-2.0)
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libnma)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libwacom)
BuildRequires : pkgconfig(mm-glib)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(pwquality)
BuildRequires : pkgconfig(smbclient)
BuildRequires : pkgconfig(udisks2)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : shared-mime-info
BuildRequires : udisks2-dev
Patch1: Check-country-value.patch

%description
Those translations are copied from system-config-date
http://git.fedorahosted.org/git/?p=system-config-date.git;a=tree;f=po/timezones
and should not be modified by the GNOME translation teams.

%package bin
Summary: bin components for the gnome-control-center package.
Group: Binaries
Requires: gnome-control-center-data = %{version}-%{release}
Requires: gnome-control-center-libexec = %{version}-%{release}
Requires: gnome-control-center-license = %{version}-%{release}

%description bin
bin components for the gnome-control-center package.


%package data
Summary: data components for the gnome-control-center package.
Group: Data

%description data
data components for the gnome-control-center package.


%package dev
Summary: dev components for the gnome-control-center package.
Group: Development
Requires: gnome-control-center-bin = %{version}-%{release}
Requires: gnome-control-center-data = %{version}-%{release}
Provides: gnome-control-center-devel = %{version}-%{release}
Requires: gnome-control-center = %{version}-%{release}

%description dev
dev components for the gnome-control-center package.


%package libexec
Summary: libexec components for the gnome-control-center package.
Group: Default
Requires: gnome-control-center-license = %{version}-%{release}

%description libexec
libexec components for the gnome-control-center package.


%package license
Summary: license components for the gnome-control-center package.
Group: Default

%description license
license components for the gnome-control-center package.


%package locales
Summary: locales components for the gnome-control-center package.
Group: Default

%description locales
locales components for the gnome-control-center package.


%package man
Summary: man components for the gnome-control-center package.
Group: Default

%description man
man components for the gnome-control-center package.


%prep
%setup -q -n gnome-control-center-3.38.0
cd %{_builddir}/gnome-control-center-3.38.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600302406
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dwith-introspection=true -Ddocumentation=true  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-control-center
cp %{_builddir}/gnome-control-center-3.38.0/COPYING %{buildroot}/usr/share/package-licenses/gnome-control-center/13d2034b5ee3cb8d1a076370cf8f0e344a5d0855
cp %{_builddir}/gnome-control-center-3.38.0/panels/wacom/calibrator/COPYING %{buildroot}/usr/share/package-licenses/gnome-control-center/5dfd8a387b5dd2491e61f9649b1cec0ab059c0dd
cp %{_builddir}/gnome-control-center-3.38.0/subprojects/libhandy/COPYING %{buildroot}/usr/share/package-licenses/gnome-control-center/01a6b4bf79aca9b556822601186afab86e8c4fbf
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-control-center-2.0
%find_lang gnome-control-center-2.0-timezones
## install_append content
mkdir -p %{buildroot}/usr/lib64/pkgconfig
mv %{buildroot}/usr/share/pkgconfig/gnome-keybindings.pc %{buildroot}/usr/lib64/pkgconfig/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-control-center

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-applications-panel.desktop
/usr/share/applications/gnome-background-panel.desktop
/usr/share/applications/gnome-bluetooth-panel.desktop
/usr/share/applications/gnome-camera-panel.desktop
/usr/share/applications/gnome-color-panel.desktop
/usr/share/applications/gnome-control-center.desktop
/usr/share/applications/gnome-datetime-panel.desktop
/usr/share/applications/gnome-default-apps-panel.desktop
/usr/share/applications/gnome-diagnostics-panel.desktop
/usr/share/applications/gnome-display-panel.desktop
/usr/share/applications/gnome-info-overview-panel.desktop
/usr/share/applications/gnome-keyboard-panel.desktop
/usr/share/applications/gnome-location-panel.desktop
/usr/share/applications/gnome-lock-panel.desktop
/usr/share/applications/gnome-microphone-panel.desktop
/usr/share/applications/gnome-mouse-panel.desktop
/usr/share/applications/gnome-network-panel.desktop
/usr/share/applications/gnome-notifications-panel.desktop
/usr/share/applications/gnome-online-accounts-panel.desktop
/usr/share/applications/gnome-power-panel.desktop
/usr/share/applications/gnome-printers-panel.desktop
/usr/share/applications/gnome-region-panel.desktop
/usr/share/applications/gnome-removable-media-panel.desktop
/usr/share/applications/gnome-search-panel.desktop
/usr/share/applications/gnome-sharing-panel.desktop
/usr/share/applications/gnome-sound-panel.desktop
/usr/share/applications/gnome-thunderbolt-panel.desktop
/usr/share/applications/gnome-universal-access-panel.desktop
/usr/share/applications/gnome-usage-panel.desktop
/usr/share/applications/gnome-user-accounts-panel.desktop
/usr/share/applications/gnome-wacom-panel.desktop
/usr/share/applications/gnome-wifi-panel.desktop
/usr/share/bash-completion/completions/gnome-control-center
/usr/share/dbus-1/services/org.gnome.ControlCenter.SearchProvider.service
/usr/share/dbus-1/services/org.gnome.ControlCenter.service
/usr/share/gettext/its/gnome-keybindings.its
/usr/share/gettext/its/gnome-keybindings.loc
/usr/share/gettext/its/sounds.its
/usr/share/gettext/its/sounds.loc
/usr/share/glib-2.0/schemas/org.gnome.ControlCenter.gschema.xml
/usr/share/gnome-control-center/keybindings/00-multimedia.xml
/usr/share/gnome-control-center/keybindings/01-input-sources.xml
/usr/share/gnome-control-center/keybindings/01-launchers.xml
/usr/share/gnome-control-center/keybindings/01-screenshot.xml
/usr/share/gnome-control-center/keybindings/01-system.xml
/usr/share/gnome-control-center/keybindings/50-accessibility.xml
/usr/share/gnome-control-center/pixmaps/noise-texture-light.png
/usr/share/gnome-shell/search-providers/gnome-control-center-search-provider.ini
/usr/share/icons/hicolor/16x16/apps/gnome-power-manager.png
/usr/share/icons/hicolor/16x16/apps/goa-panel.png
/usr/share/icons/hicolor/16x16/apps/preferences-color.png
/usr/share/icons/hicolor/16x16/apps/preferences-desktop-display.png
/usr/share/icons/hicolor/16x16/apps/preferences-system-time.png
/usr/share/icons/hicolor/22x22/apps/gnome-power-manager.png
/usr/share/icons/hicolor/22x22/apps/goa-panel.png
/usr/share/icons/hicolor/22x22/apps/preferences-color.png
/usr/share/icons/hicolor/22x22/apps/preferences-desktop-display.png
/usr/share/icons/hicolor/22x22/apps/preferences-system-time.png
/usr/share/icons/hicolor/24x24/apps/gnome-power-manager.png
/usr/share/icons/hicolor/24x24/apps/goa-panel.png
/usr/share/icons/hicolor/24x24/apps/preferences-color.png
/usr/share/icons/hicolor/24x24/apps/preferences-desktop-display.png
/usr/share/icons/hicolor/256x256/apps/gnome-power-manager.png
/usr/share/icons/hicolor/256x256/apps/goa-panel.png
/usr/share/icons/hicolor/256x256/apps/preferences-color.png
/usr/share/icons/hicolor/256x256/apps/preferences-system-time.png
/usr/share/icons/hicolor/32x32/apps/gnome-power-manager.png
/usr/share/icons/hicolor/32x32/apps/goa-panel.png
/usr/share/icons/hicolor/32x32/apps/preferences-color.png
/usr/share/icons/hicolor/32x32/apps/preferences-desktop-display.png
/usr/share/icons/hicolor/32x32/apps/preferences-system-time.png
/usr/share/icons/hicolor/48x48/apps/gnome-power-manager.png
/usr/share/icons/hicolor/48x48/apps/goa-panel.png
/usr/share/icons/hicolor/48x48/apps/preferences-color.png
/usr/share/icons/hicolor/48x48/apps/preferences-system-time.png
/usr/share/icons/hicolor/64x64/apps/preferences-color.png
/usr/share/icons/hicolor/scalable/apps/org.gnome.Settings.Devel.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.Settings.svg
/usr/share/icons/hicolor/scalable/apps/preferences-color.svg
/usr/share/icons/hicolor/scalable/apps/preferences-desktop-display.svg
/usr/share/icons/hicolor/scalable/apps/preferences-system-time.svg
/usr/share/icons/hicolor/scalable/categories/slideshow-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/slideshow-emblem.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Settings-symbolic.svg
/usr/share/metainfo/gnome-control-center.appdata.xml
/usr/share/pixmaps/faces/astronaut.jpg
/usr/share/pixmaps/faces/baseball.png
/usr/share/pixmaps/faces/bicycle.jpg
/usr/share/pixmaps/faces/book.jpg
/usr/share/pixmaps/faces/butterfly.png
/usr/share/pixmaps/faces/calculator.jpg
/usr/share/pixmaps/faces/cat-eye.jpg
/usr/share/pixmaps/faces/cat.jpg
/usr/share/pixmaps/faces/chess.jpg
/usr/share/pixmaps/faces/coffee.jpg
/usr/share/pixmaps/faces/coffee2.jpg
/usr/share/pixmaps/faces/dice.jpg
/usr/share/pixmaps/faces/energy-arc.jpg
/usr/share/pixmaps/faces/fish.jpg
/usr/share/pixmaps/faces/flake.jpg
/usr/share/pixmaps/faces/flower.jpg
/usr/share/pixmaps/faces/flower2.jpg
/usr/share/pixmaps/faces/gamepad.jpg
/usr/share/pixmaps/faces/grapes.jpg
/usr/share/pixmaps/faces/guitar.jpg
/usr/share/pixmaps/faces/guitar2.jpg
/usr/share/pixmaps/faces/headphones.jpg
/usr/share/pixmaps/faces/hummingbird.jpg
/usr/share/pixmaps/faces/launch.jpg
/usr/share/pixmaps/faces/leaf.jpg
/usr/share/pixmaps/faces/legacy/astronaut.jpg
/usr/share/pixmaps/faces/legacy/baseball.png
/usr/share/pixmaps/faces/legacy/butterfly.png
/usr/share/pixmaps/faces/legacy/cat-eye.jpg
/usr/share/pixmaps/faces/legacy/chess.jpg
/usr/share/pixmaps/faces/legacy/coffee.jpg
/usr/share/pixmaps/faces/legacy/dice.jpg
/usr/share/pixmaps/faces/legacy/energy-arc.jpg
/usr/share/pixmaps/faces/legacy/fish.jpg
/usr/share/pixmaps/faces/legacy/flake.jpg
/usr/share/pixmaps/faces/legacy/flower.jpg
/usr/share/pixmaps/faces/legacy/grapes.jpg
/usr/share/pixmaps/faces/legacy/guitar.jpg
/usr/share/pixmaps/faces/legacy/launch.jpg
/usr/share/pixmaps/faces/legacy/leaf.jpg
/usr/share/pixmaps/faces/legacy/lightning.jpg
/usr/share/pixmaps/faces/legacy/penguin.jpg
/usr/share/pixmaps/faces/legacy/puppy.jpg
/usr/share/pixmaps/faces/legacy/sky.jpg
/usr/share/pixmaps/faces/legacy/soccerball.png
/usr/share/pixmaps/faces/legacy/sunflower.jpg
/usr/share/pixmaps/faces/legacy/sunset.jpg
/usr/share/pixmaps/faces/legacy/tennis-ball.png
/usr/share/pixmaps/faces/legacy/yellow-rose.jpg
/usr/share/pixmaps/faces/lightning.jpg
/usr/share/pixmaps/faces/mountain.jpg
/usr/share/pixmaps/faces/penguin.jpg
/usr/share/pixmaps/faces/plane.jpg
/usr/share/pixmaps/faces/puppy.jpg
/usr/share/pixmaps/faces/sky.jpg
/usr/share/pixmaps/faces/soccerball.png
/usr/share/pixmaps/faces/sunflower.jpg
/usr/share/pixmaps/faces/sunset.jpg
/usr/share/pixmaps/faces/surfer.jpg
/usr/share/pixmaps/faces/tennis-ball.png
/usr/share/pixmaps/faces/tomatoes.jpg
/usr/share/pixmaps/faces/tree.jpg
/usr/share/pixmaps/faces/yellow-rose.jpg
/usr/share/polkit-1/actions/org.gnome.controlcenter.datetime.policy
/usr/share/polkit-1/actions/org.gnome.controlcenter.remote-login-helper.policy
/usr/share/polkit-1/actions/org.gnome.controlcenter.user-accounts.policy
/usr/share/polkit-1/rules.d/gnome-control-center.rules
/usr/share/sounds/gnome/default/alerts/bark.ogg
/usr/share/sounds/gnome/default/alerts/drip.ogg
/usr/share/sounds/gnome/default/alerts/glass.ogg
/usr/share/sounds/gnome/default/alerts/sonar.ogg

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/gnome-keybindings.pc

%files libexec
%defattr(-,root,root,-)
/usr/libexec/cc-remote-login-helper
/usr/libexec/gnome-control-center-print-renderer
/usr/libexec/gnome-control-center-search-provider

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-control-center/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/gnome-control-center/13d2034b5ee3cb8d1a076370cf8f0e344a5d0855
/usr/share/package-licenses/gnome-control-center/5dfd8a387b5dd2491e61f9649b1cec0ab059c0dd

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-control-center.1

%files locales -f gnome-control-center-2.0.lang -f gnome-control-center-2.0-timezones.lang
%defattr(-,root,root,-)


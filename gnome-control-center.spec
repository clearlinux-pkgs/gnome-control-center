#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-control-center
Version  : 3.24.1
Release  : 5
URL      : https://download.gnome.org/sources/gnome-control-center/3.24/gnome-control-center-3.24.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-control-center/3.24/gnome-control-center-3.24.1.tar.xz
Summary  : Keybindings configuration for GNOME applications
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: gnome-control-center-bin
Requires: gnome-control-center-data
Requires: gnome-control-center-locales
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : colord-gtk-dev
BuildRequires : cups-dev
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : intltool
BuildRequires : krb5-dev
BuildRequires : libgtop-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(accountsservice)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(colord)
BuildRequires : pkgconfig(colord-gtk)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gdk-wayland-3.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gnome-bluetooth-1.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gnome-settings-daemon)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(goa-backend-1.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(grilo-0.3)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libgtop-2.0)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libnm-glib)
BuildRequires : pkgconfig(libnm-gtk)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(pwquality)
BuildRequires : pkgconfig(smbclient)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xi)
BuildRequires : sed
BuildRequires : shared-mime-info
Patch1: 0001-Remove-support-for-Modem-manager.patch
Patch2: 0002-panels-Use-the-correct-stateless-vendor-os-release-f.patch

%description
GNOME Control Center
====================
About -
The control center is GNOME's main interface for configuration of various
aspects of your desktop.

%package bin
Summary: bin components for the gnome-control-center package.
Group: Binaries
Requires: gnome-control-center-data

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
Requires: gnome-control-center-bin
Requires: gnome-control-center-data
Provides: gnome-control-center-devel

%description dev
dev components for the gnome-control-center package.


%package locales
Summary: locales components for the gnome-control-center package.
Group: Default

%description locales
locales components for the gnome-control-center package.


%prep
%setup -q -n gnome-control-center-3.24.1
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493742219
%reconfigure --disable-static --without-cheese --disable-update-mimedb --disable-documentation
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1493742219
rm -rf %{buildroot}
%make_install
%find_lang gnome-control-center-2.0
%find_lang gnome-control-center-2.0-timezones

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-control-center
/usr/libexec/cc-remote-login-helper
/usr/libexec/gnome-control-center-search-provider

%files data
%defattr(-,root,root,-)
/usr/share/appdata/gnome-control-center.appdata.xml
/usr/share/applications/gnome-background-panel.desktop
/usr/share/applications/gnome-bluetooth-panel.desktop
/usr/share/applications/gnome-color-panel.desktop
/usr/share/applications/gnome-control-center.desktop
/usr/share/applications/gnome-datetime-panel.desktop
/usr/share/applications/gnome-display-panel.desktop
/usr/share/applications/gnome-info-panel.desktop
/usr/share/applications/gnome-keyboard-panel.desktop
/usr/share/applications/gnome-mouse-panel.desktop
/usr/share/applications/gnome-network-panel.desktop
/usr/share/applications/gnome-notifications-panel.desktop
/usr/share/applications/gnome-online-accounts-panel.desktop
/usr/share/applications/gnome-power-panel.desktop
/usr/share/applications/gnome-printers-panel.desktop
/usr/share/applications/gnome-privacy-panel.desktop
/usr/share/applications/gnome-region-panel.desktop
/usr/share/applications/gnome-search-panel.desktop
/usr/share/applications/gnome-sharing-panel.desktop
/usr/share/applications/gnome-sound-panel.desktop
/usr/share/applications/gnome-universal-access-panel.desktop
/usr/share/applications/gnome-user-accounts-panel.desktop
/usr/share/bash-completion/completions/gnome-control-center
/usr/share/dbus-1/services/org.gnome.ControlCenter.SearchProvider.service
/usr/share/dbus-1/services/org.gnome.ControlCenter.service
/usr/share/gettext/its/gnome-keybindings.its
/usr/share/gettext/its/gnome-keybindings.loc
/usr/share/gnome-control-center/icons/hicolor/16x16/devices/audio-headset.svg
/usr/share/gnome-control-center/icons/hicolor/16x16/status/audio-input-microphone-high.png
/usr/share/gnome-control-center/icons/hicolor/16x16/status/audio-input-microphone-low.png
/usr/share/gnome-control-center/icons/hicolor/16x16/status/audio-input-microphone-medium.png
/usr/share/gnome-control-center/icons/hicolor/16x16/status/audio-input-microphone-muted.png
/usr/share/gnome-control-center/icons/hicolor/22x22/status/audio-input-microphone-high.png
/usr/share/gnome-control-center/icons/hicolor/22x22/status/audio-input-microphone-low.png
/usr/share/gnome-control-center/icons/hicolor/22x22/status/audio-input-microphone-medium.png
/usr/share/gnome-control-center/icons/hicolor/22x22/status/audio-input-microphone-muted.png
/usr/share/gnome-control-center/icons/hicolor/24x24/devices/audio-headset.svg
/usr/share/gnome-control-center/icons/hicolor/24x24/status/audio-input-microphone-high.png
/usr/share/gnome-control-center/icons/hicolor/24x24/status/audio-input-microphone-low.png
/usr/share/gnome-control-center/icons/hicolor/24x24/status/audio-input-microphone-medium.png
/usr/share/gnome-control-center/icons/hicolor/24x24/status/audio-input-microphone-muted.png
/usr/share/gnome-control-center/icons/hicolor/32x32/devices/audio-headset.svg
/usr/share/gnome-control-center/icons/hicolor/32x32/status/audio-input-microphone-high.png
/usr/share/gnome-control-center/icons/hicolor/32x32/status/audio-input-microphone-low.png
/usr/share/gnome-control-center/icons/hicolor/32x32/status/audio-input-microphone-medium.png
/usr/share/gnome-control-center/icons/hicolor/32x32/status/audio-input-microphone-muted.png
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-center-back-testing.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-center-back.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-center-testing.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-center.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-left-back-testing.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-left-back.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-left-side-testing.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-left-side.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-left-testing.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-left.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-right-back-testing.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-right-back.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-right-side-testing.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-right-side.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-right-testing.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-speaker-right.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-subwoofer-testing.svg
/usr/share/gnome-control-center/icons/hicolor/48x48/devices/audio-subwoofer.svg
/usr/share/gnome-control-center/keybindings/00-multimedia.xml
/usr/share/gnome-control-center/keybindings/01-input-sources.xml
/usr/share/gnome-control-center/keybindings/01-launchers.xml
/usr/share/gnome-control-center/keybindings/01-screenshot.xml
/usr/share/gnome-control-center/keybindings/01-system.xml
/usr/share/gnome-control-center/keybindings/50-accessibility.xml
/usr/share/gnome-control-center/pixmaps/noise-texture-light.png
/usr/share/gnome-control-center/sounds/gnome-sounds-default.xml
/usr/share/gnome-shell/search-providers/gnome-control-center-search-provider.ini
/usr/share/icons/hicolor/16x16/apps/gnome-power-manager.png
/usr/share/icons/hicolor/16x16/apps/goa-panel.png
/usr/share/icons/hicolor/16x16/apps/multimedia-volume-control.png
/usr/share/icons/hicolor/16x16/apps/multimedia-volume-control.svg
/usr/share/icons/hicolor/16x16/apps/preferences-color.png
/usr/share/icons/hicolor/16x16/apps/preferences-desktop-display.png
/usr/share/icons/hicolor/16x16/apps/preferences-system-time.png
/usr/share/icons/hicolor/22x22/apps/gnome-power-manager.png
/usr/share/icons/hicolor/22x22/apps/goa-panel.png
/usr/share/icons/hicolor/22x22/apps/multimedia-volume-control.png
/usr/share/icons/hicolor/22x22/apps/multimedia-volume-control.svg
/usr/share/icons/hicolor/22x22/apps/preferences-color.png
/usr/share/icons/hicolor/22x22/apps/preferences-desktop-display.png
/usr/share/icons/hicolor/22x22/apps/preferences-system-time.png
/usr/share/icons/hicolor/24x24/apps/gnome-power-manager.png
/usr/share/icons/hicolor/24x24/apps/goa-panel.png
/usr/share/icons/hicolor/24x24/apps/multimedia-volume-control.png
/usr/share/icons/hicolor/24x24/apps/preferences-color.png
/usr/share/icons/hicolor/24x24/apps/preferences-desktop-display.png
/usr/share/icons/hicolor/256x256/apps/gnome-power-manager.png
/usr/share/icons/hicolor/256x256/apps/goa-panel.png
/usr/share/icons/hicolor/256x256/apps/preferences-color.png
/usr/share/icons/hicolor/256x256/apps/preferences-system-time.png
/usr/share/icons/hicolor/32x32/apps/gnome-power-manager.png
/usr/share/icons/hicolor/32x32/apps/goa-panel.png
/usr/share/icons/hicolor/32x32/apps/multimedia-volume-control.png
/usr/share/icons/hicolor/32x32/apps/multimedia-volume-control.svg
/usr/share/icons/hicolor/32x32/apps/preferences-color.png
/usr/share/icons/hicolor/32x32/apps/preferences-desktop-display.png
/usr/share/icons/hicolor/32x32/apps/preferences-system-time.png
/usr/share/icons/hicolor/48x48/apps/gnome-power-manager.png
/usr/share/icons/hicolor/48x48/apps/goa-panel.png
/usr/share/icons/hicolor/48x48/apps/multimedia-volume-control.png
/usr/share/icons/hicolor/48x48/apps/preferences-color.png
/usr/share/icons/hicolor/48x48/apps/preferences-system-time.png
/usr/share/icons/hicolor/48x48/devices/audio-headset.svg
/usr/share/icons/hicolor/64x64/apps/preferences-color.png
/usr/share/icons/hicolor/scalable/apps/multimedia-volume-control.svg
/usr/share/icons/hicolor/scalable/apps/preferences-color.svg
/usr/share/icons/hicolor/scalable/apps/preferences-desktop-display.svg
/usr/share/icons/hicolor/scalable/apps/preferences-system-time.svg
/usr/share/icons/hicolor/scalable/categories/slideshow-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/slideshow-emblem.svg
/usr/share/icons/hicolor/scalable/status/audio-input-microphone-high-symbolic.svg
/usr/share/icons/hicolor/scalable/status/audio-input-microphone-low-symbolic.svg
/usr/share/icons/hicolor/scalable/status/audio-input-microphone-medium-symbolic.svg
/usr/share/icons/hicolor/scalable/status/audio-input-microphone-muted-symbolic.svg
/usr/share/pixmaps/faces/astronaut.jpg
/usr/share/pixmaps/faces/baseball.png
/usr/share/pixmaps/faces/butterfly.png
/usr/share/pixmaps/faces/cat-eye.jpg
/usr/share/pixmaps/faces/chess.jpg
/usr/share/pixmaps/faces/coffee.jpg
/usr/share/pixmaps/faces/dice.jpg
/usr/share/pixmaps/faces/energy-arc.jpg
/usr/share/pixmaps/faces/fish.jpg
/usr/share/pixmaps/faces/flake.jpg
/usr/share/pixmaps/faces/flower.jpg
/usr/share/pixmaps/faces/grapes.jpg
/usr/share/pixmaps/faces/guitar.jpg
/usr/share/pixmaps/faces/launch.jpg
/usr/share/pixmaps/faces/leaf.jpg
/usr/share/pixmaps/faces/lightning.jpg
/usr/share/pixmaps/faces/penguin.jpg
/usr/share/pixmaps/faces/puppy.jpg
/usr/share/pixmaps/faces/sky.jpg
/usr/share/pixmaps/faces/soccerball.png
/usr/share/pixmaps/faces/sunflower.jpg
/usr/share/pixmaps/faces/sunset.jpg
/usr/share/pixmaps/faces/tennis-ball.png
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

%files locales -f gnome-control-center-2.0.lang -f gnome-control-center-2.0-timezones.lang
%defattr(-,root,root,-)


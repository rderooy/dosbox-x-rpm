Name:          dosbox-x
Version:       0.83.12
Release:       3%{?dist}
Summary:       DOS emulator for running DOS games and applications including Windows 3.x/9x
License:       GPLv2+
URL:           https://dosbox-x.com
Source:        https://github.com/joncampbell123/dosbox-x/archive/%{name}-v%{version}.tar.gz

# Patch to fix DOS4GW temp file creation breakage, merged upstream
# https://github.com/joncampbell123/dosbox-x/pull/2416/commits/3fd18c38b04d5299dff3d76fc6b9062b5f4f2d14
Patch:         fix-temp-filenames.patch

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: fluidsynth-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: libpcap-devel
BuildRequires: libpng-devel
BuildRequires: libslirp-devel
BuildRequires: libtool
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libxkbfile-devel
BuildRequires: libXrandr-devel
BuildRequires: make
BuildRequires: mesa-libGL-devel
BuildRequires: ncurses-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_net-devel
BuildRequires: zlib-devel

Requires:      fluid-soundfont-gm
Requires:      hicolor-icon-theme

%description
DOSBox-X is an open-source DOS emulator for running DOS games and applications.
DOS-based Windows such as Windows 3.x and Windows 9x are officially supported.
Compared to DOSBox, DOSBox-X is much more flexible and provides more features.

DOSBox-X emulates a PC necessary for running many DOS games and applications
that simply cannot be run on modern PCs and operating systems, similar to
DOSBox. However, while the main focus of DOSBox is for running DOS games,
DOSBox-X goes much further than this. Started as a fork of the DOSBox project,
it retains compatibility with the wide base of DOS games and DOS gaming DOSBox
was designed for. But it is also a platform for running DOS applications,
including emulating the environments to run Windows 3.x, 9x and ME and software
written for those versions of Windows. By adding official support for
Windows 95, 98, and ME emulation and acceleration, we hope that those old
Windows games and applications could be enjoyed or used once more. Moreover,
DOSBox-X adds support for emulating the NEC PC-98 such that you can also play
PC-98 games with it.

DOSBox-X emulates a legacy IBM PC and DOS environment, and has many emulation
options and features.

%prep
%autosetup -p1 -n dosbox-x-dosbox-x-v%{version}

%build
./autogen.sh
%configure --enable-core-inline --enable-debug=heavy --enable-sdl2
%make_build

%install
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.dosbox_x.DOSBox-X.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/com.dosbox_x.DOSBox-X.desktop
%{_datadir}/icons/hicolor/scalable/apps/dosbox-x.svg
%{_datadir}/metainfo/com.dosbox_x.DOSBox-X.metainfo.xml
%{_mandir}/man1/dosbox-x.1.gz
%doc CHANGELOG
%doc dosbox-x.reference.conf
%doc dosbox-x.reference.full.conf

# Required for NE2000 pcap networking support (promiscuous mode)
%post
if [ -x %{_sbindir}/setcap ]; then
    setcap cap_net_raw+ep %{_bindir}/%{name}
fi

%changelog
* Mon Apr 12 2021 Robert de Rooy <robert.de.rooy[AT]gmail.com> - 0.83.12-3
- Remove hardening, as it is default
- tag 2 files as doc

* Mon Apr 5 2021 Robert de Rooy <robert.de.rooy[AT]gmail.com> - 0.83.12-2
- Fix DOS4GW temp file creation

* Sun Apr 4 2021 Robert de Rooy <robert.de.rooy[AT]gmail.com> - 0.83.12-1
- Bumped to new release

* Sun Mar 28 2021 Robert de Rooy <robert.de.rooy[AT]gmail.com> - 0.83.11-3
- Add .desktop file validation
- Add .metainfo.xml file validation

* Sat Mar 6 2021 Robert de Rooy <robert.de.rooy[AT]gmail.com> - 0.83.11-2
- Fix s390x build

* Mon Mar 1 2021 Robert de Rooy <robert.de.rooy[AT]gmail.com> - 0.83.11-1
- Initial release for Fedora

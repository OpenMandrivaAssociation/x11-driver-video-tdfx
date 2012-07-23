Name: x11-driver-video-tdfx
Version: 1.4.5
Release: 1
Summary: X.org driver for Voodoo Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-tdfx-%{version}.tar.bz2
 
BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: pkgconfig(gl)

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-tdfx is the X.org driver for Voodoo Cards.

%prep
%setup -qn xf86-video-tdfx-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/tdfx_drv.so
%{_mandir}/man4/tdfx.*


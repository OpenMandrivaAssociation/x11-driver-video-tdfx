%define _disable_ld_no_undefined 1

Summary:	X.org driver for Voodoo Cards
Name:		x11-driver-video-tdfx
Version:	1.4.5
Release:	15
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-tdfx-%{version}.tar.bz2
Patch0:		remove_mibstore_h.patch
Patch1:		U_Rename-XSERVER_PCIACCESS-to-XSERVER_LIBPCIACCESS.patch
Patch2:		U_dri-Stop-uselessly-initializing-the-ValidateTree-hoo.patch 
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-tdfx is the X.org driver for Voodoo Cards.

%prep
%setup -qn xf86-video-tdfx-%{version}
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/tdfx_drv.so
%{_mandir}/man4/tdfx.*


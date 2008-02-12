Name: x11-driver-video-tdfx
Version: 1.3.0
Release: %mkrel 5
Summary: The X.org driver for Voodoo Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-tdfx-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
 
BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

Conflicts: xorg-x11-server < 7.0

Patch1: 0001-Make-TDFXGetRec-return-the-pointer-instead-of-a-bool.patch
Patch2: 0002-Add-DDC2-I2C-support-to-the-tdfx-driver.patch

%description
The X.org driver for Voodoo Cards

%prep
%setup -q -n xf86-video-tdfx-%{version}

%patch1 -p1
%patch2 -p1

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/tdfx_drv.la
%{_libdir}/xorg/modules/drivers/tdfx_drv.so
%{_mandir}/man4/tdfx.*

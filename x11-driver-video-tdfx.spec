%define debug_package	%{nil}

Name: x11-driver-video-tdfx
Version: 1.3.0
Release: %mkrel 3
Summary: The X.org driver for Voodoo Cards
Group: System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-tdfx  xorg/drivers/xf86-video-tdfx
# cd xorg/drivers/xf86-video/tdfx
# git-archive --format=tar --prefix=xf86-video-tdfx-1.3.0/ xf86-video-tdfx-1.3.0 | bzip2 -9 > xf86-video-tdfx-1.3.0.tar.bz2
########################################################################
Source0: xf86-video-tdfx-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-tdfx-1.3.0..origin/mandriva+gpl
Patch1:  0001-Add-DDC2-I2C-support-to-the-tdfx-driver.patch
Patch2:  0002-Supply-NULL-driverFunc-pointer-in-DriverRec.patch
Patch3:  0003-Wrap-pciReadLong-pciWriteLong-with-macros.patch
Patch4:  0004-Make-TDFXGetRec-return-the-pointer-instead-of-a-bool.patch
Patch5:  0005-Minor-code-cleaning-in-TDFXMapMem.patch
Patch6:  0006-White-space-police-in-TDFXInitChips.patch
Patch7:  0007-Initial-pass-at-porting-driver-to-pci-rework.-DOES.patch
Patch8:  0008-TDFX_-_VERSION-using-PACKAGE_VERSION_.patch
Patch9:  0009-Rename-.cvsignore-to-.gitignore.patch
Patch10: 0010-Add-to-.gitignore-to-skip-patch-emacs-droppings.patch
Patch11: 0011-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libdrm-devel		>= 2.3.0
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: libmesagl-devel		>= 7.0.2
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Voodoo Cards

%prep
%setup -q -n xf86-video-tdfx-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/tdfx_drv.so
%{_mandir}/man4/tdfx.*

Name: x11-driver-video-tdfx
Version: 1.3.0
Release: %mkrel 3
Summary: The X.org driver for Voodoo Cards
Group: System/X11
URL: http://xorg.freedesktop.org

########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-tdfx  xorg/drivers/xf86-video-tdfx
# cd xorg/drivers/xf86-video/tdfx
# git-archive --format=tar --prefix=xf86-video-tdfx-1.3.0/ master | bzip2 -9 > xf86-video-tdfx-1.3.0.tar.bz2
########################################################################
Source0: xf86-video-tdfx-%{version}.tar.bz2

License: MIT

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Voodoo Cards


%prep
%setup -q -n xf86-video-tdfx-%{version}

%patch1 -p1

%build
autoreconf -ifs
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



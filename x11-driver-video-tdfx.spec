Name: x11-driver-video-tdfx
Version: 1.4.5
Release: 2
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



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4.5-1
+ Revision: 810697
- version update 1.4.5

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.4.4-2
+ Revision: 787284
- Rebuild for x11-server 1.12

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4.4-1
+ Revision: 786719
- version update 1.4.4

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.4.3-7
+ Revision: 748467
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.3-6
+ Revision: 703745
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.4.3-5
+ Revision: 683588
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-4
+ Revision: 671180
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.4.3-3mdv2011.0
+ Revision: 595718
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.4.3-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 1.4.3-1mdv2010.0
+ Revision: 407724
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.4.2-1mdv2010.0
+ Revision: 391934
- update to new version 1.4.2

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.4.1-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.4.1-1mdv2009.1
+ Revision: 317852
- New version 1.4.1

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.4.0-3mdv2009.1
+ Revision: 308177
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.4.0-2mdv2009.0
+ Revision: 265951
- rebuild early 2009.0 package (before pixel changes)
- improved description
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.4.0-1mdv2009.0
+ Revision: 194134
- Update to version 1.4.0.

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.0-5mdv2008.1
+ Revision: 166141
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.3.0-4mdv2008.1
+ Revision: 156622
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.0-3mdv2008.1
+ Revision: 154792
- Updated BuildRequires and resubmit package.
- Remove debug package.
  Update BuildRequires.
  This package needs more testing. In both, cooker and code yet to enter
  cooker, it will cause the same crash when trying to just query glxinfo:
  ##------------------------------------------------------------------------
  [...]
  (EE) TDFX(0): DRIUnlock called when not locked.
  Backtrace:
  0: /etc/X11/X(xf86SigHandler+0x68) [0x80c2738]
  1: [0xffffe420]
  2: /usr/lib/dri/tdfx_dri.so [0xb38dae90]
  3: /usr/lib/xorg/modules/extensions//libglx.so [0xb7c1e3c8]
  4: /usr/lib/xorg/modules/extensions//libglx.so(DoMakeCurrent+0x362) [0xb7be75f2]
  5: /usr/lib/xorg/modules/extensions//libglx.so [0xb7be7858]
  6: /usr/lib/xorg/modules/extensions//libglx.so [0xb7be9e3c]
  7: /etc/X11/X [0x814de77]
  8: /etc/X11/X(Dispatch+0x4f0) [0x8088790]
  9: /etc/X11/X(main+0x46b) [0x806ec3b]
  10: /lib/i686/libc.so.6(__libc_start_main+0xe0) [0xb7ce8390]
  11: /etc/X11/X(FontFileCompleteXLFD+0x211) [0x806dfb1]
  Caught signal 11. Trying to kill client.
  To be debugged....
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Generate tarball from tag xf86-video-tdfx-1.3.0. And also apply several
  newer patches as there are a few bug fixes, and some cases where macros
  are used to replace old code allowing a "theoretically" easier way to
  handle server builds with libpci acccess interface enabled or not.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.3.0-2mdv2008.1
+ Revision: 99055
- minor spec cleanup
- build against new xserver (1.4)

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


#
# spec file for package foo2zjs
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
# norootforbuild

Name:           foo2zjs
Version:        2014_09_25
Release:        1
Epoch:          1
Summary:        A linux printer driver for ZjStream protocol
Group:          Hardware/Printing

License:        GPL-2.0+
URL:            http://foo2zjs.rkkda.com
Source0:        http://foo2zjs.rkkda.com/foo2zjs.tar.gz
Source1:        http://foo2zjs.rkkda.com/firmware/sihp1000.tar.gz
Source2:        http://foo2zjs.rkkda.com/firmware/sihp1005.tar.gz
Source3:        http://foo2zjs.rkkda.com/firmware/sihp1018.tar.gz
Source4:        http://foo2zjs.rkkda.com/firmware/sihp1020.tar.gz
Source5:        http://foo2zjs.rkkda.com/firmware/sihpP1005.tar.gz
Source6:        http://foo2zjs.rkkda.com/firmware/sihpP1006.tar.gz
Source7:        http://foo2zjs.rkkda.com/firmware/sihpP1505.tar.gz
Source8:        http://foo2zjs.rkkda.com/icm/dl2300.tar.gz
Source9:        http://foo2zjs.rkkda.com/icm/km2430.tar.gz
Source10:       http://foo2hp.rkkda.com/icm/hpclj2500.tar.gz
Source11:       http://foo2hp.rkkda.com/icm/hpclj2600n.tar.gz
Source12:       http://foo2hp.rkkda.com/icm/hp1215.tar.gz
Source13:       http://foo2zjs.rkkda.com/icm/hp-cp1025.tar.gz
Source14:       http://foo2lava.rkkda.com/icm/km2530.tar.gz
Source15:       http://foo2lava.rkkda.com/icm/km-1600.tar.gz
Source16:       http://foo2qpdl.rkkda.com/icm/samclp300.tar.gz
Source17:       http://foo2qpdl.rkkda.com/icm/samclp315.tar.gz
Source18:       http://foo2slx.rkkda.com/icm/lexc500.tar.gz
Source19:       http://foo2hiperc.rkkda.com/icm/okic3200.tar.gz
Source20:       http://foo2hiperc.rkkda.com/icm/okic3400.tar.gz
Source21:       http://foo2hiperc.rkkda.com/icm/okic5600.tar.gz
Source22:       http://foo2hiperc.rkkda.com/icm/okic310.tar.gz
Source23:       http://foo2hiperc.rkkda.com/icm/okic301.tar.gz
Source24:       http://foo2hiperc.rkkda.com/icm/okic810.tar.gz
# Don't try to fetch firmware when we already have it.
Patch0:         disable-fetch.diff
Patch2:         no-osx.diff

Requires:       ghostscript-x11 foomatic-filters
BuildRequires:  ghostscript-x11 foomatic-filters wget bc cups-devel
# BuildArch:      noarch

%description
foo2zjs is an open source printer driver for printers that use the
Zenographics ZjStream wire protocol for their print data, such as HP LaserJet
Pro P1566.

%prep
%setup -q -n %{name}
cp $RPM_SOURCE_DIR/*.tar.gz .
%patch0 -p1
%patch2 -p1

%build
make %{?_smp_mflags}
./getweb all

%install
mkdir -p %{buildroot}$(cups-config --serverbin)/filter
mkdir -p %{buildroot}%{_datadir}/cups/model
make install DESTDIR=%{buildroot}
# Fix broken symlink
ln -sf /usr/bin/command2foo2lava-pjl %{buildroot}$(cups-config --serverbin)/filter/command2foo2lava-pjl
# Avoid duplicated files
ln -sf %{_datadir}/foo2hp/icm/km2430_0.icm %{buildroot}%{_datadir}/foo2zjs/icm/km2430_0.icm
ln -sf %{_datadir}/foo2zjs/icm/km2430_1.icm %{buildroot}%{_datadir}/foo2hp/icm/km2430_1.icm
ln -sf %{_datadir}/foo2oak/icm/hpclj2600n-0.icm %{buildroot}%{_datadir}/foo2hp/icm/hpclj2600n-0.icm
ln -sf %{_datadir}/foo2hp/icm/hpclj2600n-1.icm %{buildroot}%{_datadir}/foo2oak/icm/hpclj2600n-1.icm
ln -sf %{_datadir}/foo2zjs/icm/km2430_2.icm %{buildroot}%{_datadir}/foo2hp/icm/km2430_2.icm
# Avoid non-redistributable files
find %{buildroot} -name hpclj2600n-1.icm \
	-o -name samclp300-0.icm \
	-o -name km2530-jconner-d50.icm \
	-o -name hp1215-argyll-0.icm \
	-o -name samclp315-argyll-0.icm \
	-o -name km-1600-rgb-392-bpp1.icm \
	-o -name hp-cp1025-rgb-392-bpp1.icm \
	-exec rm -v {} \;
# Avoid unnecessary documentation
rm -v %{buildroot}%{_datadir}/doc/foo2zjs/INSTALL

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/bin/usb_printerid
%{_bindir}/*
%{_datadir}/doc/foo2zjs/*
%{_datadir}/foo2qpdl/crd/*
%{_datadir}/foo2zjs/*
%{_datadir}/man/man1/*
%{_datadir}/foo2hiperc/icm/*
%{_datadir}/foo2hp/icm/*
%{_datadir}/foo2lava/icm/*
%{_datadir}/foo2oak/icm/*
%{_datadir}/foo2qpdl/icm/*
%{_datadir}/foo2slx/icm/*
%{_datadir}/foo2xqx/firmware/*
%{_datadir}/cups/model/*
/usr/lib/cups/filter/*
%dir /usr/lib/cups/filter
%dir %{_datadir}/doc/foo2zjs
%dir %{_datadir}/foo2qpdl
%dir %{_datadir}/foo2qpdl/crd
%dir %{_datadir}/foo2qpdl/icm
%dir %{_datadir}/foo2zjs
%dir %{_datadir}/foo2hiperc
%dir %{_datadir}/foo2hiperc/icm
%dir %{_datadir}/foo2hp
%dir %{_datadir}/foo2hp/icm
%dir %{_datadir}/foo2lava
%dir %{_datadir}/foo2lava/icm
%dir %{_datadir}/foo2oak
%dir %{_datadir}/foo2oak/icm
%dir %{_datadir}/foo2slx
%dir %{_datadir}/foo2slx/icm
%dir %{_datadir}/foo2xqx
%dir %{_datadir}/foo2xqx/firmware
%dir %{_datadir}/cups
%dir %{_datadir}/cups/model

%changelog

#
# spec file for package cpm
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

Name:           cpm
Version:        0.23beta
Release:        2
Summary:        Console Password Manager
Group:          Productivity/Security
License:        GPLv2+
URL:            http://www.harry-b.de/dokuwiki/doku.php?id=harry:cpm
Source0:        http://downloads.sourceforge.net/passwordms/cpm-0.23beta.tar.gz
Source1:        permissions
Source2:        permissions.easy
Source3:        %{name}-rpmlintrc
Patch0:         cpm-0.23beta-open.patch
Patch1:         cpm-0.23beta-make.patch
Patch2:         configure.diff

BuildRequires:  ncurses-devel libxml2-devel dotconf-devel cracklib-devel
BuildRequires:  cracklib-dict-full gpgme-devel cdk-devel
PreReq:         permissions
# BuildArch:      noarch

%description
CPM is a ncurses based console tool to manage passwords and store them public
key encrypted in a file - even for more than one person. The encryption is
handled via GnuPG so the programs data can be accessed via gpg as well, in case
you want to have a look inside. The data is stored as as zlib compressed XML so
it's even possible to reuse the data for some other purpose.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p0
sed -i 's,diff -u current.txt new.txt,diff -u current.txt new.txt || :,' Makefile.in
sed -i 's,-Wall,-Wall -fPIE,;s,^LDFLAGS=,LDFLAGS=-pie ,' Makefile.in

%build
CFLAGS="$(ncursesw6-config --cflags)"
LDFLAGS="$(ncursesw6-config --libs)"
%global optflags    %{optflags} -D_REENTRANT $LDFLAGS $CFLAGS
%configure --with-crack-dict=/usr/lib/cracklib_dict
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} mandir="%{_mandir}"
%__install -D -m 644 conf/cpmrc-default %{buildroot}%{_sysconfdir}/cpmrc
%{find_lang} cpm
%__install -D -m 644 %{S:1} %{buildroot}%{_sysconfdir}/permissions.d/%{name}
%__install -m 644 %{S:2} %{buildroot}%{_sysconfdir}/permissions.d/%{name}.easy

%clean
rm -rf %{buildroot}

%post
%set_permissions %{_bindir}/cpm

%verifyscript
%verify_permissions -e %{_bindir}/cpm

%files -f cpm.lang
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/cpmrc
%config(noreplace) %{_sysconfdir}/permissions.d/*
%verify(not mode) %attr (4755,root,root) %{_bindir}/cpm
%doc docs/*
%{_mandir}/man1/*

%changelog

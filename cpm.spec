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
Release:        1
Summary:        Console Password Manager

License:        GPLv2+
URL:            http://www.harry-b.de/dokuwiki/doku.php?id=harry:cpm
Source0:        http://downloads.sourceforge.net/passwordms/cpm-0.23beta.tar.gz

BuildRequires:  ncurses-devel libxml2-devel dotconf-devel cracklib-devel gpgme-devel cdk-devel
Requires:       
# BuildArch:      noarch

%description
CPM is a ncurses based console tool to manage passwords and store them public
key encrypted in a file - even for more than one person. The encryption is
handled via GnuPG so the programs data can be accessed via gpg as well, in case
you want to have a look inside. The data is stored as as zlib compressed XML so
it's even possible to reuse the data for some other purpose.

%prep
%setup -q -n %{name}-%{version}
sed -i 's,diff -u current.txt new.txt,diff -u current.txt new.txt || :,' Makefile.in

%build
%configure --with-crack-dict=%{_libdir}/cracklib_dict
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -D -p -m 644 conf/cpmrc-default %{buildroot}%{_sysconfdir}/cpmrc
%{find_lang} cpm

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/cpmrc
%attr (4755,root,root) %{_bindir}/cpm
%doc docs/*
%{_mandir}/man1/cpm*

%changelog

#
# spec file for package python-gtimelog
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gtimelog
Version:        0.2.3
Release:        1
License:        GPL-2.0
Summary:        A Gtk+ time tracking application
Url:            http://cgit.collabora.com/git/gtimelog.git/
Group:          Productivity/Office/Management
Source:         http://cgit.collabora.com/git/gtimelog.git/snapshot/gtimelog-0.2.3-g563ddf3.tar.bz2
BuildRequires:  python-devel python-distribute
Requires:       python-setuptools
Requires:       typelib-1_0-Gtk-3_0
Requires:       typelib-1_0-Notify-0_7
Requires:       typelib-1_0-Soup-2_4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
Simple and unintrusive time-tracking application.

There are screenshots at http://mg.pov.lt/gtimelog.

Mailing list: http://groups.google.com/group/gtimelog

Bugs: http://bugs.launchpad.net/gtimelog/

Source code: http://code.launchpad.net/gtimelog/


%prep
%setup -q -n gtimelog-%{version}-g563ddf3

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
mkdir -p %{buildroot}/usr/share/pixmaps
cp src/gtimelog/gtimelog.png %{buildroot}/usr/share/pixmaps
mkdir -p %{buildroot}/usr/share/applications
sed -i 's|Categories=Utility;|Categories=Office;ProjectManagement;|' gtimelog.desktop
sed -i 's|Icon=gnome-week.png|Icon=gtimelog|' gtimelog.desktop
cp gtimelog.desktop %{buildroot}/usr/share/applications

%files
%defattr(-,root,root,-)
%doc README.txt NEWS.txt
%{python_sitelib}/*
/usr/bin/gtimelog
/usr/share/applications/gtimelog.desktop
/usr/share/pixmaps/gtimelog.png

%changelog

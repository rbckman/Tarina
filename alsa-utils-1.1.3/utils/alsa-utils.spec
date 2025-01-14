%define ver      1.1.3
%define rel      1

Summary: Advanced Linux Sound Architecture (ALSA) - Utils
Name: alsa-utils
Version: %ver
Release: %rel
Copyright: GPL
Group: System/Libraries
Source: ftp://ftp.alsa-project.org/pub/utils/alsa-utils-%{ver}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.alsa-project.org
Requires: alsa-lib ncurses
BuildRequires: alsa-lib-devel ncurses-devel gettext

%description

Advanced Linux Sound Architecture (ALSA) - Utils

%changelog
* Sun Oct  1 2006 Jaroslav Kysela <perex@perex.cz>
- add gettext to BuildRequires
- add more files (see alsa bug#2139)

* Tue Nov 25 2003 Ronny V. Vindenes <sublett@amigascne.org>
- include all manpages

* Thu Mar  6 2003 Ronny V. Vindenes <sublett@dc-s.com>

- removed wrongly included doc file
- changed BuildRoot from /var/tmp to _tmppath
- use standard rpm macros for build & install section
- updated dependencies

* Tue Nov 20 2001 Jaroslav Kysela <perex@perex.cz>

- changed BuildRoot from /tmp to /var/tmp
- _prefix and _mandir macros are used for configure and mkdir
- DESTDIR is used for make install

* Sun Nov 11 2001 Miroslav Benes <mbenes@tenez.cz>

- dangerous command "rpm -rf $RPM_BUILD_ROOT" checks $RPM_BUILD_ROOT variable
- unset key "Docdir" - on some new systems are documentation in /usr/share/doc

* Mon May 28 1998 Helge Jensen <slog@slog.dk>

- Made SPEC file

%prep
%setup
%build
%configure
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc ChangeLog COPYING README

%{_prefix}/sbin/*
%{_prefix}/bin/*
%{_mandir}/man?/*
%{_mandir}/fr/man?/*
%{_prefix}/share/alsa/speaker-test/*
%{_prefix}/share/locale/ja/LC_MESSAGES/*
%{_prefix}/share/locale/ru/LC_MESSAGES/*
%{_prefix}/share/man/fr/man8/alsaconf.8.gz
%{_prefix}/share/sounds/alsa/*

Summary: 	A Night Stalker(MT) clone.
Name:		afternoonstalker
Version:	1.0.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www3.sympatico.ca/sarrazip/dev/%{name}-%{version}.tar.gz
URL:		http://sarrazip.com/dev/afternoonstalker.html
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	gengameng-devel >= 4.1
Requires: 	gengameng >= 4.1
Requires:	SDL >= 1.2.0
Requires:	SDL_image >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Clone of the Intellivision game Night Stalker.  The player is in
a two-dimensional maze in which you are attacked by robots that
shoot at you and that you must shoot down.  You must pick up a
gun somewhere in the maze in order to have a few bullets to shoot.
Avoid the spiders and the bats, which can paralyze you long enough
for a robot to come and shoot you.  The bunker in the center offers
some protection, but the door is open to the robots' bullets.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT/%{_applnkdir}/Games/Arcade
mv $RPM_BUILD_ROOT/%{_datadir}/gnome/apps/Games/* $RPM_BUILD_ROOT/%{_applnkdir}/Games/Arcade

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/sounds/%{name}
%{_datadir}/%{name}/*
%{_datadir}/sounds/%{name}/*
%{_pixmapsdir}/%{name}.png
%{_applnkdir}/Games/Arcade/%{name}.desktop
%lang(en) %{_mandir}/man6/%{name}.6.gz

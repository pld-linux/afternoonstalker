Summary:	A Night Stalker(TM) clone
Summary(pl):	Klon gry Night Stalker(TM)
Name:		afternoonstalker
Version:	1.0.1
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www3.sympatico.ca/sarrazip/dev/%{name}-%{version}.tar.gz
# Source0-md5:	5357e88c14f76bad94b84f099d31a606
URL:		http://sarrazip.com/dev/afternoonstalker.html
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	gengameng-devel >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Clone of the Intellivision game Night Stalker. The player is in a
two-dimensional maze in which you are attacked by robots that shoot at
you and that you must shoot down. You must pick up a gun somewhere in
the maze in order to have a few bullets to shoot. Avoid the spiders
and the bats, which can paralyze you long enough for a robot to come
and shoot you. The bunker in the center offers some protection, but
the door is open to the robots' bullets.

%description -l pl
Jest to klon gry Intellivision o nazwie Night Stalker. Gracz jest w
dwuwymiarowym labiryncie, w którym jest atakowany przez strzelaj±ce w
niego roboty, które musi wystrzelaæ. Musi odnale¼æ broñ ukryt± w
labiryncie, aby mieæ pociski do strzelania. Trzeba unikaæ paj±ków i
nietoperzy, które parali¿uj± gracza na wystarczaj±co d³ugo, by jaki¶
robot zd±¿y³ go zastrzeliæ. Bunkier w centrum daje pewne
zabezpieczenie, ale drzwi s± otwarte dla pocisków robotów.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomedesktopentrydir=%{_applnkdir}/Games/Arcade

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/sounds/%{name}
%{_pixmapsdir}/%{name}.png
%{_applnkdir}/Games/Arcade/%{name}.desktop
%{_mandir}/man6/%{name}.6*

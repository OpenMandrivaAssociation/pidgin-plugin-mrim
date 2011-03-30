%define	PackageName	mrim-prpl
Summary: 	MRIM Plugin for libpurple and derived IM clients
Summary(ru):	Плагин для мессенджера Pidgin добавляющий поддержку протокола MMP (Mail.ru Agent)
Name: 		pidgin-plugin-mrim
Version: 	0.1.26
Release: 	%mkrel 1
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://code.google.com/p/mrim-prpl/
Source0:	http://mrim-prpl.googlecode.com/files/mrim-prpl-%{version}.tar.gz
Packager: 	Sergey Zhemoitel <djam5@ya.ru>

BuildRequires: 	libpurple-devel


%description
All the other plugins for all libpurple derived clients.

%description -l ru
Плагин поддерживающий взаимодействие с пользователями сети Mail.ru

%prep
%setup -q -n %PackageName

%build
%make

%install
install -Dm0644 mrim.so %{buildroot}/%{_libdir}/purple-2/mrim.so
install -Dm0644 pixmaps/mrim16.png %{buildroot}/%{_datadir}/pixmaps/pidgin/protocols/16/mrim.png
install -Dm0644 pixmaps/mrim22.png %{buildroot}/%{_datadir}/pixmaps/pidgin/protocols/22/mrim.png
install -Dm0644 pixmaps/mrim32.png %{buildroot}/%{_datadir}/pixmaps/pidgin/protocols/32/mrim.png

%files
%doc README LICENSE TODO
%{_libdir}/purple-2/mrim.so
%{_datadir}/pixmaps/pidgin/protocols/*/mrim.png

%changelog
* Sat Dec 13 2010 Sergey Zhemoitel <djam5@ya.ru> 0.1.26-1mdv2010.1
- New version 0.1.26

* Thu Nov 04 2010 Sergey Zhemoitel <djam5@ya.ru> 0.1.1-1mdv2010.1
- rebuild for Mandriva 2010.1

* Thu Sep 02 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1.1-alt1.r8
- Core
	support pidgin 2.3.1+
	downgrade to protocol 1.9
- Account
	fix remove buddy issue
	fix authorize buddy issue
- Other
	Links "Set user info" and "Set avatar" 

* Thu Aug 26 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt1.r22
- Roster
	Group deletion fix (segfault)
	Add + Modify phones
	fix mrim_add_buddy bug(wrong pq->seq)
- Account
	Fix a crash on disconnect
- Messages
	Now, maximum mesage size is 65Kb. (1kb before)
	Free SMS

* Sat Jul 24 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt1.r21
- improve contact list

* Fri Jun 25 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt1.r19
- new revision
- initial build for ALT Linux Sisyphus

* Sat May 01 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt1.r15
- improve offline messages support

* Fri Apr 09 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt1.r13
- add avatars support
- depencies fix
- spec cleanup

* Sun Mar 28 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt0.r11.1
- add offline messages support

* Sun Mar 28 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt0.r10.1
- new revision

* Wed Mar 17 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt0.r9.1
- new revision

* Sun Mar 14 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt0.r8.1
- spec cleanup
- new revision

* Fri Mar 12 2010 Anton A. Vinogradov <arc@altlinux.org> r6-alt1
- initial build for ALT Linux


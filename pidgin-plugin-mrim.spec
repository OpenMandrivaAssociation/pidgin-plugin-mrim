%define	PackageName	mrim-prpl

Summary:	MRIM Plugin for libpurple and derived IM clients
Name:		pidgin-plugin-mrim
Version:	0.1.28
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://code.google.com/p/mrim-prpl/
Source0:	http://mrim-prpl.googlecode.com/files/mrim-prpl-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}_%{version}-build

#BuildRequires:	libpurple-devel
%ifarch x86_64
BuildRequires:	lib64purple-devel
%else
BuildRequires:	libpurple-devel
%endif

%description
All the other plugins for all libpurple derived clients.

%prep
%setup -q -n %PackageName-%{version}

%build
./configure --gtk --libdir=%{_libdir}
%make

%install
rm -rf %{buildroot}
install -Dm0644 libmrim.so %{buildroot}/%{_libdir}/purple-2/libmrim.so
install -Dm0644 pixmaps/mrim16.png %{buildroot}/%{_datadir}/pixmaps/pidgin/protocols/16/mrim.png
install -Dm0644 pixmaps/mrim22.png %{buildroot}/%{_datadir}/pixmaps/pidgin/protocols/22/mrim.png
install -Dm0644 pixmaps/mrim32.png %{buildroot}/%{_datadir}/pixmaps/pidgin/protocols/32/mrim.png

%files
%defattr (-,root,root,0755)
%doc README LICENSE TODO
%{_libdir}/purple-2/libmrim.so
%{_datadir}/pixmaps/pidgin/protocols/*/mrim.png

%clean
rm -rf %{buildroot}

%changelog
* Thu Jul 21 2011 Sergey Zhemoitel <serg@mandriva.org> 0.1.28-1mdv2012.0
+ Revision: 690794
- fix arch x86_64
- fix macros
- imported package pidgin-plugin-mrim
- new release 0.1.28
- clean changelog
- update new version 0.1.26
- imported package pidgin-plugin-mrim


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


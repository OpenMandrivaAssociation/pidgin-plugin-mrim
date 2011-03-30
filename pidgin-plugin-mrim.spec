%define	PackageName	mrim-prpl
Summary: 	MRIM Plugin for libpurple and derived IM clients
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

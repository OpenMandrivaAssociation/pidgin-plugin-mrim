Summary: MRIM Plugin for libpurple and derived IM clients
Name: pidgin-plugin-mrim
Version: 0.1.1
Release: %mkrel 1
License: GPLv2+
Group: Networking/Instant messaging
Url: http://fireforge.net/mediawiki/index.php/Mrim-prpl

Packager: Sergey Zhemoitel <djam5@ya.ru>

Source: %name.tar.gz

BuildRequires: libpurple-devel

%description
All the other plugins for all libpurple derived clients.

%prep
%setup -q -n %name

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


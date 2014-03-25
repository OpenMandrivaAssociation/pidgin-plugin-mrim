%define	PackageName	mrim-prpl
%define debug_package %{nil}

Summary:	MRIM Plugin for libpurple and derived IM clients
Name:		pidgin-plugin-mrim
Version:	0.1.28
Release:	2
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://code.google.com/p/mrim-prpl/
Source0:	http://mrim-prpl.googlecode.com/files/mrim-prpl-%{version}.tar.gz

BuildRequires:	pkgconfig(purple)

%description
All the other plugins for all libpurple derived clients.

%prep
%setup -q -n %PackageName-%{version}

%build
./configure --gtk --libdir=%{_libdir}
%make

%install
install -Dm0644 libmrim.so %{buildroot}/%{_libdir}/purple-2/libmrim.so
install -Dm0644 pixmaps/mrim16.png %{buildroot}/%{_datadir}/pixmaps/pidgin/protocols/16/mrim.png
install -Dm0644 pixmaps/mrim22.png %{buildroot}/%{_datadir}/pixmaps/pidgin/protocols/22/mrim.png
install -Dm0644 pixmaps/mrim32.png %{buildroot}/%{_datadir}/pixmaps/pidgin/protocols/32/mrim.png

%files
%defattr (-,root,root,0755)
%doc README LICENSE TODO
%{_libdir}/purple-2/libmrim.so
%{_datadir}/pixmaps/pidgin/protocols/*/mrim.png

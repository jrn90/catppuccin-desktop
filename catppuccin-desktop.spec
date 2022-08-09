Name:           catppuccin-desktop
Version:        0.0.5
Release:        1%{?dist}
Summary:        A catppuccin inspired desktop for Fedora Silverblue 
BuildArch:      noarch

License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       bash
Requires:       gnome-tweak-tool
Requires:       i3-gaps
Requires:       network-manager-applet
Requires:       nitrogen
Requires:       polybar
Requires:       rofi

%description
A Catppuccin inspired desktop for Fedora Silverblue

%prep
%autosetup

%install
install -d %{buildroot}%{_datadir}/xsessions
cp src/usr/share/xsessions/catppuccin.desktop %{buildroot}%{_datadir}/xsessions/catppuccin.desktop

%files
%license LICENSE
%doc README.md

%{_datadir}/xsessions/catppuccin.desktop

%changelog
* Tue Aug 09 2022 jrn90 <joe@joenash.org> 0.0.5-1
- updated README and spec for required programs

* Tue Aug 09 2022 jrn90 <joe@joenash.org> 0.0.4-1
- fixed spec issue with datadir

* Tue Aug 09 2022 jrn90 <joe@joenash.org> 0.0.3-1
- updated spec file

* Tue Aug 09 2022 jrn90 <joe@joenash.org> 0.0.2-1
- new package built with tito

* Tue Aug 09 2022 jrn90 <joe@joenash.org>
- 

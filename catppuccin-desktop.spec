Name:           catppuccin-desktop
Version:        0.0.7
Release:        1%{?dist}
Summary:        A catppuccin inspired desktop for Fedora Silverblue 
BuildArch:      noarch

License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       bash
Requires:       gnome-tweak-tool
Requires:       i3-gaps
Requires:       network-manager-applet
Requires:       feh
Requires:       polybar
Requires:       rofi

%description
A Catppuccin inspired desktop for Fedora Silverblue

%prep
%autosetup

%install
install -d %{buildroot}%{_datadir}/xsessions
cp src/usr/share/xsessions/catppuccin.desktop %{buildroot}%{_datadir}/xsessions/catppuccin.desktop

install -d %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds
cp src/usr/share/catppuccin-desktop/backgrounds/buttons.png %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/buttons.png
cp src/usr/share/catppuccin-desktop/backgrounds/cat-sound.png %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/cat-sound.png
cp src/usr/share/catppuccin-desktop/backgrounds/clearday.jpg %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/clearday.jpg
cp src/usr/share/catppuccin-desktop/backgrounds/clouds-night.jpg %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/clouds-night.jpg
cp src/usr/share/catppuccin-desktop/backgrounds/fedora-black-4k.png %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/fedora-black-4k.png
cp src/usr/share/catppuccin-desktop/backgrounds/flatppuccin_4k_macchiato.png %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/flatppuccin_4k_macchiato.png
cp src/usr/share/catppuccin-desktop/backgrounds/forrest.png %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/forrest.png
cp src/usr/share/catppuccin-desktop/backgrounds/hashtags-black.png %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/hashtags-black.png
cp src/usr/share/catppuccin-desktop/backgrounds/hearts.png %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/hearts.png
cp src/usr/share/catppuccin-desktop/backgrounds/shaded-landscape.png %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/shaded-landscape.png
cp src/usr/share/catppuccin-desktop/backgrounds/tetris.png %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/tetris.png
cp src/usr/share/catppuccin-desktop/backgrounds/tropic-island-day.jpg %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds/tropic-island-day.jpg

%files
%license LICENSE
%doc README.md

%{_datadir}/xsessions/catppuccin.desktop

%{_datadir}/catppuccin-desktop/backgrounds/buttons.png
%{_datadir}/catppuccin-desktop/backgrounds/cat-sound.png
%{_datadir}/catppuccin-desktop/backgrounds/clearday.jpg
%{_datadir}/catppuccin-desktop/backgrounds/clouds-night.jpg
%{_datadir}/catppuccin-desktop/backgrounds/fedora-black-4k.png
%{_datadir}/catppuccin-desktop/backgrounds/flatppuccin_4k_macchiato.png
%{_datadir}/catppuccin-desktop/backgrounds/forrest.png
%{_datadir}/catppuccin-desktop/backgrounds/hashtags-black.png
%{_datadir}/catppuccin-desktop/backgrounds/hearts.png
%{_datadir}/catppuccin-desktop/backgrounds/shaded-landscape.png
%{_datadir}/catppuccin-desktop/backgrounds/tetris.png
%{_datadir}/catppuccin-desktop/backgrounds/tropic-island-day.jpg

%changelog
* Wed Aug 10 2022 jrn90 <joe@joenash.org> 0.0.7-1
- moved from nitrogen to feh
- added backgrounds 

* Tue Aug 09 2022 jrn90 <joe@joenash.org> 0.0.6-1
- 

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

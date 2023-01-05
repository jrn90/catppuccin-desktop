Name:           catppuccin-desktop
Version:        0.0.28
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
mkdir -p %{buildroot}%{_sysconfdir}/catppuccin-desktop/i3
cp src/etc/catppuccin-desktop/i3/config %{buildroot}%{_sysconfdir}/catppuccin-desktop/i3/config

mkdir -p %{buildroot}%{_bindir}/
cp src/usr/bin/catppuccin-desktop %{buildroot}%{_bindir}/catppuccin-desktop
cp src/usr/bin/catppuccin-desktop %{buildroot}%{_bindir}/catppuccin-desktop-init

mkdir -p %{buildroot}/usr/lib/catppuccin-desktop
cp src/usr/lib/catppuccin-desktop/common.sh %{buildroot}/usr/lib/catppuccin-desktop/common.sh

mkdir -p %{buildroot}%{_datadir}/applications
cp src/usr/share/applications/catppuccin-desktop.desktop %{buildroot}%{_datadir}/applications/catppuccin-desktop.desktop

mkdir -p %{buildroot}%{_datadir}/gnome-session/sessions
cp src/usr/share/gnome-session/sessions/catppuccin-desktop.session %{buildroot}%{_datadir}/gnome-session/sessions/catppuccin-desktop.session

mkdir -p %{buildroot}%{_datadir}/xsessions
cp src/usr/share/xsessions/catppuccin.desktop %{buildroot}%{_datadir}/xsessions/catppuccin.desktop

mkdir -p %{buildroot}%{_datadir}/catppuccin-desktop/backgrounds
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

%{_sysconfdir}/catppuccin-desktop/i3/config

%{_bindir}/catppuccin-desktop
%{_bindir}/catppuccin-desktop-init

/usr/lib/catppuccin-desktop/common.sh

%{_datadir}/applications/catppuccin-desktop.desktop

%{_datadir}/gnome-session/sessions/catppuccin-desktop.session

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
* Thu Jan 05 2023 jrn90 <jrnash20650@gmail.com> 0.0.28-1
- rpm build forgot file (jrnash20650@gmail.com)

* Thu Jan 05 2023 jrn90 <jrnash20650@gmail.com> 0.0.27-1
- updated rpm build for sessions (jrnash20650@gmail.com)

* Thu Jan 05 2023 jrn90 <jrnash20650@gmail.com> 0.0.26-1
- attempting cleanup of sessions (jrnash20650@gmail.com)

* Thu Jan 05 2023 jrn90 <jrnash20650@gmail.com> 0.0.25-1
- initial session handling (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.24-1
- added executable (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.23-1
- changed bash location (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.22-1
- attempt fix at xsessions (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.21-1
- percent (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.20-1
- bleh (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.19-1
- lib fix (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.18-1
- 

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.17-1
- 

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.16-1
- Automatic commit of package [catppuccin-desktop] release [0.0.15-1].
  (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.15-1
- fix lib mismash (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.14-1
- bug: forgot i3 config (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.13-1
- added default i3 config (jrnash20650@gmail.com)
- removed rust install (duh) (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.12-1
- Updated deps (jrnash20650@gmail.com)

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.11-1
- 

* Wed Jan 04 2023 jrn90 <jrnash20650@gmail.com> 0.0.10-1
- Added startup script (jrnash20650@gmail.com)

* Wed Aug 10 2022 jrn90 <joe@joenash.org> 0.0.9-1
- added backgrounds (joe@joenash.org)

* Wed Aug 10 2022 jrn90 <joe@joenash.org> 0.0.8-1
- 

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

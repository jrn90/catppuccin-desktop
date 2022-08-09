Name:           catppuccin-desktop
Version:        0.0.2
Release:        1%{?dist}
Summary:        A catppuccin inspired desktop for Fedora Silverblue 
BuildArch:      noarch

License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       bash

%description
A Catppuccin inspired desktop for Fedora Silverblue

%prep
%autosetup

%install
cp src/usr/share/xsessions/catppuccin.desktop %{buildroot}%{_datadir}/xsessions/

%files
%license LICENSE
%doc README.md

${_datadir}/xsessions/catppuccin.desktop

%changelog
* Tue Aug 09 2022 jrn90 <joe@joenash.org> 0.0.2-1
- new package built with tito

* Tue Aug 09 2022 jrn90 <joe@joenash.org>
- 

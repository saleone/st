Name: st
Version: 0.8.1s
Release: 1%{?dist}
Summary: Simple terminal from suckless patched by saleone.

License: MIT
URL: https://github.com/saleone/st
Source0: https://github.com/saleone/st/archive/%{version}.tar.gz

BuildRequires: gcc
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel

%description
Simple terminal from suckless patched by saleone.

%define debug_package %{nil}

%prep
%autosetup

%build
%make_build


%install
%make_install

%files
/usr/local/bin/st
/usr/local/share/man/man1/st.1

%changelog
* Mon Apr 1 2019 Saša Savić <sasa@sasa-savic.com> 0.8.1s-1
- Initial RPM release


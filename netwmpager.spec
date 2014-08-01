Summary:	EWMH (NetWM) compatible pager
Summary(pl.UTF-8):	Program stronicujący zgodny z EWMH (NetWM)
Name:		netwmpager
Version:	2.05
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/sf-xpaint/%{name}-%{version}.tar.bz2
# Source0-md5:	622485be511d3258c892c68ccccc87a6
URL:		http://sourceforge.net/projects/sf-xpaint/
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
netwmpager is an EWMH (NetWM) compatible pager. Works with Openbox and
other EWMH compliant window managers.

%description -l pl.UTF-8
netwmpager to program stronicujący zgodny z EWMH (NetWM). Współpracuje
z Openboksem oraz innymi zarządcami okien zgodnymi z EWMH.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog doc/*.pdf
%attr(755,root,root) %{_bindir}/netwmpager
%{_datadir}/netwmpager

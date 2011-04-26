# TODO
# - memleak: https://bugzilla.xfce.org/show_bug.cgi?id=7363
Summary:	User switching applet for XFCE4 panel
Summary(pl.UTF-8):	Przełączanie między użytkownikami
Name:		xfce4-xfswitch-plugin
Version:	0.0.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfswitch-plugin/0.0/xfswitch-plugin-%{version}.tar.gz
# Source0-md5:	cb204f4a507f462d019529af6f547731
Patch0:		%{name}-ui.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfswitch-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a user switching plugin for the Xfce4 Panel.
It allows you to leave the current session opened and open a
new session with another user. At the moment it relies on GDM,
but other display managers will be supported in the future. 

%description -l pl.UTF-8
Ta wtyczka dla panelu Xfce4 pozwala przełączać między użytkownikami.
Obecnie działa tylko z GDM-em.

%prep
%setup -q -n xfswitch-plugin-%{version}
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang xfswitch-plugin

%clean
rm -rf $RPM_BUILD_ROOT

%files -f xfswitch-plugin.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfswitch-plugin
%{_datadir}/xfce4/panel-plugins/xfswitch-plugin.desktop

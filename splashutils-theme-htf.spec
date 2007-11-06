%define		theme	htf
Summary:	Splashutils - Happy Tree Friends theme
Name:		splashutils-theme-%{theme}
Version:	1.0
Release:	0.2
License:	?
Group:		Themes
Source0:	htf-toothy.tar.bz2
# Source0-md5:	bda05e60e3d305bd11a29ba4bf882181
Source1:	http://happytreefriends.atomfilms.com/goodies/images/desktop_patterns/toothy_800x600.jpg
# NoSource1-md5:	134254f17c9852b744ac646ec7e895d5
NoSource:	1
Source2:	http://happytreefriends.atomfilms.com/goodies/images/desktop_patterns/toothy_1024x768.jpg
# NoSource2-md5:	843736690c51347697eaf8c25f0d395a
NoSource:	2
Source3:	http://happytreefriends.atomfilms.com/goodies/images/desktop_patterns/toothy_1280x1024.jpg
# NoSource3-md5:	864cb7ed8ec91dad4203d4f9b8008013
NoSource:	3
Requires:	splashutils
Provides:	fbsplash-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/splash

%description
Happy Tree Friends theme for splashutils.

%prep
%setup -qc
cp -a %{SOURCE1} .
cp -a %{SOURCE2} .
cp -a %{SOURCE3} .

%install
rm -rf $RPM_BUILD_ROOT
THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/toothy
install -d $THEME_DIR/images
install *.cfg $THEME_DIR
install *.jpg $THEME_DIR/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/*

%define		theme	htf
Summary:	Splashutils - Happy Tree Friends theme
Summary(pl.UTF-8):	Splashutils - motyw Happy Tree Friends
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
Source4:	htf-lumpy.tar.bz2
# Source4-md5:	ad3aab3a87668d95d467ee0f09ab00eb
Source5:	http://mondo.happytreefriends.com/goodies/images/desktop_patterns/07_octcal01_800x600.jpg
# NoSource5-md5:	b623022aa05fcaaf74e887bc95fb2b16
NoSource:	5
Source6:	http://mondo.happytreefriends.com/goodies/images/desktop_patterns/07_octcal01_1024x768.jpg
# NoSource6-md5:	1c95b3e4fa9f04e484f4508ba6d59861
NoSource:	6
Source7:	http://mondo.happytreefriends.com/goodies/images/desktop_patterns/07_octcal01_1280x1024.jpg
# NoSource7-md5:	c6d82b90095e2a9bdb3a10fe1aa2a84d
NoSource:	7
Requires:	splashutils
Provides:	fbsplash-theme
Provides:	splash-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/splash

%description
Happy Tree Friends theme for splashutils.

%description -l pl.UTF-8
Motyw Happy Tree Friends dla splashutils.

%prep
%setup -qcT
# Toothy
install -d toothy/images
tar jxf %{SOURCE0} -C toothy
cp -a %{SOURCE1} toothy/images
cp -a %{SOURCE2} toothy/images
cp -a %{SOURCE3} toothy/images

# Lumpy
install -d lumpy/images
tar jxf %{SOURCE4} -C lumpy
cp -a %{SOURCE5} lumpy/images/lumpy_800x600.jpg
cp -a %{SOURCE6} lumpy/images/lumpy_1024x768.jpg
cp -a %{SOURCE7} lumpy/images/lumpy_1280x1024.jpg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
cp -a toothy lumpy $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/toothy
%{_sysconfdir}/lumpy

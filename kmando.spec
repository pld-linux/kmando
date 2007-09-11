%define rname mando
Summary:	Interactive Camera-Projector System
Name:		kmando
Version:	1.4
Release:	0.1
Source0:	http://vision.eng.shu.ac.uk/jan/mando-%{version}.tar.bz2
# Source0-md5:	d5f6718dda7bbaf361469428f19f8e66
License:	GPL
Group:		Applications/Multimedia
URL:		http://vision.eng.shu.ac.uk/mediawiki/index.php/Interactive_Camera-Projector_System
#BuildRequires:	Mesa-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	blas
BuildRequires:	boost-devel >= 1.33
BuildRequires:	f2c
BuildRequires:	fftw3-devel
#BuildRequires:	freeglut-devel
BuildRequires:	gcc-g77
BuildRequires:	lapack
#BuildRequires:	libgfortran41
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxslt
BuildRequires:	qt4-build
#BuildRequires:	qt4-qmake
#BuildRequires:	update-desktop-files
Requires:	blas
Requires:	boost
Requires:	fftw3
Requires:	freeglut
Requires:	lapack
#Requires:	libqt4 >= 4.2.90
#Requires:	libqt4-x11 >= 4.2.90
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A software for camera-projector interaction. The software makes use of
a low cost off-the shelf webcam that is calibrated against a standard
projector screen. The webcam is used to determine the position of
physical pointer (e.g. a pen) which is then used to virtually move the
X11 pointer. Point-and-click functionality has also been implemented.

%prep
%setup -q -n %{rname}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D mandologo.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
cat > $RPM_BUILD_ROOT%{_desktopdir}/kde/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
GenericName=Interactive Camera-Projector System
Version=%{version}
Type=Application
Exec=%{rname}
Icon=%{name}.png
Terminal=false
Name=Mando
Comment=Control the mouse pointer in a projector using a webcam
StartupNotify=true
Categories=Qt;KDE;Utility;Accessibility;
EOF

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING

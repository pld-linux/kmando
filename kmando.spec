%define rname mando
Summary:	Software to control the mouse pointer in a projector using a webcam
Summary(pl.UTF-8):	Program sterujący wskaźnikiem myszy w projektorze korzystającym z kamery
Name:		kmando
Version:	1.4
Release:	0.2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://vision.eng.shu.ac.uk/jan/mando-%{version}.tar.bz2
# Source0-md5:	d5f6718dda7bbaf361469428f19f8e66
Source1:	%{name}.desktop
URL:		http://vision.eng.shu.ac.uk/mediawiki/index.php/Interactive_Camera-Projector_System
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	QtGui-devel >= 4.3
BuildRequires:	QtOpenGL-devel >= 4.3
BuildRequires:	blas-devel
BuildRequires:	boost-array-devel
BuildRequires:	boost-call_traits-devel
BuildRequires:	boost-devel
BuildRequires:	boost-uBLAS-devel
BuildRequires:	f2c
BuildRequires:	fftw3-devel
BuildRequires:	gcc-fortran
BuildRequires:	lapack-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxslt-devel
BuildRequires:	qt4-build
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A software for camera-projector interaction. The software makes use of
a low cost off-the shelf webcam that is calibrated against a standard
projector screen. The webcam is used to determine the position of
physical pointer (e.g. a pen) which is then used to virtually move the
X11 pointer. Point-and-click functionality has also been implemented.

%description -l pl.UTF-8
Program do interakcji między kamerą a projektorem. Wykorzystuje tanią
kamerę internetową kalibrowaną względem standardowego ekranu
projektora. Kamera służy do określania położenia fizycznego wskaźnika
(np. długopisu), który jest następnie wykorzystywany do przesuwania
wskaźnika X11. Funkcja klikania po wskazaniu jest także
zaimplementowana.

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
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING

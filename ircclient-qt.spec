%define name    ircclient-qt
%define version 0.3.2
%define release %mkrel 1
%define major 1
%define api 0.3
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    	A cross-platform IRC client library written with Qt 4
License:    	GPLv2+
Group:      	Networking/Other
URL:        	http://bitbucket.org/jpnurmi/libircclient-qt/wiki/Home
Source:     	http://bitbucket.org/jpnurmi/libircclient-qt/downloads/libircclient-qt-src-%{version}.tar.gz
Patch0:		libircclient-qt-configure.diff
BuildRequires:  icu-devel
BuildRequires:	qt4-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
IRCclient-qt is a fully Qt-based library to create IRC clients.

%package -n     %{libname}
Summary:        Main library for ircclient-qt
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
IRCclient-qt is a fully Qt-based library to create IRC clients.


%package        -n     %{develname}
Summary:        Header files for the ircclient-qt library
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Requires:  	icu-devel
Requires:  	qt4-devel

%description    -n %{develname}
IRCclient-qt is a fully Qt-based library to create IRC clients.

%prep 
%setup -q -n libircclient-qt-%{version}
%patch0 -p1 -b .fake_configure
chmod +x configure
%configure2_5x
%qmake_qt4 -config release

%build
%make
%install
INSTALL_ROOT=%{?buildroot:%{buildroot}} %makeinstall_std 


%clean
%{__rm} -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc doc/*
%{_libdir}/libircclient-qt.so.%{major}*


%files  -n %{develname}
%doc examples/*
%defattr(-,root,root)
%{qt4include}/ircclient-qt/*
%{_libdir}/libircclient-qt.so
%{qt4dir}/mkspecs/features/libircclient-qt.prf




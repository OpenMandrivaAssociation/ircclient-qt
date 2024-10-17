%define name    ircclient-qt
%define version 0.3.2
%define release 9
%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:    	A cross-platform IRC client library written with Qt 4
License:    	GPLv2+
Group:      	Networking/Other
URL:        	https://bitbucket.org/jpnurmi/libircclient-qt/wiki/Home
Source:     	http://bitbucket.org/jpnurmi/libircclient-qt/downloads/libircclient-qt-src-%{version}.tar.gz
Patch0:		    libircclient-qt-configure.diff
BuildRequires:  icu-devel
BuildRequires:	qt4-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
IRCclient-qt is a fully Qt-based library to create IRC clients.

#--------------------------------------------------------------------

%package -n     %{libname}
Summary:        Main library for ircclient-qt
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
IRCclient-qt is a fully Qt-based library to create IRC clients.

%files -n %{libname}
%defattr(-,root,root)
%doc doc/*
%{_libdir}/libircclient-qt.so.%{major}*

#--------------------------------------------------------------------

%package        -n     %{develname}
Summary:        Header files for the ircclient-qt library
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Requires:  	    icu-devel
Requires:  	    qt4-devel

%description    -n %{develname}
This package includes the header files you will need to compile applications
for %name .

%files  -n %{develname}
%doc examples/*
%defattr(-,root,root)
%{qt4include}/ircclient-qt/*
%{_libdir}/libircclient-qt.so
%{qt4dir}/mkspecs/features/libircclient-qt.prf

#--------------------------------------------------------------------

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



%changelog
* Sun Jun 05 2011 Funda Wang <fwang@mandriva.org> 0.3.2-8mdv2011.0
+ Revision: 682814
- rebuild for new icu

* Sun Mar 20 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.3.2-7
+ Revision: 647070
- Rebuild

* Mon Mar 14 2011 Funda Wang <fwang@mandriva.org> 0.3.2-6
+ Revision: 644573
- rebuild for new icu

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-5mdv2011.0
+ Revision: 612407
- the mass rebuild of 2010.1 packages

* Sun Mar 21 2010 Funda Wang <fwang@mandriva.org> 0.3.2-4mdv2010.1
+ Revision: 526117
- rebuild for new icu

* Fri Mar 19 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.3.2-3mdv2010.1
+ Revision: 525152
- Rebuild

* Fri Nov 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.3.2-2mdv2010.1
+ Revision: 470451
- Fix lib name
- Clean Spec
    - Move file lists on package section
    - Fix description on the devel package
- Remove support for old releases no supported anymore

* Fri Nov 27 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.3.2-1mdv2010.1
+ Revision: 470426
- import ircclient-qt


* Thu Nov 26 2009 Daniel Lucio <dlucio@okay.com.mx> 0.3.2-1mdv2010.0
- First package

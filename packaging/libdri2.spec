
Name:       libdri2
Summary:    X.Org DRI2 Extension client library
Version:    0.1.0
Release:    10.6
Group:      System/Libraries
License:    MIT
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/libdri2.manifest 
BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)


%description
DRI2 Extension client library


%package devel
Summary:    X.Org DRI2 Extension client library (development library)
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libdri2

%description devel
DRI2 Extension client library (development library)


%prep
%setup -q


%build
cp %{SOURCE1001} .

%reconfigure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install










%files
%manifest libdri2.manifest
%defattr(-,root,root,-)
%{_libdir}/libdri2.so.*
%exclude %{_libdir}/dri2.h



%files devel
%manifest libdri2.manifest
%defattr(-,root,root,-)
%{_libdir}/libdri2.so
%{_includedir}/dri2/*
%{_libdir}/pkgconfig/*



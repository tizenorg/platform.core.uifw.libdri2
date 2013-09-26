Name:       libdri2
Summary:    X.Org DRI2 Extension client library
Version:    0.1.0
Release:    11
Group:      System/Libraries
License:    MIT
Source0:    %{name}-%{version}.tar.gz
Source1001: 	libdri2.manifest
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
Requires:   pkgconfig(dri2proto)
Requires:   pkgconfig(xfixes)

%description devel
DRI2 Extension client library (development library)


%prep
%setup -q
cp %{SOURCE1001} .


%build

%ifarch %{ix86}
CFLAGS="$CFLAGS -D_EMUL_" %reconfigure --disable-static
%else
%reconfigure --disable-static
%endif
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
%make_install


%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
/usr/share/license/%{name}
%{_libdir}/libdri2.so.*
%exclude %{_libdir}/dri2.h



%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/libdri2.so
%{_includedir}/dri2/*
%{_libdir}/pkgconfig/*



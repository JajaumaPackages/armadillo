Name:           armadillo
Version:        3.910.0
Release:        1%{?dist}
Summary:        Fast C++ matrix library with interfaces to LAPACK and ATLAS

Group:          Development/Libraries
License:        MPLv2.0
URL:            http://arma.sourceforge.net/
Source:         http://sourceforge.net/projects/arma/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake, boost-devel, blas-devel, lapack-devel, atlas-devel

%description
Armadillo is a C++ linear algebra library (matrix maths)
aiming towards a good balance between speed and ease of use.
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.
Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries.
A delayed evaluation approach is employed (during compile time)
to combine several operations into one and reduce (or eliminate)
the need for temporaries. This is accomplished through recursive
templates and template meta-programming.
This library is useful if C++ has been decided as the language
of choice (due to speed and/or integration capabilities), rather
than another language like Matlab or Octave.


%package devel
Summary:        Development headers and documentation for the Armadillo C++ library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       boost-devel, blas-devel, lapack-devel, atlas-devel, libstdc++-devel

# The header files of Armadillo include some Boost and ATLAS header files,
# delivered within the boost-devel and atlas-devel sub-packages, respectively.
# However, since there is no explicit dependency on Boost or ATLAS libraries
# (most of Boost is delivered as header files only), the RPM building process
# does not detect these dependencies.  These dependencies must therefore be
# added manually.

%description devel
This package contains files necessary for development using the
Armadillo C++ library. It contains header files, example programs,
and user documentation (reference guide).


%prep
%setup -q

# convert DOS end-of-line to UNIX end-of-line

for file in README.txt; do
  sed 's/\r//' $file >$file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done

%build
%{cmake}
%{__make} VERBOSE=1 %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm -f examples/Makefile.cmake
rm -rf examples/example1_win32
rm -rf examples/example2_win32
rm -rf examples/lib_win32


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*
%doc LICENSE.txt

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/armadillo
%{_includedir}/armadillo_bits/
%{_datadir}/Armadillo/
%doc README.txt index.html docs.html
%doc examples armadillo_icon.png
%doc armadillo_nicta_2010.pdf rcpp_armadillo_csda_2013.pdf

%changelog
* Fri Aug 16 2013 José Matos <jamatos@fedoraproject.org> - 3.910.0-1
- update to 3.910.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.900.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 3.900.4-2
- Rebuild for boost 1.54.0

* Wed Jun 12 2013 José Matos <jamatos@fedoraproject.org> - 3.900.4-1
- update to 3.900.4

* Mon May 13 2013 José Matos <jamatos@fedoraproject.org> - 3.820.0-1
- update to 3.820.0

* Tue Apr 30 2013 José Matos <jamatos@fedoraproject.org> - 3.810.2-1
- Update to latest stable version

* Sun Apr 21 2013 José Matos <jamatos@fedoraproject.org> - 3.810.0-1
- Update to latest stable version

* Sun Apr 14 2013 José Matos <jamatos@fedoraproject.org> - 3.800.2-1
- Update to latest stable version

* Sat Mar  2 2013 José Matos <jamatos@fedoraproject.org> - 3.800.0-1
- Update to latest stable version
- License changed from LGPLv3+ to MPLv2.0
- Added another documentation file (rcpp related)
- Spec changelog trimmed

* Thu Feb 21 2013 José Matos <jamatos@fedoraproject.org> - 3.6.3-1
- Update to latest stable release

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.6.2-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.6.2-2
- Rebuild for Boost-1.53.0

* Fri Feb  8 2013 José Matos <jamatos@fedoraproject.org> - 3.6.2-1
- Update to latest stable release

* Mon Dec 17 2012 José Matos <jamatos@fedoraproject.org> - 3.6.1-1
- Update to latest stable release

* Sat Dec  8 2012 José Matos <jamatos@fedoraproject.org> - 3.6.0-1
- Update to latest stable release

* Mon Dec  3 2012 José Matos <jamatos@fedoraproject.org> - 3.4.4-1
- Update to latest stable release
- Clean the spec files (documentation has a special treatment with rpm)

* Wed Jul 25 2012 José Matos <jamatos@fedoraproject.org> - 3.2.4-1
- Update to version 3.2.4

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 15 2011 Conrad Sanderson - 2.2.3-1
- spec updated for Armadillo 2.2.3

* Mon Apr 18 2011 Conrad Sanderson - 1.2.0-1
- spec updated for Armadillo 1.2.0

* Mon Nov 15 2010 Conrad Sanderson - 1.0.0-1
- spec updated for Armadillo 1.0.0

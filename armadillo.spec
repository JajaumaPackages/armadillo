Name:           armadillo
Version:        6.700.6
Release:        1%{?dist}
Summary:        Fast C++ matrix library with interfaces to LAPACK and ATLAS

Group:          Development/Libraries
License:        MPLv2.0
URL:            http://arma.sourceforge.net/
Source:         http://sourceforge.net/projects/arma/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake, blas-devel, lapack-devel, atlas-devel, arpack-devel, hdf5-devel
%if 0%{?fedora} > 23
BuildRequires:  SuperLU43-devel
%else
BuildRequires:  SuperLU-devel
%endif

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
Requires:       blas-devel, lapack-devel, atlas-devel, arpack-devel, hdf5-devel, libstdc++-devel
%if 0%{?fedora} > 23
BuildRequires:  SuperLU43-devel
%else
BuildRequires:  SuperLU-devel
%endif


%description devel
This package contains files necessary for development using the
Armadillo C++ library. It contains header files, example programs,
and user documentation (API reference guide).


%prep
%setup -q

%if 0%{?fedora} > 23
# fix for building using SuperLU43
sed -i 's/\/usr\/include\/SuperLU\//\/usr\/include\/SuperLU43\//' cmake_aux/Modules/ARMA_FindSuperLU.cmake
sed -i 's/NAMES superlu/NAMES superlu43/' cmake_aux/Modules/ARMA_FindSuperLU.cmake
%endif

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
rm -f examples/example1_win64.sln
rm -f examples/example1_win64.vcxproj
rm -f examples/example1_win64.README.txt
rm -rf examples/lib_win64


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_libdir}/*.so.*
%license LICENSE.txt

%files devel
%{_libdir}/*.so
%{_includedir}/armadillo
%{_includedir}/armadillo_bits/
%{_datadir}/Armadillo/
%doc README.txt index.html docs.html
%doc examples armadillo_icon.png
%doc armadillo_nicta_2010.pdf rcpp_armadillo_csda_2014.pdf
%doc mex_interface

%changelog
* Sat May  7 2016 José Matos <jamatos@fedoraproject.org> - 6.700.6-1
- update to 6.700.6

* Fri Apr 15 2016 José Matos <jamatos@fedoraproject.org> - 6.700.4-1
- update to 6.700.4
- superlu43 is only required for Fedora >= 24

* Tue Mar 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 6.600.4-3
- Add SuperLU43 (compat package) as dep
- Fix cmake files for building against SuperLU43

* Sat Mar 26 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 6.600.4-2
- Rebuild for SuperLU soname bump (libsuperlu.so.5.1)

* Tue Mar 15 2016 José Matos <jamatos@fedoraproject.org> - 6.600.4-1
- update to 6.600.4

* Fri Feb 12 2016 José Matos <jamatos@fedoraproject.org> - 6.500.5-1
- update to 6.500.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.500.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 José Matos <jamatos@fedoraproject.org> - 6.500.4-1
- update to 6.500.4
- cleaned spec file: removed %%defattr not needed in any supported
  version of fedora or epel

* Mon Sep 14 2015 José Matos <jamatos@fedoraproject.org> - 5.600.2-1
- update to 5.600.2

* Mon Aug  3 2015 José Matos <jamatos@fedoraproject.org> - 5.300.4-1
- update to 5.300.4
- add %%license tag

* Fri Jul  3 2015 José Matos <jamatos@fedoraproject.org> - 5.200.2-2
- add requires:SuperLU-devel to -devel subpackage

* Thu Jul  2 2015 José Matos <jamatos@fedoraproject.org> - 5.200.2-1
- update to 5.200.2
- add BR SuperLU-devel, required on version 5+

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.650.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.650.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 27 2015 José Matos <jamatos@fedoraproject.org> - 4.650.2-1
- update to 4.650.2

* Fri Feb 13 2015 José Matos <jamatos@fedoraproject.org> - 4.600.4-1
- update to 4.600.4

* Fri Dec  5 2014 Ryan Curtin <ryan@ratml.org> - 4.550.2-1
- update to 4.550.2 for gcc 4.4 bug which is only relevant on EL6

* Fri Nov 28 2014 José Matos <jamatos@fedoraproject.org> - 4.550.0-1
- update to 4.550.0

* Fri Nov 14 2014 José Matos <jamatos@fedoraproject.org> - 4.500.0-1
- update to 4.500.0

* Tue Sep 23 2014 José Matos <jamatos@fedoraproject.org> - 4.450.0-1
- update to 4.450.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.320.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul  4 2014 José Matos <jamatos@fedoraproject.org> - 4.320.0-1
- update to 4.320.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.300.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May  4 2014 José Matos <jamatos@fedoraproject.org> - 4.300.0-2
- add hdf5-devel as build requirement and also as required for the
  -devel sub-package

* Fri May  2 2014 José Matos <jamatos@fedoraproject.org> - 4.300.0-1
- update to 4.300.0

* Wed Apr  9 2014 José Matos <jamatos@fedoraproject.org> - 4.200.0-1
- update to 4.200.0

* Fri Mar 14 2014 José Matos <jamatos@fedoraproject.org> - 4.100.2-1
- update to 4.100.2

* Sun Mar  2 2014 José Matos <jamatos@fedoraproject.org> - 4.100.0-1
- update to 4.100.0

* Sat Jan 25 2014 José Matos <jamatos@fedoraproject.org> - 4.000.2-1
- update to 4.000.2

* Fri Jan 10 2014 José Matos <jamatos@fedoraproject.org> - 4.000.0-2
- add mex_interface to documentation (demonstration of how to connect
  Armadillo with MATLAB/Octave mex functions)

* Thu Jan  9 2014 José Matos <jamatos@fedoraproject.org> - 4.000.0-1
- update to 4.000.0
- dropped boost dependency and added arpack
- remove reference to boost in the comments

* Tue Dec 10 2013 José Matos <jamatos@fedoraproject.org> - 3.930.1-1
- update to 3.930.1
- update the name of the documentation paper from 2013 to 2014

* Mon Nov 25 2013 José Matos <jamatos@fedoraproject.org> - 3.920.3-1
- update to 3.920.3

* Tue Oct 29 2013 José Matos <jamatos@fedoraproject.org> - 3.920.2-1
- update to 3.920.2

* Mon Sep 30 2013 José Matos <jamatos@fedoraproject.org> - 3.920.1-1
- update to 3.920.1

* Mon Sep 30 2013 José Matos <jamatos@fedoraproject.org> - 3.920.0-1
- update to 3.920.0

* Sun Sep 22 2013 Orion Poplawski - 3.910.0-2
- Rebuild for atlas 3.10

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

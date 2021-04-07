#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rbibutils
Version  : 2.1
Release  : 4
URL      : https://cran.r-project.org/src/contrib/rbibutils_2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rbibutils_2.1.tar.gz
Summary  : Convert Between Bibliography Formats
Group    : Development/Tools
License  : GPL-2.0
Requires: R-rbibutils-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
including 'BibTeX', 'BibLaTeX' and 'Bibentry'.  Includes a port of the
    'bibutils' utilities by Chris Putnam

%package lib
Summary: lib components for the R-rbibutils package.
Group: Libraries

%description lib
lib components for the R-rbibutils package.


%prep
%setup -q -c -n rbibutils
cd %{_builddir}/rbibutils

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617811866

%install
export SOURCE_DATE_EPOCH=1617811866
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rbibutils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rbibutils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rbibutils
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rbibutils || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rbibutils/DESCRIPTION
/usr/lib64/R/library/rbibutils/INDEX
/usr/lib64/R/library/rbibutils/Meta/Rd.rds
/usr/lib64/R/library/rbibutils/Meta/features.rds
/usr/lib64/R/library/rbibutils/Meta/hsearch.rds
/usr/lib64/R/library/rbibutils/Meta/links.rds
/usr/lib64/R/library/rbibutils/Meta/nsInfo.rds
/usr/lib64/R/library/rbibutils/Meta/package.rds
/usr/lib64/R/library/rbibutils/NAMESPACE
/usr/lib64/R/library/rbibutils/NEWS.md
/usr/lib64/R/library/rbibutils/R/rbibutils
/usr/lib64/R/library/rbibutils/R/rbibutils.rdb
/usr/lib64/R/library/rbibutils/R/rbibutils.rdx
/usr/lib64/R/library/rbibutils/R/sysdata.rdb
/usr/lib64/R/library/rbibutils/R/sysdata.rdx
/usr/lib64/R/library/rbibutils/REFERENCES.bib
/usr/lib64/R/library/rbibutils/auto/REFERENCES.el
/usr/lib64/R/library/rbibutils/bib/auto/latin1accents_utf8.el
/usr/lib64/R/library/rbibutils/bib/auto/latin1accents_utf8c.el
/usr/lib64/R/library/rbibutils/bib/cyr_utf8.bib
/usr/lib64/R/library/rbibutils/bib/eaf_Grunert01.bib
/usr/lib64/R/library/rbibutils/bib/ex0.biblatex
/usr/lib64/R/library/rbibutils/bib/ex0.bibtex
/usr/lib64/R/library/rbibutils/bib/ex0.xml
/usr/lib64/R/library/rbibutils/bib/latin1accents_utf8.bib
/usr/lib64/R/library/rbibutils/bib/latin1accents_utf8a.bib
/usr/lib64/R/library/rbibutils/bib/latin1accents_utf8b.bib
/usr/lib64/R/library/rbibutils/help/AnIndex
/usr/lib64/R/library/rbibutils/help/aliases.rds
/usr/lib64/R/library/rbibutils/help/paths.rds
/usr/lib64/R/library/rbibutils/help/rbibutils.rdb
/usr/lib64/R/library/rbibutils/help/rbibutils.rdx
/usr/lib64/R/library/rbibutils/html/00Index.html
/usr/lib64/R/library/rbibutils/html/R.css
/usr/lib64/R/library/rbibutils/tests/testthat.R
/usr/lib64/R/library/rbibutils/tests/testthat/bibacc_1.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bibacc_2.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bibacc_3.rds
/usr/lib64/R/library/rbibutils/tests/testthat/eaf_Grunert01.rds
/usr/lib64/R/library/rbibutils/tests/testthat/test-bib.R
/usr/lib64/R/library/rbibutils/tests/testthat/test-convert.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rbibutils/libs/rbibutils.so
/usr/lib64/R/library/rbibutils/libs/rbibutils.so.avx2
/usr/lib64/R/library/rbibutils/libs/rbibutils.so.avx512

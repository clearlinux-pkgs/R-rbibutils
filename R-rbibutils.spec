#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-rbibutils
Version  : 2.3
Release  : 44
URL      : https://cran.r-project.org/src/contrib/rbibutils_2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rbibutils_2.3.tar.gz
Summary  : Read 'Bibtex' Files and Convert Between Bibliography Formats
Group    : Development/Tools
License  : GPL-2.0
Requires: R-rbibutils-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
formats, including 'Bibtex', 'Biblatex', 'PubMed', 'Endnote', and
    'Bibentry'.  Includes a port of the 'bibutils' utilities by Chris

%package lib
Summary: lib components for the R-rbibutils package.
Group: Libraries

%description lib
lib components for the R-rbibutils package.


%prep
%setup -q -n rbibutils
pushd ..
cp -a rbibutils buildavx2
popd
pushd ..
cp -a rbibutils buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728052687

%install
export SOURCE_DATE_EPOCH=1728052687
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/rbibutils/Meta/vignette.rds
/usr/lib64/R/library/rbibutils/NAMESPACE
/usr/lib64/R/library/rbibutils/NEWS.md
/usr/lib64/R/library/rbibutils/R/rbibutils
/usr/lib64/R/library/rbibutils/R/rbibutils.rdb
/usr/lib64/R/library/rbibutils/R/rbibutils.rdx
/usr/lib64/R/library/rbibutils/R/sysdata.rdb
/usr/lib64/R/library/rbibutils/R/sysdata.rdx
/usr/lib64/R/library/rbibutils/REFERENCES.bib
/usr/lib64/R/library/rbibutils/bib/00README.org
/usr/lib64/R/library/rbibutils/bib/AugBadBroZit2009hv.bib
/usr/lib64/R/library/rbibutils/bib/Cousquer_1991_PCE.bib
/usr/lib64/R/library/rbibutils/bib/Cousquer_1991_PCE2.bib
/usr/lib64/R/library/rbibutils/bib/Cousquer_1991_PCE2_e.bib
/usr/lib64/R/library/rbibutils/bib/Cousquer_1991_PCE4.bib
/usr/lib64/R/library/rbibutils/bib/Cousquer_1991_PCE5.bib
/usr/lib64/R/library/rbibutils/bib/Cousquer_1991_PCE5_e.bib
/usr/lib64/R/library/rbibutils/bib/Cousquer_1991_PCE_e.bib
/usr/lib64/R/library/rbibutils/bib/FsinR_Pudil1994.bib
/usr/lib64/R/library/rbibutils/bib/Kisung_Rdpack_21.bib
/usr/lib64/R/library/rbibutils/bib/Putnam1992.end
/usr/lib64/R/library/rbibutils/bib/Rcore.bib
/usr/lib64/R/library/rbibutils/bib/Rcore_with_abbr.bib
/usr/lib64/R/library/rbibutils/bib/WuertzEtalGarch.bib
/usr/lib64/R/library/rbibutils/bib/accents_tabbing.bib
/usr/lib64/R/library/rbibutils/bib/bib_from_medin.bib
/usr/lib64/R/library/rbibutils/bib/biblatex-examples_sans_key_aksin.bib
/usr/lib64/R/library/rbibutils/bib/cort_genest2017.bib
/usr/lib64/R/library/rbibutils/bib/cyr_utf8.bib
/usr/lib64/R/library/rbibutils/bib/eaf_GruFon2009.bib
/usr/lib64/R/library/rbibutils/bib/eaf_Grunert01.bib
/usr/lib64/R/library/rbibutils/bib/easyPubMedvig.xml
/usr/lib64/R/library/rbibutils/bib/easyPubMedvig_no_new_lines.xml
/usr/lib64/R/library/rbibutils/bib/ebi.xml
/usr/lib64/R/library/rbibutils/bib/endnote.xml
/usr/lib64/R/library/rbibutils/bib/ex0.biblatex
/usr/lib64/R/library/rbibutils/bib/ex0.bibtex
/usr/lib64/R/library/rbibutils/bib/ex0.xml
/usr/lib64/R/library/rbibutils/bib/ex1.endx
/usr/lib64/R/library/rbibutils/bib/extra.bib
/usr/lib64/R/library/rbibutils/bib/iridia_BorEly1998online.bib
/usr/lib64/R/library/rbibutils/bib/issue_5.bib
/usr/lib64/R/library/rbibutils/bib/latin1accents_utf8.bib
/usr/lib64/R/library/rbibutils/bib/latin1accents_utf8a.bib
/usr/lib64/R/library/rbibutils/bib/latin1accents_utf8a1.bib
/usr/lib64/R/library/rbibutils/bib/latin1accents_utf8b.bib
/usr/lib64/R/library/rbibutils/bib/litprog280.bib
/usr/lib64/R/library/rbibutils/bib/litprog280macros_only.bib
/usr/lib64/R/library/rbibutils/bib/litprog280no_macros.bib
/usr/lib64/R/library/rbibutils/bib/partitionComparison_Deneud2006.bib
/usr/lib64/R/library/rbibutils/bib/pkg_BayesianLaterality.bib
/usr/lib64/R/library/rbibutils/bib/pubmed-balloongui-set.nbib
/usr/lib64/R/library/rbibutils/bib/pubmed-balloongui-set_09_31542275.nbib
/usr/lib64/R/library/rbibutils/bib/single.nbib
/usr/lib64/R/library/rbibutils/bib/superb_n15.bib
/usr/lib64/R/library/rbibutils/bib/tex.bib
/usr/lib64/R/library/rbibutils/bib/texChars.bib
/usr/lib64/R/library/rbibutils/bib/texjourn001.bib
/usr/lib64/R/library/rbibutils/bib/urlR.bib
/usr/lib64/R/library/rbibutils/bib/xampl_modified.bib
/usr/lib64/R/library/rbibutils/bib/xeCJK_gb18030.bib
/usr/lib64/R/library/rbibutils/bib/xeCJK_utf8.bib
/usr/lib64/R/library/rbibutils/doc/index.html
/usr/lib64/R/library/rbibutils/doc/rbibutils.R
/usr/lib64/R/library/rbibutils/doc/rbibutils.Rnw
/usr/lib64/R/library/rbibutils/doc/rbibutils.pdf
/usr/lib64/R/library/rbibutils/help/AnIndex
/usr/lib64/R/library/rbibutils/help/aliases.rds
/usr/lib64/R/library/rbibutils/help/paths.rds
/usr/lib64/R/library/rbibutils/help/rbibutils.rdb
/usr/lib64/R/library/rbibutils/help/rbibutils.rdx
/usr/lib64/R/library/rbibutils/html/00Index.html
/usr/lib64/R/library/rbibutils/html/R.css
/usr/lib64/R/library/rbibutils/tests/testthat.R
/usr/lib64/R/library/rbibutils/tests/testthat/acc_fn.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bib2R.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bib2ads.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bib2biblatex.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bib2end.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bib2isi.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bib2rds.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bib2ris.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bib2wordbib.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bib2xml2.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bibacc_1.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bibacc_2.rds
/usr/lib64/R/library/rbibutils/tests/testthat/bibacc_3.rds
/usr/lib64/R/library/rbibutils/tests/testthat/biblatex2bib.rds
/usr/lib64/R/library/rbibutils/tests/testthat/eaf_Grunert01.rds
/usr/lib64/R/library/rbibutils/tests/testthat/end2bib.rds
/usr/lib64/R/library/rbibutils/tests/testthat/isi2bib.rds
/usr/lib64/R/library/rbibutils/tests/testthat/issue_5_utf8.rds
/usr/lib64/R/library/rbibutils/tests/testthat/issue_5a.rds
/usr/lib64/R/library/rbibutils/tests/testthat/issue_5rdpack.rds
/usr/lib64/R/library/rbibutils/tests/testthat/med2bib.rds
/usr/lib64/R/library/rbibutils/tests/testthat/rds2bbl2.rds
/usr/lib64/R/library/rbibutils/tests/testthat/rds2xml.rds
/usr/lib64/R/library/rbibutils/tests/testthat/ris2bib.rds
/usr/lib64/R/library/rbibutils/tests/testthat/test-bib.R
/usr/lib64/R/library/rbibutils/tests/testthat/test-bibentryExtra.R
/usr/lib64/R/library/rbibutils/tests/testthat/test-bibstyleExtra.R
/usr/lib64/R/library/rbibutils/tests/testthat/test-charToBib.R
/usr/lib64/R/library/rbibutils/tests/testthat/test-convert.R
/usr/lib64/R/library/rbibutils/tests/testthat/test-convert.Rsav
/usr/lib64/R/library/rbibutils/tests/testthat/test-https.R
/usr/lib64/R/library/rbibutils/tests/testthat/texChars_converted.rds
/usr/lib64/R/library/rbibutils/tests/testthat/texChars_exported.rds
/usr/lib64/R/library/rbibutils/tests/testthat/texChars_kept.rds
/usr/lib64/R/library/rbibutils/tests/testthat/wordbib2bib.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xampl2biblatex.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_1.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_1.rds_sav
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_bbl2bib.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_bib2ads.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_bib2end.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_bib2isi.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_isi2bib.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xml2bib.rds

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/rbibutils/libs/rbibutils.so
/V4/usr/lib64/R/library/rbibutils/libs/rbibutils.so
/usr/lib64/R/library/rbibutils/libs/rbibutils.so

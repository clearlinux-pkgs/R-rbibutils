#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rbibutils
Version  : 2.2.8
Release  : 25
URL      : https://cran.r-project.org/src/contrib/rbibutils_2.2.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rbibutils_2.2.8.tar.gz
Summary  : Read 'Bibtex' Files and Convert Between Bibliography Formats
Group    : Development/Tools
License  : GPL-2.0
Requires: R-rbibutils-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
formats, including 'Bibtex', 'Biblatex', 'PubMed', 'Endnote', and
    'Bibentry'.  Includes a port of the 'bibutils' utilities by Chris

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
export SOURCE_DATE_EPOCH=1649691952

%install
export SOURCE_DATE_EPOCH=1649691952
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rbibutils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
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
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_bbl2bib.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_bib2ads.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_bib2end.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_bib2isi.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xampl_isi2bib.rds
/usr/lib64/R/library/rbibutils/tests/testthat/xml2bib.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rbibutils/libs/rbibutils.so
/usr/lib64/R/library/rbibutils/libs/rbibutils.so.avx2
/usr/lib64/R/library/rbibutils/libs/rbibutils.so.avx512

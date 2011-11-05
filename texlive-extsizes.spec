# revision 17263
# category Package
# catalog-ctan /macros/latex/contrib/extsizes
# catalog-date 2010-02-28 19:16:53 +0100
# catalog-license lppl
# catalog-version 1.4a
Name:		texlive-extsizes
Version:	1.4a
Release:	1
Summary:	Extend the standard classes' size options
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/extsizes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extsizes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extsizes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides classes extarticle and extreport, extletter, extbook,
extproc which allow for documents with a base font of size 8-
20pt.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/extsizes/autopagewidth.sty
%{_texmfdistdir}/tex/latex/extsizes/extarticle.cls
%{_texmfdistdir}/tex/latex/extsizes/extbook.cls
%{_texmfdistdir}/tex/latex/extsizes/extletter.cls
%{_texmfdistdir}/tex/latex/extsizes/extproc.cls
%{_texmfdistdir}/tex/latex/extsizes/extreport.cls
%{_texmfdistdir}/tex/latex/extsizes/extsizes.sty
%{_texmfdistdir}/tex/latex/extsizes/size14.clo
%{_texmfdistdir}/tex/latex/extsizes/size17.clo
%{_texmfdistdir}/tex/latex/extsizes/size20.clo
%{_texmfdistdir}/tex/latex/extsizes/size8.clo
%{_texmfdistdir}/tex/latex/extsizes/size9.clo
%doc %{_texmfdistdir}/doc/latex/extsizes/README
%doc %{_texmfdistdir}/doc/latex/extsizes/extsizes.pdf
%doc %{_texmfdistdir}/doc/latex/extsizes/extsizes.tex
%doc %{_texmfdistdir}/doc/latex/extsizes/readme.extsizes
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

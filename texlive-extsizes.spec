Name:		texlive-extsizes
Version:	17263
Release:	2
Summary:	Extend the standard classes' size options
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/extsizes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extsizes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extsizes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides classes extarticle and extreport, extletter, extbook,
extproc which allow for documents with a base font of size 8-
20pt.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

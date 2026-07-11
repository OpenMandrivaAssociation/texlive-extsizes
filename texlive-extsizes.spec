%global tl_name extsizes
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4a
Release:	%{tl_revision}.1
Summary:	Extend the standard classes size options
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/extsizes
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/extsizes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/extsizes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides classes extarticle, extreport, extletter, extbook and extproc
which provide for documents with a base font size from 8-20pt. There is
also a LaTeX package, extsizes.sty, which can be used with nonstandard
document classes. But it cannot be guaranteed to work with any given
class.


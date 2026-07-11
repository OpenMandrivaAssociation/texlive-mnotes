%global tl_name mnotes
%global tl_revision 63406

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9
Release:	%{tl_revision}.1
Summary:	Margin annotation for collaborative writing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mnotes
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mnotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mnotes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mnotes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a flexible mechanism for annotating, and commenting
upon, collaboratively-written documents.


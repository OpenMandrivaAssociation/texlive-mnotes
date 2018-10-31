Name:		texlive-mnotes
Version:	0.8
Release:	2
Summary:	Margin annotation for collaborative writing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mnotes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mnotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mnotes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mnotes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a flexible mechanism for annotating, and
commenting upon, collaboratively-written documents.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mnotes
%doc %{_texmfdistdir}/doc/latex/mnotes
#- source
%doc %{_texmfdistdir}/source/latex/mnotes

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

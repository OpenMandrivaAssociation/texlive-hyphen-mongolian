%global tl_name hyphen-mongolian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Mongolian hyphenation patterns in Cyrillic script.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-mongolian
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-mongolian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Mongolian in T2A, LMC and UTF-8 encodings. LMC
encoding is used in MonTeX. The package includes two sets of patterns
that will hopefully be merged in future.


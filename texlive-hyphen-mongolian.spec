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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Mongolian in T2A, LMC and UTF-8 encodings. LMC
encoding is used in MonTeX. The package includes two sets of patterns
that will hopefully be merged in future.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-mongolian:
mongolian loadhyph-mn-cyrl.tex
mongolianlmc loadhyph-mn-cyrl-x-lmc.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-mongolian:
\addlanguage{mongolian}{loadhyph-mn-cyrl.tex}{}{2}{2}
\addlanguage{mongolianlmc}{loadhyph-mn-cyrl-x-lmc.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-mongolian:
['mongolian'] = {
	loader = 'loadhyph-mn-cyrl.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-mn-cyrl.pat.txt',
},
['mongolianlmc'] = {
	loader = 'loadhyph-mn-cyrl-x-lmc.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	special = '"disabled:only',
},
TL_HYPHEN_EOF

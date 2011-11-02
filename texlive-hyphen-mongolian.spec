Name:		texlive-hyphen-mongolian
Version:	20111102
Release:	1
Summary:	Mongolian hyphenation patterns in Cyrillic script
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-mongolian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Conflicts:	texlive-texmf <= 20110705-3
Requires(post):	texlive-hyphen-base

%description
Hyphenation patterns for Mongolian in T2A, LMC and UTF-8
encodings. LMC encoding is used in MonTeX. The package includes
two sets of patterns that will hopefully be merged in future.

%pre
    %_texmf_language_dat_pre
    %_texmf_language_def_pre
    %_texmf_language_lua_pre

%post
    %_texmf_language_dat_post
    %_texmf_language_def_post
    %_texmf_language_lua_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_pre
	%_texmf_language_def_pre
	%_texmf_language_lua_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_post
	%_texmf_language_def_post
	%_texmf_language_lua_post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-mongolian
%_texmf_language_def_d/hyphen-mongolian
%_texmf_language_lua_d/hyphen-mongolian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-mongolian <<EOF
%% from hyphen-mongolian:
mongolian loadhyph-mn-cyrl.tex
mongolianlmc loadhyph-mn-cyrl-x-lmc.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-mongolian <<EOF
%% from hyphen-mongolian:
\addlanguage{mongolian}{loadhyph-mn-cyrl.tex}{}{2}{2}
\addlanguage{mongolianlmc}{loadhyph-mn-cyrl-x-lmc.tex}{}{2}{2}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-mongolian <<EOF
-- from hyphen-mongolian:
	['mongolian'] = {
		loader = 'loadhyph-mn-cyrl.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-mn-cyrl.pat.txt',
		hyphenation = '',
	},
	['mongolianlmc'] = {
		loader = 'loadhyph-mn-cyrl-x-lmc.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		special = 'disabled:only for 8bit montex with lmc encoding',
	},
EOF

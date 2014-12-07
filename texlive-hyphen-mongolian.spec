# revision 25990
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-mongolian
Version:	20120611
Release:	8
Summary:	Mongolian hyphenation patterns in Cyrillic script
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-mongolian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Mongolian in T2A, LMC and UTF-8
encodings. LMC encoding is used in MonTeX. The package includes
two sets of patterns that will hopefully be merged in future.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
\%% from hyphen-mongolian:
mongolian loadhyph-mn-cyrl.tex
mongolianlmc loadhyph-mn-cyrl-x-lmc.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-mongolian
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-mongolian <<EOF
\%% from hyphen-mongolian:
\addlanguage{mongolian}{loadhyph-mn-cyrl.tex}{}{2}{2}
\addlanguage{mongolianlmc}{loadhyph-mn-cyrl-x-lmc.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-mongolian
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


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120611-1
+ Revision: 804804
- Update to latest release.

* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120124-1
+ Revision: 767569
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 759929
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718671
- texlive-hyphen-mongolian
- texlive-hyphen-mongolian
- texlive-hyphen-mongolian
- texlive-hyphen-mongolian


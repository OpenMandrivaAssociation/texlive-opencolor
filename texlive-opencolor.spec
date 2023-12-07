Name:		texlive-opencolor
Version:	66363
Release:	1
Summary:	Simple use of the Open Color colors
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/opencolor
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opencolor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opencolor.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package that provides hexadecimal color definitions of the
130 colors included in the Open Color library.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/opencolor
%doc %{_texmfdistdir}/doc/latex/opencolor

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

%define name omake
%define ver 0.9.8.5
%define index 2
%define release %mkrel 4

%define nobootstrap %{?_without_bootstrap:1}%{?!_without_bootstrap:0}

Name: %name
Version: %{ver}_%{index}
Release: %release
Summary: The omake build system
URL: https://omake.metaprl.org/
Source: http://omake.metaprl.org/downloads/%{name}-%{ver}-%{index}.tar.gz
License: GPL
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: autoconf, ocaml, make, fam-devel
BuildRequires: ncurses-devel
%if %nobootstrap
BuildRequires: omake
%endif


%description
OMake is a build system, similar to GNU make, but with many additional
features, including:
- Support for large projects spanning multiple directories;
- Support for commands that produce several targets at once;
- Fast, accurate, automated dependency analysis using MD5 digests;
- Portability: omake provides a consistent interface on Win32
  and on Unix systems including Linux, OSX, and Cygwin;
- Builtin functions that provide the most common features of
  programs like grep, sed, and awk;
- Active filesystem monitoring, where the build automatically
  restarts whenever you modify a source file.

%prep
%setup -q -n %name-%ver

%build

%if %nobootstrap
%else
make INSTALL_ROOT=$RPM_BUILD_ROOT\
   PREFIX=%{_prefix}\
   BINDIR=%{_bindir}\
   LIBDIR=%{_libdir}\
   MANDIR=%{_mandir}\
   all
%endif

make INSTALL_ROOT=$RPM_BUILD_ROOT\
   PREFIX=%{_prefix}\
   BINDIR=%{_bindir}\
   LIBDIR=%{_libdir}\
   MANDIR=%{_mandir}\
   all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/omake

make INSTALL_ROOT=$RPM_BUILD_ROOT\
   PREFIX=%{_prefix}\
   BINDIR=%{_bindir}\
   LIBDIR=%{_libdir}\
   MANDIR=%{_mandir}\
   install

chmod 755 $RPM_BUILD_ROOT%_bindir/*

# get ride of CVS file
find doc -depth -name CVS -exec rm -fr {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE doc/html/*.html doc/html/images doc/html/*.txt doc/ps/*.ps

%{_bindir}/*
%{_libdir}/omake
# %{_mandir}/man1/*



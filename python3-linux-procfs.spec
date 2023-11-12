Summary:	Linux /proc abstraction classes for Python 3
Summary(pl.UTF-8):	Klasy abstrakcji linuksowego /proc dla Pythona 3
Name:		python3-linux-procfs
Version:	0.7.3
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	https://www.kernel.org/pub/software/libs/python/python-linux-procfs/python-linux-procfs-%{version}.tar.xz
# Source0-md5:	e20d7df2bd3e142d696c9223e525a85b
URL:		https://rt.wiki.kernel.org/index.php/Tuna
# uses f-strings
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 3 abstractions to extract information from the Linux kernel
/proc files.

%description -l pl.UTF-8
Abstrakcje Pythona 3 do wydobywania informacji z plików /proc jądra
Linuksa.

%prep
%setup -q -n python-linux-procfs-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pflags
%{py3_sitescriptdir}/procfs
%{py3_sitescriptdir}/python_linux_procfs-%{version}-py*.egg-info

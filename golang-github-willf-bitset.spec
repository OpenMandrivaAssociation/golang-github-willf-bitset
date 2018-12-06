%global goipath         github.com/willf/bitset
Version:                1.1.9

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go package implementing bitsets
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for building other packages which
use import path with %{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%doc README.md
%license LICENSE


%changelog
* Wed Oct 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.9-1
- Update to latest version

* Wed Aug 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-2
- rebuilt

* Sun Aug 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-1
- First package for Fedora

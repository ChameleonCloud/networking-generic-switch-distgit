%{!?branch: %global branch master}

%global srcname networking-generic-switch
%global sum Pluggable framework to implement functionality required for use-cases like OpenStack Ironic multi-tenancy mode

Name:           %{srcname}
Version:        0.4.0
Release:        10%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/ChameleonCloud/networking-generic-switch/archive/%{branch}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
Requires: openstack-neutron-ml2 >= 10.0.0
Requires: python-netmiko >= 0.4.4
Requires: python-neutron-lib >= 1.1.0
Requires: python-oslo-config >= 2:3.14.0
Requires: python-oslo-i18n >= 2.1.0
Requires: python-oslo-log >= 3.11.0
Requires: python-six >= 1.9.0
Requires: python-stevedore >= 1.17.1
Requires: python-tenacity >= 3.2.1
Requires: python-tooz >= 1.47.0

# These are requirements for unit testing
BuildRequires: python-mock
BuildRequires: python-netmiko
BuildRequires: python-neutron-lib
BuildRequires: python-oslo-config
BuildRequires: python-oslo-i18n
BuildRequires: python-oslo-log
BuildRequires: python-oslo-sphinx
BuildRequires: python-sphinx
BuildRequires: python-stevedore

%description
Pluggable framework to implement functionality required for use-cases like OpenStack Ironic multi-tenancy mode.

%prep
%autosetup -n %{srcname}-%{branch} -p1

%build
PBR_VERSION=%{version} %{__python2} setup.py build

%install
PBR_VERSION=%{version} %{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
install -p -D -m 640 etc/neutron/plugins/ml2/ml2_conf_genericswitch.ini.sample %{buildroot}/%{_sysconfdir}/neutron/plugins/ml2/ml2_conf_genericswitch.ini

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/*
%config(noreplace) %attr(-, root, neutron) %{_sysconfdir}/neutron/plugins/ml2/ml2_conf_genericswitch.ini

%changelog
* Wed Sep 5 2018 Jason Anderson <jasonanderson@uchicago.edu> 0.4.0-10
- Update package with Chameleon patches

* Fri Aug 3 2018 Cody Hammock <hammock@tacc.utexas.edu> 0.4.0-9
- Update package with Chameleon patches

* Tue Sep 12 2017 Pierre Riteau <priteau@uchicago.edu> 0.4.0-1
- Initial package of OpenStack Pike stable branch

* Mon Aug 21 2017 Pierre Riteau <priteau@uchicago.edu> 0.2.1.dev9-1
- Initial package of OpenStack Ocata stable branch

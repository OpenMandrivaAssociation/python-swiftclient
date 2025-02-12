Name:		python-swiftclient
Version:	4.6.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/python-swiftclient/python-swiftclient-%{version}.tar.gz
Summary:	OpenStack Object Storage API Client Library
URL:		https://pypi.org/project/python-swiftclient/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
OpenStack Object Storage API Client Library

%prep -a
# Having the releasenotes there breaks the build?!
rm -rf releasenotes

%files
%{py_sitedir}/swiftclient
%{py_sitedir}/python_swiftclient-*.*-info

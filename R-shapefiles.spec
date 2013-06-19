%global packname  shapefiles
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.7
Release:          2
Summary:          Read and Write ESRI Shapefiles
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-foreign 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-foreign

%description
Functions to read and write ESRI shapefiles

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6-1
+ Revision: 775960
- Import R-shapefiles
- Import R-shapefiles


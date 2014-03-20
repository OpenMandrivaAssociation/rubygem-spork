%define oname spork

Name:       rubygem-%{oname}
Version:    0.9.2
Release:    2
Summary:    A forking Drb spec server
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/timcharper/spork
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
Requires:   rubygems
BuildRequires: rubygems
BuildRequires: rubygem(rake)
Provides:   rubygem(%{oname}) = %{version}

%description
A forking Drb spec server

%prep

%build

%install
mkdir -p %{buildroot}%{ruby_gemdir}
gem install -V --local --install-dir %{buildroot}%{ruby_gemdir} \
               --force --rdoc %{SOURCE0}

# copy binaries to bindir
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}

rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

%files
%{_bindir}/spork
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/assets/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/Gemfile
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/MIT-LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

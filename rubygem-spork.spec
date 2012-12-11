%define oname spork

Name:       rubygem-%{oname}
Version:    0.8.4
Release:    %mkrel 1
Summary:    A forking Drb spec server
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/timcharper/spork
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
Source1:    %{oname}-%{version}.gemspec
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
BuildRequires: rubygems
BuildRequires: ruby-rake
Provides:   rubygem(%{oname}) = %{version}

%description
A forking Drb spec server

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install -V --local --install-dir %{buildroot}%{ruby_gemdir} \
               --force --rdoc %{SOURCE0}

# copy binaries to bindir
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}

rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{_bindir}/spork
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/assets/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/geminstaller.yml
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/MIT-LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Thu Nov 04 2010 Rémy Clouard <shikamaru@mandriva.org> 0.8.4-1mdv2011.0
+ Revision: 593395
- import rubygem-spork


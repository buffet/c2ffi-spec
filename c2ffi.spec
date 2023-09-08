%define commit 3078cb57ccfa43736aa93720a72f1074034cb37d

Name:           c2ffi
Version:        20230608
Release:        %{autorelease}
Summary:        Clang-based FFI wrapper generator

License:        MIT
URL:            https://github.com/rpav/c2ffi
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  cmake clang clang-devel gcc-c++ llvm-devel

%description
This is a tool for extracting definitions from C, C++, and Objective C headers
for use with foreign function call interfaces.


%prep
%setup -q -n c2ffi-%{commit}


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%{_bindir}/c2ffi

%license COPYING
%doc README.md


%changelog
* Sun Aug 27 2023 buffet <niclas@countingsort.com>
- Init at 20230608

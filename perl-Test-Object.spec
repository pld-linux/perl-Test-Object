# NOTE
# - you should consider using pldcpan for new perl packages
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Object
Summary:	Test::Object - thoroughly testing objects via registered handlers
# TODO
#Summary(pl):	Test::Object - 
Name:		perl-Test-Object
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab71791756faaabc3b4fad5bcc1df50f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Test::Object" is a testing package designed to allow you to easily
test what you believe is a valid object against the expected behaviour
of all of the classes in its inheritance tree in one single call.

%description -l pl
"Test::Object" jeswt pakietem testowym, który ma s³u¿yæ ³atwemu
testowaniu czy dany obiekt zachowuje siê w oczekiwany sposób we
wszystkich klasach w swoim drzewie dziedziczenia przy pojedynczym
wywo³aniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/Object
%{_mandir}/man3/*

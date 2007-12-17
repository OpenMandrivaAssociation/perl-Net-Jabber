%define	module	Net-Jabber
%define version 2.0
%define release %mkrel 3

Summary:	%{module} perl module
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/R/RE/REATMON/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
Buildrequires:	perl-devel
Buildrequires:	perl-Net-XMPP
BuildArch:	noarch

%description
Net::Jabber is a collection of Perl modules that provide a Perl Developer
access to the Jabber protocol.  Using OOP modules we provide a clean
interface to writing anything from a full client to a simple protocol
tester.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES LICENSE.LGPL MANIFEST.SKIP README
%{_mandir}/*/*
%{perl_vendorlib}/Net/Jabber*


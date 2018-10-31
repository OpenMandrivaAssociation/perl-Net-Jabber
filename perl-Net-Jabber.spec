%define	module	Net-Jabber
%define upstream_version 2.0

Summary:	%{module} perl module
Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	22
License:	LGPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RE/REATMON/%{module}-%{upstream_version}.tar.bz2
BuildArch:	noarch
Buildrequires:	perl-devel
Buildrequires:	perl-Net-XMPP

%description
Net::Jabber is a collection of Perl modules that provide a Perl Developer
access to the Jabber protocol.  Using OOP modules we provide a clean
interface to writing anything from a full client to a simple protocol
tester.

%prep
%setup -qn %{module}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc CHANGES LICENSE.LGPL MANIFEST.SKIP README
%{perl_vendorlib}/Net/Jabber*
%{_mandir}/man3/*


%define	module	Net-Jabber
%define version 2.0
%define release 12

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
BuildRoot:	%{_tmppath}/%{name}-%{version}
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



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.0-10mdv2012.0
+ Revision: 765531
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.0-9
+ Revision: 764055
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0-8
+ Revision: 667276
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0-7mdv2011.0
+ Revision: 426547
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.0-6mdv2009.1
+ Revision: 351815
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.0-5mdv2009.0
+ Revision: 223894
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0-4mdv2008.1
+ Revision: 180524
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.0-3mdv2008.0
+ Revision: 23322
- rebuild


* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.0-1mdk
- New release 2.0 (TODO: fix tests)
- don't ship manifest
- rpmbuilupdate aware
- better URL
- spec cleanup
- fix buildrequires

* Mon Jun 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.30-2mdk
- Rebuild

* Mon Apr 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.30-1mdk
- 1.30
- drop PREFIX and use %%makeinstall_std macro

* Tue Aug 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.28-6mdk
- rebuild

* Sun Jul 27 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 1.28-5mdk
- rebuild for new rpm provides computation

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.28-4mdk
- rebuild for new auto{prov,req}

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.28-3mdk
- buildrequires

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.28-2mdk
- rebuild

* Fri Jan 17 2003 François Pons <fpons@mandrakesoft.com> 1.28-1mdk
- 1.28.

* Sat Jul 20 2002 Pixel <pixel@mandrakesoft.com> 1.26-2mdk
- rebuild for new perl
- cleanup

* Tue Jun 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.26-1mdk
- from David Walser <luigiwalser@yahoo.com> :
	- 1.26


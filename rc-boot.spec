Summary:	Wrapper for managing boot services
Summary(pl):	Skrypty do zarz±dzania "bootloaderami"
Name:		rc-boot
Version:	0.7
Release:	1
License:	GPL
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Source0:	ftp://ftp.pld.org.pl/software/rc-boot/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/sysconfig/rc-boot

%description
Wrapper for managing boot services.

%description -l pl
Skrypty do zarz±dzania bootloaderami.


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/images
install -d $RPM_BUILD_ROOT/sbin/
install -d $RPM_BUILD_ROOT%{_var}/rc-boot
install -d $RPM_BUILD_ROOT%{_mandir}/man8
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

install src/rc-boot	$RPM_BUILD_ROOT/sbin
install src/*.sh	$RPM_BUILD_ROOT%{_sysconfdir}/
install doc/config	$RPM_BUILD_ROOT%{_sysconfdir}/
install doc/rc-boot.8   $RPM_BUILD_ROOT%{_mandir}/man8/

gzip -9nf doc/{Assumtpions,Authors,BUGS,README}
install doc/*.gz       $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
install doc/image      $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(754,root,root) /sbin/rc-boot
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/config
%attr(750,root,root) %dir %{_sysconfdir}
%attr(750,root,root) %dir %{_sysconfdir}/images
%attr(750,root,root) %dir %{_var}/rc-boot
%{_mandir}/man8/*
%attr(640,root,root) %{_sysconfdir}/*_functions.sh

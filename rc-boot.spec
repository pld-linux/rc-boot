Summary:	Wrapper for managing boot services
Summary(pl):	Skrypty do zarz±dzania "bootloaderami"
Name:		rc-boot
Version:	0.6
Release:	1
License:	GPL
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Source0:	ftp://ftp.pld.org.pl/software/rc-boot/%{name}-%{version}.tar.gz
Requires:	rc-boot-loader
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/sysconfig/rc-boot

%description
Wrapper for managing boot services.

%description -l pl
Skrypty do zarz±dzania bootloaderami.


%package -n rc-boot-lilo
Summary:	Wrapper for managing boot services - lilo part
Summary(pl):	Skrypty do zarz±dzania "bootloaderami" - cze¶æ dla lilo
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Provides:	rc-boot-loader
Prereq:		fileutils
Conflicts:	rc-boot-grub
Requires:	lilo
Requires:	rc-boot

%description -n rc-boot-lilo
Wrapper for managing boot services - part for lilo.

%description -l pl -n rc-boot-lilo
Skrypty do zarz±dzania bootloaderami - czesc dla lilo


%package -n rc-boot-grub
Summary:	Wrapper for managing boot services - grub part
Summary(pl):	Skrypty do zarz±dzania "bootloaderami" - cze¶æ dla gruba
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Provides:	rc-boot-loader
Prereq:		fileutils
Conflicts:	rc-boot-lilo
Requires:	grub
Requires:	rc-boot

%description -n rc-boot-grub
Wrapper for managing boot services - part for grub.

%description -l pl -n rc-boot-grub
Skrypty do zarz±dzania bootloaderami - czesc dla gruba.


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/images
install -d $RPM_BUILD_ROOT/sbin/
install -d $RPM_BUILD_ROOT%{_var}/rc-boot
install -d $RPM_BUILD_ROOT%{_mandir}/man8

install src/rc-boot	$RPM_BUILD_ROOT/sbin
install src/*.sh	$RPM_BUILD_ROOT%{_sysconfdir}/
install doc/config	$RPM_BUILD_ROOT%{_sysconfdir}/
install doc/rc-boot.8   $RPM_BUILD_ROOT%{_mandir}/man8/
install doc/image       $RPM_BUILD_ROOT%{_sysconfdir}/images

gzip -9nf doc/{Assumtpions,Authors,BUGS,README}

%post -n rc-boot-lilo
rm -f /etc/sysconfig/rc-boot/functions.sh
ln -s /etc/sysconfig/rc-boot/lilo_functions.sh /etc/sysconfig/rc-boot/functions.sh

%post -n rc-boot-grub
rm -f /etc/sysconfig/rc-boot/functions.sh
ln -s /etc/sysconfig/rc-boot/grub_functions.sh /etc/sysconfig/rc-boot/functions.sh

%preun -n rc-boot-lilo
if [ "$1" = "0" ] ; then
	rm -f /etc/sysconfig/rc-boot/functions.sh
fi

%preun -n rc-boot-grub
if [ "$1" = "0" ] ; then
	rm -f /etc/sysconfig/rc-boot/functions.sh
fi

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
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/images/*
%{_mandir}/man8/*

%files -n rc-boot-lilo
%defattr(644,root,root,755)
%attr(640,root,root) %{_sysconfdir}/lilo_functions.sh

%files -n rc-boot-grub
%defattr(644,root,root,755)
%attr(640,root,root) %{_sysconfdir}/grub_functions.sh

# TODO:
# - what about suggesting to install GRUB? GRUB has EA: %{ix86}
Summary:	Wrapper for managing boot services
Summary(pl.UTF-8):	Skrypty do zarządzania bootloaderami
Name:		rc-boot
Version:	1.1
Release:	6
License:	GPL
Group:		Base
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	2a6e4d604d938ab7567e419c21725d88
Source1:	PLD.image
Patch0:		%{name}-prefer-PLD.patch
Requires:	rc-boot-bootloader
Requires:	sed
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/sysconfig/rc-boot

%description
Wrapper for managing boot services.

%description -l pl.UTF-8
Skrypty do zarządzania bootloaderami.

%package -n rc-boot-image-PLD
Summary:	PLD image for rc-boot
Summary(pl.UTF-8):	Obraz PLD dla rc-boot
Group:		Base
Requires:	rc-boot

%description -n rc-boot-image-PLD
PLD image for rc-boot.

%description -n rc-boot-image-PLD -l pl.UTF-8
Obraz PLD dla rc-boot.

%prep
%setup -q
%patch0 -p1
mv doc/Assum{tp,pt}ions # typo ;)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_sysconfdir}/images,%{_mandir}/man8}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/images/PLD

install src/rc-boot	$RPM_BUILD_ROOT/sbin
install doc/config	$RPM_BUILD_ROOT%{_sysconfdir}
install doc/rc-boot.8	$RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%postun -n rc-boot-image-PLD
/sbin/rc-boot 1>&2 || :

%post -n rc-boot-image-PLD
/sbin/rc-boot 1>&2 || :

%files
%defattr(644,root,root,755)
%doc doc/{Assumptions,Authors,BUGS,README,config,image}
%attr(754,root,root) /sbin/rc-boot
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/config
%attr(750,root,root) %dir %{_sysconfdir}/images
%{_mandir}/man8/*

%files -n rc-boot-image-PLD
%defattr(644,root,root,755)
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/images/PLD

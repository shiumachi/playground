mod_auth_openid.la: mod_auth_openid.slo
	$(SH_LINK) -rpath $(libexecdir) -module -avoid-version  mod_auth_openid.lo
DISTCLEAN_TARGETS = modules.mk
shared =  mod_auth_openid.la

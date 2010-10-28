mod_apm_test.la: mod_apm_test.slo
	$(SH_LINK) -rpath $(libexecdir) -module -avoid-version  mod_apm_test.lo
DISTCLEAN_TARGETS = modules.mk
shared =  mod_apm_test.la

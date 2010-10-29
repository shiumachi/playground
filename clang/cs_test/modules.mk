mod_cs_test.la: mod_cs_test.slo
	$(SH_LINK) -rpath $(libexecdir) -module -avoid-version  mod_cs_test.lo
DISTCLEAN_TARGETS = modules.mk
shared =  mod_cs_test.la

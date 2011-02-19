/* 
**  mod_auth_openid.c -- Apache sample auth_openid module
**  [Autogenerated via ``apxs -n auth_openid -g'']
**
**  To play with this sample module first compile it into a
**  DSO file and install it into Apache's modules directory 
**  by running:
**
**    $ apxs -c -i mod_auth_openid.c
**
**  Then activate it in Apache's httpd.conf file for instance
**  for the URL /auth_openid in as follows:
**
**    #   httpd.conf
**    LoadModule auth_openid_module modules/mod_auth_openid.so
**    <Location /auth_openid>
**    SetHandler auth_openid
**    </Location>
**
**  Then after restarting Apache via
**
**    $ apachectl restart
**
**  you immediately can request the URL /auth_openid and watch for the
**  output of this module. This can be achieved for instance via:
**
**    $ lynx -mime_header http://localhost/auth_openid 
**
**  The output should be similar to the following one:
**
**    HTTP/1.1 200 OK
**    Date: Tue, 31 Mar 1998 14:42:22 GMT
**    Server: Apache/1.3.4 (Unix)
**    Connection: close
**    Content-Type: text/html
**  
**    The sample page from mod_auth_openid.c
*/ 

#include "httpd.h"
#include "http_config.h"
#include "http_protocol.h"
#include "ap_config.h"

#include <string.h>
#include <time.h>

#define MAX_URL_LEN 1024
#define MAX_USERNAME_LEN 128

module AP_MODULE_DECLARE_DATA auth_openid_module;

typedef struct {
  char *url;
  char *username;
}auth_openid_cfg;

/* initialize directory config data */
static void *create_dir_config(apr_pool_t *p, char *dir)
{
  auth_openid_cfg *conf = (auth_openid_cfg *)apr_pcalloc(p, sizeof(auth_openid_cfg));
  conf->url = (char *)apr_pcalloc(p, MAX_URL_LEN);
  conf->username = (char *)apr_pcalloc(p, MAX_USERNAME_LEN);
  
  return conf;
}

/* The sample content handler */
static int auth_openid_handler(request_rec *r)
{
  char timestamp[100];
  time_t t = time(NULL);
  strftime(timestamp, 100, "%F %T", localtime(&t));

  if (strcmp(r->handler, "auth_openid")) {
        return DECLINED;
    }
    r->content_type = "text/html";
    
    if (r->header_only) {
        return DECLINED;
    }

    ap_rputs("The sample page from mod_auth_openid.c\n<br>", r);

    auth_openid_cfg *conf = 
      (auth_openid_cfg *)
      ap_get_module_config(r->per_dir_config, &auth_openid_module);

    ap_rputs(conf->url, r);
    ap_rputs("<br>", r);

    ap_rputs(conf->username, r);
    ap_rputs("<br>", r);
    
    ap_rputs(timestamp, r);

    apr_table_setn(r->headers_out, "Location", "http://localhost:10080/");
	
    return HTTP_MOVED_TEMPORARILY;
}

static const char *set_openid_url(cmd_parms *cmd, void *cfg, const char *val)
{
  auth_openid_cfg *conf = (auth_openid_cfg *)cfg;
  
  if(!ap_is_url(val)){
    return "Error: not URL";
  }
  
  strncpy(conf->url, val, MAX_URL_LEN);
  return NULL;
}

static const char *set_openid_username(cmd_parms *cmd, void *cfg, const char *val)
{
  auth_openid_cfg *conf = (auth_openid_cfg *)cfg;

  strncpy(conf->username, val, MAX_USERNAME_LEN);
  return NULL;
}


/* define directive */
static const command_rec auth_openid_cmds[] = 
  {
    AP_INIT_TAKE1("OpenIDURL", set_openid_url, NULL, ACCESS_CONF, "string"),
    AP_INIT_TAKE1("OpenIDUserName", set_openid_username, NULL, ACCESS_CONF, "string"),
    {NULL}
  };


static void auth_openid_register_hooks(apr_pool_t *p)
{
    ap_hook_handler(auth_openid_handler, NULL, NULL, APR_HOOK_MIDDLE);
}

/* Dispatch list for API hooks */
module AP_MODULE_DECLARE_DATA auth_openid_module = {
    STANDARD20_MODULE_STUFF, 
    create_dir_config,                  /* create per-dir    config structures */
    NULL,                  /* merge  per-dir    config structures */
    NULL,                  /* create per-server config structures */
    NULL,                  /* merge  per-server config structures */
    auth_openid_cmds,                  /* table of config file commands       */
    auth_openid_register_hooks  /* register hooks                      */
};


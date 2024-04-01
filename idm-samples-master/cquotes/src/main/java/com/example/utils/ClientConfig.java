/*
 * This file is subject to the terms and conditions defined in
 * file 'LICENSE.MD' which is part of this source code package.
 */
package com.example.utils;

/**
 * It contains the application configuration and constants
 * Like a properties file, but simpler
 */
public class ClientConfig {

    //YOUR IDENTITY DOMAIN AND APPLICATION CREDENTIALS
    public static final String CLIENT_ID = "67132b667e1246ac841e089da0d62016";
    public static final String CLIENT_SECRET = "fe1cecf6-9d8f-482a-9ad3-de8c70a9b1eb";

    public static final String IDCS_URL = "https://idcs-8b47c72fe0a04e70beb04471fe204d58.identity.oraclecloud.com/";

    //INFORMATION ABOUT THE CQUOTES APPLICATION
    private static final String APP_HOST = "http://129.213.47.115:8181";
    static final String APP_RETURN_URI = APP_HOST + "/cquotes/return";
    //public static final String APP_POST_LOGOUT_REDIRECT_URI = APP_HOST + "/cquotes";
    public static final String APP_POST_LOGOUT_REDIRECT_URI = "https://otn.oracle.com";

    //INFORMATION ABOUT IDENTITY CLOUD SERVICES
    static final String AUTHZ_SERVICE_URL = IDCS_URL + "/oauth2/v1/authorize";
    static final String TOKEN_SERVICE_URL = IDCS_URL + "/oauth2/v1/token";
    public static final String LOGOUT_SERVICE_URL = IDCS_URL + "/oauth2/v1/userlogout";
    static final String USERINFO_SERVICE_URL = IDCS_URL + "/oauth2/v1/userinfo";
    public static final String ADMIN_UI_URL = IDCS_URL + "/ui/v1/adminconsole";
    public static final String MYCONSOLE_UI_URL = "https://idcs-8b47c72fe0a04e70beb04471fe204d58.identity.oraclecloud.com/ui/v1/myconsole?root=my-info";
    
    //SCOPES LEVERAGED BY YOUR APPLICATION
    public static final boolean IS_RESOURCE_SERVER_ACTIVE = false;
    public static final String SCOPE_AUD = "http://localhost:8080/salesinsight/";
    public static final String SCOPE_ALL = "all";
    public static final String SCOPE_QUOTE = "quote";
    public static final String SCOPE_INSIGHT = "insight";
    public static final String SCOPE_PIPELINE = "pipeline";
    public static final String SCOPE_REPORT = "report";
    
    static String getAllScopes(){
        return ClientConfig.SCOPE_AUD+ClientConfig.SCOPE_QUOTE+" "+
               ClientConfig.SCOPE_AUD+ClientConfig.SCOPE_INSIGHT+" "+
               ClientConfig.SCOPE_AUD+ClientConfig.SCOPE_PIPELINE+" "+
               ClientConfig.SCOPE_AUD+ClientConfig.SCOPE_REPORT;
    }
    
    //PROXY
    static final boolean HAS_PROXY = false;
    static final String PROXY_HOST = "http://my.proxy.com";
    static final int PROXY_PORT = 80;
}

import time


POST_TITLE       = "排程系統"
VERSION          = '0.1.0'
POST_TIME        = time.ctime()
CURRENT_FUNCTION = '自動登入、偵測時間、自動發文'
NEW_FUNCTION     = '自動登出'
POST_CONTENT = '%s v%s\n發文時間： %s\n舊有功能：%s\n新增功能：%s'\
               %(POST_TITLE, VERSION, POST_TIME, CURRENT_FUNCTION, NEW_FUNCTION)

ELEMENTS = ['webName', 'webPortal', 'webLoginPage', 'webAccount', 'webPswrd', 'webHomePage', 'webLogoutHref']
CSS = ['loginNicknameCssId', 'loginPswrdCssId', 'loginSubmitCssId', 'checkLoginCssId', 'inputHolder', 'logoutCssId']

PLURK_ELEMENTS = ['Plurk',
                  'https://www.plurk.com/portal/',
                  'https://www.plurk.com/login?r=',
                  'THE_ACCOUNT',
                  'THE_PASSWORD',
                  'THE_ACCOUNT_HOMEPAGE',
                  ]
PLURK_CSSID = ['input_nick_name',
               'input_password',
               'login_submit',
               #'div[id = "nav-account"] span',
               'body div[class = "top-bar-user"] ul li[class = "item left"] div[id = "nav-account"] span',
               'input_big',
               '登出']
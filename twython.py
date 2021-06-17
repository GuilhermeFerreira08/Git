# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:26:40 2021

@author: gferr
"""

from twython import Twython

class AppTwitter(TwythonError):
#Obter autorização AUTH2
   # APP_KEY = '' ## username para o request pelo app
   # APP_KEY_SECRET = '' ## password para o request em nome do app
   #APP_SECRET = ''
    #ACCESS_TOKEN = '' ## token da conta do twitter que pertence ao app para permissao de fazer o request por meio da conta
    #ACCESS_TOKEN_SECRET = '' ## idem
    #BEARER_TOKEN = '' ## representa o app e permite autenticar os requests para o token de autenticacao OAuth 2.0
    custom_header={
        'headers':{
        'User-Agent':'NameApp'
        },
        'proxies':{
        'http':'http://10.0.10.1:8000'    
        },
        'timeout':10000
    }
    
    def __init__(self,app_key,app_secret):
        self.app_key = APP_KEY 
        self.app_secret = APP_SECRET 
        twitter = Twython(self.APP_KEY,self.APP_SECRET, oauth_version=2,client_args=(custom_header))#obter o token de acesso
        ACCESS_TOKEN = twitter.obtain_access_token() #salvar
        twitter = Twython(APP_KEY,access_token = ACCESS_TOKEN) #usar o token de acesso
        
    endpoint = 'https://api.twitter.com/2/tweets/'

    #Utilizar o token enviado
            
    #search
    @property
    def url_endpoint(keyword,type_search):
        constructed_url = twitter.construct_api_url(endpoint,q=keyword,result_type=type_search)
        return constructed_url

    def get(keyword,type_search='popular'):
        if keyword is not None:
            results_searches = twitter.cursor(twitter.search,q=keyword,result_type=type_search,return_pages=True)
            return results_searches
    

    def get_mentions(name):
        if name is not None:
            resuts_mentions=twitter.cursor(twitter.get_mentions_timeline,name=name,return_pages=True,include_rts=True)
            yield results_mentions
    
    def get_user(screen_name,user_id):
        if (screen_name != None | user_id != None):
            result_user = twitter.cursor(twiter.get_user_timeline,screen_name=screen_name,user_id=user_id)
            yield result_user
    
    
    
    
try:   
    app = AppTwitter()
except TwythonError as err:
    print ("Msg: " err.msg  + 'Code: '+ err.error_code,sep=',')
    
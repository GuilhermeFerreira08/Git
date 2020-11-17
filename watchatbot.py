# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:35:49 2020

@author: Microsoft
"""
import requests
import json
import datetime

class WaBot():
    
    def __init__(self,json):
        self.json = json
        self.dict_messages = json['messages']
        self.APIUrl =  ## url e token sao usados para fazer uma solicitacao a API 
        self.token = ## requisicao para ao WEbHook para obter o token    
   # enviar solicitacoes 
    def send_request(self,method,data):
        url = "{self.APIUrl}{method}?token={self.token}"
        headers = {'Content-type':'application/json'}
        answer = requests.post(url,json.dumps(data),headers) ## dados serializados
        return answer.json()
   # envio de mensagens
   def send_message(self,chatID,text):
       data = {"chatID" : chatID, ##id para onde sera enviado a mensagem
               "body" : text}
       answer = self.send_requests('sendMessage',data)
       return answer
   def saudacoes(self,chatID,bemvindo = False):
       frase_saudacao = ''
       if (bemvindo == False):
           frase_saudacao = "Olá!\n"
       else:
           frase_saudacao = """Incorrect command
           Commands:
               1. chatid - show ID of the current chat
               2. time - show server time
               3. me - show your nickname"""
       return self.send_message(chatID, frase_saudacao)
   
   def show_Id(self,chatID):
       return self.send_message(chatID,"chatID:{chatID}")
   
   def time(self,chatID):
       t = datetime.datetime.now()
       time = t.strftime("%d:%m:%Y")
       return self.send_message(chatId,time)

   def me(self, chatID, name):
       return self.send_message(chatID, name)
    
   #funcao chamada apos receber dados do webhook
    def processing(self):
       if(self.dict_message != {}):
           for message in self.dict_messages:##dicionarios de msgs recebidas
               text = message['body'].split()
               if(self.dict_messages != []):
                   for message in self.dict_messages:
                       text = message['body'].split()
                       if not(message['fromMe']):
                           id = message['chatId']
                           if text[0].lower() == 'ola':
                               return self.saudacoes(id)
                           elif text[0].lower() == 'time':
                               return self.time(id)
                           elif text[0].lower() == 'chatid':
                               return self.show_Id(id)
                           elif text[0].lower() == 'me':
                               return self.me(id, message['senderName'])
               else: return self.saudacoes(id, True)
       else: return 'NoCommand'
     
    
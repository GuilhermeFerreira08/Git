# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 23:53:27 2021

@author: gferr
"""

import json 
import requests
import datetime

class Wabot():
    def __init__(self,json):
        self.json = json
        self.message = json['message']
        self.APIUrl = ""
        self.token = ""
        
    def send_requests(self,method,data):
        url = f"{self.APIUrl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data),headers=headers)
        return answer.json()
    
    def send_message(self,chatId,text):
        data = {"chatId": chatId,
                "body": text}
        answer = self.send_requests('sendMessage',data)
        return answer
    
    def welcome(self,chatId,noWelcome = False):
        welcome_string = ''
        if(noWelcome == False):
            welcome_string = "Whatsapp\n"
        else:
            welcome_string = """ Comando errado
            1. chatId - show Id of current chat
            2. time - show server time
            3. me - show your nickname
            4. file [format] - get a file. Available formats: doc/gif/jpg/png/pdf/mp3/mp4
            5. ptt - get voice msg
            6. geo - get a location
            7. group - create a group with the bot
            """
            return self.send_message(chatId,welcome_string)
    
    def show_chat_id(self,chatId):
        return self.send_message(chatId,f"Chat ID : {chatId}")
    
    def time(self,chatId):
        t = datetime.datetime.now()
        time = t.strftime('%d:%m:%Y')
        return self.send_message(chatId, time)
    
    def file(self,chatId,format):
        availableFiles = {'doc' : 'document.doc',
                'gif' : 'giffile.gif',
                'jpg' : 'jpgfile.jpg',
                'png' : 'pngfile.png',
                'pdf' : 'presentation.pdf',
                'mp4' : 'video.mp4',
                'mp3' : 'mp3file.mp3'}
        if format in availableFiles.keys():
            data = {
                'chatId' : chatId,
                'body': f'https://domain.com/Python/{availableFiles[format]}',
                'filename' : availableFiles[format],
                'caption' : f'Get your file {availableFiles[format]}'
            }
        return self.send_requests('sendFile', data)
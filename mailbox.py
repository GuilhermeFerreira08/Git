# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:40:50 2020

@author: 
"""
#comunicacao de um provedor de email com um servidor IMAP
import imapclient,pprint,datetime,imaplib,pyzmail

class Imap:
    imaplib._MAXLINE = 1000000
    def __init__(self,email,senha):#conexao entre o provedor de email IMAP do gmail client via login
        self.email = email
        self.senha = senha
        self.obj = imapclient.IMAPClient(host='imap.gmail.com',ssl=True)
        login = self.obj.login(self.email,self.senha)
        if not(login):
            raise Exception("Login não homologado")
        
    def selecionarPastaPrincipal(self):
        #pprint.pprint(self.obj.list_folders())
        pastas = self.obj.select_folder('INBOX',readonly=True)
        return (pastas)
    
    def selecionarMensagens(self,hoje):
        uids = self.obj.search(['ON' +' '+ str(hoje)])#array com os uids de cada conta email
        return uids
    
    def buscarEmails(self,umsgs):
        bdmsgs = self.obj.fetch(self.umsgs,['BODY[]'])
        #pyzmail.PyzMessage.factory(bdmsgs)
        return bdmsgs
        
    def apagarEmail(self,hoje,readonly=False):
        self.obj.select_folder('INBOX',readonly=False)#for possivel a delecao de email da caixa principal de msgs
        delmsgs = Imap.selecionarMensagens(hoje)
        self.obj.delete_messages(delmsgs) #retorna as iuds das mesagens com a flag deleted
        self.obj.expunge() #apaga as msgs com a flag deleted
    
    def desconectarEmail(self):
        self.obj.logout()
    
try:
    email = input('Insira seu email\n')
    senha = input('Insira sua senha\n')
    imap = Imap(email,senha) #uma vez objeto instanciado de Imap e efetuado conexao e login no servidor imap cliente
    pasta = imap.selecionarPastaPrincipal(obj)
    umsgs = selecionarMensagens(datetime.datetime.now().strftime('%Y-%m-%d')) # year-month-day
    bmsg = buscarEmails(umsgs)
    pprint.pprint(bmsg)
except Exception as err:
    print('Erro detectado:' + str(err))


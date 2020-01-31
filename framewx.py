# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:50:38 2020

@author:wxUser
"""
import wx
        
class Main(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title='hi')
        self.panel = wx.Panel(self)   
        self.my_sizer = wx.BoxSizer(wx.VERTICAL) 
        self.text_ctrl = wx.TextCtrl(self.panel,pos=(5, 5))
        self.my_sizer.Add(self.text_ctrl, 10, wx.ALL | wx.EXPAND, 5)   
        self.button = wx.Button(self.panel,label='Enter',pos=(10,80))
        self.button.Bind(wx.EVT_BUTTON,self.print('ok'))
        self.Show()
        
    def click(self,event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print('You typed: "{value}"')


app = wx.App()
Main()        
app.MainLoop()



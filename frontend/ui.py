import wx
from . import widgets, events

import wx
class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="Password Strength Checker",size=(600,500))
        panel=wx.Panel(self)
        my_sizer=wx.BoxSizer(wx.VERTICAL)

        #Created a password entering textbox and binded it with the event on_password_change strength bar
        self.password_box=wx.TextCtrl(panel,style=wx.TE_PASSWORD)
        my_sizer.Add(self.password_box,0,wx.ALL | wx.EXPAND, 5)
        self.password_box.Bind(wx.EVT_TEXT,self.on_password_change)

        #Created a strength bar and added it to my_sizer which is a BoxSizer(i.e dynamic alignment)
        self.strength_bar=wx.Gauge(panel,range=100,size=(250,25))
        my_sizer.Add(self.strength_bar,0,wx.ALL | wx.EXPAND, 15)

        #A label below the strength bar that says good medium or bad password strength
        self.strength_label=wx.StaticText(panel,label="Strength: ")
        my_sizer.Add(self.strength_label,0,wx.ALL,5)

        panel.SetSizer(my_sizer)
        self.Show()
def calculate_strength(self,password):
    return 69 #I have returned 69 temporarily later we need to integrate it with backend to get proper score
    
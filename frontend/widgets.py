import wx

def create_password_box(panel, handler):
    box = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
    box.Bind(wx.EVT_TEXT, handler)   # bind event to handler
    return box

def create_strength_bar(panel):
    return wx.Gauge(panel, range=100, size=(250,25))

def create_strength_label(panel):
    return wx.StaticText(panel, label="Strength: ")
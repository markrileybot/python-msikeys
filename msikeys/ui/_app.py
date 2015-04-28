import wx

class KeyboardFrame(wx.Frame):

    def __init__(self):
        super(KeyboardFrame, self).__init__(None, title='MSI Keys', size=(400, 300))
        self.Center()
        self.Show()

def main():
    app = wx.App()
    KeyboardFrame()
    app.MainLoop()



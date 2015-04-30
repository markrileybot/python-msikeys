import wx
import msikeys

class KeyboardFrame(wx.Frame):

    def __init__(self, keyboard):
        super(KeyboardFrame, self).__init__(None, title='MSI Keys', size=(400, 300))
        self.keyboard = keyboard
        self.main_panel = wx.Panel(self, -1)
        self.main_panel.SetBackgroundColour('#4f5049')

        self.region_panels = []
        vbox = wx.BoxSizer(wx.HORIZONTAL)
        for region in keyboard:
                vbox.Add(wx.Panel(self.main_panel), 1, wx.EXPAND | wx.ALL, 10)

        self.main_panel.SetSizer(vbox)

        self.Center()
        self.Show()

def main():
    app = wx.App()
    KeyboardFrame(msikeys.get_keyboard())
    app.MainLoop()



import wx
import msikeys

class KeyboardFrame(wx.Frame):

    def __init__(self, keyboard):
        super(KeyboardFrame, self).__init__(None, title='MSI Keys', size=(400, 150))
        self.keyboard = keyboard
        self.selected_regions = []

        sizer = wx.BoxSizer(wx.VERTICAL)

        region_buttons = []
        button_panel = wx.Panel(self, -1)
        button_panel.SetBackgroundColour('#4f5049')
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        for region in keyboard:
            region_name = msikeys.Region.values()[region.id]
            region_buttons.append(wx.ToggleButton(button_panel, region.id, region_name))

        slider_panel = wx.Panel(self, -1)
        slider_panel.SetBackgroundColour('#4f5049')
        slider_sizer = wx.BoxSizer(wx.VERTICAL)
        self.color = wx.Slider(slider_panel, -1, msikeys.Color.OFF, msikeys.Color.OFF, msikeys.Color.WHITE,
                               style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)
        self.level = wx.Slider(slider_panel, -1, -msikeys.Level.LIGHT, -msikeys.Level.LIGHT, -msikeys.Level.HIGH,
                               style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)

        for region_button in region_buttons:
            button_sizer.Add(region_button, 1, wx.EXPAND | wx.ALL, 4)

        slider_sizer.Add(self.color, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=4)
        slider_sizer.Add(self.level, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=4)

        sizer.Add(button_panel, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Add(slider_panel, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        button_panel.SetSizer(button_sizer)
        slider_panel.SetSizer(slider_sizer)

        self.SetBackgroundColour('#4f5049')
        self.SetSizer(sizer)
        self.Center()
        self.Show()

        for region_button in region_buttons:
            region_button.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_region)

        self.color.Bind(wx.EVT_SLIDER, self.update_color)
        self.level.Bind(wx.EVT_SLIDER, self.update_level)

    def toggle_region(self, event):
        for region in self.keyboard:
            if region.id == event.GetId():
                for i, selected in enumerate(self.selected_regions):
                    if selected == region:
                        del self.selected_regions[i]
                        break
                if event.IsChecked():
                    self.selected_regions.append(region)
                break

    def update_color(self, event):
        new_color = self.color.GetValue()
        for region in self.selected_regions:
            region.color = new_color
        self.keyboard.commit()

    def update_level(self, event):
        new_level = -self.level.GetValue()
        for region in self.selected_regions:
            region.level = new_level
        self.keyboard.commit()


def main():
    app = wx.App()
    KeyboardFrame(msikeys.get_keyboard())
    app.MainLoop()



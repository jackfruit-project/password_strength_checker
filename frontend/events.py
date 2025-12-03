from .ui import calculate_strength,MainFrame
def on_password_change(self, frame):
    password = self.password_box.GetValue()
    score = self.calculate_strength(password)  # can calculate using custom logic later

    frame.strength_bar.SetValue(score)

    if score < 30:
        frame.strength_label.SetLabel("Strength: Weak")
    elif score < 70:
        frame.strength_label.SetLabel("Strength: Medium")
    else:
        frame.strength_label.SetLabel("Strength: Strong")

#The functions calculate_strength, MainFrame are not getting imported check it once
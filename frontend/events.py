def on_password_change(event, frame):
    password = frame.password_box.GetValue()
    score = frame.calculate_strength(password)  # your custom logic later

    frame.strength_bar.SetValue(score)

    if score < 30:
        frame.strength_label.SetLabel("Strength: Weak")
    elif score < 70:
        frame.strength_label.SetLabel("Strength: Medium")
    else:
        frame.strength_label.SetLabel("Strength: Strong")
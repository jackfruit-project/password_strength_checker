import wx
import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
backend_dir = os.path.join(parent_dir, 'backend') 

print(f"Current directory: {current_dir}")
print(f"Parent directory: {parent_dir}")
print(f"Backend directory: {backend_dir}")


if os.path.exists(backend_dir):
    print(f"✓ Found backend directory at: {backend_dir}")
    sys.path.insert(0, backend_dir)
else:
    print(f"✗ Backend directory NOT FOUND at: {backend_dir}")

try:
    from evaluator import evaluate_password
    print("✓ Successfully imported backend from evaluator.py")
except ImportError as e:
    print(f"✗ Failed to import: {e}")
    wx.MessageBox(
        f"Cannot import backend!\n\n"
        f"Backend dir: {backend_dir}\n\n"
        f"Error: {e}\n\n"
        f"Make sure evaluator.py is in the backend directory!",
        "Import Error",
        wx.OK | wx.ICON_ERROR
    )
    sys.exit(1)

# WXPYTHON FRONTEND
class PasswordCheckerFrame(wx.Frame):
    """Main application window for password strength checking"""
    
    def __init__(self):
        super().__init__(
            parent=None,
            title='Password Strength Checker',
            size=(650, 750)
        )
        
        # Setup UI
        self.init_ui()
        self.Centre()
        self.Show()
    
    def init_ui(self):
        """Initialize the user interface"""
        panel = wx.Panel(self)
        # black background
        panel.SetBackgroundColour(wx.Colour(0, 0, 0))
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Title - Matrix green
        title = wx.StaticText(panel, label='🔒 Password Strength Checker')
        title_font = wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title.SetFont(title_font)
        title.SetForegroundColour(wx.Colour(0, 255, 0))  # Bright green
        main_sizer.Add(title, 0, wx.ALL | wx.CENTER, 20)
        
        # Subtitle
        subtitle = wx.StaticText(panel, label='Analyze your password security in real-time')
        subtitle_font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL)
        subtitle.SetFont(subtitle_font)
        subtitle.SetForegroundColour(wx.Colour(0, 200, 0))  # Darker green
        main_sizer.Add(subtitle, 0, wx.ALL | wx.CENTER, 5)
        
        # Separator - green line
        separator = wx.StaticLine(panel)
        separator.SetBackgroundColour(wx.Colour(0, 255, 0))
        main_sizer.Add(separator, 0, wx.EXPAND | wx.ALL, 10)
        
        # Password input section
        input_box = wx.StaticBox(panel, label='Enter Password')
        input_box.SetForegroundColour(wx.Colour(0, 255, 0))
        input_sizer = wx.StaticBoxSizer(input_box, wx.VERTICAL)
        
        password_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.password_input = wx.TextCtrl(
            panel,
            style=wx.TE_PASSWORD,
            size=(450, 35)
        )
        self.password_input.SetBackgroundColour(wx.Colour(20, 20, 20))  # Dark gray
        self.password_input.SetForegroundColour(wx.Colour(0, 255, 0))  # Green text
        self.password_input.Bind(wx.EVT_TEXT, self.on_password_change)
        
        # Show/Hide password toggle  - masking the password
        self.show_password_btn = wx.ToggleButton(panel, label='👁️ Show', size=(90, 35))
        self.show_password_btn.SetBackgroundColour(wx.Colour(0, 100, 0))
        self.show_password_btn.SetForegroundColour(wx.Colour(0, 255, 0))
        self.show_password_btn.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_password_visibility)
        
        password_sizer.Add(self.password_input, 1, wx.ALL | wx.EXPAND, 5)
        password_sizer.Add(self.show_password_btn, 0, wx.ALL, 5)
        input_sizer.Add(password_sizer, 0, wx.EXPAND)
        
        main_sizer.Add(input_sizer, 0, wx.ALL | wx.EXPAND, 10)
        
        # Strength indicator section
        strength_box = wx.StaticBox(panel, label='Password Strength')
        strength_box.SetForegroundColour(wx.Colour(0, 255, 0))
        strength_sizer = wx.StaticBoxSizer(strength_box, wx.VERTICAL)
        
        # Progress bar
        self.strength_gauge = wx.Gauge(panel, range=100, style=wx.GA_HORIZONTAL | wx.GA_SMOOTH)
        self.strength_gauge.SetMinSize((500, 30))
        strength_sizer.Add(self.strength_gauge, 0, wx.ALL | wx.EXPAND, 5)
        
        # Strength label and score
        strength_label_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.strength_label = wx.StaticText(panel, label='Not evaluated')
        strength_label_font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.strength_label.SetFont(strength_label_font)
        self.strength_label.SetForegroundColour(wx.Colour(0, 200, 0))
        
        self.score_label = wx.StaticText(panel, label='Score: 0/100')
        score_font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.score_label.SetFont(score_font)
        self.score_label.SetForegroundColour(wx.Colour(0, 200, 0))
        
        strength_label_sizer.Add(self.strength_label, 1, wx.ALL, 5)
        strength_label_sizer.Add(self.score_label, 0, wx.ALL, 5)
        strength_sizer.Add(strength_label_sizer, 0, wx.EXPAND)
        
        main_sizer.Add(strength_sizer, 0, wx.ALL | wx.EXPAND, 10)
        
        # Character requirements checklist
        requirements_box = wx.StaticBox(panel, label='Character Requirements')
        requirements_box.SetForegroundColour(wx.Colour(0, 255, 0))
        requirements_sizer = wx.StaticBoxSizer(requirements_box, wx.VERTICAL)
        
        self.requirement_checks = {}
        requirements = [
            ('has_upper', 'Uppercase letters (A-Z)'),
            ('has_lower', 'Lowercase letters (a-z)'),
            ('has_digit', 'Numbers (0-9)'),
            ('has_symbol', 'Special characters (!@#$%^&*)')
        ]
        
        for key, label in requirements:
            cb = wx.CheckBox(panel, label=label)
            cb.SetForegroundColour(wx.Colour(0, 255, 0))
            cb.Enable(False)  # Make read-only
            self.requirement_checks[key] = cb
            requirements_sizer.Add(cb, 0, wx.ALL, 5)
        
        main_sizer.Add(requirements_sizer, 0, wx.ALL | wx.EXPAND, 10)
        
        # Security metrics section
        metrics_box = wx.StaticBox(panel, label='Security Analysis')
        metrics_box.SetForegroundColour(wx.Colour(0, 255, 0))
        metrics_sizer = wx.StaticBoxSizer(metrics_box, wx.VERTICAL)
        
        metrics_grid = wx.FlexGridSizer(rows=4, cols=2, hgap=15, vgap=8)
        metrics_grid.AddGrowableCol(1, 1)
        
        # Length
        length_text = wx.StaticText(panel, label='Password Length:')
        length_text.SetForegroundColour(wx.Colour(0, 255, 0))
        metrics_grid.Add(length_text, 0, wx.ALIGN_CENTER_VERTICAL)
        self.length_label = wx.StaticText(panel, label='0 characters')
        self.length_label.SetForegroundColour(wx.Colour(0, 200, 0))
        metrics_grid.Add(self.length_label, 0, wx.ALIGN_CENTER_VERTICAL)
        
        # Entropy
        entropy_text = wx.StaticText(panel, label='Shannon Entropy:')
        entropy_text.SetForegroundColour(wx.Colour(0, 255, 0))
        metrics_grid.Add(entropy_text, 0, wx.ALIGN_CENTER_VERTICAL)
        self.entropy_label = wx.StaticText(panel, label='N/A')
        self.entropy_label.SetForegroundColour(wx.Colour(0, 200, 0))
        metrics_grid.Add(self.entropy_label, 0, wx.ALIGN_CENTER_VERTICAL)
        
        # Pattern check
        patterns_text = wx.StaticText(panel, label='Patterns Detected:')
        patterns_text.SetForegroundColour(wx.Colour(0, 255, 0))
        metrics_grid.Add(patterns_text, 0, wx.ALIGN_CENTER_VERTICAL)
        self.patterns_label = wx.StaticText(panel, label='N/A')
        self.patterns_label.SetForegroundColour(wx.Colour(0, 200, 0))
        metrics_grid.Add(self.patterns_label, 0, wx.ALIGN_CENTER_VERTICAL)
        
        # Common password check
        common_text = wx.StaticText(panel, label='Common Password:')
        common_text.SetForegroundColour(wx.Colour(0, 255, 0))
        metrics_grid.Add(common_text, 0, wx.ALIGN_CENTER_VERTICAL)
        self.common_label = wx.StaticText(panel, label='N/A')
        self.common_label.SetForegroundColour(wx.Colour(0, 200, 0))
        metrics_grid.Add(self.common_label, 0, wx.ALIGN_CENTER_VERTICAL)
        
        metrics_sizer.Add(metrics_grid, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(metrics_sizer, 0, wx.ALL | wx.EXPAND, 10)
        
        # Feedback section
        feedback_box = wx.StaticBox(panel, label='Recommendations')
        feedback_box.SetForegroundColour(wx.Colour(0, 255, 0))
        feedback_sizer = wx.StaticBoxSizer(feedback_box, wx.VERTICAL)
        
        self.feedback_text = wx.TextCtrl(
            panel,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_WORDWRAP,
            size=(-1, 100)
        )
        self.feedback_text.SetBackgroundColour(wx.Colour(20, 20, 20))  # Dark gray
        self.feedback_text.SetForegroundColour(wx.Colour(0, 255, 0))  # Green text
        self.feedback_text.SetValue('Enter a password to see security recommendations')
        feedback_sizer.Add(self.feedback_text, 1, wx.ALL | wx.EXPAND, 5)
        
        main_sizer.Add(feedback_sizer, 1, wx.ALL | wx.EXPAND, 10)
        
        # Action buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        analyze_btn = wx.Button(panel, label='🔍 Detailed Analysis', size=(150, 40))
        analyze_btn.SetBackgroundColour(wx.Colour(0, 100, 0))
        analyze_btn.SetForegroundColour(wx.Colour(0, 255, 0))
        analyze_btn.Bind(wx.EVT_BUTTON, self.on_analyze_button)
        
        clear_btn = wx.Button(panel, label='🗑️ Clear', size=(100, 40))
        clear_btn.SetBackgroundColour(wx.Colour(0, 100, 0))
        clear_btn.SetForegroundColour(wx.Colour(0, 255, 0))
        clear_btn.Bind(wx.EVT_BUTTON, self.on_clear_button)
        
        button_sizer.Add(analyze_btn, 0, wx.ALL, 5)
        button_sizer.Add(clear_btn, 0, wx.ALL, 5)
        
        main_sizer.Add(button_sizer, 0, wx.ALL | wx.CENTER, 10)
        
        panel.SetSizer(main_sizer)
    
    def on_password_change(self, event):
        """Handle real-time password input changes"""
        password = self.password_input.GetValue()
        if password:
            self.update_strength_display(password)
        else:
            self.reset_display()
    
    def on_analyze_button(self, event):
        """Handle analyze button click - show detailed analysis popup"""
        password = self.password_input.GetValue()
        
        if not password:
            wx.MessageBox(
                'Please enter a password to analyze.',
                'No Password',
                wx.OK | wx.ICON_WARNING
            )
            return
        
        # Get evaluation from the backend
        result = evaluate_password(password)
        
        # Build detailed message / password analysis
        msg_parts = [
            "=" * 50,
            "PASSWORD STRENGTH ANALYSIS REPORT",
            "=" * 50,
            "",
            f"Password Length: {result['length']} characters",
            f"Security Score: {result['score']}/100",
            f"Strength Level: {result['strength']}",
            f"Shannon Entropy: {result['entropy']:.2f} bits",
            "",
            "CHARACTER COMPOSITION:",
            f"  ✓ Uppercase Letters: {'Yes' if result['has_upper'] else 'No'}",
            f"  ✓ Lowercase Letters: {'Yes' if result['has_lower'] else 'No'}",
            f"  ✓ Digits: {'Yes' if result['has_digit'] else 'No'}",
            f"  ✓ Special Characters: {'Yes' if result['has_symbol'] else 'No'}",
            "",
            "SECURITY CHECKS:",
            f"  {'⚠️' if result['is_common'] else '✓'} Common Password: {'Yes (WEAK!)' if result['is_common'] else 'No'}",
            f"  {'⚠️' if result['patterns'] else '✓'} Pattern Detection: {len(result['patterns'])} pattern(s) found"
        ]
        
        if result['patterns']:
            msg_parts.append("\n  Patterns detected:")
            for pattern in result['patterns']:
                msg_parts.append(f"    - {pattern}")
        
        # Generating recommendations to improve pass strength
        recommendations = self.generate_recommendations(result)
        if recommendations:
            msg_parts.append("\nRECOMMENDATIONS:")
            for rec in recommendations:
                msg_parts.append(f"  • {rec}")
        else:
            msg_parts.append("\n✓ Your password meets all security criteria!")
        
        msg = '\n'.join(msg_parts)
        
        
        dlg = wx.MessageDialog(
            self,
            msg,
            'Detailed Password Analysis',
            wx.OK | wx.ICON_INFORMATION
        )
        dlg.ShowModal()
        dlg.Destroy()
    
    def on_clear_button(self, event):
        """Clear all fields and reset display"""
        self.password_input.Clear()
        self.reset_display()
    
    def update_strength_display(self, password):
        """Update all UI elements based on password strength"""
        try:
            # Get evaluation from backend
            result = evaluate_password(password)
            
            # Update gauge
            score = result['score']
            self.strength_gauge.SetValue(score)
            
            # Update strength label with color dynamically
            strength = result['strength']
            self.strength_label.SetLabel(strength)
            
            # Color mapping based on strength - hacker theme
            color_map = {
                'Weak': wx.Colour(255, 0, 0),        # Red for danger
                'Medium': wx.Colour(255, 255, 0),    # Yellow for warning
                'Strong': wx.Colour(0, 255, 0)       # Bright green for success
            }
            color = color_map.get(strength, wx.Colour(0, 200, 0))
            self.strength_label.SetForegroundColour(color)
            
            # Update score label
            self.score_label.SetLabel(f"Score: {score}/100")
            
            # Update character requirements checkboxes
            self.requirement_checks['has_upper'].SetValue(result['has_upper'])
            self.requirement_checks['has_lower'].SetValue(result['has_lower'])
            self.requirement_checks['has_digit'].SetValue(result['has_digit'])
            self.requirement_checks['has_symbol'].SetValue(result['has_symbol'])
            
            # Update metrics
            self.length_label.SetLabel(f"{result['length']} characters")
            
            # Entropy from backend
            entropy = result['entropy']
            entropy_text = f"{entropy:.2f} bits"
            if entropy > 52:
                entropy_text += " (Excellent)"
            elif entropy > 29:
                entropy_text += " (Good)"
            else:
                entropy_text += " (Weak)"
            self.entropy_label.SetLabel(entropy_text)
            
            # Patterns
            patterns_count = len(result['patterns'])
            if patterns_count > 0:
                self.patterns_label.SetLabel(f'{patterns_count} pattern(s) ⚠️')
                self.patterns_label.SetForegroundColour(wx.Colour(255, 0, 0))  # Red
            else:
                self.patterns_label.SetLabel('None ✓')
                self.patterns_label.SetForegroundColour(wx.Colour(0, 255, 0))  # Green
            
            # Common password check
            is_common = result['is_common']
            self.common_label.SetLabel('Yes ⚠️' if is_common else 'No ✓')
            self.common_label.SetForegroundColour(
                wx.Colour(255, 0, 0) if is_common else wx.Colour(0, 255, 0)
            )
            
            # Update feedback with recommendations
            recommendations = self.generate_recommendations(result)
            if recommendations:
                feedback_text = '\n'.join(f"• {rec}" for rec in recommendations)
            else:
                feedback_text = "✓ Excellent! Your password meets all security requirements."
            
            self.feedback_text.SetValue(feedback_text)
            
            self.Layout()
            
        except Exception as e:
            wx.MessageBox(
                f'Error evaluating password:\n{str(e)}',
                'Error',
                wx.OK | wx.ICON_ERROR
            )
    
    def generate_recommendations(self, result):
        """Generate a list of recommendations based on evaluation results"""
        recommendations = []
        
        # Length recommendations
        if result['length'] < 7:
            recommendations.append("Use at least 7 characters (11+ recommended)")
        elif result['length'] < 11:
            recommendations.append("Consider using 11+ characters for better security")
        
        # Character variety recommendations
        if not result['has_upper']:
            recommendations.append("Add uppercase letters (A-Z)")
        if not result['has_lower']:
            recommendations.append("Add lowercase letters (a-z)")
        if not result['has_digit']:
            recommendations.append("Include numbers (0-9)")
        if not result['has_symbol']:
            recommendations.append("Include special characters (!@#$%^&*)")
        
        # Entropy recommendations
        if result['entropy'] < 29:
            recommendations.append("Increase complexity - use a mix of different character types")
        
        # Common password warning
        if result['is_common']:
            recommendations.append("⚠️ CRITICAL: This is a common password! Choose something unique")
        
        # Pattern warnings
        if result['patterns']:
            recommendations.append(f"⚠️ Avoid predictable patterns: {', '.join(result['patterns'])}")
        
        return recommendations
    
    def reset_display(self):
        """Reset all display elements to default state"""
        self.strength_gauge.SetValue(0)
        self.strength_label.SetLabel('Not evaluated')
        self.strength_label.SetForegroundColour(wx.Colour(0, 200, 0))  # Green
        self.score_label.SetLabel('Score: 0/100')
        
        # Reset checkboxes
        for cb in self.requirement_checks.values():
            cb.SetValue(False)
        
        # Reset metrics
        self.length_label.SetLabel('0 characters')
        self.entropy_label.SetLabel('N/A')
        self.patterns_label.SetLabel('N/A')
        self.patterns_label.SetForegroundColour(wx.Colour(0, 200, 0))
        self.common_label.SetLabel('N/A')
        self.common_label.SetForegroundColour(wx.Colour(0, 200, 0))
        
        self.feedback_text.SetValue('Enter a password to see security recommendations')
        self.Layout()
    
    def toggle_password_visibility(self, event):
        """Toggle password visibility"""
        if self.show_password_btn.GetValue():
            # Show password
            current_style = self.password_input.GetWindowStyle()
            self.password_input.SetWindowStyle(current_style & ~wx.TE_PASSWORD)
            self.show_password_btn.SetLabel('👁️ Hide')
        else:
            # Hide password
            current_style = self.password_input.GetWindowStyle()
            self.password_input.SetWindowStyle(current_style | wx.TE_PASSWORD)
            self.show_password_btn.SetLabel('👁️ Show')
        
        # Refresh to apply style change
        password = self.password_input.GetValue()
        self.password_input.ChangeValue(password)


class PasswordCheckerApp(wx.App):
    """Main application class"""
    
    def OnInit(self):
        self.frame = PasswordCheckerFrame()
        return True


#running the application
if __name__ == '__main__':
    app = PasswordCheckerApp()
    app.MainLoop()

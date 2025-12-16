#  Password Strength Checker

A powerful password security analysis tool with a sleek Matrix-themed GUI built using wxPython. Evaluates password strength using advanced algorithms including Shannon entropy, pattern detection, and common password checking.



## Features

- **Real-time Password Analysis** - Instant feedback as you type
- **Shannon Entropy Calculation** - Measures password randomness
- **Pattern Detection** - Identifies sequential characters, keyboard patterns, and repetitions
- **Common Password Detection** - Checks against known weak passwords
- **Character Composition Analysis** - Validates uppercase, lowercase, digits, and special characters
- **Security Score (0-100)** - Comprehensive password strength rating
- **Matrix-Themed UI** - Hacker-style black and green interface
- **Detailed Reports** - Export comprehensive security analysis

## Screenshots
## add later 

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/jackfruit-project/password_strength_checker.git
cd password_strength_checker
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install wxPython manually:

```bash
pip install wxPython (This will not run on WSL, so use a native OS)
```

### Step 3: Run the Application

```bash
cd frontend
python main.py
```

## 📁 Project Structure

```
password_strength_checker/
├── backend/
│   ├── __init__.py
│   ├── evaluator.py      # Main password evaluation logic
│   ├── entropy.py         # Shannon entropy calculation
│   ├── patterns.py        # Pattern detection algorithms
│   ├── blacklist.py       # Common password database
│   └── test_eval.py       # Backend unit tests
├── frontend/
│   ├── __init__.py
│   └── main.py            # wxPython GUI application
├── screenshots/           # Application screenshots
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

##  How It Works

### Password Scoring System

The password is evaluated based on multiple criteria:

1. **Length Score** (5-30 points)
   - 11+ characters: 30 points
   - 7-10 characters: 20 points
   - Less than 7: 5 points

2. **Character Variety** (60 points total)
   - Uppercase letters: 15 points
   - Lowercase letters: 15 points
   - Digits: 15 points
   - Special characters: 15 points

3. **Entropy Score** (5-20 points)
   - High entropy (>60): 20 points
   - Medium entropy (40-60): 10 points
   - Low entropy (<40): 5 points

4. **Penalties**
   - Common password: -40 points
   - Patterns detected: -20 points

### Strength Levels

- **Strong** (80-100): Excellent security, meets all criteria
- **Medium** (50-79): Acceptable but could be improved
- **Weak** (0-49): Vulnerable, needs significant improvement

##  Backend Modules

### `evaluator.py`
Main evaluation engine that coordinates all security checks and calculates the final score.

### `entropy.py`
Implements Shannon entropy calculation to measure password randomness:
```python
H(X) = -Σ p(x) * log₂(p(x))
```

### `patterns.py`
Detects common patterns including:
- Sequential numbers (123, 456)
- Sequential letters (abc, xyz)
- Repeated characters (aaa, 111)
- Keyboard patterns (qwerty, asdfgh)

### `blacklist.py`
Maintains a database of commonly used weak passwords.

##  UI Features

- **Real-time Feedback**: Updates as you type
- **Visual Progress Bar**: Color-coded strength indicator
- **Character Requirements Checklist**: Visual validation
- **Security Metrics Display**: Entropy, patterns, and length
- **Show/Hide Password Toggle**: Privacy control
- **Detailed Analysis Button**: Comprehensive report popup
- **UI**: Matrix-inspired green-on-black design

##  Testing

Run backend tests:

```bash
cd backend
python test_eval.py
```

##  Example Usage

```python
from backend.evaluator import evaluate_password

result = evaluate_password("MyP@ssw0rd123!")

print(f"Score: {result['score']}/100")
print(f"Strength: {result['strength']}")
print(f"Entropy: {result['entropy']:.2f} bits")
print(f"Patterns: {result['patterns']}")
```

##  Security Best Practices

Based on our analysis, strong passwords should:

1. **Be at least 11 characters long**
2. **Include mixed case letters** (A-Z, a-z)
3. **Contain numbers** (0-9)
4. **Use special characters** (!@#$%^&*)
5. **Avoid common words** or predictable patterns
6. **Have high entropy** (randomness)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Jackfruit Project Team** - [GitHub](https://github.com/jackfruit-project)

## Contact

For questions or support, please open an issue on GitHub.

---

**⭐ Star this repository if you find it helpful!**

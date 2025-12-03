from patterns import check_patterns 
from entropy import shannon_entropy 
from blacklist import is_common_password 

def evaluate_password(password:str) -> dict:
    results = {}

    #Standard paramaters
    length = len(password)
    results["password"] = password
    results["length"] = length

    #More standard parameters
    has_upper = any(c.isupper() for c in password)  #any keyword returns true if even a single paramater is true,  eg any[true,false,false, ... ] returns true 
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    results["has_upper"] = has_upper
    results["has_lower"] = has_lower
    results["has_digit"] = has_digit
    results["has_symbol"] = has_symbol

    # Blacklist check
    is_common = is_common_password(password)
    results["is_common"] = is_common

    # Pattern detection check
    patterns_detected = check_patterns(password)
    results["patterns"] = patterns_detected

    # Entropy calculation
    entropy_value = shannon_entropy(password)
    results["entropy"] = entropy_value

    # Scoring the password on above characterestics
    score = 0

    # Length score
    if length >= 11:
        score += 30
    elif length >= 7:
        score += 20
    else:
        score += 5

    # Character variety score
    if has_upper:
        score += 15
    if has_lower:
        score += 15
    if has_digit:
        score += 15
    if has_symbol:
        score += 15

    # Entropy score
    if entropy_value > 60:
        score += 20
    elif entropy_value > 40:
        score += 10
    else:
        score += 5

    # Penalties
    if is_common:
        score -= 40
    if len(patterns_detected) > 0:
        score -= 20

    # Keep score in range
    score = max(0, min(score, 100))
    results["score"] = score

    # Strength label
    if score >= 80:
        results["strength"] = "Strong"
    elif score >= 50:
        results["strength"] = "Medium"
        results["strength"] = "Medium"
    else:
        results["strength"] = "Weak"

    return results



    

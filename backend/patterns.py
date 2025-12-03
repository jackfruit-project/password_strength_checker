def has_repetition(password:str) -> bool:  # in order to check repetitive characters in the password, eg. 111 , xxx etc.
    if len(password)<3:
        return False
    count=1
    for i in range(1,len(password)):
        if  password[i] == password[i-1]:
            count = count+1  
            if count>2:
                return True
        else:
            count=1 

    return False

def has_sequence(password:str) -> bool:  #checking if there are character or number sequences like abc, 123 etc. using ASCII vlaues
    if len(password)<3:
        return False
    for i in range(0, len(password)-2):
        a=password[i]
        b=password[i+1]
        c=password[i+2]
        if ord(a)+1 == ord(b) and ord(b)+1 == ord(c):
            return True
        if ord(c)+1 == ord(b) and ord(b)+1 == ord(a):
            return True
    return False

def has_keyboard_pattern(password: str) -> bool: #checking for common patterns like keyboard sequences qwerty , asdfgh, hjkl etc etc. 
    weak_patterns = ["qwerty", "asdfg", "asdf", "qwer", "qwert", "hjkl", "zxcv"]
    pw_lower = password.lower()

    for i in weak_patterns:
        if i in pw_lower:
            return True
    return False

def check_patterns(password: str) -> list:  #returning the list of all the characterestics of password based on above defined functions 
                                            # eg. if a password is 'abc123qwerty', it satisfies all 3 of above functions hence the list would contain al 3 keywords.
                                            # similarly, if password is something like 'abctesting' it would only return True for the has_sequence function.
    patterns_found = []

    if has_repetition(password):
        patterns_found.append("repetition")

    if has_sequence(password):
        patterns_found.append("sequence")

    if has_keyboard_pattern(password):
        patterns_found.append("keyboard_pattern")

    return patterns_found


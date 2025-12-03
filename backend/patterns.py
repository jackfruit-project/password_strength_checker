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


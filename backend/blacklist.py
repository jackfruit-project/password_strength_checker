import os
g = os.path.join(
    os.path.dirname(__file__),    # location of the blacklist text file 
    "..",                       
    "resources",                
    "blacklist.txt"
)

# Store all blacklisted passwords here
blacklisted = set()


def load_blacklist():
    """
    Load the blacklist file into a Python set.
    Runs only once, when the module is imported.
    """
    if not os.path.exists(g):
        print("blacklist file not found", g)
        return
    
    with open(g, "r") as f:
        for line in f:
            password = line.strip().lower()
            if password:
                blacklisted.add(password)

load_blacklist() #function call


def is_common_password(password: str) -> bool:
    return password.lower() in blacklisted  #returns whether or not password is in the blacklisted set. Based on that it affects the total score of the password found by evaluator python file 



import hashlib

def list_key_exists(key: int, target_list: list):
    if(key < len(target_list)):
        return True
    else:
        return False

def dict_key_exists(key, target_dict: dict):
    if(key in target_dict):
        return True
    else:
        return False

def array_key_exists(key, target_array):
    if(type(target_array) == "dict"):
        return dict_key_exists(key, target_array)
    elif(type(target_array) == "list"):
        if(type(key) == int):
            return list_key_exists(key, target_array)
        else:
            #exception throw here
            return False
    else:
        #exception throw here
        return False

def is_null(needle):
    if(needle is None):
        return True
    else:
        return False

def htmlspecialchars(text: str):
    return text.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")





# https://www.bing.com/search?q=python+sha-256&cvid=0767d638c13d4ff192ce537f45b05dad&aqs=edge.0.69i59j69i57j0l5j69i60l2.2856j0j9&FORM=ANAB01&PC=U531
def password_hash(password: str):
    pass

def password_verify(base_password: str, input_password: str):
    pass
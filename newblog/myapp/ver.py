import string,random
import hashlib
def get_verification():
    capta=''
    
    words=''.join((string.ascii_letters,string.digits))
    
    for i in range(6):
        capta+=random.choice(words)
    
    return capta


def hashs(password):
    password = password + "salts"
    sha256 = hashlib.sha256()
    sha256.update(bytes(password,encoding='utf-8'))
    return sha256.hexdigest()



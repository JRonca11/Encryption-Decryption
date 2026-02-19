from cryptography.fernet import Fernet
import os

def generateNewKey(filePath):
    key = Fernet.generate_key()
    with open(filePath, 'wb') as file:
        file.write(key)
    return key

def encryptMessage(key,message):
    try:
        secureKey = Fernet(key)
        encryptedMessage = secureKey.encrypt(message)
        print(encryptedMessage)
    except:
        print("Could not decryptMessage")


def decryptMessage(key,message):
    try:
        secureKey = Fernet(key)
        decryptedMessage = secureKey.decrypt(message)
        print(decryptedMessage)
    except:
        print("Could not decryptMessage")

while True:
    method = input("Type E for encryption or D for decryption ")
    
    if (method != 'D' and method != 'E'):
        print("You must enter an E or D")
    else:
        break


filePath = "secureKey.txt"

if (os.path.exists(filePath)) == False:
    key = generateNewKey(filePath);

else:
    try:
        with open(filePath, 'rb') as file:
            key = file.read()
    except:
        print("Could not open and read file.")


if method == 'D':
    message = input("Enter your message to decrypt:")
    message = message.encode('utf-8')
    decryptMessage(key,message)

else:
    message = input("Enter your message to encrypt:")
    encryptMessage(key,message)



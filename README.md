# Encryption-Decryption

## Program-Overview
This program will encrypt or decrypt a message that is given to it by the user. The program will use a currently existing key or generate one for the user.
    The program works as follows:
        - If the user would like to encrypt:
            - The program will check for an existing key, if the key
            does not exist, the program will generate a new key and save
            it to a file in the current directory in a file called secureKey.txt. The encrypted message will be printed to the console.
        - If the user would like to decrypt:
            - The program will check for a key in a file called secureKey.txt. The program will use this key to decrypt the encrypted message provided by the user.
    
    ## How to run the program
        - The program requires the following dependencies:
            - python 3.13.1
            - pip
            - Python's Cryptography library
                - install with the following command: pip install cryptography
        - Important Note:
            - The program expects the key to be stored in a file called secureKey.txt stored in the same directory. If the key is stored in a file with a different name or is not in the same directory as the program, the decryption will not run or the message will be encrypted with a newly generated key.

        ##Program Limitations
            - This program is intended only for educational use and purposes and should not be used to securing or storing sensitive information.
        
        ##Responsible Use

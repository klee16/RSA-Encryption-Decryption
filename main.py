
#KEL LEE

import string

import rsa
import random

# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(512)

# this is the string that we will be encrypting

S = 53
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))


# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
encMessage = rsa.encrypt(ran.encode(),
                         publicKey)
Message = rsa.encrypt(ran.encode(),
                         privateKey)



print("original string: ", ran)
print("Private Key Encrypt: ", Message)
print("Public Key Encrypt: ", encMessage)

# the encrypted message can be decrypted
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decrypted string: ", decMessage)
# Press the green button in the gutter to run the script.


# open text file
text_file = open("Key.txt", "w")

# write string to file
n = text_file.write(str(decMessage))

# close file
text_file.close()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

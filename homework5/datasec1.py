from cryptography.fernet import Fernet 

# encryting the below string.
 
message = "hello world"

key = Fernet.generate_key() # to generate key
fernet = Fernet(key) 

print('\nThis is original string')
print("original string: {}\n".format(message))

encMessage = fernet.encrypt(message.encode()) 
print('string gets encrypted')
print("encrypted string: {}\n".format(encMessage))
 
decMessage = fernet.decrypt(encMessage).decode() 
print('string gets decrypt')
print("decrypted string: {}\n".format(decMessage)) 


import hashlib
str= "910703MR9945568"
key=hashlib.sha256(str.encode())
print("The SHA key for this person is hidden\n" + key.hexdigest())
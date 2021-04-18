encode = 'ayush'
key = 26
def caeserCipherEncryptor(string,key):
    new_letters = []
    new_key = key % 26 #when key is too big
    print(new_key)
    for letter in string:
        new_letters.append(get_new_letter(letter,new_key))
    return "".join(new_letters)

def get_new_letter(letter, key):
    print(letter)
    new_LetterCode = ord(letter) + key
    print(new_LetterCode%122)
    return chr(new_LetterCode) if new_LetterCode <= 122 else chr(96 + new_LetterCode % 122)

a = caeserCipherEncryptor(encode, key)
print(a)


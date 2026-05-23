#Name: Dulneth Lahiru Chathushka
#Student Number: 10646610
#Unit: Cryptographic Concepts
#Portfolio part 02.
#Author: Dulneth Lahiru Chathushka.



import random
import math

def prime_check(num):
    if num < 2: 
        return False
    for i in range(2, num): #starting from 2 to num range
        if num % i == 0: #If num is divisible by numbers in i then it is not a prime number.
            return False
    return True #No divisible numbers found, then initialised as num to prime number.

def prime_p_and_q():
    p, q = None, None #Initialised p, q as None, the while loop continue untill the both rpie p and q are intialised.
    while p is None or q is None:
        num = random.randint(500, 1500) #To generate random number between mentioned range in the parenthesis.
        if prime_check(num): #Within the num, it checks the generated number is prime.
            if p is None: #if the p is still none, then the prime number generated in the prime_check assign to p.
                p = num
            elif num != p: #To avoid same prime number generated in p to q. 
                q = num #Initialis the second prime number to q.
    return p, q #Return the initialised prime p and q.


def n_phi_e_d_calculation(p, q): #Function to calculate n, phi, public exponent, private exponent
    n = p * q 
    phi = (p - 1) * (q - 1)
    e = public_key(phi)
    d = pow(e, -1, phi) #multiplicative inverse mod to calculate private exponent.
    return n, phi, e, d


def public_key(phi):
    while True:
        e = random.randint(17, 65) #Public exponent will generate within the given range if the condition gets true. 
        if math.gcd(e, phi) == 1: #This will return if the condition is true. Which is public exponent value must be co-prime with phi value.
            return e

def squareAndMultiply(b, expo, mod): #Square and multiply function to calculate large exponents and values.
    output = 1
    b = b % mod
    while expo > 0:
        if expo % 2 == 1:
            output = (output * b) % mod
        expo = expo // 2
        b = (b * b) % mod
    return output

def key_encryption_k(key, e, n): #encyption involves public key and modulus n value.
    encryption = [] #variable to store encrypte output as a list.
    for char in key: 
        encryption.append(squareAndMultiply(ord(char), e, n)) #Encrypt the ASCII values of the character in the key using the public key and mod n. And also int converts characters in the key into ASCII format.
    return encryption                                                        

def encrypt_to_decrypt(encryption, d, n): #Decryption involves private key and modulus n.
    plainText = [] #Empyt list to store decrypted output.
    for num in encryption:
        plainText.append(chr(squareAndMultiply(num, d, n))) #Convert the ascii values into characters and uses square and multiply method to decrypt the ciphertext.
    return ''.join(plainText)

def RSA_GENERATION():
    p, q = prime_p_and_q()

    n, phi, e, d = n_phi_e_d_calculation(p, q)
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"n: {n}")
    print(f"phi: {phi}")
    print(f"e: {e}")
    print(f"d: {d}\n")
    
    
    key = "SHEEPOSHAN"
    print(f"KEY = {key}")

    key_encryption = key_encryption_k(key, e, n)
    print(f"Encrypted KEY k: {key_encryption}\n")
    CipherText_decryption = encrypt_to_decrypt(key_encryption, d, n)
    print(f"Decrypted KEY K: {CipherText_decryption}\n")

    print("Decrypted KEY K:")
    for en_val, plaintext_character in zip(key_encryption, CipherText_decryption):
        print(f"{en_val} ---> {plaintext_character}")
    
RSA_GENERATION()





        

#Name: Dulneth Lahiru
#Student Number: 10646610
#Unit: Cryptographic Concepts
#Portfolio Part 2
#Author: Dulneth Lahiru Chathushka.

import random
import math


def prime_check(num):
    if num < 2: #Numbers less than 2 is considered as not prime numbers
        return False
    for i in range(2, num): #starting from 2 to num range
        if num % i == 0: #If num is divisible by numbers in i then it is not a prime number.
            return False
    return True #No divisible numbers found, then initialised as num to prime number.

def prime_p_and_q():
    p, q = None, None #Initialised p, q as None, the while loop continue untill the both rpie p and q are intialised.
    while p is None or q is None:
        num = random.randint(85000, 350000) #To generate random number between mentioned range in the parenthesis.
        if prime_check(num): #Within the num, it checks the generated number is prime.
            if p is None: #if the p is still none, then the prime number generated in the prime_check assign to p.
                p = num
            elif num != p: #To avoid same prime number generated in p to q. 
                q = num #Initialis the second prime number to q.
    return p, q #Return the initialised prime p and q.


def n_phi_e_d_calculation(p, q): #Function to calculate modulo n, phi, public key, private key.
    n = p * q 
    phi = (p - 1) * (q - 1)
    e = public_key(phi)
    d = pow(e, -1, phi)
    return n, phi, e, d


def public_key(phi):
    while True:
        e = random.randint(17, 65) #Public exponent will generate within the given range if the condition gets true. Which is public exponent must co-prime with phi value.
        if math.gcd(e, phi) == 1: 
            return e
        
#Function to split message digest into blocks.
def digest_into_blocks(numbers, block_size):
    int_to_num = str(numbers) #Interger convertion to string type. (To spilt).
    return [int(int_to_num[i:i + block_size]) for i in range(0, len(int_to_num), block_size)] #Split the converted string into block according to initialised block size and convert bact to integer format.



def square_and_multiply(b, expo, mod): #Implemented a square and multiply function. since the calculations takes large exponents.
    output = 1 
    b = b % mod #Initialise modulus to base b
    while expo > 0:
        if (expo % 2) == 1: #If the exponent is odd number. It will multiply the output by base and reduce to mod.
            output = (output * b) % mod #Multiply the output by b and reduce to mod.
        expo = expo // 2 #Divide the exponent by 2 
        b = (b * b) % mod #Square the base and take the mod value.
    return output

def signature_verification(signature, block, e, n): 
    computed_digest = square_and_multiply(signature, e, n) #Recheck the message digest using the signature (using square n multiply) and public key pair.

    return computed_digest == block #This will return True if the rechecked message digest exactly same with original message diigest.

hash_value = 16897815116283201938561572347 #Message Digest in question 5 output. (Bob needs to put the received message digest into this.)

block_size = 6 #Purpose is to Spilt the digest into 5 block. There for initialised a variable equal to 5.  
hash_blocks = digest_into_blocks(hash_value, block_size) #The real splitting happens here by assigning to the function.

print("Hash Blocks: ", hash_blocks)

p, q = prime_p_and_q() #P & q primes

n, phi, e, d = n_phi_e_d_calculation(p, q)

public_key_pair = (e, n)
private_key_pair = (d, n)




digital_signatures = [] #Initialised empty list to store digital signature with each signed block.

for each_block in hash_blocks:
    digital_signature = square_and_multiply(each_block, private_key_pair[0], private_key_pair[1]) #Sigining each block using digital signature.
    digital_signatures.append(digital_signature) #Update the signature.


print("Prime p: ",p)
print("prime q: ",q)
print("n: ", n)
print("phi: ",phi)
print("e: ",e)
print("d: ", d)
print("Digital Signature for each block: ", digital_signatures)
print(f"Public Key {public_key_pair}")
print(f"private key {private_key_pair}")
print("Message Digest (within block): ",hash_blocks)

verify_sign = [] #Empty list to store verification result.
for i, sign in enumerate(digital_signatures): #Loop to verify each signature by comparing original message digest (block).
    verification_process = signature_verification(sign, hash_blocks[i] % n, public_key_pair[0], n)
    verify_sign.append((sign, verification_process)) #Process of verification and store the digital signature.

for signing, valid in verify_sign: #Each seperate message digest with corresponding verification.
    print(f"Digital Signature: {signing}, Valid: {valid}")













        

#Name: Dulneth Lahiru Chathushka
#Student Number: 10646610
#Unit: Cryptographic Concepts
#Portfolio Part 2
#Author: Dulneth Lahiru Chathushka.



x = "Exams are on red USB drive in JO 18.103. Password is CaKe314."


def padding_X(x, size_of_the_block): 
    while len(x) % size_of_the_block != 0: #I used padding to fill each block with exactly 7 characters including spaces and fullstops.
        x += '0'                            #If there is empty spaces, "O" will padded for that empty spaces.
    return x


def hash_calculation(padding, size_of_the_block): 
    A = 11*2 #Initialised constant values to achieve complex output.
    B = 19*2
    C = 14*2
    D = 12*2
    E = 15*2
    F = 32/2
    G = 10**2

    number_of_blocks = len(padding) // size_of_the_block #Calculate the total number of blocks after the padded message X.
    each_block_multiplier = [17**12, 19**11, 18**10, 25**5, 20**18, 40**8, 13**12, 19**6, 16**11] #Initialised predefine values. Used to multiply each block with corressponding values. Since the message has 7 block i have initialised 7 variation of values.
    

    for index_of_the_block in range(number_of_blocks): #To iterate through each block (index wise) starting from index_of_the_block[0].
        block = padding[index_of_the_block * size_of_the_block : (index_of_the_block + 1) * size_of_the_block]
        sum_of_block = sum(ord(char) * (i + 1) for i, char in enumerate(block)) #Calculate sum of the ASCII in the block. (Also convert each character to ASCII format. And character are multiplied according to its position in the block.)

        if index_of_the_block < len(each_block_multiplier): #to modify the sum_of_block with predefined multiplers.
            sum_of_block = (sum_of_block * each_block_multiplier[index_of_the_block]) % (3**31) #if the current index is within the range of each_block_multipler, the sum value is multipled by the corressponding multipler.
            #Internally the program divide the message x into 9 blocks. (each block has 7 characters) i have assigned each_block_multiplier predefined values to each block.    
        A = (A + sum_of_block) % (3**31)        #
        B = (B + sum_of_block * 5**11) % (3**31)#
        C = (C * sum_of_block) % (3**31)        #
        D = (D ^ sum_of_block) % (3**31)        #This will update the parameters A,B...G using the sum of ASCII values from the current block.
        E = (E + sum_of_block) % (3**31)        #Also with different kind of arithmatic operations and reduced to mod of 3**31.
        F = (F * sum_of_block) % (3**31)        #
        G = (G + sum_of_block) % (3**31)        #


    return (A * B + C) ^ int(D) + int(E) + int(F) + int(G) #Combining the vaues of A,B,C,D,E,F AND G by mix operations.

size_of_the_block = 7
padding = padding_X(x, size_of_the_block)

message_digest = hash_calculation(padding, size_of_the_block)


print("Message Digest is: ", message_digest)
     


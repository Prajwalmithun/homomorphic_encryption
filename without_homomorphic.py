"""cat_lovers_vs_dog_lovers.py: This is a python script to demonstrate PoC for integration of Fully Homomorphic Encryption to Voting system."""

__author__         = "Prajwal T"
__contributors__   = "Moein, Mehedhi, Jagadeesh"

from Pyfhel import Pyfhel
import numpy as np
import emoji
import pyfiglet
from termcolor import colored
from colorama import Style, Fore
from time import time

# Banner to display the title
title_name = "Cat <3 VS Dog <3"
title = pyfiglet.figlet_format(title_name,font="univers",width=200)
print(Style.BRIGHT, Fore.GREEN, title)

# initialize pyfhel object
fhel = Pyfhel()

# Context setup
fhel.contextGen(scheme='bfv', n=2**14, t_bits=20)

# Generate key
fhel.keyGen()

# Encrypt vote count for candidate 1,2,3
integer0 = np.array([0], dtype=np.int64)
integer1 = np.array([1], dtype=np.int64)
vote_count_1 = fhel.encryptInt(integer0)
vote_count_2 = fhel.encryptInt(integer0)

# Creating a list to store 
elapsed_time_1 = list() 
elapsed_time_2 = list()

def cast_vote(candidate_number):
    if candidate_number == 1:
        global vote_count_1
        global elapsed_time_1

        # starting the timer to capture the execution time for this operation
        start_time = time()
        vote_count_1 = fhel.add(vote_count_1, fhel.encryptInt(integer1))
        end_time = time()
        
        print(f"Encrypted vote_count_1 {vote_count_1}")
        elapsed_time_1.append((end_time - start_time))
        print(f"Time to perform 1 addition in homomorphic operation {elapsed_time_1}")

    elif candidate_number == 2:
        global vote_count_2
        global elapsed_time_2

        # starting the timer to capture the execution time for this opertion 
        start_time = time()
        vote_count_2 = fhel.add(vote_count_2, fhel.encryptInt(integer1))
        end_time = time()

        print(f"Encrypted vote_count_2 {vote_count_2}") 
        elapsed_time_2.append(( end_time - start_time ))
        print(f"Time to perform 1 addition in homomorphic operation {elapsed_time_2}")

    else:
        print("Wrong candidate number")

# Function to decrypt and display vote counts
def display_results():
    #cat = emoji.emojize(":thumbsup")
    cat = "\U0001F63B"
    heart = "\U00002764"
    dog = "\U0001F415"
    elapsed_time = sum(elapsed_time_1) + sum(elapsed_time_2)
    print(f"CAT Lovers{cat} {heart}: {fhel.decryptInt(vote_count_1)[0]}")
    print(f"DOG Lovers{dog} {heart}: {fhel.decryptInt(vote_count_2)[0]}")
    print(f"Time taken to compute each votes {elapsed_time_1} {elapsed_time_2}")
    print(f"Total time {elapsed_time}")


def get_input():
    vote = int(input("CAT Lovers press 1, DOG Lovers press 2: \t"))
    cast_vote(vote)


n = int(input("How many people are voting today? \n"))
for x in range(0,n):
    get_input()

#testing
#cast_vote(2)
#cast_vote(2)
#cast_vote(1)
#cast_vote(1)
#cast_vote(2)
#cast_vote(2)
#cast_vote(2)
#cast_vote(2)

display_results()

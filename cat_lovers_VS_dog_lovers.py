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
import time
import logging

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

# Configuring logging
logging.basicConfig(filename='voting.log', encoding='utf-8', level=logging.DEBUG)


def cast_vote(candidate_number):
    if candidate_number == 1:
        global vote_count_1
        global elapsed_time_1

        # starting the timer to capture the execution time for this operation
        start_time = time.time()
        vote_count_1 = fhel.add(vote_count_1, fhel.encryptInt(integer1))
        end_time = time.time()
        
        print(type(vote_count_1))
        # Pyfhel.PyCtxt.PyCtxt
        in_bytes = vote_count_1.__bytes__()
        print(type(in_bytes))
        #print(in_bytes.decode('UTF-16'))
        logging.info(vote_count_1)
        elapsed_time_1.append((end_time - start_time))
        elapsed_time_now = end_time - start_time
        print(f"Time taken to perform 1 addition in homomorphic operation {elapsed_time_now}\n")

    elif candidate_number == 2:
        global vote_count_2
        global elapsed_time_2

        # starting the timer to capture the execution time for this opertion 
        start_time = time.time()
        vote_count_2 = fhel.add(vote_count_2, fhel.encryptInt(integer1))
        end_time = time.time()

        logging.info(vote_count_2)
        elapsed_time_2.append(( end_time - start_time ))
        elapsed_time_now = end_time - start_time
        print(f"Time taken to perform 1 addition in homomorphic operation {elapsed_time_now}\n")

    else:
        print("Wrong candidate number.You are a HATER lol jk")

# Function to decrypt and display vote counts
def display_results():
    #cat = emoji.emojize(":thumbsup")

    cat = "\U0001F63B"
    heart = "\U00002764"
    dog = "\U0001F415"
    elapsed_time = sum(elapsed_time_1) + sum(elapsed_time_2)
    
    print("\r")
    #print("\tRESULTS")
    results = "PLEASE WAIT, VOTES ARE BEING COUNTED!! HOMOMORPHIC ENCRYPTION IS DOING ITS MAGIC \n"
    for char in results:
        print(char, end="", flush=True)
        time.sleep(0.1)
    print("VOTING RESULTS")
    print("*" * 50 )
    print(f"CAT Lovers{cat} {heart}: {fhel.decryptInt(vote_count_1)[0]}")
    print(f"DOG Lovers{dog} {heart}: {fhel.decryptInt(vote_count_2)[0]}")
    print("*" * 50)
    
    # Announce the winner
    # cat lovers winning 
    cat_votes = fhel.decryptInt(vote_count_1)[0]
    dog_votes = fhel.decryptInt(vote_count_2)[0]
    if cat_votes > dog_votes:
        print(f"WINNERS are CAT LOVERS {cat} {heart}")
    elif cat_votes < dog_votes:
        print(f"WINNERS are DOG LOVERS {dog} {heart}")
    else:
        print(f"BOTH ARE WINNERS {cat} {heart} {dog}")

    print("\n")
    print("EXECUTION TIME")
    print("#" * 25)
    #print(f"Time taken to compute each votes {elapsed_time_1} {elapsed_time_2}")
    print(f"Total time taken to compute {elapsed_time}")
    
    print(f"\nFOR MORE INFORMATION, PLEASE CHECK voting.log FOR LOGS")

def get_input():
    vote = int(input("CAT Lovers press 1, DOG Lovers press 2: \t"))
    cast_vote(vote)


n = int(input("How many people are voting today? \n"))
print("\r")
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

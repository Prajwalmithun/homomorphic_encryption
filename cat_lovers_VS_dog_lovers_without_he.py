"""cat_lovers_vs_dog_lovers_without_he.py: This is a python script to demonstrate a voting system WITHOUT homomorphic encryption."""

__author__         = "Prajwal T"
__contributors__   = "Moein, Mehedhi, Jagadeesh"

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

print(Fore.RED + "NOTE: WITHOUT HOMOMORPHIC ENCRYPTION" + Fore.CYAN)

votes_cat_lovers = 0
votes_dog_lovers = 0 

elapsed_time_list = list()

def cast_vote(candidate_number):
    if candidate_number == 1:
        # increase the count of cat lovers
        global votes_cat_lovers
        
        start_time = time.time()
        votes_cat_lovers = votes_cat_lovers + 1
        end_time = time.time()
    
        elapsed_time = end_time - start_time
        elapsed_time_list.append(elapsed_time)
        print("Time taken to perform 1 addition WITHOUT homomorphic % .16f \n" % elapsed_time)
    elif candidate_number == 2:
        # increase the count of dog lovers
        global votes_dog_lovers

        start_time = time.time()
        votes_dog_lovers = votes_dog_lovers + 1
        end_time = time.time()

        elapsed_time = end_time - start_time
        elapsed_time_list.append(elapsed_time)
        print("Time taken to perform 1 addition WITHOUT homomorphic  % .16f \n" % elapsed_time)
    else:
        # print wrong choice 
        print("You are a hater! lol")

def display_results():
    cat = "\U0001F63B"
    heart = "\U00002764"
    dog = "\U0001F415"

    # print the votes of each cat lovers and dog lovers, with total time to compute
    print("\r")
    results = "PLEASE WAIT, VOTES ARE BEING COUNTED!! NO HOMOMORPHIC ENCRYPTION TO DO MAGIC :(\n"
    for char in results:
        print(char, end="", flush=True)
        time.sleep(0.1)
    print("VOTING RESULTS")
    print("*" * 50)
    print(f"CAT Lovers{cat} {heart}: {votes_cat_lovers}")
    print(f"DOG Lovers{dog} {heart}: {votes_dog_lovers}")
    print("*" * 50)
    
    print("\n")
    print("EXECUTION TIME")
    print("#" * 25)
    print("Total time to compute % .16f" % sum(elapsed_time_list))



def get_input():
    choice = int(input("1 for Cat Lovers, 2 for Dog Lovers \t"))
    cast_vote(choice)


n = int(input("How many people are voting today? \t"))
print("\r")
for x in range(0,n):
    get_input()


display_results()

from Pyfhel import Pyfhel
import numpy as np
import emoji

# initialize pyfhel object
fhel = Pyfhel()

# Context setup
fhel.contextGen(scheme='bfv', n=2**14, t_bits=20)

# Generate key
fhel.keyGen()

# Encrypt vote count for candidate 1,2,3
integer0 = np.array([0], dtype=np.int64)
vote_count_1 = fhel.encryptInt(integer0)
vote_count_2 = fhel.encryptInt(integer0)

integer1 = np.array([1], dtype=np.int64)
# Function to cast the vote
def cast_vote(candidate_number):
    if candidate_number == 1:
        global vote_count_1
        vote_count_1 = fhel.add(vote_count_1, fhel.encryptInt(integer1))
        print(f"Encrypted vote_count_1 {vote_count_1}")

    elif candidate_number == 2:
        global vote_count_2
        vote_count_2 = fhel.add(vote_count_2, fhel.encryptInt(integer1))
        print(f"Encrypted vote_count_2 {vote_count_2}")

    else:
        print("Wrong candidate number")

# Function to decrypt and display vote counts
def display_results():
    #cat = emoji.emojize(":thumbsup")
    cat = "\U0001F63B"
    heart = "\U00002764"
    dog = "\U0001F415"
    print(f"CAT Lovers{cat}{heart}: {fhel.decryptInt(vote_count_1)[0]}")
    print(f"DOG Lovers{dog}{heart}: {fhel.decryptInt(vote_count_2)[0]}")


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


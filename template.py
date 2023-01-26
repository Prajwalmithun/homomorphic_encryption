from Pyfhel import Pyfhel
import numpy as np

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
vote_count_3 = fhel.encryptInt(integer0)

integer1 = np.array([1], dtype=np.int64)
# Function to cast the vote
def cast_vote(candidate_number):
    if candidate_number == 1:
        global vote_count_1
        vote_count_1 = fhel.add(vote_count_1, fhel.encryptInt(integer1))

    elif candidate_number == 2:
        global vote_count_2
        vote_count_2 = fhel.add(vote_count_2, fhel.encryptInt(integer1))

    elif candidate_number == 3:
        global vote_count_3
        vote_count_3 = fhel.add(vote_count_3, fhel.encryptInt(integer1))

    else:
        print("Wrong candidate number")

# Function to decrypt and display vote counts
def display_results():
    print("Candidate 1: ",fhel.decryptInt(vote_count_1)[0])
    print("Candidate 2: ",fhel.decryptInt(vote_count_2)[0])
    print("Candidate 3: ",fhel.decryptInt(vote_count_3)[0])

#testing
cast_vote(2)
cast_vote(2)
cast_vote(1)
cast_vote(1)
cast_vote(2)
cast_vote(2)
cast_vote(2)
cast_vote(2)

display_results()


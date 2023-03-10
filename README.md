# homomorphic_encryption
This a basic utility to simulate voting system integrated with Fully Homomorphic Encryption(FHE). We are conducting a voting between the CAT🐱❤️ Lovers and the DOG🐕❤️ Lovers

# DEMO
![Project working](images/cats_dogs_homomorphic_encryption.gif)

This is how the votes are being stored in memory. Output is in byte format
![](images/encrypted_vote_in_byte_format.png)

# INSTALLATION
NOTE: This has been tested on `debian 11 (Bullseye)`

1. Clone this repository

```
# git clone https://github.com/Prajwalmithun/homomorphic_encryption.git
# cd homomorphic_encryption
```

2. Create a virtual environment to execute the code without conflicting the base system's dependencies. 
Install `virtualenv` on debian using this command `sudo apt install virtualenv python3-virtualenv` 

```
# virtualenv venv
# source venv/bin/activate
```

3. Install the dependencies 
Install `pip` if not installed using this command `sudo apt install python3-pip`

```
# pip3 install -r requirements.txt
```

4. Execute the homomorphic program

```
# python3 cat_lovers_VS_dog_lovers.py
```

5. Another way to execute the program is 

```
# sudo chmod +x run.sh
# ./run.sh
```

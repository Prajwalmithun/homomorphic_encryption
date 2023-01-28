#!/bin/bash


while true
do 
	echo -e "[1] HOMOMORPHIC ELECTION \n[2] NORMAL ELECTION \n[3] EXIT"

	read -p 'Enter your choice 1, 2 OR 3: ' choice

	#echo $choice

	if [ $choice -eq 1 ]; then
		python3 cat_lovers_VS_dog_lovers.py
	elif [ $choice -eq 2 ]; then
		python3 cat_lovers_VS_dog_lovers_without_he.py
	else 
		echo "See you! Take care"
		exit 1
	fi
done 	

#!/usr/bin/env python3

# Script:       CharReplace.py
# date:         tor  6 aug 2020 11:08:36 CEST
# modified by:  Abhjeet SIngh

# imports
import os
import sys

# help menu
if sys.argv[1] == str('-h'):
    print("\nCharReplace: a multipurpose program to replace special characters in file/directories names or rename files/directories")
    print("Author: Abhijeet Singh, abhijeetsingh.aau@gmail.com\n\n")
    print("\n[EXAMPLE]: python3 CharReplace.py <directory/input_dir> <Char_to_replace, 1= one, 2= many> <what_to_replace> <what_to_replace_with>")
    print("\n[EXAMPLE]: python3 CharReplace.py <input_dir> 1 ' ' '_'")
    print("[EXAMPLE]: python3 CharReplace.py <input_dir> 2 '.)[(])/ ' '_'\n")
    exit()
else:
    # get user variables
    directory = sys.argv[1]
    char_to_replace = int(sys.argv[2])
    replace_what = sys.argv[3]
    replace_with = sys.argv[4]



# get absolute path to directory
pathabs = os.path.abspath(directory)



# single of multiple char to replace
if char_to_replace == 1:
    replace_what_list = replace_what
elif char_to_replace > 1:
    replace_what_list = list(replace_what)

#

print("." * 50)
print("Replacing \"" + str(replace_what_list) + "\" with \"" + str(replace_with) + \
    "\" from files/directories in path  \n\t=> " + str(pathabs))
print("." * 50)


#replace and rename files
for whatword in os.listdir(pathabs):
    if char_to_replace == 1:
        withword = whatword.replace(replace_what_list, replace_with)
        if (withword != whatword):
            try:
                os.rename(whatword,withword)
            except:
                pass
    elif char_to_replace > 1:
        for char in replace_what_list:
            withword = whatword.replace(char, replace_with)
            if (withword != whatword):
                try:
                    os.rename(whatword,withword)
                except:
                    pass

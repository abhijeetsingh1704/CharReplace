#!/usr/bin/env python3

# Script:       CharReplace.py
# date:         Fri May 21 15:05:50 CEST 2021
# modified by:  Abhjeet Singh

# imports
import os
import sys

# help menu
if sys.argv[1] == str('-h'):
    print("\nCharReplace:\t - a multipurpose program to replace special characters in file/directories names or rename files/directories")
    print("Version:\t - 1.0.2")
    print("Author:\t\t - Abhijeet Singh, abhijeetsingh.aau@gmail.com\n")
    print("\n[EXAMPLE]: python3 CharReplace.py <directory/input_dir> <Char_to_replace, 1= one, 2= many> <what_to_replace> <replace_with>")
    print("\n[EXAMPLE]: python3 CharReplace.py <input_dir> 1 ' ' '_'")
    print("[EXAMPLE]: python3 CharReplace.py <input_dir> 2 '.)[(])/ ' '_'\n")
    print("Changing file extensions")
    print("\n[EXAMPLE]: python3 CharReplace.py <input_dir> 1 '.fa' '.fasta'\n")
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
                os.rename(os.path.join(pathabs , whatword), os.path.join(pathabs , withword))
            except (RuntimeError, TypeError, NameError):
                pass
    elif char_to_replace > 1:
        for char in replace_what_list:
            withword = whatword.replace(char, replace_with)
            if (withword != whatword):
                try:
                    os.rename(os.path.join(pathabs , whatword), os.path.join(pathabs , withword))
                except (RuntimeError, TypeError, NameError):
                    pass
# End of script

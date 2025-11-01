# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    line_count = 1
    names_file = open('names.txt', 'r')
    line = names_file.readline()
    for line in names_file:
        line_count += 1
    print(f'There are {line_count} names in the names file.')
    ######################
    # print('In the count_file_lines function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()

#This program was written by Logan Gibson on 10/30/25
#Its name is "Line Counter"
# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    ######################
    while True:
        try:
            infile = open('numbers.txt', 'r')
            sum = 0
            line = infile.readline()
            for line in infile:
                sum += float(line)
            print(f'The sum of numbers from the file is {sum}')
            infile.close()
            break

        except IOError or FileNotFoundError:
            print("""There was trouble accessing the file.
            Please make sure that numbers.txt is accessible.""")
            try_again = str(input("Type '1' if you want to try again. Type anything else to quit:"))
            if try_again == '1':
                pass
            else:
                break


        except ValueError:
            print("""A value error occurred. 
            Please make sure that numbers.txt only contains numbers.""")
            try_again = str(input("Type '1' if you want to try again. Type anything else to quit:"))
            if try_again == '1':
                pass
            else:
                break


    ######################
# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()

#This program was written by Logan Gibson on 10/31/25
#Its name is "Mean Calculator"
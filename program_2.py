# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

def main():
    random_n_count = amount_of_random()
    random_number_generator(random_n_count)
    print(f'You have written {random_n_count} random numbers to numbers.txt')
def amount_of_random():
    while True:
        try:
            random_count = int(input('How many random numbers do you want to generate (1-1000)?'))
            if random_count > 1000:
                random_count = 1000
            break
        except ValueError:
            print('Please enter a positive whole number.')
    return random_count

def random_number_generator(random_count):
    import random
    number_file = open('random_numbers.txt','w')
    while random_count > 0:
        random_n = random.randint(1,500)
        number_file.write(str(random_n) + '\n')
        random_count -= 1
    number_file.close()
if __name__ == '__main__':
    main()

#This program was written by Logan Gibson on 10/31/25
#Its name is "Line Counter"
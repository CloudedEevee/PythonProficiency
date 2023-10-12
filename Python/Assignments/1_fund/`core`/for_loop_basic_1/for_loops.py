############ nums appended to list for easier testing of large numbers in terminal
# separator variable to print between functions - better terminal readability
separate = "*************************"

############ PLEASE SET END_NUM TO LAST NUM YOU WANT ITERATED. FUNCTIONS ACCOUNT FOR "IN RANGE" NEEDING +1 TO END NUM!!
#####EXAMPLE: if you want every num from 1 - 10, end_num = 10




# Print all integers from 0 to 150
def print_num_in_range(end_num):
    num_list = []
    for num in range(end_num + 1):
        num_list.append(num)
    print(num_list)

print_num_in_range(150)
##################################################################
print(separate)



# Print all the multiples of 5 from 5 to 1,000
def print_every_5(end_num):
    num_list = []
    for num in range(0, (end_num + 1), 5):
        num_list.append(num)
    print(num_list)

print_every_5(1000)
##################################################################
print(separate)



# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def dojo_counting(end_num):
    num_list = []
    for num in range(1, (end_num + 1)):
        if num % 10 == 0:
            num_list.append("Coding Dojo")
        elif num % 5 == 0:
            num_list.append("Coding")
        else:
            num_list.append(num)
    print(num_list)

dojo_counting(100)
##################################################################
print(separate)



# Add odd integers from 0 to 500,000, and print the final sum.
def sum_of_odd(end_num):
    sum_num = 0
    for num in range(end_num + 1):
        if num % 2 != 0:
            sum_num += num
    print(sum_num)

sum_of_odd(500000)
##################################################################
print(separate)



# Print positive numbers starting at 2018, counting down by fours.
def count_down_by_four(start_num):
    num_list = []
    for num in range(start_num, 0, -4):
        num_list.append(num)
    print(num_list)

count_down_by_four(2018)
##################################################################
print(separate)



# Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
    # For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def print_my_multiples(low_num, high_num, mult):
    for num in range (low_num, (high_num + 1)):
        if num % mult == 0:
            print(num)

print_my_multiples(4, 200000, 17)
print(":3")

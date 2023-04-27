n = int(input())
number_list = input() #inputs a string of numbers
number_list = number_list.split() #separating the string into a list

#convert each item of the list into int type
for i in range(len(number_list)):
    number_list[i] = int(number_list[i])

list_sum = sum(number_list)
total_sum = n*(n+1)/2

missing_number = int(total_sum - list_sum)

print(missing_number)


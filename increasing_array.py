# 04/26/2023
# Nandini Prasad
# CSES - Increasing Array solution

input_list_size = int(input()) 
input_list = list(map(int,input().split()))

moves = 0

max_number = input_list[0]

for number in input_list:
    if (number < max_number):
        moves += max_number - number
    max_number = max(max_number,number)
        
print(moves)

# To actually modify the list
# for i, number in enumerate(input_list):
#     if (number < max_number):
#         moves += max_number - number
#         input_list[i] = max_number

# Doesn't work for edge cases
# for i in range(len(input_list)-1):
#     if input_list[i+1] < input_list[i]:
#         moves += input_list[i] - input_list[i+1]
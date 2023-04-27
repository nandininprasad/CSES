input_string = input()
input_list = list(map(str, input_string))

repetition_length = 1
longest_repetition = 1

for i in range(len(input_list)-1):
    if (input_list[i]==input_list[i+1]):
        repetition_length += 1
        longest_repetition = max (longest_repetition,repetition_length)
    else:
        repetition_length = 1

print(longest_repetition)

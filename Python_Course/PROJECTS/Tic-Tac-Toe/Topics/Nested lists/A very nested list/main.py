str_1 = input()
str_2 = input()
str_3 = input()

very_nested_list = []
very_nested_list.append(str_1)
very_nested_list.append([str_2])
very_nested_list.append([[str_3]])
print(very_nested_list)
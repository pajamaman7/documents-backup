my_list = [6,3,5,2.1,'haha',2,4]
out_list = []
for i in range(0,len(my_list)):
    if not (type(my_list[i]) == int and my_list[i] % 2 == 0):
        out_list.append(my_list[i])

print(out_list)


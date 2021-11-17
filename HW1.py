list = [7,8,9,2,3,1,4,10,5,6]
print(sorted(list))
print(sorted(list, reverse=True))
print(sorted(list)[::-1]) # sau o alta varianta ar fi aceasta
print(list[::2])
print(list[1::2])

multiples_of_3 = []
for i in list:
    if i%3==0:
        multiples_of_3.append(i) 
print(multiples_of_3)


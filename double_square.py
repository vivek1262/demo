# a =[]
# # for i in range(1,6): # in normal order
# for i in range(6,0,-1):    # in reverse order
#     a.append(i**2)
# print(a)

# *******************************************************

data = [1,3,4,1,2,4]
new_data = set()
for i in data:
    new_data.add(i)
    print(new_data)
    total=0
for i in new_data:
    total += i
    print(total)
c = 'abcdefghijklmnopqrstuvwxyz0123456789'
# c = 'abcde'

# print(c[2])
# print(len(c))

a = []

for i in range(len(c)):
    for j in range(len(c)):
        for k in range(len(c)):
            for l in range(len(c)):
                # print(c[i] + c[j] + c[k] + c[l])
                a.append(c[i] + c[j] + c[k] + c[l])

# print(a)
# aad7

print(f"amount:{len(a)}")

with open('array.txt', 'w') as file:
    file.write(str(a))
    # Write each element of the array to the file
    # for element in a:
        # file.write(f"{element}\n")  # Each element is written in a new line



f = open("array.txt", "r")
# print(f.read())
# print(type(f.read()))
l = f.read()[1:-1]
l = l.replace("'","")
l = l.split(", ")
print(l)
print(l[6])
print(type(l))
# print(f"amount:{len(a)}")
t=l.copy()
print(l[0])
print(len(l))
print(len(t))
print(l.pop(0))
print(l[0])
print(len(l))
print(len(t))
print(f"amount:{len(l)}")
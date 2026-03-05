for p in "Python is the one of the nice programing language":
    print(p)

for h in range(10):
    print(h)
else:
    print("The else keyword in a for loop specifies a block of code to be executed when the loop is finished:")


#If the loop breaks, the else block is not executed.
for x in range(6):
    if x == 3: 
        break
    print(x)
else:
    print("Finally finished!")



name = "Muzamil"

for i in name:
    print(i)
    if i == "m":
        print("This M letter comes two times in your name.")

# range 
for j in range(30 , 40):
    print(j)

print("---------------------------------------------")

for k in range(10 , 40, 4):
    print(k)


fruits = ["watermelon", "orange", "apple", "banana", "cherry", "strawberry"]
for n in fruits:
    print(n)
    if n == "banana":     # if x == "banana":
        break               # continue
#   print(n)            #  print(n)



t = 1
while t < 10:
    print(t)
    t += 2

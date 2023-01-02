x="Abebe"
print("\n",x[-2])
print(x[-4:-2])
print(x[::-1]) #for reversing the word
y="hello, world"
print(y.split( ',')) #for spliting based on ','
n=50
print(bin(n)) #explicite casting
print(hex(n))
# logical opraters for and , or,not use 'and','or','not'
for x in range(2,100):
  if(x%3==0 and x%5==0):
    print("Hello World")
  elif(x%5==0):
    print("World")
  elif(x%3==0):
    print("Hello")
  else:
    print(x)
# print square and rectangle using '*'
print("\nSquare using '*'")
for i in range(1,6):
  for j in range(1,6):
    print("*", end="")
  print()
print("Rectangle using '*'")
for m in range(1,6):
  for y in range(1,10):
    print("*", end="")
  print()

# python3
print("hello", "world")

x = 'blue'
y = 'green'
z = x

print(x, y, z)

z = y
print(x, y, z)

x = z
print(x, y, z)

route = 86
print(route, type(route))

route = 'hello world'
print(route, type(route))

t1 = [1, 2, 3]
print(t1)

t1.append(4)
print(t1)

t2 = (1, 2)
print(t2)

t3 = 'a1e4141434414nyhrtjmuyr,muyl,iuyluiliul;iuy;oui;111a1e4141434414nyhrtjmuyr,muyl,iuyluiliul;iuy;oui;111'
t4 = 'a1e4141434414nyhrtjmuyr,muyl,iuyluiliul;iuy;oui;111a1e4141434414nyhrtjmuyr,muyl,iuyluiliul;iuy;oui;111'
print(t3 is t4)

t5 = 'aa'
print(t5 is not None)
t6 = None
print(t6 is None)

print(t5 is t6, t5 is not t6)

a = 'many money' + '1'
b = 'many money' + '1'
print(a is b, a == b)

five = 5
two = 2
nought = 0
print(five and two)
print(two and five)
print(two or five)
print(nought or five)
print(nought and five)
print(five and nought)

print(not two)
print(not nought)

# 判断条件
if 1:
    print("1 is ", True)
else:
    print("1 is ", False)

if 0:
    print("0 is ", True)
else:
    print("0 is ", False)

if -1:
    print("-1 is ", True)
else:
    print("-1 is ", False)

if "":
    print(" is ", True)
else:
    print(" is ", False)

# for in
for country in ["Denmark", "Finland", "Norway", "Sweden"]:
    print(country)

for letter in "ABCDEFGHIJKLMNOPQ":
    if letter in "AEIOU":
        print(letter, " is a vowel")
    else:
        print(letter, " is a consonant")

# exception
s = input("enter an integer:")
try:
    i = int(s)
    print("valid integer entered:", i)
except ValueError as err:
    print(err)

# +=
a = []
a += "adsada"
print(a)

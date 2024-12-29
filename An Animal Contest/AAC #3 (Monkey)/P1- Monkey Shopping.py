# Kishan Suhi
# Animal Contest 3
# P1 | Monkey Shopping

check = input().split()
a = int(check[0])
b = int(check[1])
c = int(check[2])
d = int(check[3])

grocery = False
pharmacy = False

department = False

if a < b:
    grocery = True

if c < d:
    pharmacy = True

if grocery and pharmacy:
    department = True
    grocery = False
    pharmacy = False

if department:
    print("Go to the department store")
elif grocery:
    print("Go to the grocery store")
elif pharmacy:
    print("Go to the pharmacy")
else:
    print("Stay home")
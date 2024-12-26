# Kishan Suhi
# Animal Contest 1
# P1 | Alpaca Shapes

enter = input("").split()

sarea = int(enter[0])
scircle = int(enter[1])

squarearea = sarea**2
circlearea = (scircle**2)*3.14
circlerea = round(circlearea,2)

if squarearea < circlearea:
    print("CIRCLE")
elif squarearea > circlearea:
    print("SQUARE")

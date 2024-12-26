# Kishan Suhi
# Bluebook 
# Cost

num_test_cases = int(input(""))

for _ in range(num_test_cases):
    weight = int(input(""))
    if weight <= 30:
        print(38)
    elif weight <= 50:
        print(55)
    elif weight <= 100:
        print(73)
    else:
        additional_cost = ((weight - 100 + 49) // 50) * 24
        print(73 + additional_cost)
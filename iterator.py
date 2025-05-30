l = [1,2,3,4,5]

print("----- For loop example -----")

for i in l:
    print(i)

print("----- Iterator example -----")

iterator = iter(l)

print(iterator)

l0 = next(iterator)
l1 = next(iterator)
l2 = next(iterator)
l3 = next(iterator) 
l4 = next(iterator)
# l5 = next(iterator)

print(f"First: {l0}, second: {l1}, third: {l2}, fourth: {l3}, fifth: {l4}")
set = {11, 13}
print("The set:",set)
set.update([14, 15], {10, 16, 18})
print("After modifying elements:",set)
set.discard(18)
print("After deletion:",set)
set.add(18)
print("After addition of elements:",set)
print("Is element 18 present:", 18 in set)
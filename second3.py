set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

resulti = set1.intersection(set2)
resultsd = set1.symmetric_difference(set2)
if set1 == set2:
    print("Sets are equal")
else:
    print("Sets are not equal")
max1 = max(set1)
min2 = min(set2)
print(resulti)
print(resultsd)
print(max1)
print(min2)

def max_score(beers, fries):
    beers.sort()
    fries.sort()
    res = [beers[i]*fries[i] for i in range(len(beers))]
    
    return sum(res) + 1

print(max_score([10, 11], [1, 5]))
print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))

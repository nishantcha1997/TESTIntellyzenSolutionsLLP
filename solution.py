
def minimumCost(cost, persons):
    
    cost = sorted(cost)
    totalCost = 0

    for i in range(persons - 1, 1, -2):
        if i == 2:
            totalCost += cost[2] + cost[0]
        else:
            
            price_first = cost[i] + cost[0] + 2 * cost[1]
            price_second = cost[i] + cost[i - 1] + 2 * cost[0]
            totalCost += min(price_first, price_second)

    
    if persons == 1:
        totalCost += cost[0]
    else:
        totalCost += cost[1]

    return totalCost

test_cases = int(input())
for test_case in range(test_cases):
    persons = int(input())
    cost = list(int(num) for num in input(" ").strip().split())[:persons]
    print(minimumCost(cost, persons))

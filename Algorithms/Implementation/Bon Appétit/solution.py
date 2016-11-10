n, k = [int(temp) for temp in input().split(' ')]
costs = [int(temp) for temp in input().split(' ')]
anna_paid = int(input())
assert(len(costs) == n)

diff = anna_paid - int((sum(costs) - costs[k]) / 2)
assert(diff >= 0)

if diff == 0:
    print("Bon Appetit")
else:
    print(diff)


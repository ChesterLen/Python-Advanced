from collections import deque

bowls_of_ramen = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while True:
    if not bowls_of_ramen or not customers:
        break
    ramen = bowls_of_ramen.pop()
    customer = customers.popleft()

    if ramen == customer:
        continue
    elif ramen > customer:
        ramen -= customer
        bowls_of_ramen.append(ramen)
    elif customer > ramen:
        customer -= ramen
        customers.appendleft((customer))

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")
if not bowls_of_ramen and customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
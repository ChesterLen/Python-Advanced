from collections import deque

pizzas_orders = deque([int(x) for x in input().split(", ")])
employees = deque([int(x) for x in input().split(", ")])

total_pizza_made = 0

while pizzas_orders and employees:
    pizza_order = pizzas_orders.popleft()
    employee_capacity = employees.pop()
    if pizza_order <= 0:
        employees.append(employee_capacity)
        continue
    elif pizza_order > 10:
        employees.append(employee_capacity)
        continue

    if pizza_order <= employee_capacity:
        total_pizza_made += pizza_order
    elif pizza_order > employee_capacity:
        total_pizza_made += pizza_order - employee_capacity
        pizzas_orders.appendleft(pizza_order - employee_capacity)

if not pizzas_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_made}")
    if employees:
        print(f"Employees: {', '.join(str(x) for x in employees)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizzas_orders)}")
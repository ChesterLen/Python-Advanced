from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
total_bullet_price = 0
reloading = gun_barrel_size
total_money_earned = intelligence_value

while bullets and locks:
    shoot = bullets.pop()
    shoot_lock = locks.popleft()

    if shoot <= shoot_lock:
        reloading -= 1
        total_bullet_price += bullet_price
        print("Bang!")
    else:
        reloading -= 1
        total_bullet_price += bullet_price
        print("Ping!")
        locks.appendleft(shoot_lock)

    if not reloading:
        if bullets:
            reloading = gun_barrel_size
            print("Reloading!")

total_money_earned -= total_bullet_price

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${total_money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

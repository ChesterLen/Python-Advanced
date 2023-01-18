n, m = [int(x) for x in input().split()]
n_items_set = {input() for _ in range(n)}
m_items_set = {input() for _ in range(m)}

print(*n_items_set.intersection(m_items_set), sep="\n")

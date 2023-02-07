from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
papers = deque([int(x) for x in input().split(", ")])

box_size = 50
filled_boxes = 0

for _ in range(len(eggs)):
    if not papers or not eggs:
        break

    egg = eggs.popleft()
    paper = papers.pop()

    if egg <= 0:
        papers.append(paper)
        continue
    if egg == 13:
        papers.append(papers.popleft())
        papers.appendleft(paper)
        continue
    elif egg + paper <= box_size:
        filled_boxes += 1

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")
if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
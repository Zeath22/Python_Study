from collections import deque
# Last in Last out (LiLo)
# First in First out (FiFo)
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
# the reason we dont use pop(0) is it will take alot of memory if its a big list
# and it has adjust each index again
# But with deque that problem is solved
print(queue)

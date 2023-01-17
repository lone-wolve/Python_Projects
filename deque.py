import collections
import string

d = collections.deque(string.ascii_lowercase)

print( "item count" , str(len(d)))

# for elem in d:

#     print(elem.upper(), end=',')

d.pop()
d.popleft()
d.append(2)
d.appendleft(1)
print(d)
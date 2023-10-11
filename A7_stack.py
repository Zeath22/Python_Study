# last in First Out (LiFo)
browsing_history = []
browsing_history.append(1)
browsing_history.append(2)
browsing_history.append(3)

print(browsing_history)
print(browsing_history.pop())
print(browsing_history)

# as in our browser tabs, when we go back, we are redirected where we were
if browsing_history:
    print("redirected to ", browsing_history[-1])

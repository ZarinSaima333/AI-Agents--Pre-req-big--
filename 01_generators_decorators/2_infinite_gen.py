def inifinite_happiness():
    count = 1
    while True:
        yield f'Refil #{count}'
        count +=1

refill = inifinite_happiness()
user2=inifinite_happiness()

for _ in range(3):
    print(next(refill))

for _ in range(5):
    print(next(user2))

#running 2 for loops refill
# Refil #1
# Refil #2
# Refil #3
# Refil #4
# Refil #5
# Refil #6
# Refil #7
# Refil #8

#running 1 for loops refill and one for user2
# Refil #1
# Refil #2
# Refil #3
# Refil #1
# Refil #2
# Refil #3
# Refil #4
# Refil #5
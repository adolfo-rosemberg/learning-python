import time

start_time = time.time()

# outer loop
for i in range(10):
    # inner loop
    for j in range(10):
        if (j == 9):
            print(j, end="")
        else:
            print(j, end=" - ")
    print()

print(round((time.time() - start_time), 2))

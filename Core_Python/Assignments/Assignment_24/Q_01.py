# Write A Program Calculate the sum of squares of numbers from 1 to 100 using four threads. Divide the range equally among the threads, and each thread calculates the sum of squares for its range. Finally, combine the results to get the total sum of squares.
from threading import Thread

results = [0, 0, 0, 0]

def ran1():
    s = 0
    for i in range(1, 26):
        s += i * i
    results[0] = s

def ran2():
    s = 0
    for i in range(26, 51):
        s += i * i
    results[1] = s

def ran3():
    s = 0
    for i in range(51, 76):
        s += i * i
    results[2] = s

def ran4():
    s = 0
    for i in range(76, 101):
        s += i * i
    results[3] = s

if __name__ == "__main__":
    t1 = Thread(target=ran1)
    t2 = Thread(target=ran2)
    t3 = Thread(target=ran3)
    t4 = Thread(target=ran4)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    total_sum = sum(results)
    print("Sum of squares from 1 to 100:", total_sum)

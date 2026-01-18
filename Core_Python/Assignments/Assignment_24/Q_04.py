# Write A Program Implement a producer-consumer problem with a limited buffer of size 5. Create two producer threads and two consumer threads. Producers produce items, and consumers consume them. Ensure proper synchronization to avoid buffer overflows underflows.

from threading import Thread, Condition
import time
import random

BUFFER_SIZE = 5
buffer = []

cond = Condition()

def producer(pid):
    global buffer
    for i in range(5):
        item = f"P{pid}-Item{i}"
        with cond:
            while len(buffer) == BUFFER_SIZE:
                cond.wait()   # wait if buffer is full

            buffer.append(item)
            print(f"Producer {pid} produced {item} | Buffer: {buffer}")
            cond.notify_all()   # notify consumers

        time.sleep(random.uniform(0.5, 1.5))

def consumer(cid):
    global buffer
    for i in range(5):
        with cond:
            while len(buffer) == 0:
                cond.wait()   # wait if buffer is empty

            item = buffer.pop(0)
            print(f"Consumer {cid} consumed {item} | Buffer: {buffer}")
            cond.notify_all()   # notify producers

        time.sleep(random.uniform(0.5, 1.5))

if __name__ == "__main__":
    p1 = Thread(target=producer, args=(1,))
    p2 = Thread(target=producer, args=(2,))
    c1 = Thread(target=consumer, args=(1,))
    c2 = Thread(target=consumer, args=(2,))

    p1.start()
    p2.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    c1.join()
    c2.join()

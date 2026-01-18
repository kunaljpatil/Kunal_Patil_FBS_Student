# Write A Program Create two threads, one printing even numbers and the other printing odd numbers from 1 to 10. Ensure proper synchronization to alternate between even and odd numbers.

from threading import Thread, Condition

cond = Condition()
current = 1

def even():
    global current
    with cond:
        while current<=10:
            if current % 2 == 0:
                print('EVEN:',current)
                print()
                current = current + 1
                cond.notify()
            else:
                cond.wait()
    
def odd():
    global current
    with cond:
        while current <= 10:
            if current % 2 == 1:
                print('ODD:',current)
                current = current + 1
                cond.notify()
            else:
                cond.wait()

if __name__ == '__main__':
    t1 = Thread(target=even)
    t2 = Thread(target=odd)
    
    t2.start()
    t1.start()
    
    t1.join()
    t2.join()
from queue import Queue
from threading import Thread


q1 = Queue()

q1.put(1)
q1.put(2)

print("Item 1 from queue:", q1.get())
print("Item 2 from queue:", q1.get())
# The line below will block program execution, because there is no more elements left in the queue.
# print("Item 3 from queue:", q1.get())


numbers_queue = Queue()
pows_queue = Queue()


def numbers(start_num: int, end_num: int, num_q: Queue):
    while start_num <= end_num:
        print(f"T1: Put {start_num} to numbers queue")
        num_q.put(start_num)
        start_num += 1


def pow_numbers(num_q: Queue, pow_q: Queue):
    while True:
        number = num_q.get()
        if number % 2 == 0:
            print(f"T2: Put square of {number} to pows queue")
            pow_q.put(number**2)


def print_result(result_q: Queue):
    while True:
        print("Q: Result is", result_q.get())


t1 = Thread(target=numbers, args=(1, 10, numbers_queue))
t2 = Thread(target=pow_numbers, args=(numbers_queue, pows_queue))

t1.start()
t2.start()

print_result(pows_queue)
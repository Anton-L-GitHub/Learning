import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    start = time.time()
    user_input = input("Enter your name: ")
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask_user, {time.time() - start}")


def complex_calculation():
    start = time.time()
    print("Started calculating...")
    [x ** 2 for x in range(20_000_000)]
    print(f"complex_calculation, {time.time() - start}")


# ---------------- Without threads ----------------

start = time.time()
ask_user()
complex_calculation()
print(f"Single thread total time: {time.time() - start}")


# ---------------- With threads -----------------
start = time.time()

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

thread1.start()
thread2.start()


thread1.join()
thread2.join()

print(f'Two thread total time: {time.time() - start}')


# ---------------- Using context manager -----------------------

start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f'Two threads total time: {time.time() - start}')

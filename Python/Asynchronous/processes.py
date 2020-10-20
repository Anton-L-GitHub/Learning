import time
from concurrent.futures import ProcessPoolExecutor


def complex_calculation():
    start = time.time()
    print("Started calculating...")
    [x ** 2 for x in range(20_000_000)]
    print(f"complex_calculation, {time.time() - start}")



start = time.time()

# if name == main is a must to run in windows
if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)


print(f'Two process total time: {time.time()- start}')

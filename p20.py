# def calc_avg():
#     """流式计算平均值"""
#     total, counter = 0, 0
#     avg_value = None
#     while True:
#         value = yield avg_value
#         total, counter = total + value, counter + 1
#         avg_value = total / counter


# gen = calc_avg()
# next(gen)
# print(gen.send(10))
# print(gen.send(20))
# print(gen.send(30))


# from concurrent.futures import ThreadPoolExecutor
# from random import randint
# import threading
# from time import sleep


# class Counter():

#     def __init__(self) -> None:
#         self.count = 0
#         self.lock = threading.Lock()
#         self.condition = threading.Condition(self.lock)

#     def add(self, i):
#         with self.lock:
#             self.count += i
#             print(f"{threading.current_thread.__name__} : add {i}, 当前为{self.count}")
#             sleep(0.01)

#     def sub(self, i):
#         with self.lock:
#             if i > self.count:
#                 print(
#                     f"{threading.current_thread.__name__} : 要减{i}，当前为{self.count}，不够了，等待")
#                 self.condition.wait()
#             self.count -= i
#             print(f"{threading.current_thread.__name__} : sub {i}, 当前为{self.count}")
#             sleep(0.01)


# def main():
#     counter = Counter()
#     pool = ThreadPoolExecutor(10)
#     futures = []
#     for _ in range(10):
#         futures.append(pool.submit(counter.add, randint(5, 10)))
#     for _ in range(5):
#         futures.append(pool.submit(counter.sub, randint(10, 15)))
#     pool.shutdown()
#     # for future in futures:
#     #     future.result()


# from concurrent.futures import ProcessPoolExecutor


# def square(x):
#     return x * x


# def main():
#     numbers = [1, 2, 3, 4, 5]
#     with ProcessPoolExecutor(max_workers=5) as pool:
#         results = pool.map(square, numbers)
#     for number, result in zip(numbers, results):
#         print(number, result)


# if __name__ == '__main__':
#     main()


import asyncio
import re

import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    tasks = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.gather(*tasks))
    print("before close")
    loop.close()
    print("end")


if __name__ == '__main__':
    main()

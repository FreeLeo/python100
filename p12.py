from threading import Thread, Lock
from time import time, sleep


class Account(object):

    def __init__(self) -> None:
        self._balance = 0
        self._lock = Lock()

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        self._lock.acquire()
        new_balance = self._balance + money
        sleep(0.01)
        self._balance = new_balance
        self._lock.release()


def add(account, money):
    account.deposit(money)


def main():
    start = time()
    account = Account()
    threads = []
    for _ in range(100):
        thread = Thread(target=add, args=(account, 1))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end = time()
    print(account.balance,  end-start)


if __name__ == '__main__':
    main()

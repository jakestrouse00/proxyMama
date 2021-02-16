from multiprocessing import Lock
import random
import time


class Proxy:
    def __init__(self, proxy: dict, manager):
        self.proxy = proxy
        self.manager = manager

    def __str__(self):
        return f"<<address: {self.proxy['proxy']}, in_use: {self.proxy['in_use']}, timeout: {self.proxy['timeout_until']}>>"

    def address(self):
        return self.proxy['proxy']

    def release(self):
        proxyIndex = self.manager.temp_proxies.index(self.proxy['proxy'])
        self.manager.proxies[proxyIndex]['thread_lock'].acquire()
        self.proxy['in_use'] = False
        self.manager.proxies[proxyIndex] = self.proxy
        self.manager.proxies[proxyIndex]['thread_lock'].release()


class Manager:
    def __init__(self, set_timeout: bool = False, timeout: int = 0, single_use: bool = True):
        self.set_timeout = set_timeout
        self.timeout = timeout
        self.single_use = single_use
        # {"proxy": "111.111.111", "in_use": True/False, "thread_lock": Lock(), "timeout_until": 111111}
        self.proxies = []
        self.temp_proxies = []

    def load_file(self, file_path: str):
        with open(file_path, "r") as f:
            proxies = f.read().splitlines()
        self.temp_proxies = proxies
        for proxy in proxies:
            self.proxies.append({"proxy": str(proxy), "in_use": False, "thread_lock": Lock(), "timeout_until": 0})

    def random(self):
        proxy = random.choice(self.proxies)
        proxyIndex = self.proxies.index(proxy)
        proxy['thread_lock'].acquire()
        if self.single_use:
            if not proxy['in_use']:
                if self.set_timeout:
                    current_time = int(time.time())
                    if current_time >= proxy['timeout_until']:
                        proxy['in_use'] = True
                        if self.set_timeout:
                            proxy['timeout_until'] = int(time.time()) + self.timeout
                        self.proxies[proxyIndex] = proxy
                        proxy['thread_lock'].release()
                        return Proxy(proxy, self)
                else:

                    proxy['in_use'] = True
                    self.proxies[proxyIndex] = proxy
                    proxy['thread_lock'].release()
                    return Proxy(proxy, self)
        else:
            self.proxies[proxyIndex] = proxy
            proxy['thread_lock'].release()
            return Proxy(proxy, self)


x = Manager(set_timeout=True, timeout=10)
x.load_file("proxies.txt")
print(x.proxies)
print(x.temp_proxies)
j = x.random()
print(j)
print(x.proxies)
j.release()
print(x.proxies)

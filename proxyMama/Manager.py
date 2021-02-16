from multiprocessing import Lock
import time
import random
from .Proxy import Proxy


class Manager:
    def __init__(self, set_timeout: bool = False, timeout: int = 0, single_use: bool = False):
        self.set_timeout = set_timeout
        self.timeout = timeout
        self.single_use = single_use
        # {"proxy": "111.111.111", "in_use": True/False, "thread_lock": Lock(), "timeout_until": 111111}
        self.proxies = []
        # temp_proxies is used in the Proxy() obj to make sure updating proxies in the Manager is happening in the right index
        self.temp_proxies = []

    def load_file(self, file_path: str):
        """
        loads proxies into dict. Each proxy gets a multiprocessing.Lock() to make sure everything is multi-thread safe and data is overwritten.
        """
        with open(file_path, "r") as f:
            proxies = f.read().splitlines()
        self.temp_proxies = proxies
        for proxy in proxies:
            self.proxies.append({"proxy": str(proxy), "in_use": False, "thread_lock": Lock(), "timeout_until": 0})

    def random(self):
        """
        Chooses a random proxy from the proxy list. If the proxy can be used, the object Proxy() is returned. Otherwise None is returned.
        This is thread safe, because each proxy has a Lock() that must be free before any data a read/manipulated.

        :return: Proxy() object or None if no proxy can be found."""
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
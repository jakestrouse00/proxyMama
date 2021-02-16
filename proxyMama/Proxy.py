from multiprocessing import Lock
import time
import random

class Proxy:
    def __init__(self, proxy: dict, manager):
        self.proxy = proxy
        self.manager = manager

    def __repr__(self):
        return f"<address: {self.proxy['proxy']}, in_use: {self.proxy['in_use']}, timeout: {self.proxy['timeout_until']}>"

    def address(self):
        # returns the proxy ip
        return self.proxy['proxy']

    def release(self):
        """
        Releases a proxy after it has been used. This should only be used if the Manager() has 'single_use' set to True.
        It is unclear if this will work for multiprocessing, but it should work for multithreading
        """
        proxyIndex = self.manager.temp_proxies.index(self.proxy['proxy'])
        self.manager.proxies[proxyIndex]['thread_lock'].acquire()
        self.proxy['in_use'] = False
        self.manager.proxies[proxyIndex] = self.proxy
        self.manager.proxies[proxyIndex]['thread_lock'].release()
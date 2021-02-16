import proxyMama

manager = proxyMama.Manager()
manager.load_file("proxies.txt")
proxy = manager.random()
print(proxy)
proxyIP = proxy.release()
print(proxyIP)
import proxyMama

x = proxyMama.Manager(set_timeout=True, timeout=10)
x.load_file("proxies.txt")
print(x.proxies)
print(x.temp_proxies)
j = x.random()
print(j)
print(x.proxies)
j.release()
print(x.proxies)
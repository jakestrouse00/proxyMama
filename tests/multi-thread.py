import proxyMama
import threading
import time


def use_proxy(manager):
    proxy = manager.random(blocking=True)
    print(f"using proxy: {proxy.address()}")
    time.sleep(2)
    print(f"releasing proxy")
    proxy.release()


manager = proxyMama.Manager(single_use=True)
manager.load_file("proxies.txt")
for i in range(6):
    threading.Thread(target=use_proxy, args=(manager,)).start()

print(manager.proxies)

import proxyMama
import threading
import time


def use_proxy(manager):
    # will block until a new proxy is ready
    proxy = manager.random(blocking=True)
    print(f"using proxy: {proxy.address()}\n")
    time.sleep(2)

    proxy.release()
    print(f"released proxy\n")


manager = proxyMama.Manager(single_use=True)
manager.load_file("proxies.txt")
# giving an example of what happens if all proxies are in use and blocking = True.
for i in range(8):
    threading.Thread(target=use_proxy, args=(manager,)).start()

# showing that proxies are now in use
print(manager.proxies)


# proxyMama
A simple proxy manager for your web scraping journey


### Features
- Multi-thread safe
- Easy to use
- No external packages
- Highly customizable

### Installation
#### With pip
`pip install proxyMama`

## Examples

#### Single-thread
```python
import proxyMama

manager = proxyMama.Manager()
manager.load_file("proxies.txt")
proxy = manager.random()
print(proxy)
# get the actual ip
proxyIP = proxy.address()
print(proxyIP)
# proxy.release() is only necessary if proxyMama.Manager.single_use is set to True 
proxy.release()
```

#### Multi-thread

```python
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
```
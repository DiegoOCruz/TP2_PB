import asyncio
import aiohttp
import time
import matplotlib.pyplot as plt

urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
        "https://jsonplaceholder.typicode.com/posts/4",
        "https://jsonplaceholder.typicode.com/posts/5",
        "https://jsonplaceholder.typicode.com/posts/6",
        "https://jsonplaceholder.typicode.com/posts/7",
        "https://jsonplaceholder.typicode.com/posts/8",
        "https://jsonplaceholder.typicode.com/posts/9",
        "https://jsonplaceholder.typicode.com/posts/10"
        * 10
    ] 

async def download_url(session, url):
    async with session.get(url) as response:
        content = await response.text()
        #print(f"Downloaded {url}: {len(content)} bytes")

async def main(concurrency):
    async def sem_download_url(url):
            async with aiohttp.ClientSession() as session:
                await download_url(session, url)

    await asyncio.gather(*(sem_download_url(url) for url in urls))

if __name__ == "__main__":
    threads = [1, 2, 4, 8, 16, 32, 64, 128]
    times = []
    for thread in threads:
        print(f"Testando com thread: {thread}")
        start_time = time.perf_counter()
        asyncio.run(main(thread))
        end_time = time.perf_counter()
        times.append(end_time - start_time)
        print(f"Tempo total: {end_time - start_time:.2f} segundos\n")

plt.plot(threads, times, marker="o")
plt.title("Número de Threads vs Tempo de Download")
plt.xlabel("Número de Threads")
plt.ylabel("Tempo (s)")
plt.grid()
plt.show()

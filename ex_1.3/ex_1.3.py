import asyncio
import os
import time
from PIL import Image, ImageFilter
import concurrent.futures
import matplotlib.pyplot as plt


def process_image(image_path, output_path):
    with Image.open(image_path) as img:
        img = img.filter(ImageFilter.BLUR)
        img.save(output_path)


async def process_images_async(input_dir, output_dir, max_workers):
    tasks = []
    

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        loop = asyncio.get_event_loop()
        
        for filename in os.listdir(input_dir):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            task = loop.run_in_executor(executor, process_image, input_path, output_path)
            tasks.append(task)
        
        await asyncio.gather(*tasks)

def count_time(input_dir, output_dir, max_workers):
    start_time = time.time()
    asyncio.run(process_images_async(input_dir, output_dir, max_workers))
    end_time = time.time()
    return end_time - start_time


def plot_performance(input_dir, output_dir, thread_list):
    times = []
    
    for thread in thread_list:
        time_taken = count_time(input_dir, output_dir, thread)
        times.append(time_taken)
        print(f"Threads: {thread}, Tempo: {time_taken:.2f} segundos")
    

    plt.plot(thread_list, times, marker='o')
    plt.xlabel('Número de Threads')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Desempenho do Processamento Assíncrono de Imagens')
    plt.grid(True)
    plt.show()


#threads
threads = [1, 2, 4, 8, 16]


plot_performance('imagens', 'imagens_', threads)

import os
import psutil
import sys
import time
import multiprocessing
import GPUtil
import pyamdgpuinfo
from tabulate import tabulate

#pip install setuptools, if no module named 'distutils'

def main():
    print("Welcome to EasyBench! Choose one of these tools:\n")
    print("1. RAM benchmark")
    print("2. CPU benchmark")
    print("3. GPU benchmark (beta)")
    print("4. Help")
    print("5. Exit\n")
    tool_choice = input("Input number of tool: ")

    if tool_choice == '1':
        mb = int(input("How many MB of RAM we have to fill?: "))
        safe = int(input("Safe mode ON (1) or OFF (0) ?: "))
        refresh_time = float(input("Refresh time in seconds ('0' to live refresh)?: "))
        allocate_memory(mb, safe, refresh_time)

    if tool_choice == '2':
        percentage = int(input("Enter CPU usage percentage (0-100): "))
        duration = int(input("Enter duration in seconds: "))
        refresh_time = float(input("Refresh time in seconds ('0' to live refresh)?: "))
        stress_cpu(percentage, duration)

    if tool_choice == '3':
        refresh_time = float(input("Refresh time in seconds ('0' to live refresh)?: "))
        print_gpu_usage(refresh_time)

    if tool_choice == '4':
        print("Q: How to exit from app if during the benchmark something went wrong?")
        print("A: To exit from app click Ctrl + C on Linux, or Alt + F4 on Windows. Very soon we will add a hotkey to close this app.")

    if tool_choice == '5':
        os._exit(1)

def clearScr():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')

def print_gpu_usage(refresh_time):
    pyamdgpuinfo.detect_gpus()
    gpus = GPUtil.getGPUs()
    gpu_list = []

    i = 1

    while i == 1:
        clearScr()
        for gpu in gpus:
            gpu_list.append((
                gpu.id,
                gpu.name,
                f"{gpu.load * 100:.0f}%",
                f"{gpu.memoryUtil * 100:.0f}%",
                f"{gpu.temperature}°C",
                f"{gpu.memoryFree / 1024**2:.0f} MB",
                f"{gpu.memoryUsed / 1024**2:.0f} MB",
                f"{gpu.memoryTotal / 1024**2:.0f} MB",
            ))

        for i in range(pyamdgpuinfo.detect_gpus()):
            gpu_list.append((
                i,
                pyamdgpuinfo.get_gpu_name(i),
                f"{pyamdgpuinfo.get_gpu_usage(i)}%",
                f"{pyamdgpuinfo.get_vram_usage(i)}%",
                f"{pyamdgpuinfo.get_gpu_temperature(i)}°C",
                f"{pyamdgpuinfo.get_vram_free(i) / 1024**2:.0f} MB",
                f"{pyamdgpuinfo.get_vram_used(i) / 1024**2:.0f} MB",
                f"{pyamdgpuinfo.get_vram_size(i) / 1024**2:.0f} MB",
            ))

        print(tabulate(gpu_list, headers=("ID", "Name", "Load", "Memory Util", "Temperature", "Free Memory", "Used Memory", "Total Memory")))

        time.sleep(refresh_time)

def allocate_memory(mb, safe, refresh_time):
    memory_hog = bytearray(mb * 1024 * 1024)

    i = 1

    while i == 1:
        total, available, used, free, percent = ram_info()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Allocated {mb} MB of RAM")
        print(f"Total RAM: {total / (1024 * 1024):.2f} MB")
        print(f"Available RAM: {available / (1024 * 1024):.2f} MB")
        print(f"Used RAM: {used / (1024 * 1024):.2f} MB")
        print(f"Free RAM: {free / (1024 * 1024):.2f} MB")
        print(f"Percentage of RAM used: {percent}%")
        safe_mode(safe, percent)
        refresh_time
        time.sleep(refresh_time)


    return memory_hog

def safe_mode(safe, percent):
    if safe == 1:
        print("Safe mode status: ON")
        if percent >= 90.0:
            print("Usage of RAM is more than 90%, emergency shutdown!")
            os._exit(1)
    else:
        print("! Safe mode status: OFF !")

def ram_info():
    ram = psutil.virtual_memory()

    total_ram = ram.total
    available_ram = ram.available
    used_ram = ram.used
    free_ram = ram.free
    percent_used = ram.percent

    return total_ram, available_ram, used_ram, free_ram, percent_used

def cpu_stress(percentage):
    while True:
        start_time = time.time()
        while (time.time() - start_time) < (percentage / 100.0):
            pass
        time.sleep((100 - percentage) / 100.0)

def monitor_cpu():
    while True:
        usage = psutil.cpu_percent(interval=1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Current CPU usage: {usage}%")
        if os.name == 'posix':  # Linux/Unix
            try:
                temp_output = os.popen("sensors").read()
                print(f"Full sensors output:\n{temp_output}")
                temp = None
                for line in temp_output.split('\n'):
                    if 'Tdie' in line or 'Package id 0:' in line:
                        temp = line.split()[-2].strip('+°C')
                        break
                if temp:
                    temp = float(temp)
                    print(f"CPU Temperature: {temp}°C")
                    if temp >= 90:
                        print("High temperature!")
            except Exception as e:
                print("Failed to get temperature: ", e)
        time.sleep(1)

def stress_cpu(percentage, duration):
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=cpu_stress, args=(percentage,))
        processes.append(p)
        p.start()

    monitor = multiprocessing.Process(target=monitor_cpu)
    monitor.start()

    time.sleep(duration)

    for p in processes:
        p.terminate()
        p.join()  # Ensure the process has finished

    monitor.terminate()
    monitor.join()

if __name__ == "__main__":
    main()

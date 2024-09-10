import os
import psutil
import sys
import time

def allocate_memory(mb, safe, refresh_time):
    # Convert MB to bytes
    bytes_to_allocate = mb * 1024 * 1024
    # Create a large list to consume memory
    memory_hog = bytearray(bytes_to_allocate)

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

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python allocate_memory.py <amount_in_MB> <1/0> <refresh_time_in_seconds>")
        sys.exit(1)

    try:
        mb = int(sys.argv[1])
        safe = int(sys.argv[2])
        refresh_time = int(sys.argv[3])
        allocate_memory(mb, safe, refresh_time)
    except ValueError:
        print("Please enter a valid integer for the amount of RAM to allocate.")


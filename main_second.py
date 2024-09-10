import os
import psutil

def reserve_memory(size_in_gb):
    size_in_bytes = size_in_gb * 1024 * 1024 * 1024
   
    reserved_memory = bytearray(size_in_bytes)
    return reserved_memory

def main():
    # Reserve 3 GB of RAM, change '1' to any value in GB which you need
    reserved_memory = reserve_memory(1)
    print(f"Reserved RAM. Current usage: {psutil.virtual_memory().used / (1024 * 1024 * 1024):.2f} GB")

    # Keep the program running to hold the memory, very important part of code!
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Releasing reserved memory.")
        del reserved_memory

if __name__ == "__main__":
    main()


import sys

def allocate_memory(mb):
    # Convert MB to bytes
    bytes_to_allocate = mb * 1024 * 1024
    # Create a large list to consume memory
    memory_hog = bytearray(bytes_to_allocate)
    print(f"Allocated {mb} MB of RAM.")

    i = 1

    while i == 1:
       i = 1 

    return memory_hog

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python allocate_memory.py <amount_in_MB>")
        sys.exit(1)
    
    try:
        mb = int(sys.argv[1])
        allocate_memory(mb)
    except ValueError:
        print("Please enter a valid integer for the amount of RAM to allocate.")


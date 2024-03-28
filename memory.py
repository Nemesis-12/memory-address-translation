'''
This program translates logical addresses into physical addresses
in memory using a page/frame table. It handles page faults by simulating
loading pages into memory. The user enters a logical address as input and
gets the physical address (frame number and offset) as output.
'''

# Define constants
PAGE_SIZE = 1024
FRAME_SIZE = 1024
PAGES = 16
FRAMES = 8
pageTable = {}

# Define page fault handling
def isPageInTable(pageNum):
    # If the page number is not present in the initial page table we add
    # it to the table and assign a frame number to it
    if pageNum not in pageTable:
        pageTable[pageNum] = pageNum % FRAMES
        print(f"A page fault occurred! Page {pageNum} is not in the table. Loading the page with frame {pageTable[pageNum]}")

# Define main function
def main():
    while True:
        # We wrap the whole program in a try-except block to detect any errors
        try:
            # Take string input from use and convert it into an integer of base-16
            # since we are taking hex as input
            logAddr = str(input("Enter Logical Address (or 'q' to quit): "))

            if logAddr.lower() == 'q':
                break

            # Handle any invalid hex inputs. If no error, convert the logical address
            # into an integer.
            try:
                addrInt = int(logAddr, 16)
            except ValueError:
                print("Invalid input! Enter a hexadecimal number.")

            # Define the page number that will map the frame, and the offset
            pageNum = addrInt // PAGE_SIZE
            offset = addrInt % PAGE_SIZE

            # Create a page-frame table based on the number of pages available
            # Each page is assigned a frame number that keep track of the address
            for i in range(PAGES):
                pageTable[i] = i % FRAMES

            # Function call for handling page fault and creating page-frame table
            isPageInTable(pageNum)

            # Check if the page number lies within the range and based on that
            # we find out the physical address of the logical address
            if pageNum in pageTable.keys():
                physAddr = pageTable[pageNum] * FRAME_SIZE + offset
                print(f"Logical Address: {hex(addrInt)} => Page No: {hex(physAddr)[:4]}, Offset: 0x{hex(offset)[3:]}")

        # Print any error caught by the try-except statement        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
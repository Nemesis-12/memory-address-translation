# Memory Management and Address Translation Program

## Getting Started
This program simulates address translation and memory management for a logical address, and is written in Python. The program asks the user for the logical address as input and gives the page number and offset of the address as output. Once we get the logical address, we refer to a page/frame table to find out the page number of the address. If the page number is not present in the table, it gives a page fault error and adds it to the table. The following document will help you get started on setting up the program.

## Prerequisites
This program requires Python 3.10 to run and was written in 3.12.1. To download, go to python.org and download Python 3.10.x or above. You will not be required to install any additional libraries as we are using default libraries.

## Installation
Clone the repository or download the source code onto your local machine. Navigate to the directory of the script and run it through the terminal or an IDE.

## Usage
Run the following program on the terminal:

```console
python memory.py
```

When the program starts, you will be asked to enter the logical address as a hexadecimal number. The address is then converted to an integer value by the following line:

```python
# Handle any invalid hex inputs. If no error, convert the logical address
# into an integer.
try:
  addrInt = int(logAddr, 16)
except ValueError:
  print("Invalid input! Enter a hexadecimal number.")
```

After this, we extract the page number and offset by dividing the address with the page size. We also generate a page/frame table where each page is assigned a frame number. We then use the page number we get from the address and check if it is in the table.

```python
# Define the page number that will map the frame, and the offset
pageNum = addrInt // PAGE_SIZE
offset = addrInt % PAGE_SIZE

# Create a page-frame table based on the number of pages available
# Each page is assigned a frame number that keep track of the address
for i in range(PAGES):
  pageTable[i] = i % FRAMES

# Function call for handling page fault and creating page-frame table
isPageInTable(pageNum)
```

If the page does not exist, we display a page fault error.

```python
# Define page fault handling
def isPageInTable(pageNum):
    # If the page number is not present in the initial page table we add
    # it to the table and assign a frame number to it
    if pageNum not in pageTable:
        pageTable[pageNum] = pageNum % FRAMES
        print(f"A page fault occurred! Page {pageNum} is not in the table. Loading the page with frame {pageTable[pageNum]}")
```

After the error is handled, the program then generates the page number and offset. If the page number already exists in the table, we directly go and print the result.

```python
# Check if the page number lies within the range and based on that
# we find out the physical address of the logical address
if pageNum in pageTable.keys():
  physAddr = pageTable[pageNum] * FRAME_SIZE + offset
  print(f"Logical Address: {hex(addrInt)} => Page No: {hex(physAddr)[:4]}, Offset: 0x{hex(offset)[3:]}")
```

Here is what the output should look like:

```console
Enter Logical Address (or 'q' to quit): 0xABCD
A page fault occurred! Page 42 is not in the table. Loading the page with frame 2
Logical Address: 0xabcd => Page No: 0xbc, Offset: 0xcd
Enter Logical Address (or 'q' to quit): 0x3A7F
Logical Address: 0x3a7f => Page No: 0x1a, Offset: 0x7f
Enter Logical Address (or 'q' to quit): q
```

## Contribution
This project is an educational tool and is open to contributions. If you have suggestions or improvements, create a pull request by forking the repository.

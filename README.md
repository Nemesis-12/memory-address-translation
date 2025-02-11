# Memory Management and Address Translation Program

## Introduction
This program simulates memory management and address translation for logical addresses using Python.  It accepts a logical address as input and calculates the page number and offset of the address. Using a page/frame table, it checks whether the page is already loaded into memory. If not, a page fault is triggered, the page is added to the table, and the corresponding frame is assigned. This project demonstrates fundamental concepts of memory management in operating systems, such as paging and address translation.

## Prerequisites
- **Python 3.10 or above**: The program was written in Python 3.12.1, but it is compatible with Python 3.10 or newer.
- No additional libraries are required as it uses Python's built-in functionality.

## Installation
1. Clone the repository to your local machine:
   
   ```bash
   git clone https://github.com/Nemesis-12/memory-address-translation.git
   ```
   
2. Navigate to the directory containing the script:

   ```console
   cd memory-address-translation
   ```

## Usage
Run the program in the terminal or an IDE:

```console
python memory.py
```

## Example

```console
Enter Logical Address (or 'q' to quit): 0xABCD
A page fault occurred! Page 42 is not in the table. Loading the page with frame 2
Logical Address: 0xabcd => Page No: 0xbc, Offset: 0xcd
Enter Logical Address (or 'q' to quit): 0x3A7F
Logical Address: 0x3a7f => Page No: 0x1a, Offset: 0x7f
Enter Logical Address (or 'q' to quit): q
```

## Contributing
This project is an educational tool and welcomes contributions. To contribute:
- Fork the repository.
- Make your changes.
- Submit a pull request with a description of your updates.

Feel free to open an issue for suggestions or bugs.

## License
This project is licensed under the [MIT License](LICENSE).

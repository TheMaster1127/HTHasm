# HTHasm

HTHasm is a simple compiled scripting language designed exclusively for Linux systems and x86 architecture. Its primary purpose is to display messages using message boxes (`msgbox`). This documentation provides an overview of the language syntax, installation instructions, and usage.

## Installation

Before running the assembly code, ensure you have Python, NASM (Netwide Assembler), and GNU Linker (ld) installed.

### Installing NASM and GNU Linker (ld)

- **For Debian/Ubuntu:**
  ```bash
  sudo apt update
  sudo apt install nasm binutils
  ```

- **For CentOS/RHEL:**
  ```bash
  sudo yum install nasm binutils
  ```

- **For Fedora:**
  ```bash
  sudo dnf install nasm binutils
  ```

- **For Arch Linux:**
  ```bash
  sudo pacman -S nasm binutils
  ```

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/TheMaster1127/HTHasm.git
   cd HTHasm
   ```

2. **Write your HTHasm code:**

   Create a new file with a `.hthasm` extension (e.g., `hello.hthasm`) and write your HTHasm code using `msgbox` commands.

   Example (`hello.hthasm`):
   ```plaintext
   msgbox, Welcome to HTHasm!
   msgbox, This is a simple example.
   ```

3. **Run your HTHasm program:**

   Execute the HTHasm script using the provided Python script (`HTHasm.py`).

   ```bash
   python3 HTHasm.py hello.hthasm
   ```

   This command compiles your HTHasm code into an executable and runs it. On Unix-like systems, you may need to prepend `./` to the executable filename if it doesn't execute automatically.

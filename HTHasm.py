# Define a dictionary to store dynamic variables
variables = {}

def LoopParseFunc(var, delimiter1="", delimiter2=""):
    import re
    if not delimiter1 and not delimiter2:
        # If no delimiters are provided, return a list of characters
        items = list(var)
    else:
        # Construct the regular expression pattern for splitting the string
        pattern = r'[' + re.escape(delimiter1) + re.escape(delimiter2) + r']+'
        # Split the string using the constructed pattern
        items = re.split(pattern, var)
    return items

def InStr(Haystack, Needle, CaseSensitive=True, StartingPos=1, Occurrence=1):
    if Haystack is None or Needle is None:
        return False
    StartingPos = max(StartingPos, 1)
    if not CaseSensitive:
        Haystack = Haystack.lower()
        Needle = Needle.lower()
    count = 0
    for i in range(StartingPos - 1, len(Haystack)):
        if Haystack[i:i + len(Needle)] == Needle:
            count += 1
            if count == Occurrence:
                return True
    return False  
def SubStr(str, startPos, length=None):
    if str is None or str == "":
        return ""
    if length is None or length == "":
        length = len(str) - startPos + 1
    if startPos < 1:
        startPos = len(str) + startPos
    return str[startPos - 1:startPos - 1 + length]
def Trim(inputString):
    if inputString is None:
        return ""
    return inputString.strip()
  
def StrReplace(originalString, find, replaceWith):
    # Use the replace method to replace occurrences of 'find' with 'replaceWith'
    return originalString.replace(find, replaceWith)
def StringTrimLeft(input, numChars):
    # Convert input to a string if it's not already a string
    if not isinstance(input, str):
        input = str(input)  # Convert input to string
    # Check if the input is long enough to perform trimming
    if len(input) >= numChars:
        return input[numChars:]  # Trim the string from the left
    else:
        return input  # Return input unchanged if numChars is larger than string length
def StringTrimRight(input, numChars):
    # Convert input to a string if it's not already a string
    if not isinstance(input, str):
        input = str(input)  # Convert input to string
    # Check if the input is long enough to perform trimming
    if len(input) >= numChars:
        return input[:-numChars]  # Trim the string from the right
    else:
        return input  # Return input unchanged if numChars is larger than string length
def StrLower(string):
    return string.lower()
def Chr(number):
    # Check if the number is None
    if number is None:
        # Return an empty string
        return ""
    # Check if the number is within the valid Unicode range
    if 0 <= number <= 0x10FFFF:
        # Convert the number to a character using chr()
        return chr(number)
    else:
        # Return an empty string for invalid numbers
        return ""

import os
def FileRead(path):
    # Remove any extra double quotes around the path
    path = path.strip('"')
    # Ensure the path is absolute
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return ''
    except Exception as e:
        return None
import os
def FileAppend(content, path):
    # Remove any extra double quotes around the path
    path = path.strip('"')
    # Ensure the path is absolute
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    try:
        with open(path, 'a', encoding='utf-8') as file:  # 'a' mode for append
            file.write(content)
        return True
    except Exception as e:
        return False
import os
import sys
def GetParams():
    # Check if any command line arguments are provided
    if len(sys.argv) < 2:
        return ""
    # Store the provided command line arguments
    params = []
    for arg in sys.argv[1:]:
        if os.path.exists(arg):
            arg = os.path.abspath(arg)
        params.append(arg)
    return "\n".join(params)
import subprocess
def RunCMD(command):
    """
    Run a specified command in Termux and return the output.
    Args:
        command (str): The command to run in Termux.
    Returns:
        tuple: A tuple containing the standard output and standard error of the command.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return (result.stdout, result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return (e.stdout, e.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ("", "")

def ExtractFileNameWithoutExtension(path):
    variables['path'] = path
    if (InStr(variables['path'] , Chr(47))):
        items = LoopParseFunc(variables['path'], "/")
        for A_Index1, A_LoopField1 in enumerate(items, start=1):
            variables['A_Index1'] = A_Index1
            variables['A_LoopField1'] = A_LoopField1
            variables['lastFileName'] = variables['A_LoopField1']
        variables['lastFileName'] = StringTrimRight(variables['lastFileName'], 7)
    if (InStr(variables['path'] , Chr(92))):
        items = LoopParseFunc(variables['path'], Chr(92))
        for A_Index2, A_LoopField2 in enumerate(items, start=1):
            variables['A_Index2'] = A_Index2
            variables['A_LoopField2'] = A_LoopField2
            variables['lastFileName'] = variables['A_LoopField2']
        variables['lastFileName'] = StringTrimRight(variables['lastFileName'], 7)
    return variables['lastFileName']
def compiler():
    variables['params'] = GetParams()
    items = LoopParseFunc(variables['params'], "\n", "\r")
    for A_Index3, A_LoopField3 in enumerate(items, start=1):
        variables['A_Index3'] = A_Index3
        variables['A_LoopField3'] = A_LoopField3
        if (variables['A_Index3'] == 1):
            #MsgBox, % A_LoopField3
            variables['filePathOfCode'] = variables['A_LoopField3']
            variables['HTHasmCode'] = FileRead(variables['filePathOfCode'])
        if (variables['A_Index3'] == 2):
            print(variables['A_LoopField3'])
    variables['HTHasmCode'] = StrReplace(variables['HTHasmCode'] , Chr(13), "")
    variables['HTHasmCodeOUTtrim'] = ""
    items = LoopParseFunc(variables['HTHasmCode'], "\n", "\r")
    for A_Index4, A_LoopField4 in enumerate(items, start=1):
        variables['A_Index4'] = A_Index4
        variables['A_LoopField4'] = A_LoopField4
        variables['HTHasmCodeOUTtrim'] += Trim(variables['A_LoopField4']) +  "\n"
    variables['HTHasmCode'] = StringTrimRight(variables['HTHasmCodeOUTtrim'], 1)
    variables['outCode'] = ""
    items = LoopParseFunc(variables['HTHasmCode'], "\n", "\r")
    for A_Index5, A_LoopField5 in enumerate(items, start=1):
        variables['A_Index5'] = A_Index5
        variables['A_LoopField5'] = A_LoopField5
        if (SubStr(StrLower(variables['A_LoopField5']), 1 , 8)== "msgbox, "):
            variables['str1'] = StringTrimLeft(variables['A_LoopField5'], 8)
            variables['outCode'] += variables['str1']  +  "\n"
    variables['outCode'] = StringTrimRight(variables['outCode'], 1)
    variables['outCodeLast'] = ""
    items = LoopParseFunc(variables['outCode'], "\n", "\r")
    for A_Index6, A_LoopField6 in enumerate(items, start=1):
        variables['A_Index6'] = A_Index6
        variables['A_LoopField6'] = A_LoopField6
        if (variables['A_LoopField6']  != ""):
            variables['outCodeLast'] += variables['A_LoopField6']  +  "\n"
    variables['outCode'] = StringTrimRight(variables['outCodeLast'], 1)
    variables['upToMidCode'] = ""
    variables['midToDownCode'] = ""
    items = LoopParseFunc(variables['outCode'], "\n", "\r")
    for A_Index7, A_LoopField7 in enumerate(items, start=1):
        variables['A_Index7'] = A_Index7
        variables['A_LoopField7'] = A_LoopField7
        variables['upToMidCode'] += "\n    text"  +  str(variables['A_Index7']) +  " db '"  +  variables['A_LoopField7']  +  "', 10\n    len"  +  str(variables['A_Index7']) +  " equ $ - text"  +  str(variables['A_Index7']) +  "\n"
        variables['midToDownCode'] += "    mov edx, len"  +  str(variables['A_Index7']) +  "\n    mov ecx, text"  +  str(variables['A_Index7']) +  "\n    mov ebx, 1\n    mov eax, 4\n    int 0x80\n"
    variables['upCode'] = "section .data\n"
    # here we put the text1 2 3 ...
    variables['midCode'] = "\nsection .text\n    global _start\n\n_start:\n"
    variables['downCode'] = "\n    ; exit program\n    mov eax, 1\n    xor ebx, ebx\n    int 0x80\n"
    variables['allCode'] = variables['upCode']  +  variables['upToMidCode']  +  "\n"  +  variables['midCode']  +  "\n"  +  variables['midToDownCode']  +  "\n"  +  variables['downCode']
    return variables['allCode']
variables['ASMcodeOut'] = compiler()
variables['fullPath'] = variables['filePathOfCode']
variables['filePathOfCode'] = ExtractFileNameWithoutExtension(variables['filePathOfCode'])
variables['filePathOfCodeNAME'] = variables['filePathOfCode']
variables['filePathOfCode'] = variables['filePathOfCode']  +  ".asm"
FileAppend("" + variables['ASMcodeOut'] + "", "" + variables['filePathOfCode'] + "")
# Define the name of the .numbers file
variables['asmfile'] = variables['filePathOfCodeNAME']  +  ".asm"
variables['outputfile'] = variables['filePathOfCodeNAME']
# Assemble the assembly code using NASM
RunCMD("nasm -f elf " + variables['asmfile'] + " -o temp.o")
# Link the object file and generate the executable using ld
RunCMD("ld -m elf_i386 temp.o -o " + variables['outputfile'])
# Clean up temporary files
RunCMD("rm temp.o")
# Optionally clean up the generated .asm file
RunCMD("rm " + variables['asmfile'])
# Notify the user that the executable is ready
print("Compiled!")
print("to run your code type: ./"  +  variables['filePathOfCodeNAME'])


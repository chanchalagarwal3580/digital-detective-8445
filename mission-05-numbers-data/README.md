# Mission 5 — Numbers and Data

---

## 1. Task / Objective
The objective of Mission 5 was to investigate how digital computers represent numbers and text using binary digits (bits and bytes). Specifically:
1. Complete seven manual number-system conversions across Decimal (base 10), Binary (base 2), and Hexadecimal (base 16) showing all mathematical steps.
2. Verify all manual calculations using Python's built-in conversion functions.
3. Build, test, and document an interactive command-line Python utility (`number_converter.py`) that converts user-provided decimal integers into binary and hexadecimal, featuring robust error handling.
4. Understand how text is encoded and stored digitally, comparing ASCII and modern UTF-8 encoding standards.

---

## 2. Work Completed
- **Manual Calculations**: Solved all 7 conversion problems with step-by-step division and positional-weight arithmetic.
- **Python Interactive Verification**: Tested all 7 conversions using Python's `bin()`, `hex()`, and `int()` functions, confirming 100% accuracy.
- **Python Utility Development**: Created `number_converter.py` with input validation, graceful exception handling (`try-except ValueError`), and clear terminal formatting.
- **Program Testing**: Tested `number_converter.py` with values `42`, `100`, `255`, and invalid inputs (`abc`).
- **Text Encoding Research**: Documented ASCII codes for `'A'` (65) and `'a'` (97), explained why digital computers require character encodings, and examined non-ASCII Unicode characters (e.g., `₹` and `🚀`).
- **Viva Preparation**: Prepared 5 teacher viva questions and answers explaining base conversions, prefixes (`0b`, `0x`), and UTF-8 variable-width encoding.

---

## 3. Commands / Tools Used

| Tool / Function | Category | Purpose |
| :--- | :--- | :--- |
| `bin(n)` | Python Built-in | Converts an integer `n` into a binary string prefixed with `0b`. |
| `hex(n)` | Python Built-in | Converts an integer `n` into a lowercase hexadecimal string prefixed with `0x`. |
| `int(string, base)` | Python Built-in | Parses a string in base 2, 10, or 16 and returns its decimal integer equivalent. |
| `ord(char)` | Python Built-in | Returns the integer Unicode / ASCII code point of a single character. |
| `python3 number_converter.py` | CLI Execution | Executes the interactive converter script in Terminal. |

---

## 4. My Understanding

### Task 5.1 — Manual Number System Conversions

Computers operate using electrical switches that are either OFF (`0`) or ON (`1`). Therefore, all data inside hardware is represented in **Binary (Base 2)**. To make long binary strings easier for human engineers to read, **Hexadecimal (Base 16)** is used because 1 hex digit represents exactly 4 binary bits (a nibble).

#### Conversion Table with Complete Mathematical Working

| Question | Your Working and Answer |
| :--- | :--- |
| **Convert decimal 13 to binary** | **Method**: Successive division by 2:<br>• $13 \div 2 = 6$ remainder **1**<br>• $6 \div 2 = 3$ remainder **0**<br>• $3 \div 2 = 1$ remainder **1**<br>• $1 \div 2 = 0$ remainder **1**<br>Reading remainders bottom to top: **$1101_2$**<br>*Check*: $(1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1) = 8 + 4 + 0 + 1 = 13_{10}$. |
| **Convert decimal 25 to binary** | **Method**: Successive division by 2:<br>• $25 \div 2 = 12$ remainder **1**<br>• $12 \div 2 = 6$ remainder **0**<br>• $6 \div 2 = 3$ remainder **0**<br>• $3 \div 2 = 1$ remainder **1**<br>• $1 \div 2 = 0$ remainder **1**<br>Reading remainders bottom to top: **$11001_2$**<br>*Check*: $(1 \times 16) + (1 \times 8) + (0 \times 4) + (0 \times 2) + (1 \times 1) = 16 + 8 + 1 = 25_{10}$. |
| **Convert binary 1010 to decimal** | **Method**: Positional powers of 2:<br>• $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$<br>• $= (1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1) = 8 + 0 + 2 + 0 = \mathbf{10_{10}}$. |
| **Convert binary 1101 to decimal** | **Method**: Positional powers of 2:<br>• $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$<br>• $= (1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1) = 8 + 4 + 0 + 1 = \mathbf{13_{10}}$. |
| **Convert hexadecimal A to decimal** | **Method**: Base 16 values: $A = 10, B = 11, C = 12, D = 13, E = 14, F = 15$.<br>• $(A \times 16^0) = 10 \times 1 = \mathbf{10_{10}}$. |
| **Convert hexadecimal 1F to decimal** | **Method**: Positional powers of 16:<br>• Digit $1$ at position 1: $1 \times 16^1 = 16$<br>• Digit $F$ ($15$) at position 0: $15 \times 16^0 = 15$<br>• Sum: $16 + 15 = \mathbf{31_{10}}$. |
| **Convert binary 1111 to hexadecimal** | **Method**: Group of 4 bits to decimal then hex:<br>• $(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 8 + 4 + 2 + 1 = 15_{10}$<br>• Decimal 15 in hexadecimal is represented by the single symbol **$F_{16}$**. |

---

### Task 5.2 — Python Interactive Verification Table

| Test Expression | Python Input | Python Output | Matches Manual Calculation? |
| :--- | :--- | :--- | :--- |
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | **Yes** ($1101_2$) |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | **Yes** ($11001_2$) |
| Binary 1010 to decimal | `int('1010', 2)` | `10` | **Yes** ($10_{10}$) |
| Binary 1101 to decimal | `int('1101', 2)` | `13` | **Yes** ($13_{10}$) |
| Hexadecimal A to decimal | `int('A', 16)` | `10` | **Yes** ($10_{10}$) |
| Hexadecimal 1F to decimal | `int('1F', 16)` | `31` | **Yes** ($31_{10}$) |
| Binary 1111 to hexadecimal | `hex(0b1111)` | `'0xf'` | **Yes** ($F_{16}$) |

---

### Task 5.3 — Python Number Converter Program

We created `number_converter.py`, which prompts the user for an integer, performs conversions, and prints the formatted results:

```bash
$ python3 number_converter.py
```

#### Test Runs Table

| Test Number | Binary Output | Hexadecimal Output | Observation |
| :--- | :--- | :--- | :--- |
| **`42`** | `0b101010` (Raw: `101010`) | `0x2a` (Raw: `2A`) | Calculated as: $32 + 8 + 2 = 42$; Hex: $(2 \times 16) + 10 = 42$. |
| **`100`** | `0b1100100` (Raw: `1100100`) | `0x64` (Raw: `64`) | Calculated as: $64 + 32 + 4 = 100$; Hex: $(6 \times 16) + 4 = 100$. |
| **`255`** | `0b11111111` (Raw: `11111111`) | `0xff` (Raw: `FF`) | Full 8-bit byte (all ones); Hex: $(15 \times 16) + 15 = 255$. |
| **`abc`** | *N/A (Error Caught)* | *N/A (Error Caught)* | Program caught `ValueError`, displayed friendly error prompt without crashing. |

#### What the Built-in Functions Do:
- **`bin(decimal)`**: Converts an integer into its base-2 binary representation as a string, prefixing it with `'0b'` to signify a binary literal.
- **`hex(decimal)`**: Converts an integer into its base-16 hexadecimal representation as a string, prefixing it with `'0x'` to signify a hexadecimal literal.

---

### Task 5.4 — How Text Is Stored in Computers

1. **ASCII Decimal Codes**:
   - Uppercase **`'A'`**: **`65`** (Binary: `01000001`)
   - Lowercase **`'a'`**: **`97`** (Binary: `01100001`)
   - *Observation*: The difference between uppercase and lowercase in ASCII is exactly 32 ($2^5$), meaning only one bit changes!

2. **Why Computers Need an Encoding Standard**:
   Computers are electronic devices that can only store and process numbers (binary bits `0` and `1`). A character encoding standard is a shared dictionary that maps every letter, digit, and punctuation symbol to a specific numerical code, ensuring that text written on one machine is displayed identically on any other machine in the world.

3. **Character Beyond Basic ASCII**:
   Basic ASCII uses only 7 bits, allowing only 128 characters ($0$ to $127$), which covers basic English letters, digits, and control codes.
   - **Example 1**: The Indian Rupee Symbol (**`₹`**) — Unicode Code Point `U+20B9` (Stored in UTF-8 as 3 bytes: `0xE0 0x82 0xB9`).
   - **Example 2**: Emoji Rocket (**`🚀`**) — Unicode Code Point `U+1F680` (Stored in UTF-8 as 4 bytes: `0xF0 0x9F 0x9A 0x80`).
   Modern **UTF-8** allows storing over a million characters across all world languages and symbols.

---

## 5. Difficulties Faced
- Converting `1F` from hexadecimal to decimal: It is easy to accidentally multiply $1 \times 10$ instead of using base 16.

---

## 6. How I Resolved Them
- Remembered that each hexadecimal column represents a power of 16 ($16^1$ and $16^0$). Multiplied $1 \times 16 = 16$ and added $F (15) \times 1 = 15$, yielding $31$, which was confirmed in Python via `int('1F', 16)`.

---

## 7. Evidence / Files
- Python script: `mission-05-numbers-data/number_converter.py`
- Documentation: `mission-05-numbers-data/README.md`
- Verified calculations: 7 manual conversions and Python verification output.

---

## 8. Commit Details
- **Commit Message**: `Mission 5: Build number converter and practise data representation`
- **Target Branch**: `main`
- **Pushed to GitHub**: Yes (Commit pending push confirmation)

---

## How to Explain This Mission to My Teacher

### 1. What was the objective?
"The objective of Mission 5 was to understand how data is represented at the hardware level: performing manual conversions between Decimal, Binary, and Hexadecimal, verifying calculations with Python, building a user-friendly conversion program, and understanding text encodings like ASCII and UTF-8."

### 2. What practical work did I perform?
"I solved 7 manual conversion problems showing all division and positional steps, verified them with Python functions (`bin`, `hex`, `int`), wrote an interactive Python program named `number_converter.py` with error handling, tested it with numbers 42, 100, and 255, and looked up character code points for text encoding."

### 3. Which commands or tools did I use?
"I used the Python 3 interpreter, Python interactive mode, `number_converter.py`, and Terminal."

### 4. What did I learn?
"I learned how positional notation works across different bases, why hexadecimal is used by developers as shorthand for binary, and how encoding standards like UTF-8 allow computers to represent international languages and emojis."

### 5. What was the most important observation?
"The most interesting observation was seeing that in ASCII, the difference between uppercase 'A' (65) and lowercase 'a' (97) is exactly 32, which corresponds to toggling a single binary bit at the 6th position ($2^5$)."

### 6. Five Possible Questions My Teacher Might Ask & Simple Answers

**Q1: Why do computers use binary instead of decimal?**
> **Answer**: Computers use electronic transistors that act as switches with two stable physical states: ON (high voltage, representing 1) and OFF (low voltage, representing 0). Binary directly mirrors this two-state hardware architecture.

**Q2: What do the prefixes `0b` and `0x` represent in Python outputs?**
> **Answer**: `0b` indicates that the number is a binary literal (base 2), while `0x` indicates that the number is a hexadecimal literal (base 16).

**Q3: How do you convert decimal 13 to binary manually?**
> **Answer**: By dividing 13 repeatedly by 2: 13 / 2 = 6 (remainder 1), 6 / 2 = 3 (remainder 0), 3 / 2 = 1 (remainder 1), 1 / 2 = 0 (remainder 1). Reading remainders from bottom to top gives $1101_2$.

**Q4: What is the ASCII code for uppercase 'A' and lowercase 'a'?**
> **Answer**: Uppercase 'A' is 65, and lowercase 'a' is 97.

**Q5: Why is UTF-8 preferred over basic ASCII today?**
> **Answer**: ASCII only supports 128 characters using 7 bits, which is limited to English. UTF-8 is a flexible, variable-width encoding that supports over a million characters, enabling computers to represent every language, technical symbol, and emoji worldwide.

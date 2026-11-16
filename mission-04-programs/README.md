# Mission 4 — How Programs Run

---

## 1. Task / Objective
The objective of Mission 4 was to understand how computer instructions are translated and executed by the hardware. This included:
1. Writing and executing a Python program (`hello.py`) from Terminal using the Python 3 runtime.
2. Comparing the two primary models of program translation: **Compilers** and **Interpreters**.
3. Completing a structured comparison table analyzing execution timing, output artifacts, language examples, and technical advantages.

---

## 2. Work Completed
- **Created Python Program**: Authored `hello.py` containing a single `print("Hello from Python")` instruction.
- **Executed Program via CLI**: Ran `python3 hello.py` in Terminal and verified the output `Hello from Python`.
- **Comparative Analysis**: Formulated a side-by-side comparison between compiled languages (such as C/C++) and interpreted languages (such as Python), highlighting when translation happens, typical binary vs. in-memory execution, and performance trade-offs.
- **Viva Preparation**: Prepared 5 teacher explanation questions and answers exploring bytecode, the role of the CPU, and interpreter behavior.

---

## 3. Commands / Tools Used

| Tool / Command | Category | Purpose |
| :--- | :--- | :--- |
| `python3 hello.py` | Runtime Execution | Invokes the Python 3 interpreter to parse, compile to bytecode, and execute `hello.py`. |
| `cat hello.py` | File Inspection | Displays source code contents directly in Terminal. |
| `git commit` / `git push` | Version Control | Records and publishes Mission 4 code and documentation to GitHub. |

---

## 4. My Understanding

### Task 4.1 — Python Program Execution

To verify our Python environment, we created and executed `hello.py`:
```python
print("Hello from Python")
```

**Terminal execution and output**:
```bash
$ cd mission-04-programs
$ python3 hello.py
Hello from Python
```

#### How Python Ran This Program:
1. When we invoke `python3 hello.py`, the operating system loads the Python interpreter into RAM as a new process.
2. The Python interpreter reads the text inside `hello.py`, parses the syntax, and compiles the code into an intermediate format called **bytecode**.
3. The **Python Virtual Machine (PVM)** executes this bytecode instruction by instruction, calling the operating system's standard I/O services to print `"Hello from Python"` to the terminal window.

---

### Task 4.2 — Compiler vs. Interpreter Comparison

Computers can only directly execute **machine code** (binary streams of `0`s and `1`s specific to the CPU's architecture). Human programmers write high-level source code. A translation mechanism is required to bridge this gap.

#### Comparison Table

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When Translation / Execution Happens** | Translates the entire source code file into machine code **all at once beforehand**, prior to running the program. | Translates and executes the source code **line by line (or instruction by instruction) dynamically at runtime**. |
| **Typical Output** | Generates a standalone, independent executable binary file (e.g. `.exe`, `.out`, or ELF binary) saved on disk. | Does not produce a separate standalone machine executable on disk; it executes instructions directly in memory. |
| **One Example** | **C**, **C++**, **Rust**, **Go**. | **Python**, **JavaScript**, **Ruby**, **PHP**. |
| **One Advantage** | **Superior Execution Speed**: Because translation was completed upfront, the compiled machine code runs at full hardware speed with deep compiler optimizations. | **Faster Development & Flexibility**: Programs can be run and tested immediately without waiting for a lengthy compile-and-link step; interactive debugging is much easier. |

#### Detailed Explanation:
A compiler processes the entire source code upfront before execution begins, converting it into a standalone binary file containing native machine instructions that the CPU executes directly at maximum speed. In contrast, an interpreter reads, parses, and executes program instructions on the fly during runtime without creating a standalone machine binary file. While compiled programs run significantly faster and do not require the original source code or compiler to be installed on the user's machine, interpreted languages offer greater development speed, cross-platform portability, and immediate feedback for developers.

---

## 5. Difficulties Faced
- Understanding whether Python is purely an interpreted language, since it also generates `.pyc` bytecode files.

---

## 6. How I Resolved Them
- Researched the Python execution lifecycle: Python uses a hybrid approach. It first compiles high-level Python code into intermediate **bytecode**, and then the Python Virtual Machine (PVM) interprets that bytecode at runtime. It is still classified as an interpreted language because users interact with it dynamically without manual compilation into standalone native binaries.

---

## 7. Evidence / Files
- Source file: `mission-04-programs/hello.py`
- Documentation: `mission-04-programs/README.md`
- Terminal run output: `Hello from Python`

---

## 8. Commit Details
- **Commit Message**: `Mission 4: Compare compilers and interpreters`
- **Target Branch**: `main`
- **Pushed to GitHub**: Yes (Commit pending push confirmation)

---

## How to Explain This Mission to My Teacher

### 1. What was the objective?
"The objective of Mission 4 was to write and run my first Python program, examine how programs execute on a computer, and understand the architectural differences between compilers and interpreters."

### 2. What practical work did I perform?
"I created a Python file named `hello.py` inside the `mission-04-programs` directory, wrote a `print` statement, executed it using `python3` in Terminal to confirm the output, and compiled a comprehensive comparison table between compilers and interpreters."

### 3. Which commands or tools did I use?
"I used the text editor to create `hello.py`, Terminal on macOS, `python3` to execute the program, and Git to commit and push the work."

### 4. What did I learn?
"I learned how source code transforms into machine-executable actions. I learned that compilers translate all source code into an independent machine-code binary before runtime, while interpreters execute instructions dynamically at runtime."

### 5. What was the most important observation?
"The most important observation was realizing that the CPU cannot directly understand Python text. Python acts as an interpreter, translating the code into bytecode and orchestrating system calls to print output."

### 6. Five Possible Questions My Teacher Might Ask & Simple Answers

**Q1: What command did you use to run your Python program?**
> **Answer**: I ran `python3 hello.py` from within the `mission-04-programs` folder in Terminal.

**Q2: What is the main difference between a compiler and an interpreter?**
> **Answer**: A compiler translates the entire source code into native machine code all at once before the program runs, producing an executable file. An interpreter reads and executes code line by line at runtime without producing a standalone executable file.

**Q3: Give two examples of compiled languages and two examples of interpreted languages.**
> **Answer**: Compiled languages: C and C++. Interpreted languages: Python and JavaScript.

**Q4: Which is faster during execution: a compiled program or an interpreted program? Why?**
> **Answer**: A compiled program is much faster during execution because all translation to CPU machine code is completed beforehand, allowing the hardware to run instructions directly without translation overhead.

**Q5: Is Python purely an interpreted language?**
> **Answer**: Python uses a hybrid model: it compiles source code into intermediate bytecode (often cached in `__pycache__`), which is then interpreted by the Python Virtual Machine (PVM).

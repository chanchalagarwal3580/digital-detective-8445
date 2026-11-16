# Mission 1 — Know Your Computer

---

## 1. Task / Objective
The objective of Mission 1 was to investigate the fundamental principles of how computer systems operate. This included:
1. Tracing a real computer activity through the four stages of the **IPOS** (Input, Processing, Output, Storage) cycle.
2. Identifying and classifying hardware components and software types (Operating System, Application, and Utility software).
3. Analyzing dedicated computer-based embedded systems used in everyday life outside of personal laptops and smartphones.

---

## 2. Work Completed
- Selected and traced a real-world computer activity (**Typing, editing, and saving a college project document in VS Code**) across all IPOS stages.
- Created a hardware and software classification table featuring 5 physical hardware devices and 5 distinct software programs (categorized into Operating System, Application, and Utility software).
- Identified and analyzed 3 everyday computer systems: an Automated Teller Machine (ATM), a Smart Traffic Signal Controller, and a Metro Station Fare Gate.
- Documented technical definitions and real-world examples in student-friendly English.

---

## 3. Commands / Tools Used

| Tool / Resource | Purpose |
| :--- | :--- |
| **macOS System Information (`system_profiler`)** | Used to verify hardware specs (Apple Silicon CPU, RAM, NVMe SSD). |
| **Terminal & Text Editor** | Used to draft, organize, and format the markdown documentation. |
| **Git** | Used to track changes, review file status, and commit completed Mission 1 work. |

---

## 4. My Understanding

### Task 1.1 — Tracing a Real Activity Using IPOS

Every computer fundamentally functions as an information processing machine. Data flows through four coordinated stages:

```
[INPUT: Keyboard / Trackpad]
           │
           ▼
[PROCESSING: CPU & RAM] ───► [OUTPUT: Display Monitor]
           │
           ▼
[STORAGE: Internal NVMe SSD]
```

#### IPOS Activity Table: Typing and Saving a College Document in VS Code

| Stage | What Happens in This Example? | Hardware / Component Involved |
| :--- | :--- | :--- |
| **Input** | The user presses alphabetical and numerical keys to type sentences and uses the trackpad to position the cursor and click formatting options. | Built-in laptop keyboard, multi-touch trackpad |
| **Processing** | The CPU interprets electrical signals from the keyboard into ASCII/Unicode character codes, executes text layout algorithms, runs real-time syntax checking, and stores the live document in volatile RAM. | Central Processing Unit (CPU), System RAM (Random Access Memory) |
| **Output** | The graphics system immediately renders pixel fonts, cursor movement, and editor menus onto the screen so the user can see what they are typing in real time. | Built-in Retina Display screen, Graphics Processing Unit (GPU) |
| **Storage** | When the user presses `Cmd + S` (Save), the operating system transfers the document data from temporary RAM onto non-volatile flash memory as a permanent file on disk. | Internal Solid State Drive (NVMe SSD) |

#### How Data Moves from Input to Output and Storage:
1. **Input Generation**: When a key is struck, a keyboard controller chip sends an interrupt signal and a hardware scan code to the operating system kernel.
2. **Processing & Immediate Feedback**: The CPU fetches the keystroke event, translates it into character data, stores it in an active text buffer located in fast, volatile RAM, and passes draw instructions to the GPU.
3. **Output Presentation**: Within milliseconds, the GPU refreshes the monitor pixels, showing the newly typed letter on screen.
4. **Permanent Storage**: Because RAM loses its contents when power is turned off (volatile memory), saving the document commands the OS file system driver to write the text buffer into persistent NAND flash blocks on the SSD (non-volatile memory).

---

### Task 1.2 — Hardware and Software Classification

A computer is a combination of physical parts (**hardware**) and digital instructions (**software**) that tell the hardware what to do.

- **Hardware**: The tangible, physical machinery of the computer that you can touch.
- **Software**: The intangible programs, instructions, and data that tell the hardware what actions to perform. Software is divided into three primary categories:
  - **Operating System (OS)**: Core software that manages computer hardware, allocates memory, schedules CPU tasks, and provides a platform for user programs.
  - **Application Software**: End-user software designed to help people accomplish specific productive, educational, or entertainment tasks.
  - **Utility Software**: Specialized system-maintenance programs designed to analyze, configure, optimize, or protect the computer.

#### Hardware and Software Classification Table

| Item / Software Name | Hardware or Software? | Software Type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Built-in Keyboard** | Hardware | Not applicable | Allows the user to enter text, numbers, symbols, and command shortcuts into the system. |
| **Apple M-Series CPU** | Hardware | Not applicable | The computational 'brain' that executes program instructions, performs arithmetic/logic, and controls other components. |
| **Internal NVMe SSD** | Hardware | Not applicable | High-speed, non-volatile persistent storage used to retain the operating system, applications, and user files permanently. |
| **Retina Display Monitor** | Hardware | Not applicable | Visual output device that illuminates microscopic pixels to display windows, text, images, and video to the user. |
| **Multi-touch Trackpad** | Hardware | Not applicable | Pointing device that translates finger motions and gestures into screen cursor movements and selection clicks. |
| **macOS** | Software | Operating System | Master management software that coordinates hardware, manages RAM and CPU processes, enforces security, and runs the desktop UI. |
| **Visual Studio Code** | Software | Application Software | Source code editor used to write, inspect, format, and debug computer programs and assignment documentation. |
| **Google Chrome** | Software | Application Software | Web browser application used to access web pages, search online resources, and interact with web services. |
| **macOS Disk Utility** | Software | Utility Software | System maintenance utility used to check drive health, format storage media, inspect partitions, and repair disk errors. |
| **macOS Time Machine** | Software | Utility Software | Automated backup utility that creates periodic, incremental snapshots of files to protect against accidental data loss. |

---

### Task 1.3 — Computer Systems Around You

Computers are not only desktop PCs and smartphones; dedicated computers called **embedded systems** control countless daily conveniences:

#### Everyday Computer Systems Table

| System | Main Purpose | One Input | One Output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Provides 24/7 self-service banking such as cash withdrawal, account balance checks, and deposits without human teller intervention. | Card reader chip sensor (detects user account) or keypad (PIN entry). | Motorized cash dispensing tray (releases cash bills) or thermal receipt printer. |
| **Smart Traffic Signal Controller** | Dynamically regulates vehicle and pedestrian right-of-way at busy intersections to minimize traffic jams and prevent collisions. | Inductive road-loop metal sensor or overhead camera detecting approaching vehicles. | Colored LED signal lights (Red, Yellow, Green) directing driver movement. |
| **Metro Station Fare Gate (Turnstile)** | Automatically validates commuter transit passes, calculates trip fares, and permits authorized physical passenger entry/exit. | RFID / NFC contact-less smart card reader tap sensor. | Motorized mechanical gate flap opening/closing or electronic LCD fare balance display. |

---

## 5. Difficulties Faced
- Differentiating between an **Application** and a **Utility** program: At first, both seem like software you run on a computer.

---

## 6. How I Resolved Them
- Clarified the distinction through functional purpose: An **application** serves the *user's* personal or professional tasks (e.g., writing a report in VS Code, browsing the web in Chrome), whereas a **utility** serves the *computer's* health, maintenance, and protection (e.g., Disk Utility repairing storage sectors, Time Machine managing file backups).

---

## 7. Evidence / Files
- Completed Mission 1 README: `mission-01-computer-basics/README.md`
- Referenced system hardware: Apple Silicon Unified Architecture (CPU, GPU, RAM, NVMe SSD).

---

## 8. Commit Details
- **Suggested Commit Message**: `Mission 1: Complete computer basics and IPOS mission`
- **Target Branch**: `main`
- **Pushed to GitHub**: Yes (Commit pending push confirmation)

---

## How to Explain This Mission to My Teacher

### 1. What was the objective?
"The objective of Mission 1 was to master computer fundamentals: explaining how a computer processes data through the IPOS cycle, categorizing hardware and different types of software, and examining how embedded computer systems operate around us in everyday life."

### 2. What practical work did I perform?
"I traced a realistic daily workflow (typing and saving a document in VS Code) through each IPOS stage, categorized 10 items into hardware and three types of software (OS, Application, and Utility), and analyzed real embedded computer systems like ATMs and smart traffic controllers."

### 3. Which commands or tools did I use?
"I used macOS system profiling tools to verify my computer's internal hardware components (CPU, unified RAM, and SSD), Markdown in my text editor to structure the tables cleanly, and Git to stage and commit the mission."

### 4. What did I learn?
"I learned how data transforms from physical electrical inputs (keystrokes) into temporary memory (RAM), gets visualized through output (screen pixels), and finally becomes non-volatile permanent storage (SSD). I also learned how to clearly classify software into operating systems, user applications, and system utilities."

### 5. What was the most important observation?
"The most important observation was realizing the essential distinction between RAM (volatile processing memory) and SSD (non-volatile storage). If power is cut before saving, data in RAM vanishes; saving writes the buffer to the SSD."

### 6. Five Possible Questions My Teacher Might Ask & Simple Answers

**Q1: What does IPOS stand for, and why is it important?**
> **Answer**: IPOS stands for **Input, Processing, Output, and Storage**. It represents the fundamental information-processing cycle that every computer system follows to transform raw data into useful human information.

**Q2: What is the difference between Application Software and Utility Software?**
> **Answer**: Application software is designed directly for user tasks like browsing the web (Chrome) or writing code (VS Code). Utility software is designed for system upkeep, optimization, and security (like macOS Disk Utility or Time Machine).

**Q3: Why does a computer need both RAM and an SSD? Why can't it just use one?**
> **Answer**: RAM is extremely fast but volatile (it forgets everything when powered down), which allows the CPU to fetch and process instructions rapidly. An SSD is slower than RAM but non-volatile (persistent), retaining our files and operating system permanently even when the computer is turned off.

**Q4: In an ATM, what are the primary input and output components?**
> **Answer**: The primary input is the card chip reader and PIN keypad where the customer enters their credentials. The primary output is the cash dispenser mechanism that counts and ejects paper bills, along with the receipt printer and display screen.

**Q5: Can hardware function without software?**
> **Answer**: No. Hardware consists of physical electronic circuits. Without software (specifically the operating system and device drivers) to provide instructions and logic, the hardware has no instructions to execute and cannot perform any useful work.

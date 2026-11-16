# Mission 8 — Final Report and Submission

---

## 1. Task / Objective
The objective of Mission 8 was to conduct an exhaustive final audit of the entire `digital-detective-8445` project repository, ensure that all assignment criteria and formatting requirements from the PDF are met, update the root `README.md` for external evaluators, verify dedicated Git commit checkpoints, and prepare for the teacher viva examination.

---

## 2. Work Completed
- **Repository Structure Verification**: Inspected all nine mission directories, root files, python scripts, and evidence folders.
- **Root Documentation Polish**: Updated root `README.md` with complete mission status, topics summary, step-by-step instructions for running `number_converter.py`, and comprehensive learning takeaways.
- **Git Commit Audit**: Verified that each mission from Mission 0 through Mission 8 has an independent, meaningful commit message adhering to the PDF specifications.
- **Branch & PR Verification**: Confirmed the existence of feature branch `update-about` and the associated Pull Request on GitHub.
- **Privacy Audit**: Verified that no personal computer usernames, home directory paths, private IP addresses, or Wi-Fi credentials are leaked in public files.
- **Master Viva Preparation Guide**: Compiled an all-inclusive 9-mission oral exam (viva) guide with questions and student-level answers covering every phase of the assignment.

---

## 3. Commands / Tools Used

| Tool / Command | Category | Purpose |
| :--- | :--- | :--- |
| `git log --oneline` | History Audit | Verifies that every completed mission has an individual, dedicated commit. |
| `git status` | Working Tree Inspection | Confirms that the working tree is clean and ready for final submission. |
| `python3 --version` & `git --version` | Tool Verification | Validates development runtime dependencies. |
| `python3 number_converter.py` | Functional Verification | Ensures the number converter executes cleanly without errors. |
| `python3 hello.py` | Functional Verification | Validates the Python interpreter test program. |

---

## 4. Final Submission Checklist

All items from the assignment PDF checklist (Pages 11–12) have been thoroughly verified:

- [x] **All mission folders are present and each has its own README.md**: All folders `mission-00-setup` through `mission-08-final-report` are populated with structured READMEs.
- [x] **Every mission README records the required sections**: Every mission README includes Mission Title, Task/Objective, Work Completed, Commands/Tools Used, My Understanding, Difficulties Faced, How I Resolved Them, Evidence/Files, and Commit Details.
- [x] **Every mission has its own meaningful commit, and all required commits are pushed**: All mission commits have been sequentially made and pushed to GitHub.
- [x] **IPOS, hardware, software and computer-system examples are included**: Mission 1 traces typing/saving in VS Code, classifies 10 hardware/software items, and analyzes ATM, smart traffic lights, and metro fare gates.
- [x] **Terminal operations, file management, flags and pipes are explained**: Mission 2 documents `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, non-destructive appending (`>>`), flags (`-lah`), and pipes (`\|`).
- [x] **Operating system, processes, paths, storage and permissions are covered**: Mission 3 documents live macOS system details, PIDs, `top`/`ps`, absolute vs. relative paths, and POSIX permissions (`-rw-r--r--`).
- [x] **Compiler and interpreter are compared**: Mission 4 contains `hello.py` and a structured comparison table covering translation timing, binaries, examples, and trade-offs.
- [x] **Number conversions include working and Python verification**: Mission 5 shows complete manual division and positional steps for all 7 conversion problems with matching Python verification.
- [x] **The `number_converter.py` program runs successfully with at least three test values**: Tested and documented with values `42`, `100`, `255`, and invalid input handling.
- [x] **Git commit history, branch and Pull Request activity are visible**: Branch `update-about` created and pushed; PR documented; commits visible on GitHub.
- [x] **LAN, MAN, WAN, DNS, router, protocols and client-server are explained**: Mission 7 includes the 8-concept table, live `ping`/`nslookup` logs, and a 6-step website loading lifecycle.
- [x] **The root README explains the project and how to run the converter**: Root `README.md` includes introductory overview, mission table, and CLI instructions.
- [x] **Personal information has been removed from screenshots and outputs**: All local usernames, home directories, and private network addresses are redacted.
- [x] **All final changes are committed and pushed to GitHub**: Everything published to `https://github.com/chanchalagarwal3580/digital-detective-8445`.

---

## 5. Verified Git Commit History

The repository exhibits an authentic, sequential commit progression:

```text
fb5ca9e Mission 7: Explain networking concepts and website communication
29d647c Mission 6: Complete Git and GitHub collaboration mission
352b353 Add My Learning section on update-about branch
e80d7c4 Mission 5: Build number converter and practise data representation
cf49b07 Mission 4: Compare compilers and interpreters
eb8d15c Mission 3: Document operating system and file management
d2d79ab Mission 2: Complete Terminal and file management mission
e0c1cb5 Mission 1: Complete computer basics and IPOS mission
c056ffa Mission 0: Set up Digital Detective mission structure
```

---

## 6. Difficulties Faced & Final Resolutions

| Mission | Challenge Faced | How I Resolved It |
| :--- | :--- | :--- |
| **Mission 0** | Setting up a clean, multi-folder structure matching exact naming guidelines. | Used `mkdir -p` with brace expansion to create the exact skeleton specified in the PDF. |
| **Mission 1** | Distinguishing between Application Software and Utility Software. | Identified the beneficiary: Applications serve user tasks (writing documents, web browsing), while Utilities maintain and protect the computer (Disk Utility, Time Machine). |
| **Mission 2** | Remembering the difference between `>` and `>>`. | Established the rule: `>` overwrites and erases existing file contents, while `>>` safely appends new lines to the bottom. |
| **Mission 3** | Understanding why `top` reported over 790 processes running when only a few apps were open. | Discovered that modern operating systems run hundreds of headless background daemons and system services to manage hardware, security, and display compositing. |
| **Mission 4** | Classifying Python when it produces `.pyc` bytecode files. | Learned that Python uses a hybrid approach (compiles to bytecode, which is then interpreted by the Python Virtual Machine at runtime). |
| **Mission 5** | Converting multi-digit hexadecimal numbers like `1F` without confusion. | Broke down each digit by its power of 16 ($1 \times 16^1 + 15 \times 16^0 = 16 + 15 = 31$) and verified in Python via `int('1F', 16)`. |
| **Mission 6** | Publishing a newly created branch so it tracks upstream on GitHub. | Used `git push -u origin update-about` to establish upstream tracking. |
| **Mission 7** | Differentiating between a Router and a Protocol. | Clarified that a Router is physical networking hardware that forwards packets, whereas a Protocol is the software standard/rules governing data format. |

---

## 7. Master Viva Preparation Guide (All Missions 0–8)

Use this comprehensive guide to prepare for any questions your teacher or lab examiner might ask:

### Mission 0: GitHub Workspace Setup
- **Q: What is the purpose of Git and GitHub in this assignment?**
  - *Answer*: Git is a local version control system that tracks every change made to our files across history. GitHub is a cloud hosting platform where local commits are pushed, providing a public portfolio and enabling instructors to review project development.
- **Q: Why was the repository named `digital-detective-8445`?**
  - *Answer*: The assignment specification mandates naming the repository with the project title followed by the student's last 4 digits of USN (`8445`), ensuring uniqueness and easy student identification.

### Mission 1: Computer Basics & IPOS
- **Q: Explain the IPOS cycle using typing a document as an example.**
  - *Answer*: **Input**: Keystrokes on the keyboard. **Processing**: The CPU translates keystroke scan codes and manages text buffers in RAM. **Output**: The display screen renders formatted pixels for the user. **Storage**: The operating system commits the file buffer to persistent NVMe SSD memory when saved.
- **Q: What is the difference between volatile and non-volatile memory?**
  - *Answer*: Volatile memory (like RAM) requires continuous electrical power to retain data and is wiped when the computer powers off. Non-volatile memory (like an SSD or hard drive) permanently retains data even without power.

### Mission 2: Terminal & File Management
- **Q: What does the command `ls -lah` output?**
  - *Answer*: It lists files in a detailed long-listing format (`-l`), includes hidden files that start with a dot (`-a`), and prints file sizes in human-readable units like KB and MB (`-h`).
- **Q: How does a Unix pipe (`|`) work?**
  - *Answer*: A pipe redirects the standard output (stdout) of the command on the left into the standard input (stdin) of the command on the right, allowing commands to be chained together without intermediate files.

### Mission 3: Operating System & Processes
- **Q: What is a process, and what is a PID?**
  - *Answer*: A program is passive code stored on disk; a process is an active instance of that program running in RAM. A PID (Process Identifier) is a unique integer assigned by the OS kernel to monitor, manage, and schedule that process.
- **Q: Explain what the permission string `-rw-r--r--` signifies.**
  - *Answer*: The initial hyphen indicates a regular file. The first triplet (`rw-`) gives the owner read and write permissions. The second (`r--`) and third (`r--`) triplets give read-only access to group members and all other users, respectively.

### Mission 4: How Programs Run
- **Q: What is the primary difference between a compiler and an interpreter?**
  - *Answer*: A compiler converts the entire source code into native machine code beforehand, producing a standalone executable binary that runs at maximum speed. An interpreter translates and executes source code line by line at runtime without producing an independent binary file.
- **Q: Give examples of compiled versus interpreted languages.**
  - *Answer*: Compiled: C, C++, Rust, Go. Interpreted: Python, JavaScript, Ruby, PHP.

### Mission 5: Number Systems & Data
- **Q: How do you convert decimal 25 to binary manually?**
  - *Answer*: Divide 25 repeatedly by 2 and collect the remainders: $25 / 2 = 12$ (rem 1), $12 / 2 = 6$ (rem 0), $6 / 2 = 3$ (rem 0), $3 / 2 = 1$ (rem 1), $1 / 2 = 0$ (rem 1). Reading remainders from bottom to top yields $11001_2$.
- **Q: Why does the computer industry use hexadecimal?**
  - *Answer*: Binary strings are long and error-prone for humans to read. Since $16 = 2^4$, each hexadecimal digit maps directly to exactly four binary bits (a nibble), making memory addresses and byte representations compact and clear.
- **Q: What is the difference between ASCII and UTF-8?**
  - *Answer*: ASCII uses 7 bits and can only represent 128 English characters and control codes. UTF-8 is a modern, variable-width encoding that can represent over 1.1 million characters across all world languages, technical symbols, and emojis.

### Mission 6: Git & GitHub Collaboration
- **Q: What is a Git branch, and why should you use one?**
  - *Answer*: A branch is an independent timeline of development that diverges from the main branch. It allows developers to create features, experiment, or fix bugs safely without disrupting the working production code.
- **Q: What is a Pull Request (PR)?**
  - *Answer*: A Pull Request is a feature on GitHub where a developer proposes merging changes from a feature branch into the main branch, enabling teammates to review the code diff, leave feedback, and run automated checks before merging.

### Mission 7: Networking & Communication
- **Q: What happens when you type `example.com` into your web browser?**
  - *Answer*: The browser checks its cache for the IP address; if not found, it queries DNS servers to translate the domain into an IP address. The browser establishes a TCP/TLS connection with the server, sends an HTTP `GET` request packet via routers, the server responds with HTTP response packets (HTML/CSS), and the browser renders the webpage.
- **Q: What is packet switching?**
  - *Answer*: Packet switching is a networking technique where digital messages are divided into small packets that travel independently across optimal network paths and are reassembled at the receiving destination.

### Mission 8: Final Review & Submission
- **Q: How did you ensure your repository was safe for public grading?**
  - *Answer*: I audited all Terminal outputs and markdown documents to ensure private information—such as local home directory usernames, private LAN IP addresses, and Wi-Fi network names—was completely redacted.

---

## 8. Final Submission Details
- **Student Name**: Chanchal Agarwal
- **USN (Last 4 Digits)**: `8445`
- **GitHub Repository URL**: [https://github.com/chanchalagarwal3580/digital-detective-8445](https://github.com/chanchalagarwal3580/digital-detective-8445)
- **Submission Status**: All 9 missions (0 to 8) complete, verified, committed, and published to GitHub.

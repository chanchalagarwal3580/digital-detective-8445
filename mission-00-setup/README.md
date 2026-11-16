# Mission 0 — Create Your GitHub Workspace

---

## 1. Task / Objective
The objective of Mission 0 was to set up a standardized, professional local workspace for the Digital Detective assignment, verify the required programming and version control tools (Python 3 and Git), create a structured directory hierarchy covering all nine missions, document the setup, and initialize a Git repository to be published to GitHub.

---

## 2. Work Completed
- **Environment Verification**: Checked and confirmed the installed versions of Python 3 (`Python 3.9.6`), Git (`git version 2.54.0`), and Homebrew (`Homebrew 7.0.13`) using Terminal.
- **Repository Directory Creation**: Created the official project folder `digital-detective-8445` following the naming rule (`digital-detective-XXXX` where `XXXX` is the last four digits of my USN).
- **Mission Folder Structure**: Created dedicated folders for all missions (`mission-00-setup` through `mission-08-final-report`) along with an `evidence/` folder.
- **Root README**: Created a comprehensive root `README.md` that introduces the project, lists student details, provides a complete mission index with navigation links, and outlines the commit rules.
- **Git Initialization & First Commit**: Initialized the local repository using `git init`, staged the initial structure, and created the first official commit with the required message.

---

## 3. Commands / Tools Used

| Tool / Command | Purpose |
| :--- | :--- |
| `python3 --version` | Checks the installed version of Python 3 interpreter. |
| `git --version` | Checks the installed version of the Git version control system. |
| `brew --version` | Checks the installed version of the Homebrew package manager. |
| `mkdir -p <folders>` | Creates directories and subdirectories safely in one step. |
| `ls -la` | Lists all files and directories, including hidden items, with detailed file metadata. |
| `git init` | Initializes a brand-new local Git repository in the current directory. |
| `git status` | Displays the current state of the working directory and staged files. |
| `git add .` | Stages all new and modified files for the upcoming commit. |
| `git commit -m "..."` | Permanently records the staged changes into the repository history with an explanatory message. |
| `git remote add origin <URL>` | Connects the local repository to the remote GitHub repository. |
| `git push -u origin main` | Uploads local commits to the main branch on GitHub and sets up tracking. |

---

## 4. My Understanding

### What is a Git Repository?
A Git repository is a tracked workspace. Unlike a regular computer folder where editing or deleting a file permanently replaces the previous version, a Git repository maintains a complete ledger (history) of changes. Every time we take a snapshot by making a "commit", Git records:
1. Exactly what lines of code or text were added, modified, or removed.
2. Who made the changes (author and email).
3. When the changes were made (timestamp).
4. A commit message explaining *why* the changes were made.

### Local vs. Remote Repository
- **Local Repository**: Lives physically on my computer's storage drive. I can create files, modify code, and make commits offline.
- **Remote Repository**: Stored in the cloud on GitHub (`https://github.com/Chanchal3580/digital-detective-8445`). It acts as a secure backup, a public portfolio, and a central platform for instructors or teammates to review the work.

### Why Organize the Repository by Mission?
Structuring the project with dedicated folders (`mission-00-setup`, `mission-01-computer-basics`, etc.) makes the project modular, clean, and professional. An evaluator can easily navigate to any specific topic, verify its README documentation, run the associated code, and view the supporting evidence without any clutter.

---

## 5. Difficulties Faced
- Ensuring that no mission files were placed loose in the root folder, and keeping all mission-specific documentation neatly contained inside its designated folder.

---

## 6. How I Resolved Them
- Carefully followed the directory layout specified in the assignment PDF (Page 3) and used `mkdir -p` to establish the exact folder hierarchy before adding any content.

---

## 7. Evidence / Files

The following folder structure was generated:
```
digital-detective-8445/
├── README.md
├── mission-00-setup/
│   └── README.md
├── mission-01-computer-basics/
│   └── README.md
├── mission-02-terminal/
│   └── README.md
├── mission-03-operating-system/
│   └── README.md
├── mission-04-programs/
│   └── README.md
├── mission-05-numbers-data/
│   └── README.md
├── mission-06-git-github/
│   └── README.md
├── mission-07-networking/
│   └── README.md
├── mission-08-final-report/
│   └── README.md
└── evidence/
```

- Local verified environment outputs:
  - Python 3 version: `Python 3.9.6`
  - Git version: `git version 2.54.0`
  - Homebrew version: `Homebrew 7.0.13`

---

## 8. Commit Details
- **Commit Message**: `Mission 0: Set up Digital Detective mission structure`
- **Target Branch**: `main`
- **Remote Repository**: `https://github.com/chanchalagarwal3580/digital-detective-8445`

---

## How to Explain This Mission to My Teacher

### 1. What was the objective?
"The objective of Mission 0 was to set up my project workspace for the entire assignment, verify that my laptop has Python 3 and Git installed, create an organized folder structure for Missions 0 through 8, and initialize Git version control to publish it on GitHub."

### 2. What practical work did I perform?
"I opened Terminal, verified my Python version (`3.9.6`) and Git version (`2.54.0`), created my project folder named `digital-detective-8445` using the last four digits of my USN, created folders for all nine missions plus an evidence folder, wrote the root `README.md` and Mission 0 README, initialized the repository with `git init`, and created my first commit."

### 3. Which commands or tools did I use?
"I used Terminal on macOS, `python3 --version` and `git --version` to check tools, `mkdir -p` to build the directory tree, `ls -la` to inspect file listings, and Git commands (`git init`, `git status`, `git add`, `git commit`, `git remote add`, and `git push`)."

### 4. What did I learn?
"I learned what a Git repository is, how local repositories differ from remote repositories on GitHub, and why structuring code cleanly by mission is important for reproducibility and grading."

### 5. What was the most important observation?
"The most important observation was seeing how Git initializes a hidden `.git` folder that turns a standard directory into a version-controlled tracking system."

### 6. Five Possible Questions My Teacher Might Ask & Simple Answers

**Q1: What does the command `git init` do?**
> **Answer**: `git init` creates a new, empty Git repository by generating a hidden `.git` directory inside the project folder. This folder allows Git to track file changes, branches, and commit history.

**Q2: What is the difference between your local repository and GitHub?**
> **Answer**: The local repository exists on my computer's physical drive and works offline. GitHub is a remote cloud hosting service where I push my local commits so others can view and review my code.

**Q3: Why did you name your repository `digital-detective-8445`?**
> **Answer**: The assignment guidelines require naming the repository using the assignment title followed by a hyphen and the student's last four digits of USN (`digital-detective-XXXX`), which for my USN is `8445`.

**Q4: What does the `-p` flag do in the command `mkdir -p`?**
> **Answer**: The `-p` flag stands for 'parents'. It creates any missing parent directories automatically and prevents errors if the target directory already exists.

**Q5: Why is it important to create separate folders for each mission instead of putting everything in the root directory?**
> **Answer**: Having separate folders keeps the codebase organized, modular, and easy to navigate. Each mission has its own documentation, code, and evidence without colliding with other missions.

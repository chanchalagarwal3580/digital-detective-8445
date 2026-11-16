# Mission 6 — Git and GitHub

---

## 1. Task / Objective
The objective of Mission 6 was to understand professional version control principles, practice collaborative branching workflows, and master the interaction between local Git repositories and GitHub. This included:
1. Documenting the foundational Git workflow (working directory, staging area, repository history).
2. Creating an isolated feature branch named `update-about`.
3. Updating the root `README.md` with a "My Learning" reflection on the branch, committing it, and publishing the branch to GitHub.
4. Opening and reviewing a Pull Request (PR) from `update-about` into `main`.
5. Compiling a comprehensive one-line Git command glossary covering all primary operations.

---

## 2. Work Completed
- **Inspected Working Tree**: Analyzed differences between unstaged, staged, and committed states using `git status` and `git diff`.
- **Created & Switched Branch**: Created the feature branch `update-about` using `git checkout -b update-about`.
- **Branch Development**: Enhanced the root `README.md` by adding a structured "My Learning" section highlighting mastery of Terminal commands, OS process monitoring, and number systems.
- **Published Feature Branch**: Committed the modifications on `update-about` (`352b353`) and pushed the branch to GitHub (`git push -u origin update-about`).
- **Pull Request Lifecycle**: Formulated the PR process comparing `update-about` against `main` on GitHub: [PR Creation Link](https://github.com/chanchalagarwal3580/digital-detective-8445/pull/new/update-about).
- **Git Glossary Compilation**: Authored a clear, student-level glossary defining 9 core Git operations.
- **Viva Preparation**: Prepared 5 teacher viva questions and answers covering Git branches, merge conflicts, staging vs committing, and PR reviews.

---

## 3. Commands / Tools Used

| Command | Purpose |
| :--- | :--- |
| `git status` | Displays working tree status, modified files, and staged changes. |
| `git add <file>` | Moves changes from working directory to the Git staging index. |
| `git commit -m "..."` | Records staged snapshot into the permanent repository commit history. |
| `git log --oneline` | Displays a condensed history of recent commits. |
| `git checkout -b <branch>` | Creates a new branch and immediately switches the working tree to it. |
| `git branch` | Lists all local branches and marks the active branch with an asterisk (`*`). |
| `git push -u origin <branch>` | Pushes the local branch to GitHub and configures remote upstream tracking. |
| `git switch <branch>` | Switches between existing branches safely. |
| `git pull` | Fetches and integrates remote changes from GitHub into the current local branch. |

---

## 4. My Understanding

### Task 6.1 — The Basic Git Workflow Table

| Git Operation | What It Does (In My Own Words) |
| :--- | :--- |
| **Check repository status (`git status`)** | Shows which files have been modified, which are staged for the next commit, and which are untracked by Git. |
| **Stage selected changes (`git add <file>`)** | Places specific modified files into the "staging area", preparing them to be part of the next official snapshot. |
| **Create a commit (`git commit -m "..."`)** | Permanently records the staged changes into the project history with a descriptive message explaining what was done. |
| **View commit history (`git log`)** | Displays the chronological timeline of past commits, showing commit hashes, authors, timestamps, and messages. |

#### Difference Between Staging a Change and Committing It:
- **Staging (`git add`)**: Staging is like placing items into a shipping box. You can selectively choose which file modifications belong together in a logical group, review them, and make further changes before finalizing.
- **Committing (`git commit`)**: Committing is sealing the box and stamping it with a permanent tracking number. It creates an indelible, cryptographic checkpoint in project history that you can always return to or inspect later.

---

### Task 6.2 — Creating and Using a Feature Branch

We branched off `main` to safely add a new section without risking the stability of our primary branch:

```bash
# Create and switch to new branch
$ git checkout -b update-about
Switched to a new branch 'update-about'

# Verify active branch
$ git branch
  main
* update-about
```

#### Modifications Made to `README.md`:
Added the section **"## My Learning"**, summarizing three major educational takeaways:
1. *Command-Line Precision & Safe File Operations*: Navigating directories, manipulating file streams with `>` vs `>>`, and piping (`|`).
2. *Operating System Resource & Process Management*: Inspecting background daemons, understanding PIDs, and decoding POSIX file permissions (`r-w-x`).
3. *Data Representation & Number Systems*: Converting bases (Base 2, 10, 16) and understanding ASCII/UTF-8 text encoding.

#### Commit and Remote Push:
```bash
$ git add README.md
$ git commit -m "Add My Learning section on update-about branch"
$ git push -u origin update-about
```
- Remote branch published: `https://github.com/chanchalagarwal3580/digital-detective-8445/tree/update-about`

---

### Task 6.3 — Pull Requests & Team Collaboration

#### What is a Branch?
A **branch** is an independent, parallel line of development. It allows a developer to build a feature, test experimental code, or fix a bug in complete isolation without disrupting the main codebase (`main`). If the experiment fails, the branch can simply be discarded without harming the production code.

#### What is a Pull Request (PR)?
A **Pull Request (PR)** is a formal proposal on GitHub to merge code from one branch (e.g. `update-about`) into another (e.g. `main`). It provides:
1. **Visual Code Diff**: Side-by-side green (additions) and red (deletions) highlighting every line changed.
2. **Peer Review & Discussion**: Allows teammates or teachers to comment on code quality, request adjustments, and verify tests.
3. **Approval & Merge Gate**: Ensures code is reviewed and approved before becoming part of the main branch.

#### Pull Request Lifecycle for This Project:
1. **Compare & Open**: Navigated to GitHub PR interface: `https://github.com/chanchalagarwal3580/digital-detective-8445/pull/new/update-about`.
2. **Review**: Confirmed the diff strictly contained the 20 lines added for "My Learning".
3. **Merge Action**: Once reviewed and approved, merging completes the integration into `main`. The local working directory is then synchronized using:
   ```bash
   git switch main
   git pull origin main
   ```

---

### Task 6.4 — Git Command Glossary

| Git Operation | One-Line Explanation (In My Own Words) |
| :--- | :--- |
| **Initialise a repository (`git init`)** | Creates a new, empty Git repository and starts tracking changes in the current directory. |
| **Check status (`git status`)** | Shows which files are modified, untracked, or ready to be committed. |
| **Stage changes (`git add`)** | Selects and stages modified files into the preparation area for the next commit. |
| **Commit changes (`git commit`)** | Saves the staged changes permanently into the project's historical timeline with an explanatory message. |
| **View history (`git log`)** | Lists the chronological log of all previous commits made in the repository. |
| **Create or list branches (`git branch`)** | Lists all local branches or creates a new parallel branch when given a name. |
| **Switch branches (`git switch` / `git checkout`)** | Changes your active working environment from one branch to another. |
| **Publish changes (`git push`)** | Uploads local branch commits to the remote repository on GitHub. |
| **Retrieve remote changes (`git pull`)** | Downloads and integrates the latest commits from GitHub into your current local branch. |

---

## 5. Difficulties Faced
- Remembering to publish the newly created local branch to GitHub using `-u origin <branch>` instead of a plain `git push`.

---

## 6. How I Resolved Them
- Used `git push -u origin update-about`, where the `-u` (upstream) flag links the local branch to the remote branch on GitHub, allowing future pushes with a simple `git push`.

---

## 7. Evidence / Files
- Active branch on GitHub: `update-about`
- Updated root documentation: `README.md`
- Documentation: `mission-06-git-github/README.md`
- PR reference: [https://github.com/chanchalagarwal3580/digital-detective-8445/pull/new/update-about](https://github.com/chanchalagarwal3580/digital-detective-8445/pull/new/update-about)

---

## 8. Commit Details
- **Branch Commit**: `352b353` – *"Add My Learning section on update-about branch"*
- **Target Main Commit Message**: `Mission 6: Complete Git and GitHub collaboration mission`
- **Pushed to GitHub**: Yes (Both on `update-about` and `main`)

---

## How to Explain This Mission to My Teacher

### 1. What was the objective?
"The objective of Mission 6 was to understand collaborative version control: learning how the Git staging area works, creating an isolated feature branch (`update-about`), updating our project overview, publishing the branch to GitHub, and practicing the Pull Request review workflow."

### 2. What practical work did I perform?
"I used `git checkout -b update-about` to branch off main, updated the root `README.md` with my learning reflections, committed the changes on the branch, pushed the branch to GitHub, documented the Pull Request process, and created a 9-command Git glossary."

### 3. Which commands or tools did I use?
"I used `git status`, `git add`, `git commit`, `git checkout -b`, `git branch`, `git push -u origin`, `git switch`, and the GitHub web interface for Pull Requests."

### 4. What did I learn?
"I learned the difference between staging and committing, why development teams never push directly to main without feature branches, and how Pull Requests allow teammates to review and approve code before merging."

### 5. What was the most important observation?
"The most valuable observation was realizing how branches allow developers to work in parallel on separate features without interfering with each other's code."

### 6. Five Possible Questions My Teacher Might Ask & Simple Answers

**Q1: What is the difference between `git add` and `git commit`?**
> **Answer**: `git add` stages changes (prepares them in a staging area), whereas `git commit` permanently saves that staged snapshot into the project's historical timeline.

**Q2: Why do software developers use branches?**
> **Answer**: Branches allow developers to create isolated workspaces where they can build features, test ideas, or fix bugs without risking the stability of the main production codebase (`main`).

**Q3: What is a Pull Request (PR)?**
> **Answer**: A Pull Request is a feature on platforms like GitHub that lets a developer notify teammates that their branch is ready to be merged into another branch. It provides a visual diff and discussion forum for code review.

**Q4: What does `git push -u origin <branch>` do?**
> **Answer**: It uploads the local branch commits to the remote GitHub repository and configures tracking (upstream) so Git knows which remote branch to link to in future pushes.

**Q5: How do you bring the latest changes from GitHub into your local repository?**
> **Answer**: By running `git pull origin <branch>` (or simply `git pull` if upstream tracking is set up).

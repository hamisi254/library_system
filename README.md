 📚 Smart Library Management System (MOB)

A terminal-based **Smart Library Management System** built with **Python Object-Oriented Programming (OOP)**. Designed to manage books, members, and borrowing/returning transactions efficiently with persistent data storage.

**MOB** — *Modern, Organized, and Book-focused Library System*

---
<img width="1170" height="759" alt="Image" src="https://github.com/user-attachments/assets/baa7018c-668c-4313-a3fa-166a5ba80279" />

## ✅ Features

- **Core OOP Implementation**  
  Uses `Book`, `Member`, and `Library` classes with full encapsulation, methods, and relationships.
  
- **Persistent Data Storage**  
  Saves and loads books, members, and transaction history using `books.txt`, `members.txt`, and `transactions.txt` (JSON format).

- **Interactive Menu System**  
  Clean, user-friendly terminal interface with numbered options.

- **Smart Borrow/Return Flow**  
  - When returning, users see a numbered list of their borrowed books.
  - Input validation prevents errors (e.g., returning un-borrowed books).

- **Bonus Features**  
  - 🔍 Search books by author  
  - 🏆 Track and display the **most borrowed book**  
  - 📜 Transaction history logging  
  - ⏳ Loading animations for borrow/return actions  
  - 🎉 Custom **MOB-themed welcome screen**

- **Error Handling**  
  Gracefully handles invalid inputs, missing members/books, and logic errors.

---

## 🛠️ How to Run

**Step 1: Install Python (if not already installed)**
Go to https://www.python.org/downloads/
Download Python 3.7 or newer for your operating system (Windows, macOS, or Linux)
Run the installer and check "Add Python to PATH" during installation (important on Windows!)

**Step 2: Get the Project Files**
You can either:

**Option A: Download as ZIP**
On GitHub, click the green "Code" button
Click "Download ZIP"
Extract the ZIP file to a folder (e.g., smart-library-system)
Option B: Clone with Git (if you have Git installed)
bash

git clone https://github.com/hamisi254/smart-library-system.git
cd smart-library-system

**Step 3: Open the Project Folder**
Navigate to the folder containing these files:
library_system.py
models.py
(The .txt files will be created automatically on first run)
Step 4: Run the Program

On Windows:
Open Command Prompt or PowerShell
Use cd to go to your project folder
<img width="1104" height="168" alt="Image" src="https://github.com/user-attachments/assets/544fc9db-be2b-4998-84e9-4d00d0d44bb8" />

python library_system.py
On macOS or Linux:
Open Terminal
Navigate to the project folder
Example: cd ~/Downloads/smart-library-system

python3 library_system.py

<img width="1887" height="1005" alt="Image" src="https://github.com/user-attachments/assets/d971d274-f1fb-4f74-9680-3e2a30d141a1" />
<img width="1379" height="358" alt="Image" src="https://github.com/user-attachments/assets/c4051eb5-51e8-4476-a92f-72ae22a93d9b" />

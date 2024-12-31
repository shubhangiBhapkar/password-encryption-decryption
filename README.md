# 🔒 Password Encryption and Decryption
## 📋 Project Overview

**The Password Encryption and Decryption** is a secure application designed to encrypt and decrypt passwords using advanced cryptographic techniques. It allows users to manage their credentials securely, offering features like password encryption, decryption, storage, and retrieval through a user-friendly interface.
This project showcases best practices in Python development and serves as a comprehensive learning experience for individuals interested in cybersecurity and cryptography.

## 📝 Planning and Development Documentation
### 1. Goals and Objectives
The main goal is to provide a secure platform for managing sensitive credentials and Key Objectives are :
- Securely encrypt passwords using AES encryption.
- Allow users to decrypt and access stored passwords when necessary.
- Provide file-based storage for managing passwords.
- Ensure scalability for future enhancements like multi-user support.
 ### 2. Target Audience
- **General Users:** Individuals who want to securely manage their passwords.
- **Students and Developers:** Learners interested in understanding Python-based encryption techniques and file management.
 ### 3. Development Platform
- **Programming Language**: Python 3.6 or later.
- **Libraries Used**:
 cryptography for encryption and decryption.  
 unittest for testing the codebase.

## 🛠️ Features
**1. Encryption:** Encrypts passwords using the cryptography library's AES implementation.  
**2. Decryption:** Decrypts passwords securely upon user authentication.  
**3. File-Based Storage:** Stores encrypted passwords in a text file for persistence.  
**4. User-Friendly Interface:** Simple command-line interface for password management.  
**5. Secure Key Management:** Automatically generates and stores a secure encryption key.  


## Name of Team Members
 1.Bhapkar Shubhangi Sambhaji  
 2.Kore Shubhangi Chandrakant  
 3.Hase Chaitanya  
 4.Dighe Suyog Ashok  
 

## 📌 Project Phases
**1.Planning and Requirements Analysis:**
- Description: This phase involves identifying the project’s primary goals and objectives, understanding the needs of the target audience, and selecting the appropriate tools and libraries for development. It 
  establishes the foundation for the project’s success by clearly defining its scope and purpose.
  
 **2.Design:**
- Description: The design phase focuses on planning the application’s core features and functionalities, such as encryption, decryption, and storage mechanisms. It also includes designing the user interface (UI) 
  and determining the flow of the command-line interface (CLI) for user interaction.
  
 **3.Implementation:**
- Description: This phase involves writing the code for the PasswordManager class and implementing functionalities like encryption, decryption, key management, and file-based storage. Error handling mechanisms 
  are also integrated to enhance reliability.
  
 **4.Testing:**
- Description: During this phase, unit testing is performed to validate the functionality of encryption, decryption, and storage operations. The application is tested against various edge cases to ensure 
  robustness and accuracy.
  
 **5.Documentation:**  
- Description: Comprehensive documentation is created to detail the project’s features, setup instructions, usage guidelines, and potential enhancements. This phase ensures that the project is well-documented for 
  future reference or sharing with others.
  
 **6.Deployment:**
- Description: In this phase, the project is packaged for distribution, making it accessible for users. Clear installation and usage guidelines are provided to simplify deployment and usage.
  

##  Requirements for the Password Encryption Decryption
**1.Software Requirements:**
- Operating System: Any system with Python 3.6 or later installed (Windows, macOS, Linux).
- Python Version: Python 3.6 or higher.
- Libraries: Install the cryptography library for encryption and unittest for testing

**2.Hardware Requirements:**
- Minimum 4 GB RAM for running Python scripts and testing.
- At least 500 MB of free storage space to manage project files and logs.

**3.Functional Requirements:**
- Ability to securely encrypt and decrypt passwords.
- Store encrypted passwords in a file (passwords.txt).
- Retrieve and display decrypted passwords as needed.
- Generate and store an encryption key in a secure file (key.key).

**4.Development Requirements:**
- Development Environment: Any code editor like VSCode, PyCharm, or a text editor like Sublime Text.
- Testing Tools: Use unittest for validating the code functionalities.
  
**5.User Requirements:**
- Basic understanding of running Python scripts.
- Ability to install required libraries using pip.

## 🚀 Getting Started
### Steps to Run the Project
**1.Clone the Repository**  

 > This is a blockquote.https://github.com/shubhangiBhapkar/password-encryption-decryption.git

**2. Navigate to the Project Directory**

   cd password-manager
**3.Install Dependencies**
 Ensure Python 3.6 or later is installed on your system.
 Install the required library:

  pip install cryptography

**4.Run the Application**
  Start the Password Manager by running the main script:

   python manager.py
   
**5.Follow the Prompts**
  The application will guide you to add, retrieve, or manage passwords through a simple command-line interface.












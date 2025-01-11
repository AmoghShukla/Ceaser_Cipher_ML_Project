# Ceaser_Cipher_ML_Project

**Project Description: Caesar Cipher Dataset Generator**

The Caesar Cipher Dataset Generator is a Python-based project designed to create synthetic datasets for machine learning and cryptography research. The project generates random text samples, encrypts them using the Caesar cipher algorithm with random shifts, and saves the data in a structured CSV file. This dataset can be used for educational purposes, training models to predict cipher shifts, or exploring cryptographic techniques.

The Caesar cipher is a simple substitution cipher that shifts each letter in the plaintext by a fixed number of positions in the alphabet. This project automates the encryption process and provides labeled data for analysis or machine learning tasks.

**Key Features:-**
• Random Text Generation: Creates text samples with varying lengths, including uppercase, lowercase letters, and spaces.
• Encryption with Caesar Cipher: Encrypts each sample using a random shift value (1–25).
• Dataset Creation: Saves the encrypted text and corresponding shift values into a CSV file for further analysis.
•Scalability: Easily configurable to generate datasets of any size.

**Goals of the Project:-**
Provide a tool to generate datasets for cryptography and machine learning research.
Offer a practical demonstration of the Caesar cipher encryption algorithm.
Enable training of machine learning models to predict cipher shifts or decrypt text.
Simplify the creation of labeled datasets for educational and research purposes.

---

**Features**

- Generate random text samples.
- Encrypt the text using a Caesar cipher with a random shift.
- Save the dataset as a CSV file.

---

**Installation**

1. Clone the repository:
   
   git clone https://github.com/amoghshukla/CaesarCipherProject.git
   cd CaesarCipherProject

2. Install dependencies:
   
  pip install -r requirements.txt

3. Usage

  To generate a dataset with 5000 samples, run the following command:
  
  python caesar_cipher.py

  (The dataset will be saved to the dataset/ folder as caesar_cipher_dataset.csv)

4. Project Structure

   CaesarCipherProject/
   
      │
   
      ├── caesar_cipher.py        # Main script
   
      ├── requirements.txt        # Python dependencies
   
      ├── README.md               # Project documentation
   
      ├── .gitignore              # Files to ignore in the repository
   
      └── dataset/                # Folder for generated datasets
   
          ├── caesar_cipher_dataset.csv
   

6. How It Works:-
   
  Generate Random Text: The program creates random text samples containing letters (uppercase and lowercase) and spaces.
  Apply Caesar Cipher: Each sample is encrypted using a Caesar cipher with a random shift between 1 and 25.
  Save Dataset: The encrypted text and corresponding shift values are saved in a CSV file.

6. Contributions

  Contributions are welcome! If you have any suggestions, feel free to open an issue or submit a pull request.

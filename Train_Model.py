import random
import string
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def load_corpus(num_samples, filename="caesar_cipher_ds.csv"):
    with open(filename, "r") as file:
        lines = file.readlines()
    samples = random.choices(lines, k=num_samples)
    return [line.strip()[:random.randint(10, 50)] for line in samples]

def generate_caesar_dataset(num_samples):
    plain_texts = load_corpus(num_samples)
    dataset = []
    for text in plain_texts:
        shift = random.randint(1, 25)
        encrypted_text = caesar_cipher_encrypt(text, shift)
        dataset.append((encrypted_text, shift))
    return dataset

def extract_features(text):
    char_freq = [0] * 26
    for char in text:
        if char.isalpha():
            char_freq[ord(char.lower()) - ord('a')] += 1
    total_chars = sum(char_freq)
    char_freq = [freq / total_chars if total_chars > 0 else 0 for freq in char_freq]
    return char_freq

def save_dataset_to_csv(filename, num_samples):
    dataset = generate_caesar_dataset(num_samples)
    df = pd.DataFrame(dataset, columns=['EncryptedText', 'Shift'])
    df.to_csv(filename, index=False)
    print(f"Dataset saved to {filename}")

def load_and_preprocess_dataset(filename):
    df = pd.read_csv(filename)
    X = df['EncryptedText'].apply(extract_features).tolist()
    y = df['Shift'].tolist()
    return np.array(X), np.array(y)

def train_and_save_model(dataset_file, model_file="model.pkl"):
    X, y = load_and_preprocess_dataset(dataset_file)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=200, max_depth=15, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    with open(model_file, "wb") as file:
        pickle.dump(model, file)
    print(f"Model saved to {model_file}")

if __name__ == "__main__":
    save_dataset_to_csv("caesar_cipher_dataset.csv", 5000)
    train_and_save_model("caesar_cipher_dataset.csv")

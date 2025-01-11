import random
import string
import pandas as pd

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep spaces and punctuation unchanged
    return result

# Generate random text samples (you can customize this with a larger corpus)
def generate_random_text(num_samples, max_length=50):
    samples = []
    for _ in range(num_samples):
        length = random.randint(10, max_length)
        text = ''.join(random.choices(string.ascii_letters + ' ', k=length))
        samples.append(text)
    return samples

# Generate dataset with random shifts
def generate_caesar_dataset(num_samples):
    plain_texts = generate_random_text(num_samples)
    dataset = []
    for text in plain_texts:
        shift = random.randint(1, 25)  # Shifts from 1 to 25
        encrypted_text = caesar_cipher_encrypt(text, shift)
        dataset.append((encrypted_text, shift))
    return dataset

# Create dataset and save it to a CSV file
def save_dataset_to_csv(filename, num_samples):
    dataset = generate_caesar_dataset(num_samples)
    df = pd.DataFrame(dataset, columns=['EncryptedText', 'Shift'])
    df.to_csv(filename, index=False)
    print(f"Dataset saved to {filename}")

# Generate and save a dataset of 5000 samples
save_dataset_to_csv("caesar_cipher_dataset.csv", 5000)
import string

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def extract_features(text):
    char_freq = [0] * 26
    for char in text:
        if char.isalpha():
            char_freq[ord(char.lower()) - ord('a')] += 1
    total_chars = sum(char_freq)
    char_freq = [freq / total_chars if total_chars > 0 else 0 for freq in char_freq]
    return char_freq

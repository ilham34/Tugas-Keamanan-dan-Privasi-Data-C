import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Vigenere Cipher")

root.geometry("400x300")

def encrypt(plain_text, key):
    cipher_text = ""
    key_len = len(key)
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            key_char = key[key_index].upper()
            shift = ord(key_char) - 65

            if char.isupper():
                cipher_char = chr((ord(char) + shift - 65) % 26 + 65)
            else:
                cipher_char = chr((ord(char) + shift - 97) % 26 + 97)

            key_index = (key_index + 1) % key_len
        else:
            cipher_char = char

        cipher_text += cipher_char

    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    key_len = len(key)
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            key_char = key[key_index].upper()
            shift = ord(key_char) - 65

            if char.isupper():
                plain_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plain_char = chr((ord(char) - shift - 97) % 26 + 97)

            key_index = (key_index + 1) % key_len
        else:
            plain_char = char

        plain_text += plain_char

    return plain_text

def showPlainText():
    ciphertext = ciphertext_entry.get().upper()
    key = "265"
    plaintext = decrypt(ciphertext, key)
    plaintext_entry.delete(0, tk.END)
    plaintext_entry.insert(0, plaintext)

def showCipherText():
    plaintext = plaintext_entry.get().upper()
    key = "265"
    ciphertext = encrypt(plaintext, key)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, ciphertext)

plaintext_label = ttk.Label(root, text="Plaintext:")
plaintext_label.pack()
plaintext_entry = ttk.Entry(root)
plaintext_entry.pack()

ciphertext_label = ttk.Label(root, text="Ciphertext:")
ciphertext_label.pack()
ciphertext_entry = ttk.Entry(root)
ciphertext_entry.pack()

encrypt_button = ttk.Button(root, text="Encrypt", command=showCipherText)
encrypt_button.pack(pady=10)
decrypt_button = ttk.Button(root, text="Decrypt", command=showPlainText)
decrypt_button.pack()

window.resizable(width=False, height=False)

root.mainloop()
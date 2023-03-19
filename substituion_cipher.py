import tkinter as tk
import random

def generate_key():
    chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(chars)
    key = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", chars))
    return key


def encrypt(plain_text, key):
    cipher_text = ""

    for char in plain_text.upper():
        if char.isalpha():
            cipher_char = key[char]
        else:
            cipher_char = char

        cipher_text += cipher_char

    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""

    for char in cipher_text.upper():
        if char.isalpha():
            for k, v in key.items():
                if v == char:
                    plain_char = k
                    break
        else:
            plain_char = char

        plain_text += plain_char

    return plain_text

key = generate_key()

def encrypt_text():
    plain_text = input_box.get()
    cipher_text = encrypt(plain_text, key)
    output_box.delete(0, tk.END)
    output_box.insert(0, cipher_text)

def decrypt_text():
    cipher_text = input_box.get()
    plain_text = decrypt(cipher_text, key)
    output_box.delete(0, tk.END)
    output_box.insert(0, plain_text)

window = tk.Tk()
window.title("Substitution Cipher")
window.geometry("350x150")

input_label = tk.Label(text="Input Text:")
input_label.pack()
input_box = tk.Entry(width=30)
input_box.pack()

encrypt_button = tk.Button(text="Encrypt", command=encrypt_text)
encrypt_button.pack()

decrypt_button = tk.Button(text="Decrypt", command=decrypt_text)
decrypt_button.pack()

output_label = tk.Label(text="Output Text:")
output_label.pack()
output_box = tk.Entry(width=30)
output_box.pack()

window.resizable(width=False, height=False)

window.mainloop()
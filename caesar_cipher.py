import tkinter as tk

def shift_cipher_encrypt(plain_text, shift):
    cipher_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char == " ":
            cipher_text += char
        elif (char.isupper()):
            cipher_text += chr((ord(char) + shift-65) % 26 + 65)
        else:
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
    return cipher_text

def shift_cipher_decrypt(cipher_text, shift):
    plain_text=""
    for char in cipher_text:
        if char == " ":
            plain_text += char
        elif char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
    return plain_text

def encrypt_text():
    plain_text = input_box.get()
    # shift = int(shift_box.get())
    shift = 65
    cipher_text = shift_cipher_encrypt(plain_text, shift)
    output_box.delete(0, tk.END)
    output_box.insert(0, cipher_text)

def decrypt_text():
    cipher_text = input_box.get()
    shift = 65
    plain_text = shift_cipher_decrypt(cipher_text, shift)
    output_box.delete(0, tk.END)
    output_box.insert(0, plain_text)

window = tk.Tk()
window.title("Shift Cipher Encryptor/Decryptor")
window.geometry("450x450")

shift_label = tk.Label(text="Berikut merupakan program decrypter dan encrypter")
shift_label2 = tk.Label(text="yang menggunakan algoritma shift cipher dengan shift sebanyak 65")
shift_label.pack()
shift_label2.pack()

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
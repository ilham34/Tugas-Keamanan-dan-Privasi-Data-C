import tkinter as tk

import math
  
def encryptMessage(msg, key):
    cipher = ""
  
    k_indx = 0
  
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
  
    col = len(key)
      
    row = int(math.ceil(msg_len / col))
  
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
  
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
  
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] 
                          for row in matrix])
        k_indx += 1
  
    return cipher
  
def decryptMessage(cipher, key):
    msg = ""
  
    k_indx = 0
  
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
  
    col = len(key)
      
    row = int(math.ceil(msg_len / col))
  
    key_lst = sorted(list(key))
  
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
  
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
  
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
  
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
  
    null_count = msg.count('_')
  
    if null_count > 0:
        return msg[: -null_count]
  
    return msg

key = "HACK"

def encrypt_text():
    plain_text = input_box.get()
    cipher_text = encryptMessage(plain_text, key)
    output_box.delete(0, tk.END)
    output_box.insert(0, cipher_text)

def decrypt_text():
    cipher_text = input_box.get()
    plain_text = decryptMessage(cipher_text, key)
    output_box.delete(0, tk.END)
    output_box.insert(0, plain_text)

window = tk.Tk()
window.title("Transposition Cipher")
window.geometry("350x150")

input_label = tk.Label(text="Input Text:")
input_label.grid(row=2, column=0)
input_box = tk.Entry(width=30)
input_box.grid(row=2, column=1)

encrypt_button = tk.Button(text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=3, column=1, sticky="w")

decrypt_button = tk.Button(text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=3, column=1, sticky="e")

output_label = tk.Label(text="Output Text:")
output_label.grid(row=4, column=0)
output_box = tk.Entry(width=30)
output_box.grid(row=4, column=1)

window.resizable(width=False, height=False)

window.mainloop()
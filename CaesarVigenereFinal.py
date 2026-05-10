import tkinter as tk
from tkinter import filedialog, messagebox



def caesar_encrypt(text, key):
    result = ""
    key = int(key)

    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char

    return result


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -int(key))



def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char

    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char

    return result



def browse_input():
    path = filedialog.askopenfilename()
    input_path.delete(0, tk.END)
    input_path.insert(0, path)


def browse_output():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    output_path.delete(0, tk.END)
    output_path.insert(0, path)



def validate_inputs():
    key = key_entry.get()
    algorithm = algorithm_var.get()

    if not input_path.get() or not output_path.get():
        messagebox.showerror("Error", "Zgjidh fajllin hyrës dhe dalës!")
        return False

    if algorithm == "Caesar":
        if not key.isdigit():
            messagebox.showerror("Error", "Key për Caesar duhet të jetë numër!")
            return False

    elif algorithm == "Vigenere":
        if not key.isalpha():
            messagebox.showerror("Error", "Key për Vigenere duhet të jetë tekst!")
            return False

    return True



def encrypt_file():
    process("Encrypt")


def decrypt_file():
    process("Decrypt")


def process(mode):
    if not validate_inputs():
        return

    try:
        algorithm = algorithm_var.get()
        key = key_entry.get()

        with open(input_path.get(), "r", encoding="utf-8") as f:
            text = f.read()

        if algorithm == "Caesar":
            result = caesar_encrypt(text, key) if mode == "Encrypt" else caesar_decrypt(text, key)

        elif algorithm == "Vigenere":
            result = vigenere_encrypt(text, key) if mode == "Encrypt" else vigenere_decrypt(text, key)

        with open(output_path.get(), "w", encoding="utf-8") as f:
            f.write(result)

        messagebox.showinfo("Success", f"{mode} u krye me sukses!")

    except Exception as e:
        messagebox.showerror("Error", str(e))



def save_textbox_to_file():
    text = text_box.get("1.0", tk.END)

    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
        messagebox.showinfo("Saved", "Teksti u ruajt me sukses!")



root = tk.Tk()
root.title("Encryption / Decryption App")
root.geometry("600x550")

tk.Label(root, text="Zgjedh Algoritmin:", font=("Arial", 12)).pack()
algorithm_var = tk.StringVar(value="Caesar")
tk.OptionMenu(root, algorithm_var, "Caesar", "Vigenere").pack(pady=5)

tk.Label(root, text="Key:", font=("Arial", 12)).pack()
key_entry = tk.Entry(root, width=30)
key_entry.pack(pady=5)

tk.Label(root, text="Input File:", font=("Arial", 12)).pack()
input_path = tk.Entry(root, width=50)
input_path.pack()
tk.Button(root, text="Browse Input", command=browse_input).pack(pady=5)

tk.Label(root, text="Output File:", font=("Arial", 12)).pack()
output_path = tk.Entry(root, width=50)
output_path.pack()
tk.Button(root, text="Browse Output", command=browse_output).pack(pady=5)

tk.Button(root, text="Encrypt", command=encrypt_file, bg="lightblue", width=20).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt_file, bg="lightcoral", width=20).pack(pady=5)

tk.Label(root, text="Text (opsionale):", font=("Arial", 12)).pack(pady=5)
text_box = tk.Text(root, height=8, width=60)
text_box.pack()

tk.Button(root, text="Save TextBox to File", command=save_textbox_to_file, bg="lightgreen").pack(pady=10)

root.mainloop()
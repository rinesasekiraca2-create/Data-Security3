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




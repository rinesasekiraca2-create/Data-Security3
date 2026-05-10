root = tk.Tk()
root.title("Encryption / Decryption App")
root.geometry("600x550")

tk.Label(root, text="Zgjedh Algoritmin:").pack()
algorithm_var = tk.StringVar(value="Caesar")
tk.OptionMenu(root, algorithm_var, "Caesar", "Vigenere").pack()
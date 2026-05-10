# Zgjedh input file
def browse_input():

    path = filedialog.askopenfilename()

    input_path.delete(0, tk.END)
    input_path.insert(0, path)



# Zgjedh output file
def browse_output():

    path = filedialog.asksaveasfilename(defaultextension=".txt")

    output_path.delete(0, tk.END)
    output_path.insert(0, path)

# Kontrollon validimin e inputeve
def validate_inputs():

    key = key_entry.get()
    algorithm = algorithm_var.get()


    # Kontrollon file-at
    if not input_path.get() or not output_path.get():

        messagebox.showerror("Error", "Zgjidh fajllin hyrës dhe dalës!")
        return False
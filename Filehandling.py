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

import tkinter as tk
from tkinter import filedialog, messagebox
from encryption import xor_encrypt_decrypt, xor_decrypt, get_key_from_file
import os

# Function to handle file encryption
def encrypt_file():
    input_file = filedialog.askopenfilename(title="Select file to encrypt")
    if not input_file:
        return  # User canceled the file dialog

    output_file = filedialog.asksaveasfilename(defaultextension=".txt", title="Save encrypted file as")
    if not output_file:
        return  # User canceled the save dialog

    key_file = filedialog.askopenfilename(title="Select key file", filetypes=[("Text Files", "*.txt")])
    if not key_file:
        return  # User canceled key file selection
    
    key = get_key_from_file(key_file)  # Get the key from the selected key file
    if not key:
        return  # Handle if key reading fails

    try:
        with open(input_file, 'r') as f:
            text = f.read()
        
        # Encrypt the text using XOR encryption
        encrypted_text = xor_encrypt_decrypt(text, key)
        
        with open(output_file, 'w') as f:
            f.write(encrypted_text)

        messagebox.showinfo("Success", "File encrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to handle file decryption
def decrypt_file():
    input_file = filedialog.askopenfilename(title="Select file to decrypt")
    if not input_file:
        return  # User canceled the file dialog

    output_file = filedialog.asksaveasfilename(defaultextension=".txt", title="Save decrypted file as")
    if not output_file:
        return  # User canceled the save dialog

    key_file = filedialog.askopenfilename(title="Select key file", filetypes=[("Text Files", "*.txt")])
    if not key_file:
        return  # User canceled key file selection
    
    key = get_key_from_file(key_file)  # Get the key from the selected key file
    if not key:
        return  # Handle if key reading fails

    try:
        with open(input_file, 'r') as f:
            encrypted_text = f.read()
        
        # Decrypt the text using XOR
        decrypted_text = xor_decrypt(encrypted_text, key)

        with open(output_file, 'w') as f:
            f.write(decrypted_text)

        messagebox.showinfo("Success", "File decrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Main window
root = tk.Tk()
root.title("XOR Encryption")
root.geometry("450x350")

# Load and display image (optional)
image_path = "logo1.png"
if os.path.exists(image_path):
    img = tk.PhotoImage(file=image_path)
    image_label = tk.Label(root, image=img)
    image_label.pack(pady=10)
else:
    messagebox.showwarning("Image not found", f"Could not find {image_path}. Please check the path.")

# Create buttons for encrypt and decrypt
encrypt_button = tk.Button(root, text="Encrypt a File", command=encrypt_file, width=25)
decrypt_button = tk.Button(root, text="Decrypt a File", command=decrypt_file, width=25)
exit_button = tk.Button(root, text="Exit", command=root.quit, width=25)

# Position buttons in the window
encrypt_button.pack(pady=10)
decrypt_button.pack(pady=10)
exit_button.pack(pady=10)

# Label for name
name_label = tk.Label(root, text="Made by Noah Sanderson")
name_label.pack(pady=(10, 20))

# Start the Tkinter event loop
root.mainloop()


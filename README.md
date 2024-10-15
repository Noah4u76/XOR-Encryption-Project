# XOR Encryption Program

## Overview
This project is an encryption program that features two key processes: encryption/decryption and a graphical user interface (GUI) for user interaction. The encryption process uses XOR (exclusive OR) encryption, a simple and effective symmetric encryption algorithm based on binary operations. The GUI is built using the Tkinter library, allowing users to select files for encryption or decryption without needing to use the command line.

## Encryption Algorithm: XOR
The XOR algorithm operates on ASCII characters, making it compatible with both printable and non-printable characters. In this encryption method, each character in the plaintext is XOR-ed with a corresponding character from the key using the bitwise XOR operator (^). The result is a value representing the XOR of the ASCII values of the plaintext and key characters. Since XOR is a symmetric operation, the same process is used for decryption, restoring the original text when applied with the same key.

To handle keys that are shorter than the input text, the key is repeated (extended) to match the length of the text. Each character in the plaintext is XOR-ed with the corresponding extended key character. The output is then encoded in Base64 to ensure that the encrypted data can be saved as a printable string. During decryption, the Base64-encoded string is decoded, and the same XOR process is used to recover the original plaintext.

The function `xor_encrypt_decrypt` handles both encryption and decryption since XOR is a reversible operation.

## Decoding for Decryption: Base64
The decryption process starts by decoding the Base64 string back into the original XOR-encrypted form. The function `xor_decrypt` reads the Base64 string, decodes it, and repeats the key if necessary. It then XORs the encrypted text with the original key to recover the plaintext.

## Program Structure

### `encryption.py`
This module contains the core encryption functions:
- `xor_encrypt_decrypt(text, key)` – Encrypts the plaintext using XOR and encodes the result in Base64. This function is also used for decryption by applying XOR with the key again.
- `xor_decrypt(text, key)` – Decodes the Base64 string and applies XOR to decrypt the text and restore the original plaintext.
- `get_key_from_file(filepath)` – Reads the encryption key from a text file and handles file-related issues.

### `gui.py`
This module provides the graphical interface for the program. It allows users to:
- Select files for encryption or decryption.
- Choose an encryption key.
- Select the destination to save the output files.
- Trigger the encryption or decryption process with dedicated buttons.

The GUI also handles basic error management, such as missing files or invalid inputs, to ensure a smooth user experience.

# Instructions on How to Use the Program

### Prerequisites:
- **Python installation**: Install Python if not already installed. You can download it from [Python.org](https://www.python.org/).
- **Tkinter Library**: This library is typically pre-installed with most Python installations. If it is missing, install it using the following command:

```bash
pip install tk
```

## Preparing Files:

Download or copy the `encryption.py`, `gui.py`, and `logo1.png` files into a folder on your system.

Ensure you have a key file (.txt) that will contain the key to be used during encryption and decryption. This key should be a string of characters. Do not lose this key after encryption, as you will need it for decryption.
Example Key:

```bash
Jd93kL7xqV9rWmN2PzFgBtX5YsQ8UwHp
```

## Preparing the Text File to Encrypt:

Create a plaintext file that you want to encrypt. The file can contain any text data.
Example File: `message.txt`
```bash
Content: This is top secret!
```

## Step 1: Running the Program

Open a terminal or command line and navigate to the folder where `encryption.py`, `gui.py`, and `logo1.png` are located.

Run the `gui.py` file using Python:
```bash
python gui.py
```
This will launch the graphical interface for the program.

## Step 2: Encrypting a File

Once the GUI opens, click the button labeled `"Encrypt a File"`. This will open a file selection dialog.

In the dialog, navigate your system to find the plaintext file you want to encrypt. After selecting it, click `"Open"`.

After selecting the file, another dialog will open asking where you would like to save the encrypted file. Choose a destination and provide a name, such as `encrypted.txt`, then click `"Save"`.

Next, a dialog will open for you to choose the key. Browse your system and select the file containing your key, such as `key.txt`. Click `"Open"` to continue.

Your plaintext file should now be encrypted. The program will read the input file and encrypt the message using the XOR algorithm with the provided key. After completion, you should see a message stating `"File encrypted successfully"`.

## Step 3: Decrypting a File

Click the button labeled `"Decrypt a File"`. This will open a file selection dialog.

In the dialog, navigate your system to find the encrypted file you want to decrypt. After selecting it, click `"Open".`

After selecting the file, another dialog will open asking where you would like to save the decrypted file. Choose a destination and provide a name, such as `decrypted.txt`, then click `"Save"`.

Next, a dialog will open for you to choose the key. Browse your system and select the same key file used during encryption, such as `key.txt`. Click `"Open"` to continue.

Your encrypted file should now be decrypted. The program will read the input file and decrypt the message using the XOR algorithm with the provided key. After completion, you should see a message stating `"File decrypted successfully"`.

## Step 4: Viewing Files

The file `encrypted.txt` will contain the XOR-encrypted and Base64-encoded data. It will look something like this:
```bash
U2FsdGVKX1+qdf07...
```

The file `decrypted.txt` will contain the original message:
```bash
This is top secret!
```

## Step 5: Handling Errors
If any file errors occur, the program will handle them accordingly and display a message in a pop-up window. Examples of errors include:

`Error:` 
```bash
File Not Found: This occurs when a selected file does not exist.
```
`Error:`
```bash
Invalid Key: This occurs when the key is incorrect or cannot be read properly.
```

## Step 6: Exiting the Program
To exit, click the `"Exit"` button on the GUI or simply close the window by clicking the `"X"` in the top-right corner.

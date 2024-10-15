import base64

# XOR encryption and decryption using ASCII values (safe for all characters)
def xor_encrypt_decrypt(text, key):
    encrypted_chars = []
    key = key  # Keep the key as is

    # Extend or truncate the key to match the text length
    repeated_key = (key * (len(text) // len(key) + 1))[:len(text)]

    for i, char in enumerate(text):
        # XOR each character's ordinal value (ASCII)
        xor_value = chr(ord(char) ^ ord(repeated_key[i]))
        encrypted_chars.append(xor_value)

    # Convert the XOR-ed result to Base64 to ensure it's printable
    return base64.b64encode(''.join(encrypted_chars).encode('utf-8')).decode('utf-8')

# XOR decryption (Base64 decoded)
def xor_decrypt(text, key):
    encrypted_bytes = base64.b64decode(text).decode('utf-8')
    key = key  # Keep the key as is

    # Extend or truncate the key to match the text length
    repeated_key = (key * (len(encrypted_bytes) // len(key) + 1))[:len(encrypted_bytes)]
    
    decrypted_chars = [
        chr(ord(encrypted_bytes[i]) ^ ord(repeated_key[i])) for i in range(len(encrypted_bytes))
    ]

    return ''.join(decrypted_chars)

# Read the key from a text file
def get_key_from_file(filepath):
    try:
        with open(filepath, 'r') as file:
            key = file.read().strip()  # Read the key and strip any leading/trailing whitespace
        return key
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None



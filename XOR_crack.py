import itertools
import string

def decode_flag(hex_encoded, key):
    bytes_encoded = bytes.fromhex(hex_encoded)
    
    decoded_chars = []
    for i in range(len(bytes_encoded)):
        decoded_chars.append(chr(bytes_encoded[i] ^ ord(key[i % len(key)])))
    
    decoded_flag = ''.join(decoded_chars)
    return decoded_flag

def brute_force_key(hex_encoded, key_length):
    charset = string.ascii_letters + string.digits
    possible_keys = itertools.product(charset, repeat=key_length)
    
    for key_tuple in possible_keys:
        key = ''.join(key_tuple)
        decoded_flag = decode_flag(hex_encoded, key)
        
        if decoded_flag.startswith("THM{") and decoded_flag.endswith("}"):  # Check if the flag starts with "THM{"
            return key, decoded_flag
    
    return None, None

if __name__ == '__main__':
    hex_encoded = input("Enter the hex encoded flag: ").strip()
    
    key_length = 5
    
    # Brute force the key
    key, decoded_flag = brute_force_key(hex_encoded, key_length)
    
    if key:
        print(f"Key: {key}")
        print(f"Decoded Flag: {decoded_flag}")
    else:
        print("Key not found.")


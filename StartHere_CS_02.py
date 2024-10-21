
from PIL import Image

# Function to encrypt the image
def encrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()  # Load pixel data
    
    # Encrypt the image by shifting pixel values
    for i in range(img.size[0]):  # Traverse through width
        for j in range(img.size[1]):  # Traverse through height
            r, g, b = pixels[i, j]  # Get the RGB values of the pixel
            # Modify each RGB value based on the key (mod 256 to prevent overflow)
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    
    # Save the encrypted image
    img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

# Function to decrypt the image
def decrypt_image(encrypted_image_path, key, output_path):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    pixels = img.load()  # Load pixel data
    
    # Decrypt the image by reversing the shift of pixel values
    for i in range(img.size[0]):  # Traverse through width
        for j in range(img.size[1]):  # Traverse through height
            r, g, b = pixels[i, j]  # Get the RGB values of the pixel
            # Reverse the modification of each RGB value (mod 256 to prevent underflow)
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    
    # Save the decrypted image
    img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example usage
image_path = "pexels-philippedonn-1133957.jpg"
encrypted_image_path = "encrypted_image.jpg"
decrypted_image_path = "decrypted_image.jpg"
encryption_key = 50  # The key for encryption and decryption

# Encrypt the image
encrypt_image(image_path, encryption_key, encrypted_image_path)

# Decrypt the image
decrypt_image(encrypted_image_path, encryption_key, decrypted_image_path)
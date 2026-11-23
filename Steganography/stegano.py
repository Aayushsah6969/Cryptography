from PIL import Image


# ---------------- HELPER FUNCTION ----------------

def text_to_binary(text):
    """
    Convert text into a binary string.

    UTF-8 allows us to handle ordinary text, symbols,
    and non-English characters.

    Example:
    "A" -> "01000001"
    """

    # Convert text into bytes using UTF-8 encoding.
    text_bytes = text.encode("utf-8")

    # Convert every byte into an 8-bit binary string.
    binary = ''.join(format(byte, '08b') for byte in text_bytes)

    return binary


# ---------------- HIDE MESSAGE ----------------

def hide_message(input_image, output_image, secret_message):

    # Open the original image.
    # convert("RGB") ensures that every pixel has
    # exactly three color channels: Red, Green, Blue.
    image = Image.open(input_image).convert("RGB")

    # Convert the image into a list of RGB pixel values.
    pixels = list(image.getdata())

    # Convert the secret message into binary.
    message_binary = text_to_binary(secret_message)

    # Store the message length as a 32-bit binary number.
    # This tells the extraction function where the message ends.
    message_length = len(message_binary)

    length_binary = format(message_length, '032b')

    # Combine the length header and the actual message.
    # The first 32 bits store the message length.
    # The remaining bits store the secret message.
    full_binary = length_binary + message_binary

    # Each RGB pixel contains 3 color values.
    # Each color value can store 1 bit using its LSB.
    capacity = len(pixels) * 3

    # Make sure the image has enough space for the message.
    if len(full_binary) > capacity:
        raise ValueError(
            "Message is too large for this image. "
            "Use a larger image or a shorter message."
        )

    # Create a new list to store modified pixel values.
    new_pixels = []

    # Keep track of which message bit we are embedding.
    bit_index = 0

    # Process each pixel in the image.
    for pixel in pixels:

        # Store the modified RGB values of the current pixel.
        new_pixel = []

        # Process Red, Green, and Blue separately.
        for color_value in pixel:

            # If there are still message bits to hide,
            # replace the least significant bit of this color.
            if bit_index < len(full_binary):

                # Get the current bit from the message.
                bit = int(full_binary[bit_index])

                # Clear the last bit using & 254 (11111110).
                # Then insert our secret bit using | bit.
                #
                # Example:
                # 100 -> 101 when the secret bit is 1.
                color_value = (color_value & 254) | bit

                # Move to the next message bit.
                bit_index += 1

            # Add the original or modified color value.
            new_pixel.append(color_value)

        # Add the completed RGB pixel.
        new_pixels.append(tuple(new_pixel))

    # Replace the original image pixels with modified pixels.
    image.putdata(new_pixels)

    # Save the new image as PNG.
    # PNG is lossless, so the hidden bits are preserved.
    image.save(output_image, format="PNG")

    print("Message hidden successfully!")
    print("Output image:", output_image)


# ---------------- EXTRACT MESSAGE ----------------

def extract_message(input_image):

    # Open the image containing the hidden message.
    image = Image.open(input_image).convert("RGB")

    # Get all RGB pixel values.
    pixels = list(image.getdata())

    # Store the extracted binary bits.
    extracted_bits = ""

    # Extract the first 32 bits to obtain the message length.
    # We need this information before extracting the message.
    for pixel in pixels:

        for color_value in pixel:

            # The LSB is the rightmost bit.
            # & 1 extracts that bit.
            bit = color_value & 1

            # Convert the bit into a string and append it.
            extracted_bits += str(bit)

            # Stop once we have collected 32 bits.
            if len(extracted_bits) == 32:
                break

        if len(extracted_bits) == 32:
            break

    # Convert the 32-bit binary header into an integer.
    message_length = int(extracted_bits, 2)

    # The message length is stored in bits.
    # Check whether the image has enough data for the message.
    if message_length > (len(pixels) * 3 - 32):
        raise ValueError("No valid hidden message found.")

    # Extract the message bits after the 32-bit header.
    message_bits = ""

    # Skip the first 32 bits because they contain the length.
    bit_index = 0

    for pixel in pixels:

        for color_value in pixel:

            if bit_index >= 32:

                # Extract the least significant bit.
                bit = color_value & 1

                # Add it to the message.
                message_bits += str(bit)

                # Stop after extracting the expected message length.
                if len(message_bits) == message_length:
                    break

            bit_index += 1

        if len(message_bits) == message_length:
            break

    # Convert the binary message back into bytes.
    message_bytes = bytes(
        int(message_bits[i:i + 8], 2)
        for i in range(0, len(message_bits), 8)
    )

    # Decode the bytes into readable UTF-8 text.
    return message_bytes.decode("utf-8")


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":

    # Image containing the original pixels.
    input_image = "input.png"

    # Image that will contain the hidden message.
    output_image = "output.png"

    # The message we want to hide.
    secret_message = "Hello Bob! This is my first steganography program."

    # Hide the message inside the image.
    hide_message(input_image, output_image, secret_message)

    # Extract the hidden message from the new image.
    extracted_message = extract_message(output_image)

    print("\nExtracted message:", extracted_message)
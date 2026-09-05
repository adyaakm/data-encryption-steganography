from PIL import Image

DELIMITER = "1111111111111110"


def text_to_binary(text):
    """Convert text to a binary string."""
    return ''.join(format(ord(char), '08b') for char in text)


def encode_image(input_path, output_path, message):
    """Hide a text message inside an RGB/RGBA image using LSB steganography."""

    image = Image.open(input_path).convert("RGB")
    pixels = list(image.getdata())

    binary_message = text_to_binary(message) + DELIMITER

    capacity = len(pixels) * 3

    if len(binary_message) > capacity:
        raise ValueError(
            f"Message is too large for this image. "
            f"Maximum capacity is approximately {capacity // 8} characters."
        )

    data_index = 0
    encoded_pixels = []

    for pixel in pixels:

        channels = list(pixel)

        for channel_index in range(3):

            if data_index < len(binary_message):

                bit = int(binary_message[data_index])

                channels[channel_index] = (
                    channels[channel_index] & ~1
                ) | bit

                data_index += 1

        encoded_pixels.append(tuple(channels))

    encoded_image = Image.new("RGB", image.size)
    encoded_image.putdata(encoded_pixels)

    encoded_image.save(output_path, format="PNG")

    print(f"Message successfully hidden in: {output_path}")


if __name__ == "__main__":

    input_image = input("Enter input image path: ").strip()
    output_image = input("Enter output image path: ").strip()
    secret_message = input("Enter secret message: ")

    try:
        encode_image(
            input_image,
            output_image,
            secret_message
        )

    except Exception as error:
        print(f"Error: {error}")

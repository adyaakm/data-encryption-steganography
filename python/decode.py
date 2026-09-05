from PIL import Image

DELIMITER = "1111111111111110"


def binary_to_text(binary_data):
    """Convert an 8-bit binary string into text."""

    characters = []

    for index in range(0, len(binary_data), 8):

        byte = binary_data[index:index + 8]

        if len(byte) == 8:
            characters.append(chr(int(byte, 2)))

    return ''.join(characters)


def decode_image(image_path):
    """Extract a hidden text message from an image using LSB steganography."""

    image = Image.open(image_path).convert("RGB")
    pixels = list(image.getdata())

    binary_data = ""

    for pixel in pixels:

        for channel in pixel[:3]:

            binary_data += str(channel & 1)

            if binary_data.endswith(DELIMITER):

                message_binary = binary_data[
                    :-len(DELIMITER)
                ]

                return binary_to_text(message_binary)

    raise ValueError(
        "No hidden message was found in the image."
    )


if __name__ == "__main__":

    encoded_image = input(
        "Enter encoded image path: "
    ).strip()

    try:

        message = decode_image(encoded_image)

        print("\nHidden message:")
        print(message)

    except Exception as error:

        print(f"Error: {error}")

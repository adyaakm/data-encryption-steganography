# Data Encryption and Hiding in Image using Steganographic Methods

## Overview

This project implements an image steganography system for securely hiding confidential
messages inside digital images.

The system uses steganographic techniques to embed text information into an image in
such a way that the presence of the hidden message is not easily noticeable. The
embedded message can later be extracted from the encoded image using the decoding
process.

The project demonstrates the use of image processing, data hiding techniques,
encoding and decoding algorithms, and secure information handling.

---

## Features

- Hide confidential text messages inside digital images.
- Extract hidden messages from encoded images.
- Encoding and decoding functionality.
- Preserves the visual appearance of the image after message embedding.
- Simple and user-friendly workflow.
- Supports secure handling of confidential information.
- Demonstrates practical application of steganographic methods.

---

## Technologies Used

- **Python** – Core implementation and steganography logic
- **Pillow** – Image processing
- **LSB Steganography** – Technique used for hiding information within images

---

## How It Works

The project follows two main operations:

### 1. Encoding

The encoding process takes an input image and a confidential message.

```text
Input Image + Secret Message
            ↓
       Encoding Process
            ↓
      Encoded Image
```

The message is converted into a suitable binary representation and embedded into
the image using steganographic techniques.

### 2. Decoding
The resulting image looks visually similar to the original image but contains the
hidden message.

The decoding process takes the encoded image and extracts the hidden information.

Encoded Image
      ↓
Decoding Process
      ↓
Hidden Message

The encoded information is read from the image and converted back into the original
text message.

## Project Structure
``` text
data-encryption-steganography/
│
├── python/
│   ├── encode.py
│   └── decode.py
│
├── sample/
│   ├── input.png
│   └── output.png
│
├── screenshots/
│   └── application.png
│
├── requirements.txt
└── README.md
```
### Directory Description

| Directory/File     | Description                                        |
| ------------------ | -------------------------------------------------- |
| `python/`          | Contains the encoding and decoding implementation  |
| `sample/`          | Contains sample input and encoded images           |
| `screenshots/`     | Contains screenshots demonstrating the application |
| `requirements.txt` | Lists the Python dependencies                      |
| `README.md`        | Project documentation                              |


## Installation

### Prerequisites

Make sure the following are installed on your system:

Python 3.x
pip
Git

### Clone the Repository

``` git clone https://github.com/adyaakm/data-encryption-steganography.git ```

Navigate to the project directory:

``` cd data-encryption-steganography ```

Install Dependencies

Install the required Python packages:

``` pip install -r requirements.txt ```


## Usage

### Encoding

The encoding process hides a confidential message inside an image.

A typical workflow is:

Select the input image.
Enter the confidential message.
Run the encoding process.
Specify the output image location.
The encoded image is generated.

Example:

``` python python/encode.py ```

The output will be an image containing the hidden message.

### Decoding

The decoding process extracts the hidden message from an encoded image.

Steps:

Select the encoded image.
Run the decoding process.
The hidden message is extracted from the image.
The original confidential message is displayed.

Example:

```python python/decode.py ```


## Example

Consider an input image:
``` text
Input Image
    +
"Confidential Message"
    ↓
Encoding
    ↓
Encoded Image
```
The encoded image can be opened normally and should appear similar to the original
image. The hidden message can be recovered by running the decoding process on the
encoded image.

Example Message:
``` This is a confidential message. ```

After encoding, the message is hidden within the image.

During decoding:
``` text
Encoded Image
      ↓
   Decoder
      ↓
This is a confidential message.
```

## Limitations
- The amount of information that can be hidden depends on the size and properties
  of the input image.
- The project is primarily designed for educational and demonstration purposes.
- Image modifications such as compression, resizing, or significant format changes
  may affect the hidden information.
- Steganography hides the existence of information but should not be considered a
  replacement for strong encryption.
- Large messages may require larger images to provide sufficient embedding capacity.

## Future Improvements

Possible improvements include:

- Adding password-based protection for hidden messages.
- Combining encryption with steganography before embedding the message.
- Supporting additional image formats.
- Improving the graphical user interface.
- Adding support for hiding files in addition to text messages.
- Improving error handling and validation.
- Adding stronger encryption algorithms before the steganographic embedding process.

## Learning Outcomes

Through this project, the following concepts were explored:

- Image-based data hiding
- Steganographic techniques
- Encoding and decoding
- Binary data representation
- Image processing
- Secure information handling
- Algorithmic problem solving
- Application development

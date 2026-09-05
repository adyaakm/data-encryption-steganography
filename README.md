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
- **PHP** – Application/interface development
- **Image Processing** – Processing images for data embedding and extraction
- **Steganography** – Technique used for hiding information within images

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

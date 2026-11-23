# **Steganography**

Steganography is the technique of hiding secret information inside an ordinary-looking file or message so that other people do not notice that the information exists.

It is different from encryption, which protects information by making it unreadable.

Since you're learning cryptography with Python, steganography is a useful next topic. We'll first understand the concepts, then implement a simple program that hides and extracts a secret message inside an image.

## **1. What is steganography?**

The word steganography comes from Greek words meaning "covered writing."

The main goal is to hide the existence of a secret message.

For example, Alice wants to send Bob a secret message. Instead of sending the message directly, she hides it inside an ordinary image.

Bob receives the image and extracts the hidden message.

[Mesmerizing view of a calm lake on the background of mountains under a blue sky](https://images.openai.com/static-rsc-4/-CYeOmNC7yNTd_Gbb1TopCz2XnmSw9gpUqvImZHDz8QuGsK4_mzq7-ssdB_N_jdo76lFrGZnngoLwMj-qOTTwfPfAiQ2JEtqE6SRtLtMWI2UY3bMVk7ng4HjdEWh4sflXeBA_if7Ce8VStC094_bMaA05-DsXX8rLzH-st0uOI51eKEu0XUGmgKyeAkKs59g?purpose=inline)

**Original image**

An ordinary image used as the carrier

Hide a secret message inside the image

[Mesmerizing view of a calm lake on the background of mountains under a blue sky](https://images.openai.com/static-rsc-4/-CYeOmNC7yNTd_Gbb1TopCz2XnmSw9gpUqvImZHDz8QuGsK4_mzq7-ssdB_N_jdo76lFrGZnngoLwMj-qOTTwfPfAiQ2JEtqE6SRtLtMWI2UY3bMVk7ng4HjdEWh4sflXeBA_if7Ce8VStC094_bMaA05-DsXX8rLzH-st0uOI51eKEu0XUGmgKyeAkKs59g?purpose=inline)

**Stego image**

Looks almost identical to the original image

Extract the hidden message

**Secret message:** `Meet me at 10 PM`

The image containing the hidden information is called a **stego image**.

The original image is called the **cover image**.

## **2. Steganography vs encryption**

| Feature      | Encryption                      | Steganography                     |
| ------------ | ------------------------------- | --------------------------------- |
| Main purpose | Hide the meaning of information | Hide the existence of information |
| Input        | Plaintext                       | Secret message and a carrier      |
| Output       | Ciphertext                      | Stego file                        |
| Example      | AES encryption                  | Hiding text inside an image       |

These techniques can also be combined.

For example, encrypt a secret message using AES and then hide the ciphertext inside an image. Even if someone discovers the hidden data, they still need the encryption key to read it.

## **3. How does image steganography work?**

One of the simplest techniques is called **LSB (Least Significant Bit) steganography**.

To understand it, you need to know how digital images store colors.

### **Pixels and RGB values**

A digital image consists of pixels. Each pixel usually contains three color values:

- Red (R)
- Green (G)
- Blue (B)

Each color value ranges from 0 to 255 and is stored using 8 bits.

For example:

```
Red   = 100 = 01100100
Green = 150 = 10010110
Blue  = 200 = 11001000
```

The least significant bit (LSB) is the rightmost bit.

If we change that bit, the color value changes by only 1.

```
Original: 100 = 01100100
Modified: 101 = 01100101
```

This tiny change is usually imperceptible to the human eye.

### **Hiding a message**

Suppose we want to hide the letter `A`.

Its ASCII value is 65, which is represented in binary as:

```
A = 01000001
```

We can hide these 8 bits inside the least significant bits of 8 color values.

For example:

```
Original pixel values:
100 150 200 120 180 210 90  140

Message bits:
  0   1   0   0   0   0   0   1

Modified values:
100 151 200 120 180 210 90  141
```

Only the last bit of each color value is changed.

The modified image looks almost identical to the original, but it now contains the hidden letter.

To extract the message, the receiver reads the least significant bits in the same order and converts them back into characters.

## **4. Important concepts**

| Term           | Meaning                                                    |
| -------------- | ---------------------------------------------------------- |
| Cover image    | Original image used to hide data                           |
| Secret message | Information that we want to hide                           |
| Stego image    | Image containing the hidden information                    |
| Embedding      | Process of hiding the secret message                       |
| Extraction     | Process of recovering the hidden message                   |
| LSB            | Least Significant Bit; the rightmost bit of a binary value |

## **5. Limitations of LSB steganography**

- **Image capacity:** Larger messages require more pixels.
- **Image modification:** Resizing, cropping, or compressing the image may destroy the hidden message.
- **Detection:** Statistical analysis can sometimes reveal that data has been hidden.
- **No encryption:** Anyone who knows the extraction method can potentially read the message.

For our implementation, we'll use PNG images because they preserve pixel values without lossy compression.

## **6. What we'll implement in Python**

We'll use the `Pillow` library to work with images.

Our program will:

1. Load an image.
2. Convert a secret message into binary.
3. Hide the binary message inside the image using LSB.
4. Save the resulting stego image.
5. Extract the hidden message from the stego image.

We'll also add a simple message-length marker so the extraction process knows where the secret message ends.

This will be a basic educational implementation, not a secure steganography system. Later, we can combine it with AES encryption to hide encrypted messages inside images.
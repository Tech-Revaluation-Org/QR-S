

# **QR Code Generator GUI**

A modern, customizable QR Code Generator built with **PyQt6** and **Python**, featuring foreground/background color selection and optional logo embedding.

## **Features**

* **User-friendly interface** with dark theme and styled buttons.
* Generate QR codes from **text or URLs**.
* Customize **foreground and background colors**.
* Upload and embed a **logo/image** into the QR code.
* Preview the QR code inside the app.
* Save the generated QR code to your computer.

## **Screenshots**

*Add your screenshots here (e.g., `img/screenshot.png`)*

## **Installation**

### **Dependencies**

Make sure you have Python 3.7+ installed. Then, install the required packages:

```bash
pip install qrcode[pil] PyQt6 pillow
```

## **Usage**

Run the script:

```bash
python qrcode_generator.py
```

## **How It Works**

1. Enter the text or URL you want to encode.
2. Choose your preferred foreground and background colors.
3. (Optional) Upload a logo to embed in the center of the QR code.
4. Click **Generate & Save QR Code** to see the preview.
5. Click **Save QR Code As...** to save it as a PNG file.

## **Code Highlights**

* Uses `qrcode` and `Pillow` to generate QR codes and handle images.
* PyQt6 powers the interactive GUI with custom styling.
* Embeds logos using PIL with anti-aliasing for best results.


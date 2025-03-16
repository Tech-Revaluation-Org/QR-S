import qrcode
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog, QColorDialog
)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from PIL import Image
from io import BytesIO

class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.fg_color = "black"
        self.bg_color = "white"
        self.image_path = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(400, 200, 450, 550)
        self.setStyleSheet("background-color: #121212; color: white; font-size: 16px; border-radius: 10px;")

        layout = QVBoxLayout()
        layout.setSpacing(10)

        self.input_text = QLineEdit(self)
        self.input_text.setPlaceholderText("Enter text or URL")
        self.input_text.setStyleSheet("padding: 10px; border-radius: 5px; background: #222; color: white;")
        layout.addWidget(self.input_text)

        self.select_fg_btn = QPushButton("Choose Foreground Color", self)
        self.select_fg_btn.setStyleSheet("background: #1DB954; color: white; padding: 10px; border-radius: 5px;")
        self.select_fg_btn.clicked.connect(self.select_fg_color)
        layout.addWidget(self.select_fg_btn)

        self.select_bg_btn = QPushButton("Choose Background Color", self)
        self.select_bg_btn.setStyleSheet("background: #FF5733; color: white; padding: 10px; border-radius: 5px;")
        self.select_bg_btn.clicked.connect(self.select_bg_color)
        layout.addWidget(self.select_bg_btn)

        self.upload_img_btn = QPushButton("Upload Image for QR", self)
        self.upload_img_btn.setStyleSheet("background: #FFC107; color: black; padding: 10px; border-radius: 5px;")
        self.upload_img_btn.clicked.connect(self.upload_image)
        layout.addWidget(self.upload_img_btn)

        self.generate_btn = QPushButton("Generate & Save QR Code", self)
        self.generate_btn.setStyleSheet("background: #007BFF; color: white; padding: 10px; border-radius: 5px;")
        self.generate_btn.clicked.connect(self.generate_qr)
        layout.addWidget(self.generate_btn)

        self.qr_label = QLabel(self)
        self.qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.qr_label)

        self.save_btn = QPushButton("Save QR Code As...", self)
        self.save_btn.setStyleSheet("background: #17A2B8; color: white; padding: 10px; border-radius: 5px;")
        self.save_btn.clicked.connect(self.save_qr)
        self.save_btn.setEnabled(False)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

    def select_fg_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.fg_color = color.name()

    def select_bg_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.bg_color = color.name()

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Upload Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path

    def generate_qr(self):
        text = self.input_text.text()
        if text:
            qr = qrcode.QRCode(box_size=10, border=2)
            qr.add_data(text)
            qr.make(fit=True)

            img = qr.make_image(fill=self.fg_color, back_color=self.bg_color).convert("RGB")

            if self.image_path:
                logo = Image.open(self.image_path)
                img = self.embed_logo(img, logo)

            img.save("qrcode.png")
            print("QR code saved as 'qrcode.png'")

            buffer = BytesIO()
            img.save(buffer, format="PNG")
            qimage = QImage.fromData(buffer.getvalue(), "PNG")
            pixmap = QPixmap.fromImage(qimage)
            self.qr_label.setPixmap(pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))

            self.save_btn.setEnabled(True)

    def embed_logo(self, qr_img, logo_img):
        qr_size = qr_img.size[0]
        logo_size = qr_size // 4
        logo_img = logo_img.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

        qr_img.paste(logo_img, ((qr_size - logo_size) // 2, (qr_size - logo_size) // 2), mask=logo_img)
        return qr_img

    def save_qr(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "", "PNG Files (*.png);;All Files (*)")
        if file_path:
            pixmap = self.qr_label.pixmap()
            if pixmap:
                pixmap.save(file_path, "PNG")

if __name__ == "__main__":
    app = QApplication([])
    window = QRCodeGenerator()
    window.show()
    app.exec()

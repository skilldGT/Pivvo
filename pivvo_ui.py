import sys
import threading
import os
import webbrowser
import socket
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QMessageBox, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from app import app, PIN, DOWNLOAD_FOLDER


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


class PivvoUI(QWidget):
    def __init__(self):
        super().__init__()
        self.local_ip = get_local_ip()
        self.setWindowTitle("Pivvo - Local P2P File Sharing")
        self.setWindowIcon(QIcon("icon.png"))  # Add your icon here
        self.setFixedSize(400, 320)
        self.setStyleSheet(self.load_styles())
        self.init_ui()
        self.run_flask_server()

    def load_styles(self):
        return """
            QWidget {
                background-color: #111827;
                color: #f9fafb;
                font-family: 'Segoe UI', sans-serif;
                font-size: 15px;
            }

            QPushButton {
                background-color: #2563eb;
                border: none;
                padding: 10px 15px;
                border-radius: 6px;
                color: white;
                font-weight: 600;
            }

            QPushButton:hover {
                background-color: #1d4ed8;
            }

            QPushButton:pressed {
                background-color: #1e40af;
            }

            QLabel#title {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 15px;
            }

            QLabel#pin {
                font-size: 36px;
                font-weight: bold;
                color: #10b981;
                margin: 10px 0;
            }

            QLabel#ip {
                font-size: 18px;
                font-weight: 600;
                color: #3b82f6;
                margin-bottom: 15px;
            }
        """

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("📡 Pivvo File Share")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        pin_label = QLabel(f"PIN: {PIN}")
        pin_label.setObjectName("pin")
        pin_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(pin_label)

        ip_label = QLabel(f"Connect at: {self.local_ip}:5000")
        ip_label.setObjectName("ip")
        ip_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(ip_label)

        btn_layout = QVBoxLayout()

        open_browser = QPushButton("🌐 Open in Browser")
        open_browser.clicked.connect(self.open_browser)
        btn_layout.addWidget(open_browser)

        open_folder = QPushButton("📂 Open Shared Folder")
        open_folder.clicked.connect(self.open_folder)
        btn_layout.addWidget(open_folder)

        exit_btn = QPushButton("❌ Exit Pivvo")
        exit_btn.clicked.connect(self.close_app)
        btn_layout.addWidget(exit_btn)

        layout.addLayout(btn_layout)
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)

    def run_flask_server(self):
        threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000), daemon=True).start()

    def open_browser(self):
        webbrowser.open(f"http://{self.local_ip}:5000")

    def open_folder(self):
        os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
        if sys.platform == 'win32':
            os.startfile(DOWNLOAD_FOLDER)
        elif sys.platform == 'darwin':
            os.system(f'open "{DOWNLOAD_FOLDER}"')
        else:
            os.system(f'xdg-open "{DOWNLOAD_FOLDER}"')

    def close_app(self):
        reply = QMessageBox.question(self, 'Exit Pivvo', 'Are you sure you want to exit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()


if __name__ == '__main__':
    app_qt = QApplication(sys.argv)
    window = PivvoUI()
    window.show()
    sys.exit(app_qt.exec_())

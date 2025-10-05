MAIN_STYLE = """
QWidget#MainWin {
    background-color: #020659;
    color: white;
    font-size: 16px;
}

QWidget {
    color: white;
    font-size: 16px;
}

QGroupBox {
    background-color: rgba(9, 3, 166, 0.55);
    border: 2px solid rgba(2, 8, 115, 0.9);
    border-radius: 12px;
    margin-top: 12px;
    padding: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 10px;
    color: white;
    font-size: 20px;
    font-weight: bold;
}

QPushButton {
    background-color: #8C085E;
    border-radius: 10px;
    color: white;
    padding: 8px 20px;
    min-height: 36px;
    border: none;
}

QPushButton:hover {
    /* лёгкий визуальный отклик */
    background-color: #a60f72;
}

QPushButton:pressed {
    background-color: #6a0545;
}

QRadioButton, QCheckBox {
    spacing: 8px;
    font-size: 16px;
}

QRadioButton::indicator, QCheckBox::indicator {
    width: 18px;
    height: 18px;
}

QSlider::groove:horizontal {
    height: 6px;
    background: #020873;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #8C085E;
    border: 1px solid white;
    width: 18px;
    margin: -6px 0;
    border-radius: 9px;
}

QLabel {
    font-size: 16px;
    color: white;
}

#resultLabel {
    font-size: 20px;
    background-color: rgba(2, 8, 115, 0.5);
    border: 1px solid #020659;
    border-radius: 10px;
    padding: 50px;
    line-height: 1.5;
}

#imageLabel {
    border: 2px solid #020659;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.3);
}
"""

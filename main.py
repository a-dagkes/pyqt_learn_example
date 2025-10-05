from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QButtonGroup, QCheckBox, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSlider, QVBoxLayout, QWidget
)
from PyQt5.QtGui import QIcon, QPixmap

from random import shuffle
from pathlib import Path
import json

from styles import MAIN_STYLE


IMAGES_DIR = Path(__file__).parent / "images"
DATA_FILE = Path(__file__).parent / "data.json"


class MainWin(QWidget):
    def __init__(self, data=None):
        super().__init__()
        self.setObjectName("MainWin")
        self.setWindowTitle('Генератор идей для разработки видеоигр')
        self.resize(1200, 700)
        full_path = IMAGES_DIR / "icon.icns"  # или icon.png
        self.setWindowIcon(QIcon(str(full_path)))
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.data = data
        self.types = list(self.data.keys())
        self.type_choice = ''
        self.setting_choice = ''
        self.hero_choice = ''

        self.button_next = QPushButton('Показать результат')

        self.typebox = QGroupBox('Выбери жанр игры')
        self.type_button1 = QRadioButton()
        self.type_button2 = QRadioButton()
        self.type_button3 = QRadioButton()
        self.type_button4 = QRadioButton()
        self.set_shuffled_types()

        self.type_button1.setCheckable(True)
        self.type_button2.setCheckable(True)
        self.type_button3.setCheckable(True)
        self.type_button4.setCheckable(True)
        self.typegroup = QButtonGroup()
        self.typegroup.addButton(self.type_button1)
        self.typegroup.addButton(self.type_button2)
        self.typegroup.addButton(self.type_button3)
        self.typegroup.addButton(self.type_button4)

        type_line1 = QHBoxLayout()
        type_line2 = QVBoxLayout()
        type_line3 = QVBoxLayout()
        type_line2.addWidget(self.type_button1)
        type_line2.addWidget(self.type_button2)
        type_line3.addWidget(self.type_button3)
        type_line3.addWidget(self.type_button4)
        type_line1.addLayout(type_line2)
        type_line1.addLayout(type_line3)
        self.typebox.setLayout(type_line1)

        self.setting = QGroupBox('Выбери сеттинг')
        self.setting_button1 = QRadioButton()
        self.setting_button2 = QRadioButton()
        self.setting_button3 = QRadioButton()
        self.setting_button4 = QRadioButton()
        self.setting_button1.setCheckable(True)
        self.setting_button2.setCheckable(True)
        self.setting_button3.setCheckable(True)
        self.setting_button4.setCheckable(True)
        self.settinggroup = QButtonGroup()
        self.settinggroup.addButton(self.setting_button1)
        self.settinggroup.addButton(self.setting_button2)
        self.settinggroup.addButton(self.setting_button3)
        self.settinggroup.addButton(self.setting_button4)
        setting_line1 = QHBoxLayout()
        setting_line2 = QVBoxLayout()
        setting_line3 = QVBoxLayout()
        setting_line2.addWidget(self.setting_button1)
        setting_line2.addWidget(self.setting_button2)
        setting_line3.addWidget(self.setting_button3)
        setting_line3.addWidget(self.setting_button4)
        setting_line1.addLayout(setting_line2)
        setting_line1.addLayout(setting_line3)
        self.setting.setLayout(setting_line1)

        self.difficult = QGroupBox('Выбери сложность')
        difficult_line1 = QVBoxLayout()
        difficult_line2 = QHBoxLayout()
        difficult_line3 = QHBoxLayout()
        difficult_slider = QSlider()
        difficult_slider.setOrientation(Qt.Horizontal)
        difficult_slider.setMinimum(0)
        difficult_slider.setMaximum(4)
        difficult_slider.setTickPosition(QSlider.TicksBelow)
        difficult_slider.setTickInterval(1)
        difficult_line2.addWidget(difficult_slider)
        text_easy = QLabel('Легко')
        text_normal = QLabel('Нормально')
        text_hard = QLabel('Сложно')
        text_expert = QLabel('Эксперт')
        text_survivle = QLabel('Выживание')
        difficult_line3.addWidget(text_easy, alignment=Qt.AlignLeft)
        difficult_line3.addWidget(text_normal, alignment=Qt.AlignLeft)
        difficult_line3.addWidget(text_hard, alignment=Qt.AlignHCenter)
        difficult_line3.addWidget(text_expert, alignment=Qt.AlignRight)
        difficult_line3.addWidget(text_survivle, alignment=Qt.AlignRight)
        difficult_line1.addLayout(difficult_line2)
        difficult_line1.addLayout(difficult_line3)
        self.difficult.setLayout(difficult_line1)

        self.choose = QGroupBox('Выбери тип игры')
        self.choose_solo = QCheckBox('Одиночный режим')
        self.choose_multy = QCheckBox('Мультиплеер')
        self.choose_solo.setCheckable(True)
        self.choose_multy.setCheckable(True)
        self.choosegroup = QButtonGroup()
        self.choosegroup.addButton(self.choose_solo)
        self.choosegroup.addButton(self.choose_multy)
        choose_line1 = QVBoxLayout()
        choose_line2 = QHBoxLayout()
        choose_line2.addWidget(self.choose_solo)
        choose_line2.addWidget(self.choose_multy)
        choose_line1.addLayout(choose_line2)
        self.choose.setLayout(choose_line1)

        self.hero = QGroupBox('Выбери героя')
        self.hero1_button = QCheckBox()
        self.hero2_button = QCheckBox()
        self.hero3_button = QCheckBox()
        self.hero1_button.setCheckable(True)
        self.hero2_button.setCheckable(True)
        self.hero3_button.setCheckable(True)
        self.hero_group = QButtonGroup()
        self.hero_group.addButton(self.hero1_button)
        self.hero_group.addButton(self.hero2_button)
        self.hero_group.addButton(self.hero3_button)
        hero_line1 = QVBoxLayout()
        hero_line1.addWidget(self.hero1_button)
        hero_line1.addWidget(self.hero2_button)
        hero_line1.addWidget(self.hero3_button)
        self.hero.setLayout(hero_line1)

        self.i_line = QLabel()
        self.i_line.setObjectName("imageLabel")
        self.i_line.setFixedSize(450, 450)
        self.i_line.setAlignment(Qt.AlignCenter)
        self.i_line.setScaledContents(False)

        self.label = QLabel('Сюжет игры')
        self.label.setObjectName("resultLabel")
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Левая колонка (жанр + герой)
        left_column = QVBoxLayout()
        left_column.addWidget(self.typebox, 0, Qt.AlignTop)
        left_column.addWidget(self.hero)
        self.typebox.setMaximumHeight(self.height() // 2)
        self.typebox.setMinimumHeight(self.height() // 2)

        # Правая колонка (сеттинг + тип игры + сложность)
        right_column = QVBoxLayout()
        right_column.addWidget(self.setting)
        right_column.addSpacing(20)
        right_column.addWidget(self.choose)
        right_column.addSpacing(15)
        right_column.addWidget(self.difficult)

        # Горизонтальное деление: левая колонка (1 часть) и правая (2 части)
        main_split = QHBoxLayout()
        main_split.addLayout(left_column, 1)
        main_split.addSpacing(40)
        main_split.addLayout(right_column, 2)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.button_next)
        button_layout.addStretch()

        self.result_container = QWidget()
        result_layout = QHBoxLayout()
        result_layout.setContentsMargins(0, 0, 0, 0)
        result_layout.addStretch()
        result_layout.addWidget(self.i_line)
        result_layout.addSpacing(30)
        result_layout.addWidget(self.label, 1)
        result_layout.addStretch()
        self.result_container.setLayout(result_layout)

        main_layout.addLayout(main_split, 3)  # 1:2 по горизонтали
        main_layout.addSpacing(20)
        main_layout.addWidget(self.result_container)
        main_layout.addSpacing(20)
        main_layout.addLayout(button_layout)
        main_layout.setContentsMargins(30, 30, 30, 30)

        self.type_button1.clicked.connect(self.choose_type)
        self.type_button2.clicked.connect(self.choose_type)
        self.type_button3.clicked.connect(self.choose_type)
        self.type_button4.clicked.connect(self.choose_type)

        self.setting_button1.clicked.connect(self.choose_setting)
        self.setting_button2.clicked.connect(self.choose_setting)
        self.setting_button3.clicked.connect(self.choose_setting)
        self.setting_button4.clicked.connect(self.choose_setting)

        self.hero1_button.clicked.connect(self.finalize_setup)
        self.hero2_button.clicked.connect(self.finalize_setup)
        self.hero3_button.clicked.connect(self.finalize_setup)

        self.button_next.clicked.connect(self.click_ok)

        self.start()

    def set_shuffled_types(self):
        shuffle(self.types)
        self.type_button1.setText(self.types[0])
        self.type_button2.setText(self.types[1])
        self.type_button3.setText(self.types[2])
        self.type_button4.setText(self.types[3])

    def choose_type(self):
        for button in (
            self.type_button1,
            self.type_button2,
            self.type_button3,
            self.type_button4
        ):
            if button.isChecked():
                self.reset_setting()
                self.reset_hero()
                self.type_choice = button.text()
                self.set_setting()
                return

    def set_setting(self):
        if self.type_choice:
            setting_options = list(self.data[self.type_choice].keys())
            for button, setting_option in zip(
                (
                    self.setting_button1,
                    self.setting_button2,
                    self.setting_button3,
                    self.setting_button4
                ),
                setting_options
            ):
                button.setText(setting_option)

    def choose_setting(self):
        for button in (
            self.setting_button1,
            self.setting_button2,
            self.setting_button3,
            self.setting_button4
        ):
            if button.isChecked():
                self.reset_hero()
                self.setting_choice = button.text()
                self.set_hero_options()
                return

    def set_hero_options(self):
        if self.type_choice and self.setting_choice:
            hero_options = list(
                self.data[self.type_choice][self.setting_choice].keys()
            )
            shuffle(hero_options)
            for button, hero_option in zip(
                (self.hero1_button, self.hero2_button, self.hero3_button),
                hero_options
            ):
                button.setText(hero_option)
            self.hero.show()

    def reset_type(self):
        self.type_choice = ''
        self.typegroup.setExclusive(False)
        for button in (
            self.type_button1,
            self.type_button2,
            self.type_button3,
            self.type_button4,
        ):
            button.setChecked(False)
        self.typegroup.setExclusive(True)

    def reset_setting(self):
        self.setting_choice = ''
        self.settinggroup.setExclusive(False)
        for button in (
            self.setting_button1,
            self.setting_button2,
            self.setting_button3,
            self.setting_button4,
        ):
            button.setChecked(False)
            button.setText('')
        self.settinggroup.setExclusive(True)

    def reset_hero(self):
        self.hero_choice = ''
        self.hero_group.setExclusive(False)
        for button in (
            self.hero1_button,
            self.hero2_button,
            self.hero3_button,
        ):
            button.setChecked(False)
        self.hero_group.setExclusive(True)
        self.hero.hide()

    def reset_solo_or_multi(self):
        self.choosegroup.setExclusive(False)
        self.choose_solo.setChecked(False)
        self.choose_multy.setChecked(False)
        self.choosegroup.setExclusive(True)

    def start(self):
        self.result_container.hide()
        self.i_line.hide()
        self.label.hide()
        shuffle(self.types)
        self.set_shuffled_types()
        self.reset_type()
        self.typebox.show()
        self.reset_setting()
        self.setting.show()
        self.difficult.show()
        self.reset_solo_or_multi()
        self.choose.show()
        self.reset_hero()
        self.hero.hide()
        self.type_button1.click()
        self.button_next.setText('Показать результат')

    def set_image(self, image_path):
        full_path = IMAGES_DIR / image_path
        pixmap = QPixmap(str(full_path))
        if pixmap.isNull():
            print(f"Ошибка загрузки: {image_path}")
            return
        pixmap = pixmap.scaled(
            430, 430,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.i_line.setPixmap(pixmap)
        print(f'Картинка обновилась на {image_path}')

    def finalize_setup(self):
        if self.type_choice and self.setting_choice:
            for button in (
                self.hero1_button,
                self.hero2_button,
                self.hero3_button
            ):
                if button.isChecked():
                    self.hero_choice = button.text()
                    game_data = self.data[self.type_choice][self.setting_choice][self.hero_choice]
                    self.set_image(game_data['image'])
                    self.label.setText(game_data['text'])

    def click_ok(self):
        if self.button_next.text() == 'Начать заново':
            self.start()
        elif self.button_next.text() == 'Показать результат':
            self.show_result()

    def show_result(self):
        if self.type_choice and self.setting_choice and self.hero_choice:
            self.typebox.hide()
            self.setting.hide()
            self.difficult.hide()
            self.choose.hide()
            self.hero.hide()
            self.i_line.show()
            self.label.show()
            self.result_container.show()
            self.button_next.setText('Начать заново')


def load_data(file_path):
    """Загружает данные из JSON файла"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка чтения JSON из {file_path}")
        return {}


def main():
    data = load_data(DATA_FILE)
    app = QApplication([])
    app.setStyleSheet(MAIN_STYLE)
    main_win = MainWin(data)
    main_win.show()
    app.exec_()


if __name__ == '__main__':
    main()

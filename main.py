from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, 
QGroupBox, QButtonGroup, QRadioButton, QSlider, QCheckBox)
from PyQt5.QtGui import *
from random import randint, shuffle
types = ['экшен', 'приключения', 'РПГ', 'стратегия', 'симулятор', 'спорт', 'головоломка', 'инди']
shuffle(types)
type1 = types[randint(0,len(types)-1)]
type2 = types[randint(0,len(types)-1)]
if type2 == type1:
    while type2 == type1:
        type2 = types[randint(0,len(types)-1)]
type3 = types[randint(0,len(types)-1)]
if type3 == type1 and type3 == type2:
    while type3 == type1 and type3 == type2:
        type3 = types[randint(0, len(types)-1)]
type4 = types[randint(0,len(types)-1)]
if type4 == type1 and type4 == type2 and type4 == type3:
    while type4 == type1 and type4 == type2 and type4 == type3:
        type4 = types[randint(0,len(types)-1)]

type_choose = ''    

settings_action = ('альтернативная реальность','исторический', 'научная фантастика', 'постапокалипсис')
settings_adventure = ('киберпанк', 'нуар', 'постапокалипсис', 'фэнтези')
settings_rpg = ('научная фантастика', 'постапокалипсис', 'сверхъестественное', 'фэнтези')
settings_strategy = ('абстрактные миры', 'будущее с искусственным интеллектом', 'альтернативная реальность', 'средневековье')
settings_simulation = ('профессии', 'путешествия и приключения', 'экологическая деятельность', 'экономика и бизнес')
settings_sport = ('экстримальные условия', 'историческое воссоздание', 'аркадный юмор и карикатурный стиль', 'фэнтези')
settings_puzzle = ('детективная история','античные цивилизации', 'пространственно-временные манипуляции','пиксельная ретро-графика')
settings_indie = ('психологический хоррор', 'современность', 'научная фантастика', 'фэнтези')

setting1 = ''
setting2 = ''
setting3 = ''
setting4 = ''

def choose_setting():
    if type_choose == 'экшен':
        setting1 = settings_action[0]
        setting2 = settings_action[1]
        setting3 = settings_action[2]
        setting4 = settings_action[3]
    elif type_choose == 'приключения':
        setting1 = settings_adventure[0]
        setting2 = settings_adventure[1]
        setting3 = settings_adventure[2]
        setting4 = settings_adventure[3]
    elif type_choose == 'РПГ':
        setting1 = settings_rpg[0]
        setting2 = settings_rpg[1]
        setting3 = settings_rpg[2]
        setting4 = settings_rpg[3]
    elif type_choose == 'стратегия':
        setting1 = settings_strategy[0]
        setting2 = settings_strategy[1]
        setting3 = settings_strategy[2]
        setting4 = settings_strategy[3]
    elif type_choose == 'симулятор':
        setting1 = settings_simulation[0]
        setting2 = settings_simulation[1]
        setting3 = settings_simulation[2]
        setting4 = settings_simulation[3]
    elif type_choose == 'спорт':
        setting1 = settings_sport[0]
        setting2 = settings_sport[1]
        setting3 = settings_sport[2]
        setting4 = settings_sport[3]
    elif type_choose == 'головоломка':
        setting1 = settings_puzzle[0]
        setting2 = settings_puzzle[1]
        setting3 = settings_puzzle[2]
        setting4 = settings_puzzle[3]
    elif type_choose == 'инди':
        setting1 = settings_indie[0]
        setting2 = settings_indie[1]
        setting3 = settings_indie[2]
        setting4 = settings_indie[3]

setting_choose = ''

hero_action1 = ()
hero_action2 = ()
hero_action3 = ()
hero_action4 = ()
hero_adventure1 = ()
hero_adventure2 = ()
hero_adventure3 = ()
hero_adventure4 = ()
hero_rpg1 = ()
hero_rpg2 = ()
hero_rpg3 = ()
hero_rpg4 = ()
hero_strategy1 = ()
hero_strategy2 = ()
hero_strategy3 = ()
hero_strategy4 = ()
hero_simlation1 = ()
hero_simlation2 = ()
hero_simlation3 = ()
hero_simlation4 = ()
hero_sport1 = ()
hero_sport2 = ()
hero_sport3 = ()
hero_sport4 = ()
hero_puzzle1 = ()
hero_puzzle2 = ()
hero_puzzle3 = ()
hero_puzzle4 = ()
hero_indie1 = ()
hero_indie2 = ()
hero_indie3 = ()
hero_indie4 = ()

def choose_hero():
    if type_choose == 'экшен' and setting_choose == 'альтернативная реальность':
        hero_action1
    elif type_choose == 'экшен' and setting_choose == 'исторический':
        hero_action2
    elif type_choose == 'экшен' and setting_choose == 'научная фантастика':
        hero_action3
    elif type_choose == 'экшен' and setting_choose == 'постапокалипсис':
        hero_action4
    elif type_choose == 'приключения' and setting_choose == 'киберпанк':
        hero_adventure1
    elif type_choose == 'приключения' and setting_choose == 'нуар':
        hero_adventure2
    elif type_choose == 'приключения' and setting_choose == 'постапокалипсис':
        hero_adventure3
    elif type_choose == 'приключения' and setting_choose == 'фэнтези':
        hero_action4
    elif type_choose == 'РПГ' and setting_choose == 'научная фантастика':
        hero_rpg1
    elif type_choose == 'РПГ' and setting_choose == 'постапокалипсис':
        hero_rpg2
    elif type_choose == 'РПГ' and setting_choose == 'сверхъестественное':
        hero_rpg3
    elif type_choose == 'РПГ' and setting_choose == 'фэнтези':
        hero_rpg4
    elif type_choose == 'стратегия' and setting_choose == 'абстрактные миры':
        hero_strategy1
    elif type_choose == 'стратегия' and setting_choose == 'будущее с искусственным интеллектом':
        hero_strategy2
    elif type_choose == 'стратегия' and setting_choose == 'альтернативная реальность':
        hero_strategy3
    elif type_choose == 'стратегия' and setting_choose == 'средневековье':
        hero_strategy4
    elif type_choose == 'симулятор' and setting_choose == 'профессии':
        hero_simlation1
    elif type_choose == 'симулятор' and setting_choose == 'путешествия и приключения':
        hero_simlation2
    elif type_choose == 'симулятор' and setting_choose == 'экологичнская деятельность':
        hero_simlation3
    elif type_choose == 'симулятор' and setting_choose == 'экономика и бизнес':
        hero_simlation4
    elif type_choose == 'спорт' and setting_choose == 'экстримальные условия':
        hero_sport1
    elif type_choose == 'спорт' and setting_choose == 'историческое воссоздание':
        hero_sport2
    elif type_choose == 'спорт' and setting_choose == 'аркадный юмор и карикатурный стиль':
        hero_sport3
    elif type_choose == 'спорт' and setting_choose == 'фэнтези':
        hero_sport4
    elif type_choose == 'головоломка' and setting_choose == 'детективная история':
        hero_puzzle1
    elif type_choose == 'головоломка' and setting_choose == 'античные цивилизации':
        hero_puzzle2
    elif type_choose == 'головоломка' and setting_choose == 'пространственно-временные манипуляции':
        hero_puzzle3
    elif type_choose == 'головоломка' and setting_choose == 'пиксельная ретро-графика':
        hero_puzzle4
    elif type_choose == 'инди' and setting_choose == 'психологический хоррор':
        hero_indie1
    elif type_choose == 'инди' and setting_choose == 'современность':
        hero_indie2
    elif type_choose == 'инди' and setting_choose == 'научная фантастика':
        hero_indie3
    elif type_choose == 'инди' and setting_choose == 'фэнтези':
        hero_indie4
    
app = QApplication([])

button_next = QPushButton('Продолжить выбор')

typebox = QGroupBox('Выбери жанр игры')
type_button1 = QRadioButton(type1)
type_button2 = QRadioButton(type2)
type_button3 = QRadioButton(type3)
type_button4 = QRadioButton(type4)
typegroup = QButtonGroup()
typegroup.addButton(type_button1)
typegroup.addButton(type_button2)
typegroup.addButton(type_button3)
typegroup.addButton(type_button4)
type_line1 = QHBoxLayout()
type_line2 = QVBoxLayout()
type_line3 = QVBoxLayout()
type_line2.addWidget(type_button1)
type_line2.addWidget(type_button2)
type_line3.addWidget(type_button3)
type_line3.addWidget(type_button4)
type_line1.addLayout(type_line2)
type_line1.addLayout(type_line3)
typebox.setLayout(type_line1)

setting = QGroupBox('Выбери сеттинг')
setting_button1 = QRadioButton(setting1)
setting_button2 = QRadioButton(setting2)
setting_button3 = QRadioButton(setting3)
setting_button4 = QRadioButton(setting4)
settinggroup = QButtonGroup()
settinggroup.addButton(setting_button1)
settinggroup.addButton(setting_button2)
settinggroup.addButton(setting_button3)
settinggroup.addButton(setting_button4)
setting_line1 = QHBoxLayout()
setting_line2 = QVBoxLayout()
setting_line3 = QVBoxLayout()
setting_line2.addWidget(setting_button1)
setting_line2.addWidget(setting_button2)
setting_line3.addWidget(setting_button3)
setting_line3.addWidget(setting_button4)
setting_line1.addLayout(setting_line2)
setting_line1.addLayout(setting_line3)
setting.setLayout(setting_line1)

difficult = QGroupBox('Выбери сложность')
difficult_line1 = QVBoxLayout()
difficult_line2 = QHBoxLayout()
difficult_line3 = QHBoxLayout()
difficult_slider = QSlider()
difficult_line2.addWidget(difficult_slider)
text_easy = QLabel('Легко')
text_normal = QLabel('Нормально')
text_hard = QLabel('Сложно')
text_expert = QLabel('Эксперт')
text_survivle = QLabel('Режим выживания')
difficult_line3.addWidget(text_easy)
difficult_line3.addWidget(text_normal)
difficult_line3.addWidget(text_hard)
difficult_line3.addWidget(text_expert)
difficult_line3.addWidget(text_survivle)
difficult_line1.addLayout(difficult_line2)
difficult_line1.addLayout(difficult_line3)
difficult.setLayout(difficult_line1)

choose = QGroupBox('Выбери тип игры')
choose_solo = QPushButton('Одиночный режим')
choose_solo.setGeometry(50, 40, 50, 40)
choose_multy = QPushButton('Мультиплеер')
choose_multy.setGeometry(50, 40, 50, 40)
choosegroup = QButtonGroup()
choosegroup.addButton(choose_solo)
choosegroup.addButton(choose_multy)
choose_line1 = QVBoxLayout()
choose_line2 = QHBoxLayout()
choose_line2.addWidget(choose_solo)
choose_line2.addWidget(choose_multy)
choose_line1.addLayout(choose_line2)
choose.setLayout(choose_line1)

text_hero = QLabel('Выбери героя')

layout_line1 = QHBoxLayout()
layout_line2 = QVBoxLayout()
layout_line3 = QVBoxLayout()
layout_line4 = QHBoxLayout()
layout_line2.addWidget(typebox)
layout_line2.addWidget(difficult)
layout_line3.addWidget(setting)
layout_line3.addWidget(choose)
layout_line1.addLayout(layout_line2, stretch=8)
layout_line1.addLayout(layout_line3,stretch=8)

layout_line4.addStretch(1)
layout_line4.addWidget(button_next, stretch=1)
layout_line4.addStretch(1)

main_layout = QVBoxLayout()
main_layout.addLayout(layout_line1, stretch=2)
main_layout.addStretch(1)
main_layout.addLayout(layout_line4, stretch=1)
main_layout.addStretch(1)
main_layout.setSpacing(8)

main = QWidget()
main.setWindowTitle('Генератор идей для разработки видеоигр')
main.resize (1000,500)
main.setLayout(main_layout)


main.show()
app.exec_()

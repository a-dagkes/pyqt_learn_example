from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, 
QGroupBox, QButtonGroup, QRadioButton, QSlider, QCheckBox)
from PyQt5.QtGui import *
from PIL import Image, ImageDraw, ImageFont
from random import randint, shuffle
types = ['экшен', 'приключения', 'РПГ', 'стратегия', 'симулятор', 'спорт', 'головоломка', 'инди']
shuffle(types)
r = randint(1,2)
if r == 1:
    type1 = types[0]
    type2 = types[1]
    type3 = types[2]
    type4 = types[3]
elif r == 2:
    type1 = types[4]
    type2 = types[5]
    type3 = types[6]
    type4 = types[7]

type_choose = '' 

def choose_type():
    if type_button1.isChecked():
        type_choose = type1
    elif type_button2.isChecked():
        type_choose = type2
    elif type_button3.isChecked():
        type_choose = type3
    elif type_button4.isChecked():
        type_choose = type4
    return type_choose
  

settings_action = ('альтернативная реальность','исторический', 'научная фантастика', 'постапокалипсис')
settings_adventure = ('киберпанк', 'нуар', 'постапокалипсис', 'фэнтези')
settings_rpg = ('научная фантастика', 'постапокалипсис', 'сверхъестественное', 'фэнтези')
settings_strategy = ('абстрактные миры', 'будущее с искусственным интеллектом', 'альтернативная реальность', 'средневековье')
settings_simulation = ('профессии', 'путешествия и приключения', 'экологическая деятельность', 'экономика и бизнес')
settings_sport = ('экстремальные условия', 'историческое воссоздание', 'аркадный юмор и карикатурный стиль', 'фэнтези')
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
    return type_choose

setting_choose = ''

def type_setting():
    if setting_button1.isChecked():
        setting_choose = setting1
    elif setting_button2.isChecked():
        setting_choose = setting2
    elif setting_button3.isChecked():
        setting_choose = setting3
    elif setting_button4.isChecked():
        setting_choose = setting4
    return setting_choose

hero_action1 = ('историограф/хранитель памяти','охотник за временем/агент изменений','параллельный двойник/альтер эго')
hero_action2 = ('воин/рыцарь','ассасин/убийца','правитель/император')
hero_action3 = ('космодесантник/солдат будущего','хакер','механик/инженер-конструктор')
hero_action4 = ('выживальщик/бродяга','охотник за головой/нарушитель','проводник')
hero_adventure1 = ('хакер','маргинал/антигерой','модификатор сознания')
hero_adventure2 = ('безработный коп','журналист-исследователь','консультант/информатор')
hero_adventure3 = ('выживальщик','купец/поставщик','исследователь/картограф')
hero_adventure4 = ('приржденный лидер/полководец','некромант/повелитель мертвецов','политик/дипломат')
hero_rpg1 = ('инженер/техник','ученый-исследователь','контабандист/пират')
hero_rpg2 = ('трейдер/проводник','железнодорожник/водитель','рукводитель коммуны')
hero_rpg3 = ('экстрасенс/ясновидящий','ангел/небесный посланник','детектив')
hero_rpg4 = ('некромант/повелитель нежити','друид/жрец природы','драконоборец/охотник на монстров')
hero_strategy1 = ('логик','музыкант','хаотик')
hero_strategy2 = ('командир армии ИИ','хакер - человек-киборг','биомеханический боец')
hero_strategy3 = ('хроноанархист','архитектор реальности','хранитель хроносферы')
hero_strategy4 = ('разведчик/лучник','алхимик/инженер','священнослужитель/жрец')
hero_simlation1 = ('пилот гражданской авиации','Нейрохирург','дальнобойщик')
hero_simlation2 = ('капитан дальнего плавания','робототехник космических кораблей','археолог-архивариус древнего храма')
hero_simlation3 = ('археолог раскопок древних поселений','биолог-защитник коралловых рифов','паркостроитель зелёных насаждений')
hero_simlation4 = ('девелопер жилой застройки','инвестор фондового рынка','администратор крупного гостиничного комплекса')
hero_sport1 = ('профессиональный экстремал','авантюрист, ищущий приключения','трюкач')
hero_sport2 = ('старинный атлет','выдющийся исторически известный игрок','игрок спортивного клуба')
hero_sport3 = ('какрикатурная версия знаменитости','веселый мультяшный персонаж','сказочное существо')
hero_sport4 = ('супергерой','мутант','антропоморфоное животное')
hero_puzzle1 = ('частный детектив','журналист','следователь')
hero_puzzle2 = ('археолог','египетсикй жрец','египетский фараон')
hero_puzzle3 = ('изобритатель-путешественник во времени','мастер портала','путешественник сквозь параллельные реальности')
hero_puzzle4 = ('любитель старых консолей','виртуальный аватар прошлого','создатель классических аркадных игр')
hero_indie1 = ('детектив-психолог','ученик ученого, потерявшего рассудок','лесничий')
hero_indie2 = ('художник','старшеклассник','коллекционер книг')
hero_indie3 = ('инженер-исследователь','капитан корабля','искусственный интеллект робота-философа')
hero_indie4 = ('друид','привидение','библиотекарь')

hero1 = ''
hero2 = ''
hero3 = ''

def choose_hero():
    if type_choose == 'экшен' and setting_choose == 'альтернативная реальность':
        hero1 = hero_action1[0]
        hero2 = hero_action1[1]
        hero3 = hero_action1[2]
    elif type_choose == 'экшен' and setting_choose == 'исторический':
        hero1 = hero_action2[0]
        hero2 = hero_action2[1]
        hero3 = hero_action2[2]
    elif type_choose == 'экшен' and setting_choose == 'научная фантастика':
        hero1 = hero_action3[0]
        hero2 = hero_action3[1]
        hero3 = hero_action3[2]
    elif type_choose == 'экшен' and setting_choose == 'постапокалипсис':
        hero1 = hero_action4[0]
        hero2 = hero_action4[1]
        hero3 = hero_action4[2]
    elif type_choose == 'приключения' and setting_choose == 'киберпанк':
        hero1 = hero_adventure1[0]
        hero2 = hero_adventure1[1]
        hero3 = hero_adventure1[2]
    elif type_choose == 'приключения' and setting_choose == 'нуар':
        hero1 = hero_adventure2[0]
        hero2 = hero_adventure2[1]
        hero3 = hero_adventure2[2]
    elif type_choose == 'приключения' and setting_choose == 'постапокалипсис':
        hero1 = hero_adventure3[0]
        hero2 = hero_adventure3[1]
        hero3 = hero_adventure3[2]
    elif type_choose == 'приключения' and setting_choose == 'фэнтези':
        hero1 = hero_action4[0]
        hero2 = hero_action4[1]
        hero3 = hero_action4[2]
    elif type_choose == 'РПГ' and setting_choose == 'научная фантастика':
        hero1 = hero_rpg1[0]
        hero2 = hero_rpg1[1]
        hero3 = hero_rpg1[2]
    elif type_choose == 'РПГ' and setting_choose == 'постапокалипсис':
        hero1 = hero_rpg2[0]
        hero2 = hero_rpg2[1]
        hero3 = hero_rpg2[2]
    elif type_choose == 'РПГ' and setting_choose == 'сверхъестественное':
        hero1 = hero_rpg3[0]
        hero2 = hero_rpg3[1]
        hero3 = hero_rpg3[2]
    elif type_choose == 'РПГ' and setting_choose == 'фэнтези':
        hero1 = hero_rpg4[0]
        hero2 = hero_rpg4[1]
        hero3 = hero_rpg4[2]
    elif type_choose == 'стратегия' and setting_choose == 'абстрактные миры':
        hero1 = hero_strategy1[0]
        hero2 = hero_strategy1[1]
        hero3 = hero_strategy1[2]
    elif type_choose == 'стратегия' and setting_choose == 'будущее с искусственным интеллектом':
        hero1 = hero_strategy2[0]
        hero2 = hero_strategy2[1]
        hero3 = hero_strategy2[2]
    elif type_choose == 'стратегия' and setting_choose == 'альтернативная реальность':
        hero1 = hero_strategy3[0]
        hero2 = hero_strategy3[1]
        hero3 = hero_strategy3[2]
    elif type_choose == 'стратегия' and setting_choose == 'средневековье':
        hero1 = hero_strategy4[0]
        hero2 = hero_strategy4[1]
        hero3 = hero_strategy4[2]
    elif type_choose == 'симулятор' and setting_choose == 'профессии':
        hero1 = hero_simlation1[0]
        hero2 = hero_simlation1[1]
        hero3 = hero_simlation1[2]
    elif type_choose == 'симулятор' and setting_choose == 'путешествия и приключения':
        hero1 = hero_simlation2[0]
        hero2 = hero_simlation2[1]
        hero3 = hero_simlation2[2]
    elif type_choose == 'симулятор' and setting_choose == 'экологичнская деятельность':
        hero1 = hero_simlation3[0]
        hero2 = hero_simlation3[1]
        hero3 = hero_simlation3[2]
    elif type_choose == 'симулятор' and setting_choose == 'экономика и бизнес':
        hero1 = hero_simlation4[0]
        hero2 = hero_simlation4[1]
        hero3 = hero_simlation4[2]
    elif type_choose == 'спорт' and setting_choose == 'экстримальные условия':
        hero1 = hero_sport1[0]
        hero2 = hero_sport1[1]
        hero3 = hero_sport1[2]
    elif type_choose == 'спорт' and setting_choose == 'историческое воссоздание':
        hero1 = hero_sport2[0]
        hero2 = hero_sport2[1]
        hero3 = hero_sport2[2]
    elif type_choose == 'спорт' and setting_choose == 'аркадный юмор и карикатурный стиль':
        hero1 = hero_sport3[0]
        hero2 = hero_sport3[1]
        hero3 = hero_sport3[2]
    elif type_choose == 'спорт' and setting_choose == 'фэнтези':
        hero1 = hero_sport4[0]
        hero2 = hero_sport4[1]
        hero3 = hero_sport4[2]
    elif type_choose == 'головоломка' and setting_choose == 'детективная история':
        hero1 = hero_puzzle1[0]
        hero2 = hero_puzzle1[1]
        hero3 = hero_puzzle1[2]
    elif type_choose == 'головоломка' and setting_choose == 'античные цивилизации':
        hero1 = hero_puzzle2[0]
        hero2 = hero_puzzle2[1]
        hero3 = hero_puzzle2[2]
    elif type_choose == 'головоломка' and setting_choose == 'пространственно-временные манипуляции':
        hero1 = hero_puzzle3[0]
        hero2 = hero_puzzle3[1]
        hero3 = hero_puzzle3[2]
    elif type_choose == 'головоломка' and setting_choose == 'пиксельная ретро-графика':
        hero1 = hero_puzzle4[0]
        hero2 = hero_puzzle4[1]
        hero3 = hero_puzzle4[2]
    elif type_choose == 'инди' and setting_choose == 'психологический хоррор':
        hero1 = hero_indie1[0]
        hero2 = hero_indie1[1]
        hero3 = hero_indie1[2]
    elif type_choose == 'инди' and setting_choose == 'современность':
        hero1 = hero_indie2[0]
        hero2 = hero_indie2[1]
        hero3 = hero_indie2[2]
    elif type_choose == 'инди' and setting_choose == 'научная фантастика':
        hero1 = hero_indie3[0]
        hero2 = hero_indie3[1]
        hero3 = hero_indie3[2]
    elif type_choose == 'инди' and setting_choose == 'фэнтези':
        hero1 = hero_indie4[0]
        hero2 = hero_indie4[1]
        hero3 = hero_indie4[2]

    
def click_ok():
    if button_next.text() == 'Начать заново':
        restart()
    elif button_next.text() == 'Показать результат':
        show_result()

def show_result():
    typebox.hide()
    setting.hide()
    difficult.hide()
    choose.hide()
    hero.hide()
    image = Image.open("1.Тайна советсткой империи.jpg")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((50, 250), "Hello Pillow!", font=font)
    button_next.setText('Начать заново')

def restart():
    typegroup.setExclusive(False)    
    type_button1.setChecked(False)
    type_button2.setChecked(False)
    type_button3.setChecked(False)
    type_button4.setChecked(False)
    typegroup.setExclusive(True) 
    shuffle(types)
    r = randint(1,2)
    if r == 1:
        type1 = types[0]
        type2 = types[1]
        type3 = types[2]
        type4 = types[3]
    elif r == 2:
        type1 = types[4]
        type2 = types[5]
        type3 = types[6]
        type4 = types[7]
    typebox.update()
    typebox.show()
    settinggroup.setExclusive(False)    
    setting_button1.setChecked(False)
    setting_button2.setChecked(False)
    setting_button3.setChecked(False)
    setting_button4.setChecked(False)
    settinggroup.setExclusive(True) 
    setting.update()
    setting.show()
    difficult.show()
    choosegroup.setExclusive(False)
    choose_solo.setChecked(False)
    choose_multy.setChecked(False)
    choosegroup.setExclusive(True)
    choose.update()
    choose.show()
    hero_group.setExclusive(False)    
    hero1_button.setChecked(False)
    hero2_button.setChecked(False)
    hero3_button.setChecked(False)
    hero_group.setExclusive(True) 
    hero.update()
    hero.show()
    button_next.setText('Показать результат')


app = QApplication([])

button_next = QPushButton('Показать результат')


typebox = QGroupBox('Выбери жанр игры')
type_button1 = QRadioButton(type1)
type_button2 = QRadioButton(type2)
type_button3 = QRadioButton(type3)
type_button4 = QRadioButton(type4)
type_button1.setCheckable(True)
type_button2.setCheckable(True)
type_button3.setCheckable(True)
type_button4.setCheckable(True)
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
setting_button1.setCheckable(True)
setting_button2.setCheckable(True)
setting_button3.setCheckable(True)
setting_button4.setCheckable(True)
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
choose_multy = QPushButton('Мультиплеер')
choose_solo.setCheckable(True)
choose_multy.setCheckable(True)
choosegroup = QButtonGroup()
choosegroup.addButton(choose_solo)
choosegroup.addButton(choose_multy)
choose_line1 = QVBoxLayout()
choose_line2 = QHBoxLayout()
choose_line2.addWidget(choose_solo)
choose_line2.addWidget(choose_multy)
choose_line1.addLayout(choose_line2)
choose.setLayout(choose_line1)

hero = QGroupBox('Выбери героя')
hero1_button = QCheckBox(hero1)
hero2_button = QCheckBox(hero2)
hero3_button = QCheckBox(hero3)
hero1_button.setCheckable(True)
hero2_button.setCheckable(True)
hero3_button.setCheckable(True)
hero_group = QButtonGroup()
hero_group.addButton(hero1_button)
hero_group.addButton(hero2_button)
hero_group.addButton(hero3_button)
hero_line1 = QHBoxLayout()
hero_line2 = QVBoxLayout()
hero_line3 = QVBoxLayout()
hero_line4 = QVBoxLayout()
hero_line2.addWidget(hero1_button)
hero_line3.addWidget(hero2_button)
hero_line4.addWidget(hero3_button)
hero_line1.addLayout(hero_line2)
hero_line1.addLayout(hero_line3)
hero_line1.addLayout(hero_line4)
hero.setLayout(hero_line1)

layout_line1 = QHBoxLayout()
layout_line2 = QVBoxLayout()
layout_line3 = QVBoxLayout()
layout_line4 = QHBoxLayout()
layout_line5 = QHBoxLayout()
layout_line2.addStretch(1)
layout_line2.addWidget(typebox)
layout_line2.addStretch(1)
layout_line2.addWidget(difficult)
layout_line2.addStretch(1)
layout_line3.addStretch(1)
layout_line3.addWidget(setting)
layout_line3.addStretch(1)
layout_line3.addWidget(choose)
layout_line3.addStretch(1)
layout_line1.addLayout(layout_line2, stretch=5)
layout_line1.addStretch(1)
layout_line1.addLayout(layout_line3, stretch=5)

layout_line4.addStretch(1)
layout_line4.addWidget(hero, stretch=10)
layout_line4.addStretch(1)

layout_line5.addStretch(1)
layout_line5.addWidget(button_next, stretch=1)
layout_line5.addStretch(1)

main_layout = QVBoxLayout()
main_layout.addLayout(layout_line1, stretch=1)
main_layout.addStretch(1)
main_layout.addLayout(layout_line4, stretch=1)
main_layout.addStretch(1)
main_layout.addLayout(layout_line5, stretch=1)
main_layout.setSpacing(3)

main = QWidget()
main.setWindowTitle('Генератор идей для разработки видеоигр')
main.resize (1000,500)
main.setLayout(main_layout)

type_button1.clicked.connect(choose_type)
setting.hide()
setting.update()
setting.show()
choose_setting()
type_button2.clicked.connect(choose_type)
setting.hide()
setting.update()
setting.show()
choose_setting()
type_button3.clicked.connect(choose_type)
setting.hide()
setting.update()
setting.show()
choose_setting()
type_button4.clicked.connect(choose_type)
setting.hide()
setting.update()
setting.show()
choose_setting()


setting_button1.clicked.connect(type_setting)
hero.hide()
hero.update()
hero.show()
choose_hero()
setting_button2.clicked.connect(type_setting)
hero.hide()
hero.update()
hero.show()
choose_hero()
setting_button3.clicked.connect(type_setting)
hero.hide()
hero.update()
hero.show()
choose_hero()
setting_button4.clicked.connect(type_setting)
hero.hide()
hero.update()
hero.show()
choose_hero()

button_next.clicked.connect(click_ok)

main.update()
main.show()
app.exec_()




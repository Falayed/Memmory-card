from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox, QApplication
from PyQt5.QtCore import Qt

# Основне вікно додатку
app_window = QWidget()

# Кнопки для навігації та взаємодії
btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочити')
btn_next = QPushButton('Відповісти')

# Варіанти відповідей (радіокнопки)
rb_answer1 = QRadioButton("1")
rb_answer2 = QRadioButton("2")
rb_answer3 = QRadioButton("3")
rb_answer4 = QRadioButton("4")

# Група радіокнопок для вибору відповіді
answer_group = QButtonGroup()
answer_group.addButton(rb_answer1)
answer_group.addButton(rb_answer2)
answer_group.addButton(rb_answer3)
answer_group.addButton(rb_answer4)

# Мітки для питань та відповідей
lbl_question = QLabel('Запитання')
lbl_rest_time = QLabel('хвилин')
lbl_result = QLabel('Правильно')
lbl_correct_answer = QLabel('відповідь')

# SpinBox для вибору часу відпочинку
spinbox_rest_time = QSpinBox()

# Група для відображення варіантів відповідей
groupbox_answers = QGroupBox('Варіанти відповідей')

# Вкладені вертікальні та горизонтальні лейаути для радіокнопок
layout_v1 = QVBoxLayout()
layout_v2 = QVBoxLayout()
layout_h1 = QHBoxLayout()
layout_v1.addWidget(rb_answer1)
layout_v1.addWidget(rb_answer2)
layout_v2.addWidget(rb_answer3)
layout_v2.addWidget(rb_answer4)

layout_h1.addLayout(layout_v1)
layout_h1.addLayout(layout_v2)

groupbox_answers.setLayout(layout_h1)  # Встановлюємо лейаут для групи варіантів відповідей

# Група для відображення результату відповіді
groupbox_result = QGroupBox()
layout_result = QVBoxLayout()
layout_result.addWidget(lbl_result)
layout_result.addWidget(lbl_correct_answer)
groupbox_result.setLayout(layout_result)
groupbox_result.hide()

# Основні лейаути для компонування всього вікна
layout_main_h1 = QHBoxLayout()
layout_main_h2 = QHBoxLayout()
layout_main_h3 = QHBoxLayout()
layout_main_h4 = QHBoxLayout()
layout_main_v1 = QVBoxLayout()

# Лейаут для кнопок вгорі (меню, відпочинок)
layout_main_h1.addWidget(btn_menu)
layout_main_h1.addStretch(1)
layout_main_h1.addWidget(btn_rest)
layout_main_h1.addWidget(spinbox_rest_time)
layout_main_h1.addWidget(lbl_rest_time)

# Лейаут для питання та варіантів відповідей
layout_main_h2.addWidget(lbl_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_main_h3.addWidget(groupbox_result)
layout_main_h3.addWidget(groupbox_answers)
layout_main_h3.setStretch(1, 1)

# Лейаут для кнопки "Відповісти"
layout_main_h4.addStretch(1)
layout_main_h4.addWidget(btn_next, stretch=2)
layout_main_h4.addStretch(1)

# Збираємо все разом у вертикальний лейаут
layout_main_v1.addLayout(layout_main_h1, stretch=1)
layout_main_v1.addLayout(layout_main_h2, stretch=2)
layout_main_v1.addLayout(layout_main_h3, stretch=8)
layout_main_v1.addLayout(layout_main_h4)
layout_main_v1.setSpacing(5)

# Встановлюємо головний лейаут для вікна
app_window.setLayout(layout_main_v1)
app_window.resize(550, 450)

# Показуємо вікно
app_window.show()

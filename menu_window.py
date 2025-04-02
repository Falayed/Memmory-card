from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

# Основне вікно для меню
menu_window = QWidget()

# Мітки для введення запитань і відповідей
label_question = QLabel('Введіть запитання:')
label_right_answer = QLabel('Введіть вірну відповідь:')
label_wrong_answer1 = QLabel('Введіть першу хибну відповідь')
label_wrong_answer2 = QLabel('Введіть другу хибну відповідь')
label_wrong_answer3 = QLabel('Введіть третю хибну відповідь')

# Поля для введення запитань та відповідей
input_question = QLineEdit()
input_right_answer = QLineEdit()
input_wrong_answer1 = QLineEdit()
input_wrong_answer2 = QLineEdit()
input_wrong_answer3 = QLineEdit()

# Мітка для заголовка статистики
label_stat_header = QLabel('Статистика')
label_stat_header.setStyleSheet('font-size: 19px; font-weight: bold;')

# Мітка для тексту статистики
label_statistic = QLabel()

# Вкладання для міток
labels_layout = QVBoxLayout()
labels_layout.addWidget(label_question)
labels_layout.addWidget(label_right_answer)
labels_layout.addWidget(label_wrong_answer1)
labels_layout.addWidget(label_wrong_answer2)
labels_layout.addWidget(label_wrong_answer3)

# Вкладання для полів введення
inputs_layout = QVBoxLayout()
inputs_layout.addWidget(input_question)
inputs_layout.addWidget(input_right_answer)
inputs_layout.addWidget(input_wrong_answer1)
inputs_layout.addWidget(input_wrong_answer2)
inputs_layout.addWidget(input_wrong_answer3)

# Горизонтальний лейаут для запитання та відповідей
question_layout = QHBoxLayout()
question_layout.addLayout(labels_layout)
question_layout.addLayout(inputs_layout)

# Кнопки для взаємодії
button_back = QPushButton('Назад')
button_add_question = QPushButton('Додати запитання')
button_clear = QPushButton('Очистити')

# Горизонтальний лейаут для кнопок
buttons_layout = QHBoxLayout()
buttons_layout.addWidget(button_add_question)
buttons_layout.addWidget(button_clear)

# Основний вертикальний лейаут для всього вікна
main_layout = QVBoxLayout()
main_layout.addLayout(question_layout)
main_layout.addLayout(buttons_layout)
main_layout.addWidget(label_stat_header)
main_layout.addWidget(label_statistic)
main_layout.addWidget(button_back)

# Встановлюємо основний лейаут для вікна
menu_window.setLayout(main_layout)
menu_window.resize(400, 300)  # Розмір вікна

# Показуємо вікно
menu_window.show()

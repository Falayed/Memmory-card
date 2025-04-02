from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication

# Ініціалізація додатку PyQt
app = QApplication([])

# Імпортування вікон
from main_window import *
from menu_window import *

# Клас, який представляє питання
class Question:
    def __init__(self, question_text, correct_answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question_text = question_text  # Питання
        self.correct_answer = correct_answer  # Правильна відповідь
        self.wrong_answer1 = wrong_answer1  # Перша хибна відповідь
        self.wrong_answer2 = wrong_answer2  # Друга хибна відповідь
        self.wrong_answer3 = wrong_answer3  # Третя хибна відповідь
        self.is_asking = True  # Статус, чи питаємо ще
        self.count_ask = 0  # Лічильник заданих питань
        self.count_right = 0  # Лічильник правильних відповідей

    def got_right(self):
        """Якщо відповідь правильна, збільшуємо лічильник правильних відповідей"""
        self.count_ask += 1
        self.count_right += 1

    def got_wrong(self):
        """Якщо відповідь неправильна, збільшуємо лише лічильник заданих питань"""
        self.count_ask += 1

# Створення екземплярів класу Question
question_1 = Question('Яблуко', 'apple', 'application', 'pineapple', 'apply')
question_2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
question_3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
question_4 = Question('Число', 'number', 'digit', 'amount', 'summary')

# Список для радіокнопок і запитань
radio_buttons = [rb_answer1, rb_answer2, rb_answer3, rb_answer4]
questions = [question_1, question_2, question_3, question_4]

def new_question():
    """Функція для генерації нового питання і випадкового розміщення відповідей"""
    global current_question
    current_question = choice(questions)  # Вибір випадкового питання
    lbl_question.setText(current_question.question_text)  # Виведення питання
    lbl_correct_answer.setText(current_question.correct_answer)  # Виведення правильної відповіді
    shuffle(radio_buttons)  # Перемішуємо відповіді

    # Встановлюємо текст для радіокнопок
    radio_buttons[0].setText(current_question.wrong_answer1)
    radio_buttons[1].setText(current_question.wrong_answer2)
    radio_buttons[2].setText(current_question.wrong_answer3)
    radio_buttons[3].setText(current_question.correct_answer)

# Генерація першого питання
new_question()

def check():
    """Перевірка вибраної відповіді"""
    answer_group.setExclusive(False)  # Дозволяємо перевіряти всі кнопки
    for answer in radio_buttons:
        if answer.isChecked():  # Якщо вибрано варіант відповіді
            if answer.text() == lbl_correct_answer.text():  # Якщо правильна відповідь
                current_question.got_right()  # Відзначаємо правильну відповідь
                lbl_result.setText('Вірно!')  # Виводимо повідомлення про правильну відповідь
                answer.setChecked(False)  # Знімаємо вибір з радіокнопки
                break
    else:
        lbl_result.setText('Не вірно!')  # Якщо відповідь була неправильною
        current_question.got_wrong()  # Відзначаємо неправильну відповідь
    answer_group.setExclusive(True)  # Повертаємо режим для вибору лише одного варіанту

def click_ok():
    """Обробка натискання кнопки 'Відповісти' або 'Наступне запитання'"""
    if btn_next.text() == 'Відповісти':  # Якщо натиснули кнопку 'Відповісти'
        check()  # Перевіряємо відповідь
        groupbox_answers.hide()  # Ховаємо групу з варіантами відповідей
        groupbox_result.show()  # Показуємо результат
        btn_next.setText('Наступне запитання')  # Змінюємо текст на кнопці
    else:  # Якщо натиснули кнопку 'Наступне запитання'
        new_question()  # Генеруємо нове питання
        groupbox_answers.show()  # Показуємо групу з варіантами відповідей
        groupbox_result.hide()  # Ховаємо результат
        btn_next.setText('Відповісти')  # Змінюємо текст на кнопці

# Підключення функції до кнопки 'Наступне запитання'
btn_next.clicked.connect(click_ok)

def rest():
    """Функція для відпочинку (записуємо час відпочинку і чекаємо)"""
    app_window.hide()  # Ховаємо вікно
    rest_time = spinbox_rest_time.value() * 60  # Обчислюємо час відпочинку в секундах
    sleep(rest_time)  # Чекаємо вказаний час
    app_window.show()  # Показуємо вікно після відпочинку

# Підключення функції до кнопки 'Відпочити'
btn_rest.clicked.connect(rest)

def menu_generation():
    """Генерація статистики та відкриття меню"""
    if current_question.count_ask == 0:
        success_rate = 0  # Якщо ще не задавались питання
    else:
        success_rate = (current_question.count_right / current_question.count_ask) * 100  # Обчислюємо успішність

    # Виведення статистики
    statistics_text = f'Разів відповіли: {current_question.count_ask}\n' \
                      f'Вірних відповідей: {current_question.count_right}\n' \
                      f'Успішність: {round(success_rate, 2)}%'
    label_statistic.setText(statistics_text)  # Виводимо статистику
    menu_window.show()  # Показуємо меню
    app_window.hide()  # Ховаємо головне вікно

# Підключення функції до кнопки 'Меню'
btn_menu.clicked.connect(menu_generation)

def back_menu():
    """Функція для повернення до головного вікна"""
    menu_window.hide()  # Ховаємо меню
    app_window.show()  # Показуємо головне вікно

# Підключення функції до кнопки 'Назад'
button_back.clicked.connect(back_menu)

def clear():
    """Очищення полів для введення нових даних"""
    input_question.clear()
    input_right_answer.clear()
    input_wrong_answer1.clear()
    input_wrong_answer2.clear()
    input_wrong_answer3.clear()

# Підключення функції до кнопки 'Очистити'
button_clear.clicked.connect(clear)

def add_question():
    """Додавання нового питання"""
    new_q = Question(input_question.text(), input_right_answer.text(),
                     input_wrong_answer1.text(), input_wrong_answer2.text(),
                     input_wrong_answer3.text())
    questions.append(new_q)  # Додаємо нове питання в список
    clear()  # Очищаємо поля

# Підключення функції до кнопки 'Додати запитання'
button_add_question.clicked.connect(add_question)

# Показуємо головне вікно та запускаємо додаток
app_window.show()
app.exec_()

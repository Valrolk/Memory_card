#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QInputDialog, QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QGroupBox, QButtonGroup, QLineEdit, QTextEdit, QListWidget
from random import *
import json

notes = {

}

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Умные заметки')
main_win.resize(700, 500)
main_win.setStyleSheet("""
    background-color: #f0f0f0;
""")
#блокнот
text = QTextEdit()
text.show()
#текст
list_notes = QLabel('Список заметок')
list_tags = QLabel('Список тегов')
#Ввод
entry = QLineEdit()
entry.setPlaceholderText('Введите тег')

#Лист
notes_window = QListWidget()
tags_win = QListWidget()
#кнопки
btn_add_note = QPushButton('Создать fhdfhd')
btn_del_note = QPushButton('Удалить заметку')
btn_save_note = QPushButton('Сохранить заметку')

btn_notes4 = QPushButton('Добавить к заметке')
btn_notes5 = QPushButton('Открепить от заметки')
btn_notes6 = QPushButton('Искать заметки по тегу')


layout_main0 = QHBoxLayout()
layout_main1 = QVBoxLayout()
layout_main2 = QVBoxLayout()
layout_Edit = QHBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()
layout4 = QHBoxLayout()
layout5 = QHBoxLayout()
layout6 = QHBoxLayout()
layout7 = QHBoxLayout()
layout8 = QHBoxLayout()
layout9 = QHBoxLayout()

layout_Edit.addWidget(text)

layout5.addWidget(list_tags)
layout6.addWidget(tags_win)
layout7.addWidget(entry)
layout8.addWidget(btn_notes4)
layout8.addWidget(btn_notes5)
layout9.addWidget(btn_notes6)

layout1.addWidget(list_notes)
layout2.addWidget(notes_window)
layout3.addWidget(btn_add_note)
layout3.addWidget(btn_del_note)
layout4.addWidget(btn_save_note)

layout_main1.addLayout(layout_Edit)

layout_main2.addLayout(layout1)
layout_main2.addLayout(layout2)
layout_main2.addLayout(layout3)
layout_main2.addLayout(layout4)

layout_main2.addLayout(layout5)
layout_main2.addLayout(layout6)
layout_main2.addLayout(layout7)
layout_main2.addLayout(layout8)
layout_main2.addLayout(layout9)

layout_main0.addLayout(layout_main1)
layout_main0.addLayout(layout_main2)

def show_note():
    key = notes_window.selectedItems()[0].text()
    print(key)
    text.setText(notes[key]["текст"])
    tags_win.clear()
    tags_win.addItems(notes[key]["теги"])

def add_note():
    note_name, ok = QInputDialog.getText(
        notes_window, 'Добавить заметку', 'Название заметки: '
    )
    if ok and note_name != '':
        notes[note_name] = {'текст' : '', 'теги' : []}
        notes_window.addItem(note_name)

def del_note():
    if notes_window.currentItem():
        key = notes_window.currentItem().text()
        del notes[key]
        notes_window.takeItem(notes_window.currentRow())
        with open("f.json", "w", encoding = 'utf-8') as file:
            json.dump(notes, file)
        text.clear()
        tags_win.clear()

def save_note():
    if notes_window.currentItem():
        key = notes_window.currentItem().text()
        notes[key]["текст"] = text.toPlainText()
        with open("f.json", "w", encoding = 'utf-8') as file:
            json.dump(notes, file)

def add_tag():
    if notes_window.currentItem():
        key = notes_window.currentItem().text()
        tag = entry.text()
        if tag not in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            tags_win.addItem(tag)
            entry.clear()
            with open("notes_data.json", "w") as file:
                json.dump(notes, file, sort_keys=True)
        else:
            print("Тег уже существует!")

def del_tag():
    if notes_window.currentItem() and tags_win.currentItem():
        key = notes_window.currentItem().text()
        tag = tags_win.currentItem().text()
        if tag in notes[key]["теги"]:
            notes[key]["теги"].remove(tag)
            tags_win.takeItem(tags_win.currentRow())
            with open("notes_data.json", "w", encoding = 'utf-8') as file:
                json.dump(notes, file, sort_keys=True)
        else:
            print("Тег не найден!")

def search_tag():
    tag = entry.text()
    if tag and btn_notes6.text() == 'Искать заметки по тегу':
        filtered_notes = {key: value for key, value in notes.items() if tag in value["теги"]}
        notes_window.clear()
        notes_window.addItems(filtered_notes)
        btn_notes6.setText("Сбросить поиск")
    else:
        notes_window.clear()
        tags_win.clear()
        entry.clear()
        notes_window.addItems(notes)
        btn_notes6.setText("Искать заметки по тегу")


notes_window.itemClicked.connect(show_note)

with open("f.json", "r", encoding = 'utf-8') as file:
    notes = json.load(file)
notes_window.addItems(notes)


btn_add_note.clicked.connect(add_note)
btn_del_note.clicked.connect(del_note)
btn_save_note.clicked.connect(save_note)
btn_notes4.clicked.connect(add_tag)
btn_notes5.clicked.connect(del_tag)
btn_notes6.clicked.connect(search_tag)

main_win.setLayout(layout_main0)

main_win.show()
app.exec_()



# Парсим файл теха, который открыт
#
# Выдергиваем ласт строчку
#
# Запускаем в latex и вывод направляем в txt файл
#
# сравниваем полученный результат с тем что надо и либо выкидываем сообщение, либо выкидываем ошибку
import os

system = os.uname()[0]

# passwords = {
#     'pass 1': 1,
#     'pass 2': 2,
#     'pass 3': 3
# }

regStatus = False

print('To exit, type \'exit\', otherwise - the password to the next document')

reboot = input("Press Enter to check answer")

while reboot != 'exit':
    try:
        input = open("Overleaf_PDFLaTeX_2.tex", "r", encoding="utf-8")

        text = input.read()

        output = open("OutFile.tex", "w", encoding="utf-8")

        output.write((text.split("Create the expression for the formula presented on the picture~\\ref{fig:Pers_Task_1}:")[1]).split("\\begin{figure}")[0])
        #Получено уравнение пользователя

        os.system("pdflatex OutFile.tex")
        #Компилируем ввод пользователя в Tex
        # Продумать как перенаправить вывод скомпилированного файла в текстовый подготовленный
        # Найти библиотеку перевода такой хуйни в символы
        # Останется сделать сравнение набора символов с шаблоном и вывести результат либо выкинуть ошибку
        # Это масштабируется на все темы!!!


        # file_name = str(passwords[pasw])
        # os.system('pdflatex ' + file_name + '.tex')
        # if system == 'Linux':
        #     os.system('less ' + file_name + '.pdf')
        # else:
        #     os.system(file_name + '.pdf')
        print('Success')
    except KeyError:
        print('Invalid password')

    pasw = input()

regStatus = False

#запуск файла



exec

while not regStatus:

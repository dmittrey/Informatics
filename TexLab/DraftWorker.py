import os
import re

import StatementWorker as sw
import StandartsCreator as sc


def StepWorker(step_name):
    simple_file_name = "Overleaf_PDFLaTeX_" + str(step_name)
    file_name = simple_file_name + ".tex"
    file_pdf_name = simple_file_name + ".pdf"

    if step_name == 2:
        print("\033[32m {}".format("\n\nOpening second LaTeX file..."))
        sc.create_second_standard()
    if step_name == 3:
        print("\033[32m {}".format("\n\nOpening third LaTeX file..."))

        input_for_correct = open("Overleaf_PDFLaTeX_3.tex", "r", encoding="utf-8")
        text = input_for_correct.read()
        input_for_correct.close()

        os.remove("Overleaf_PDFLaTeX_3.tex")
        os.system("echo off > Overleaf_PDFLaTeX_3.tex")

        match = re.search(
            r"([\w\W]+)!!! YOU SHOULD SUBSTITUTE THIS TEXT WITH THE EXPRESSION ACCORDING TO PERSONAL TASK 1 !!!"
            r"([\w\W]+)", text)
        output_for_correct = open("Overleaf_PDFLaTeX_3.tex", "w", encoding="utf-8")
        output_for_correct.write(match.group(1))
        output_for_correct.write(sc.get_second_standard())
        output_for_correct.write(match.group(2))
        output_for_correct.close()

        sc.create_third_standard()
    if step_name == 4:
        print("\033[32m {}".format("\n\nOpening fourth LaTeX file..."))

        input_for_correct = open("Overleaf_PDFLaTeX_4.tex", "r", encoding="utf-8")
        text = input_for_correct.read()
        input_for_correct.close()

        os.remove("Overleaf_PDFLaTeX_4.tex")
        os.system("echo off > Overleaf_PDFLaTeX_4.tex")

        match = re.search(
            r"([\w\W]+)!!! YOU SHOULD SUBSTITUTE THIS TEXT WITH THE EXPRESSION ACCORDING TO PERSONAL TASK 1 !!!"
            r"([\w\W]+)", text)
        output_for_correct = open("Overleaf_PDFLaTeX_4.tex", "w", encoding="utf-8")
        output_for_correct.write(match.group(1))
        output_for_correct.write(sc.get_second_standard())
        output_for_correct.write(match.group(2))
        output_for_correct.close()

        input_for_correct = open("Overleaf_PDFLaTeX_4.tex", "r", encoding="utf-8")
        text = input_for_correct.read()
        input_for_correct.close()

        os.remove("Overleaf_PDFLaTeX_4.tex")
        os.system("echo off > Overleaf_PDFLaTeX_4.tex")

        match = re.search(
            r"([\w\W]+)!!! YOU SHOULD SUBSTITUTE THIS TEXT WITH THE EXPRESSION ACCORDING TO PERSONAL TASK 2 !!!"
            r"([\w\W]+)", text)
        output_for_correct = open("Overleaf_PDFLaTeX_4.tex", "w", encoding="utf-8")
        output_for_correct.write(match.group(1))
        output_for_correct.write(sc.get_third_standard())
        output_for_correct.write(match.group(2))
        output_for_correct.close()

        sc.create_fourth_standard()

    os.system("pdflatex " + file_name + "> nul")  # !!!
    os.system("start " + file_pdf_name)

    print("\033[32m {}".format("Correct " + file_name + " file! Enter the required formula!"))

    files_comparing_status = False
    while not files_comparing_status:
        input("\033[31m {}".format("Press Enter if you are ready to check answer!"))
        files_comparing_status = sw.statement_validator(file_name, step_name, "Validator" + str(step_name) + ".pdf")

    print("\033[32m {}".format("Statement entered correctly!"))
    os.system("del " + simple_file_name + ".aux")
    os.system("del " + simple_file_name + ".log")
    os.system("del " + simple_file_name + ".out")

    os.system("del Validator" + str(step_name) + ".*")


print("\033[32m {}".format("Opening first LaTeX file..."))
os.system("pdflatex Overleaf_PDFLaTeX_1.tex > nul")  # !!!
os.system("start /b Overleaf_PDFLaTeX_1.pdf")

input("\033[31m {}".format("Press Enter to continue!"))

os.system("del Overleaf_PDFLaTeX_1.aux")
os.system("del Overleaf_PDFLaTeX_1.log")

StepWorker(2)

StepWorker(3)

StepWorker(4)

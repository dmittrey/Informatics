import os

import FileComparator as comparator
import re


def statement_checker(input_file, file_number):
    input = open(input_file, "r", encoding="utf-8")
    text = input.read()
    input.close()

    if file_number == 2:
        start_text = "\\documentclass[a4paper]{article}\n\\begin{document}"
        match = re.search(
            r"Create the expression for the formula presented on the picture~\\ref{fig:Pers_Task_1}:([\w\W]+?)\\begin{figure}",
            text)
    elif file_number == 3:
        start_text = "\\documentclass[a4paper]{article}\n\\usepackage{multirow}\n\\usepackage{diagbox}\n\\begin{" \
                     "document}\n"
        match = re.search(
            r"Create a table to be the same as the table presented on the picture~\\ref{tab:Pers_Task_2}:([\w\W]+?)\\begin{figure}",
            text)
    else:
        start_text = "\\documentclass[a4paper]{article}\n\\usepackage{multirow}\n" \
                     "\\usepackage{diagbox}\n\\usepackage{tikz}\n" \
                     "\\usetikzlibrary{automata,positioning}\n\\begin{document}\n"
        match = re.search(
            r"(\\begin{center}\s*\\usetikzlibrary{automata,positioning}[\w\W]+\\end{tikzpicture}\s*}\s*\\end{center})",
            text)

    os.system("echo off > statement.tex")

    end_text = "\\end{document}"

    if match.group(1).strip() != "":
        output = open("statement.tex", "w", encoding="utf-8")
        output.write(start_text)
        output.write(match.group(1))
        output.write(end_text)
        output.close()

        os.system("pdflatex statement.tex > nul")  # !!!

        return True

    return False


def statement_validator(input_file, file_number, standard_file):
    print("Checking the answer...")

    statement_exist_status = statement_checker(input_file, file_number)

    if statement_exist_status:
        comparing_status = comparator.compare_files("statement.pdf", standard_file)

        os.system("del statement.*")

        return comparing_status

    return False

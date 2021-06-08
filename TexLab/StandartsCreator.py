import os


def get_second_standard():
    return "$f(x) = \\frac{A_0}{2} + A_n*\\cos(\\frac{2 n \\pi x}{\\nu} - \\alpha_n)$"


def get_third_standard():
    return "\\begin{table}[h!]\n\\begin{center}\n\\begin{tabular}{|ll|l|ll|}\n\\hline\n" \
           "                       &  &  &                       &  \\\\ \\cline{2-4}\n" \
           "\\multicolumn{1}{|l|}{} &  &  & \\multicolumn{1}{l|}{} &  \\\\ \\hline\n" \
           "\\multicolumn{1}{|l|}{} &  &  & \\multicolumn{1}{l|}{} &  \\\\ \\hline\n" \
           "\\multicolumn{1}{|l|}{} &  &  & \\multicolumn{1}{l|}{} &  \\\\ \\hline\n" \
           "\\multicolumn{1}{|l|}{} &  &  & \\multicolumn{1}{l|}{} &  \\\\ \\hline\n" \
           "\\end{tabular}\n" \
           "\\end{center}\n" \
           "\\end{table}\n"


def get_fourth_standard():
    return "\\begin{center}" \
           "\n\\usetikzlibrary{automata, positioning}\n\\fbox{" \
           "\\begin{tikzpicture}[shorten >= 1pt, node distance=3.5cm, on grid, auto]\n" \
           "\\node[state](b_1) {$b_1$};\n\\node[state, right = of b_1] (b_2) {$b_2$};\n" \
           "\\node[state, right = of b_2] (b_3) {$b_3$};\n\\node[state, below = of b_1] (b_4) {$b_4$};\n" \
           "\\node[state, below = of b_2] (b_5) {$b_5$};\n\\node[state, below = of b_3] (b_6) {$b_6$};\n" \
           "\\path[->, -latex] (b_1) edge[loop left] node {$z_1$} ()\nedge node {$z_3$} (b_2)\n" \
           "(b_2) edge[loop above] node {$z_2$} ()\nedge node[near start] {$z_1$} (b_6)\n(b_3) edge node[above] {" \
           "$z_2$} (b_2)\nedge[bend left] node {$z_1$} (b_6)\n(b_4)edge[loop left] node {$z_3$} ()\nedge node {" \
           "$z_1$} (b_1)\nedge node {$z_0$} (b_2)\n(b_5) edge node {$z_2$} (b_4)\nedge node[near start] {$z_3$} (b_3)\n" \
           "edge[loop above] node {}() (b_6)\nedge[bend left] node {$z_2$} (b_4)\nedge node {$z_3$} (b_3);\n\\end{" \
           "tikzpicture}\n}\n\\end{center}"


def create_second_standard():
    text = "\\documentclass[a4paper]{article}\n\\begin{document}" + get_second_standard() + "\\end{document}"

    os.system("echo off > Validator2.tex")

    output = open("Validator2.tex", "w", encoding="utf-8")
    output.write(text)
    output.close()

    os.system("pdflatex Validator2.tex > nul")  # !!!


def create_third_standard():
    text = "\\documentclass[a4paper]{article}\n\\usepackage{multirow}\n\\usepackage{diagbox}\n\\begin{document}\n" + \
           get_third_standard() + "\\end{document}\n"

    os.system("echo off > Validator3.tex")

    output = open("Validator3.tex", "w", encoding="utf-8")
    output.write(text)
    output.close()

    os.system("pdflatex Validator3.tex > nul")  # !!!


def create_fourth_standard():
    text = "\\documentclass[a4paper]{article}\n\\usepackage{multirow}\n" \
           "\\usepackage{diagbox}\n\\usepackage{tikz}\n" \
           "\\usetikzlibrary{automata,positioning}\n\\begin{document}\n" + get_fourth_standard() + "\\end{document}\n"

    os.system("echo off > Validator4.tex")

    output = open("Validator4.tex", "w", encoding="utf-8")
    output.write(text)
    output.close()

    os.system("pdflatex Validator4.tex > nul")  # !!!

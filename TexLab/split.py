input = open("Overleaf_PDFLaTeX_2.tex","r",encoding="utf-8")

text = input.read()

output = open("OutFile.tex", "w", encoding="utf-8")

output.write(
            (text.split("Create the expression for the formula presented on the picture~\\ref{fig:Pers_Task_1}:")[1]).split("\\begin{figure}")[0])
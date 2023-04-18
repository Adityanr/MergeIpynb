import nbformat

#read first ipynb file
with open("first.ipynb", "r", encoding="utf-8") as f1:
    nb1 = nbformat.read(f1, nbformat.NO_CONVERT)

#read second ipynb file
with open("second.ipynb", "r", encoding="utf-8") as f2:
    nb2 = nbformat.read(f2, nbformat.NO_CONVERT)

#read third ipynb file
with open("third.ipynb", "r", encoding="utf-8") as f3:
    nb3 = nbformat.read(f3, nbformat.NO_CONVERT)
    
#append second ipynb file cells to first one
for cell in nb2.cells:
    nb1.cells.append(cell)
    
#append third ipynb file cells to first one
for cell in nb3.cells:
    nb1.cells.append(cell)

#add merged cells to new notebook
merged_nb = nbformat.v4.new_notebook()
merged_nb["cells"] = nb1.cells

#write to new notebook
with open("final.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(merged_nb, f)


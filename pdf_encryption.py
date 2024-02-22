import pikepdf
from tkinter.filedialog import *

pdf = askopenfilename()

old_pdf = pikepdf.Pdf.open(pdf)

no_extr = pikepdf.Permissions(extract=False)

file = input("choose a name for saving file \'Without \' .pdf  = ")
file1 = file+".pdf"
password = input("Choose a strong Password = ")
old_pdf.save(file1,encryption = pikepdf.Encryption(user=password,owner="me",allow=no_extr))

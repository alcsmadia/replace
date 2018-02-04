# -*- coding: utf-8_sig -*-
import os, tkinter, tkinter.filedialog

# 置換文字の指定
before = input("from: ")
after = input("to: ")

# ファイル選択
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

data = open(file, "r", encoding="utf-8_sig")
fout = open("result.txt", "w", encoding="shift-jis")


# 置換処理
for line in data:
    result = line.replace(before, after)
    fout.writelines(result)
fout.close() # result.txtファイルを閉じる

print("Finish!")
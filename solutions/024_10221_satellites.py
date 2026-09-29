"""
UVA 10221 - Satellites

題目中文意思：
已知地球表面上方高度 s 與中心角 a，計算弧長與弦長；角度可能是 degree 或 minute。

這題需要什麼資料：
多組 s a unit；地球半徑固定 6440。

解法重點：
minute 要除以 60 變 degree；大於 180 度取較小角 360-a；再轉弧度計算。

寫程式時可以照這個順序想：
1. 先把輸入讀進來，確認是一行一組、第一行有測資數，還是讀到 EOF。
2. 把題目要的規則轉成變數、迴圈、判斷式或函式。
3. 按照題目指定格式輸出，CPE/UVA 很常因為空格、空行、大小寫錯而 WA。
"""

# ===== 程式開始 =====
# 下面保留可以直接提交的 Python 解答。
# 註解會寫「這行在做什麼」以及「為什麼要這樣做」，
# 你用 Cursor 看時，可以先讀上面的題目說明，再對照下面程式。

# 匯入 sys：CPE/UVA 常用 sys.stdin 讀輸入，速度快，也能自然讀到 EOF。
import sys
# 匯入 math：需要 sqrt、sin、radians、isqrt 這類數學函式時使用。
import math

R = 6440
# 逐行讀到 EOF：不知道有幾筆測資時最常用這種寫法。
for line in sys.stdin:
    s, a, unit = line.split()
    radius = R + float(s)
    angle = float(a)
    # if 判斷題目的特殊情況或規則分支。
    if unit == "min":
        angle /= 60
    # if 判斷題目的特殊情況或規則分支。
    if angle > 180:
        angle = 360 - angle
    rad = math.radians(angle)
    arc = radius * rad
    chord = 2 * radius * math.sin(rad / 2)
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(f"{arc:.6f} {chord:.6f}")

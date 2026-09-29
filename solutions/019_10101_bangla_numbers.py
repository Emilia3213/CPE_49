"""
UVA 10101 - Bangla Numbers

題目中文意思：
把整數轉成 Bangla 計數單位格式：kuti, lakh, hajar, shata。

這題需要什麼資料：
多行非負整數；每行輸出編號加轉換結果。

解法重點：
每 7 位會重複 kuti；遞迴處理高位，再處理 lakh/hajar/shata/個位。

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

# def 定義函式，把會重複使用的邏輯整理起來。
def bangla(n):
    parts = []
    # if 判斷題目的特殊情況或規則分支。
    if n >= 10000000:
        parts += bangla(n // 10000000)
        parts.append("kuti")
        n %= 10000000
    # if 判斷題目的特殊情況或規則分支。
    if n >= 100000:
        parts += [str(n // 100000), "lakh"]
        n %= 100000
    # if 判斷題目的特殊情況或規則分支。
    if n >= 1000:
        parts += [str(n // 1000), "hajar"]
        n %= 1000
    # if 判斷題目的特殊情況或規則分支。
    if n >= 100:
        parts += [str(n // 100), "shata"]
        n %= 100
    # if 判斷題目的特殊情況或規則分支。
    if n:
        parts.append(str(n))
    # return 把函式算出的結果交回呼叫它的地方。
    return parts

# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for case, line in enumerate(sys.stdin, 1):
    n = int(line)
    parts = bangla(n) if n else ["0"]
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(f"{case:4d}. {' '.join(parts)}")

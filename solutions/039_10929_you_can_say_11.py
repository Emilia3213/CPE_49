"""
UVA 10929 - You can say 11

題目中文意思：
判斷大整數是否為 11 的倍數。

這題需要什麼資料：
多行數字字串，以 0 結束。

解法重點：
交錯位數和差若可被 11 整除，原數可被 11 整除。

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

# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for s in sys.stdin.read().split():
    # if 判斷題目的特殊情況或規則分支。
    if s == "0":
        # break 代表題目的結束條件成立，離開目前迴圈。
        break
    odd = sum(int(s[i]) for i in range(0, len(s), 2))
    even = sum(int(s[i]) for i in range(1, len(s), 2))
    # if 判斷題目的特殊情況或規則分支。
    if (odd - even) % 11 == 0:
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"{s} is a multiple of 11.")
    # else 處理前面條件都不成立時的情況。
    else:
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"{s} is not a multiple of 11.")

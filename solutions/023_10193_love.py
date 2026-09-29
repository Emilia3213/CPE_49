"""
UVA 10193 - All You Need Is Love

題目中文意思：
兩個二進位數若轉十進位後最大公因數大於 1，就代表有共同因子。

這題需要什麼資料：
第一行測資數；每組兩行二進位字串。

解法重點：
int(s, 2) 轉換後用 gcd。

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
# gcd 用來求最大公因數，直接用內建函式比自己寫更快更不容易錯。
from math import gcd

# splitlines() 逐行保留資料，適合每一行都有意義的題目。
lines = sys.stdin.read().splitlines()
t = int(lines[0])
p = 1
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for case in range(1, t + 1):
    a = int(lines[p], 2)
    b = int(lines[p + 1], 2)
    p += 2
    # if 判斷題目的特殊情況或規則分支。
    if gcd(a, b) > 1:
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"Pair #{case}: All you need is love!")
    # else 處理前面條件都不成立時的情況。
    else:
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"Pair #{case}: Love is not all you need!")

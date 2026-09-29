"""
UVA 10035 - Primary Arithmetic

題目中文意思：
計算兩個非負整數直式加法時產生幾次進位。

這題需要什麼資料：
多組 a b，以 `0 0` 結束。

解法重點：
從個位數往前加，記錄 carry，每次和 >=10 就多一次進位。

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

# 逐行讀到 EOF：不知道有幾筆測資時最常用這種寫法。
for line in sys.stdin:
    a, b = line.split()
    # if 判斷題目的特殊情況或規則分支。
    if a == "0" and b == "0":
        # break 代表題目的結束條件成立，離開目前迴圈。
        break
    i, j, carry, ans = len(a) - 1, len(b) - 1, 0, 0
    # while 迴圈適合「做到某個條件成立為止」的模擬題。
    while i >= 0 or j >= 0:
        da = ord(a[i]) - 48 if i >= 0 else 0
        db = ord(b[j]) - 48 if j >= 0 else 0
        carry = 1 if da + db + carry >= 10 else 0
        ans += carry
        i -= 1
        j -= 1
    # if 判斷題目的特殊情況或規則分支。
    if ans == 0:
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print("No carry operation.")
    # elif 是第二種判斷情況，讓不同規則分開處理。
    elif ans == 1:
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print("1 carry operation.")
    # else 處理前面條件都不成立時的情況。
    else:
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"{ans} carry operations.")

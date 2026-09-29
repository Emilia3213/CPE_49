"""
UVA 10093 - An Easy Problem!

題目中文意思：
給一串由 0-9、A-Z、a-z 組成的數，找最小進位 base，使這個數能被 base-1 整除。

這題需要什麼資料：
多行字串，讀到 EOF；忽略非英數字元。

解法重點：
字元值最大值 + 1 是最低 base；base 範圍至少 2 到 62。利用 N mod (base-1) 等於各位值總和 mod (base-1)。

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
def val(ch):
    # if 判斷題目的特殊情況或規則分支。
    if ch.isdigit():
        # return 把函式算出的結果交回呼叫它的地方。
        return ord(ch) - ord("0")
    # if 判斷題目的特殊情況或規則分支。
    if "A" <= ch <= "Z":
        # return 把函式算出的結果交回呼叫它的地方。
        return ord(ch) - ord("A") + 10
    # if 判斷題目的特殊情況或規則分支。
    if "a" <= ch <= "z":
        # return 把函式算出的結果交回呼叫它的地方。
        return ord(ch) - ord("a") + 36
    return -1

# 逐行讀到 EOF：不知道有幾筆測資時最常用這種寫法。
for line in sys.stdin:
    digits = [val(ch) for ch in line.strip() if val(ch) >= 0]
    # if 判斷題目的特殊情況或規則分支。
    if not digits:
        # continue 代表跳過這一輪，直接讀下一行或下一筆資料。
        continue
    start = max(2, max(digits) + 1)
    s = sum(digits)
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for base in range(start, 63):
        # if 判斷題目的特殊情況或規則分支。
        if s % (base - 1) == 0:
            # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
            print(base)
            # break 代表題目的結束條件成立，離開目前迴圈。
            break
    # else 處理前面條件都不成立時的情況。
    else:
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print("such number is impossible!")

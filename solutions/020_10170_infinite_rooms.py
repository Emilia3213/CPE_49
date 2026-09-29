"""
UVA 10170 - The Hotel with Infinite Rooms

題目中文意思：
第 1 天住 S 人，之後每天人數加 1，找累積人數第一次達到或超過 D 的那天人數。

這題需要什麼資料：
多組 S D，讀到 EOF。

解法重點：
從 S 開始累加直到 sum >= D。數字不大時最直觀，也可用公式；這裡用 while 容易記。

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
    s, d = map(int, line.split())
    total = 0
    day_people = s
    # while 迴圈適合「做到某個條件成立為止」的模擬題。
    while total < d:
        total += day_people
        # if 判斷題目的特殊情況或規則分支。
        if total >= d:
            # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
            print(day_people)
            # break 代表題目的結束條件成立，離開目前迴圈。
            break
        day_people += 1

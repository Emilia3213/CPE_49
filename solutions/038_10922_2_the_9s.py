"""
UVA 10922 - 2 the 9s

題目中文意思：
判斷大整數是否為 9 的倍數；若是，計算反覆各位數相加到 9 需要幾層，稱為 9-degree。

這題需要什麼資料：
多行數字字串，以 0 結束。

解法重點：
數位和不是 9 倍數就不是；是的話反覆 digit sum 計 degree。

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
    total = sum(map(int, s))
    # if 判斷題目的特殊情況或規則分支。
    if total % 9 != 0:
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"{s} is not a multiple of 9.")
    # else 處理前面條件都不成立時的情況。
    else:
        degree = 1
        # while 迴圈適合「做到某個條件成立為止」的模擬題。
        while total != 9:
            total = sum(map(int, str(total)))
            degree += 1
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"{s} is a multiple of 9 and has 9-degree {degree}.")

"""
UVA 12019 - Doom's Day Algorithm

題目中文意思：
給 2011 年的月日，輸出那天是星期幾。

這題需要什麼資料：
第一行測資數；每組 month day。

解法重點：
直接用 2011 年每月天數累積，已知 2011/1/1 是 Saturday。

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

days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 一次讀完所有整數：適合輸入格式固定、只需要照順序取數字的題目。
data = list(map(int, sys.stdin.read().split()))
t, p = data[0], 1
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for _ in range(t):
    m, d = data[p], data[p + 1]; p += 2
    day_of_year = sum(month_days[:m-1]) + d
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(days[day_of_year % 7])

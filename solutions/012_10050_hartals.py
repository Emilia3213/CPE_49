"""
UVA 10050 - Hartals

題目中文意思：
多個政黨每隔 h 天罷工，計算 n 天內有多少工作日受罷工影響；週五、週六不算。

這題需要什麼資料：
第一行測資數；每組 n、政黨數 p、接著 p 個 hartal 參數。

解法重點：
逐天檢查是否非週末且能被任一 h 整除。UVA 的第 6、7 天是週五、週六。

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

# 一次讀完所有整數：適合輸入格式固定、只需要照順序取數字的題目。
data = list(map(int, sys.stdin.read().split()))
t, p = data[0], 1
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for _ in range(t):
    n = data[p]; parties = data[p + 1]; p += 2
    hs = data[p:p+parties]; p += parties
    lost = 0
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for day in range(1, n + 1):
        # if 判斷題目的特殊情況或規則分支。
        if day % 7 in (6, 0):
            # continue 代表跳過這一輪，直接讀下一行或下一筆資料。
            continue
        # if 判斷題目的特殊情況或規則分支。
        if any(day % h == 0 for h in hs):
            lost += 1
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(lost)

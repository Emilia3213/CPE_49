"""
UVA 10226 - Hardwood Species

題目中文意思：
統計每種樹名在森林資料中的百分比。

這題需要什麼資料：
第一行測資數，空白行分隔測資；每組多行樹名。

解法重點：
每組用 Counter 計數，按樹名字典序輸出比例到小數四位。

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
# Counter 是計數工具，適合統計字母、樹名、國家等出現次數。
from collections import Counter

text = sys.stdin.read().splitlines()
t = int(text[0])
idx = 1
# while 迴圈適合「做到某個條件成立為止」的模擬題。
while idx < len(text) and text[idx] == "":
    idx += 1
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for case in range(t):
    cnt = Counter()
    total = 0
    # while 迴圈適合「做到某個條件成立為止」的模擬題。
    while idx < len(text) and text[idx] != "":
        cnt[text[idx]] += 1
        total += 1
        idx += 1
    # if 判斷題目的特殊情況或規則分支。
    if case:
        # 題目要求測資之間空一行時，直接 print() 輸出空白行。
        print()
    # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
    for name in sorted(cnt):
        # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
        print(f"{name} {cnt[name] * 100 / total:.4f}")
    # while 迴圈適合「做到某個條件成立為止」的模擬題。
    while idx < len(text) and text[idx] == "":
        idx += 1

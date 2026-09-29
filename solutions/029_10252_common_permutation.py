"""
UVA 10252 - Common Permutation

題目中文意思：
找兩個字串共同擁有的字母，依字母順序輸出，每個字母次數取兩邊較小值。

這題需要什麼資料：
每兩行一組字串，讀到 EOF。

解法重點：
Counter 交集後按字母排序。

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

# splitlines() 逐行保留資料，適合每一行都有意義的題目。
lines = sys.stdin.read().splitlines()
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for i in range(0, len(lines), 2):
    a = Counter(lines[i])
    b = Counter(lines[i + 1])
    common = a & b
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print("".join(ch * common[ch] for ch in sorted(common)))

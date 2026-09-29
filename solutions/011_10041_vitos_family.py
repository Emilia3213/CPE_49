"""
UVA 10041 - Vito's family

題目中文意思：
找一個街號讓所有親戚到該處的距離總和最小。

這題需要什麼資料：
第一行測資數；每組第一個數是親戚數 r，後面 r 個街號。

解法重點：
一維絕對距離總和最小點是中位數。

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
    r = data[p]; p += 1
    streets = sorted(data[p:p+r]); p += r
    mid = streets[r // 2]
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(sum(abs(x - mid) for x in streets))

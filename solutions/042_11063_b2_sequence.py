"""
UVA 11063 - B2-Sequence

題目中文意思：
判斷序列是否為 B2：正整數、嚴格遞增，且任兩項 i<=j 的和都不重複。

這題需要什麼資料：
多組資料，每組 n 後接 n 個數。

解法重點：
先檢查遞增與正數，再用 set 檢查所有 pair sum。

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
p = 0
case = 1
# while 迴圈適合「做到某個條件成立為止」的模擬題。
while p < len(data):
    n = data[p]; p += 1
    arr = data[p:p+n]; p += n
    ok = all(arr[i] > 0 and (i == 0 or arr[i] > arr[i-1]) for i in range(n))
    seen = set()
    # if 判斷題目的特殊情況或規則分支。
    if ok:
        # for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
        for i in range(n):
            for j in range(i, n):
                s = arr[i] + arr[j]
                # if 判斷題目的特殊情況或規則分支。
                if s in seen:
                    ok = False
                    # break 代表題目的結束條件成立，離開目前迴圈。
                    break
                seen.add(s)
            # if 判斷題目的特殊情況或規則分支。
            if not ok:
                # break 代表題目的結束條件成立，離開目前迴圈。
                break
    # print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
    print(f"Case #{case}: It is {'a' if ok else 'not a'} B2-Sequence.")
    # 題目要求測資之間空一行時，直接 print() 輸出空白行。
    print()
    case += 1

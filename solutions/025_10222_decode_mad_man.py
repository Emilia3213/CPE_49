"""
UVA 10222 - Decode the Mad man

題目中文意思：
把輸入字元換成鍵盤上左邊第二個鍵，還原打錯位置的文字。

這題需要什麼資料：
任意文字到 EOF；保留換行。

解法重點：
建立鍵盤字串，每個可見字元找 index 後輸出 index-2 的字。

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

keys = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
pos = {ch: i for i, ch in enumerate(keys)}
out = []
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for ch in sys.stdin.read():
    low = ch.lower()
    # if 判斷題目的特殊情況或規則分支。
    if low in pos and pos[low] >= 2:
        out.append(keys[pos[low] - 2])
    # else 處理前面條件都不成立時的情況。
    else:
        out.append(ch)
# print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
print("".join(out), end="")

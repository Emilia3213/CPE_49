"""
UVA 272 - TeX Quotes

題目中文意思：
把文章中的雙引號依序替換成 TeX 的左引號 `` 與右引號 ''。

這題需要什麼資料：
任意多行文字，保留其他字元與換行。

解法重點：
遇到 `"` 時用布林值交替輸出開引號與關引號。

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

open_quote = True
out = []
# for 迴圈用來逐筆處理測資、逐格檢查，或跑完整個範圍。
for ch in sys.stdin.read():
    # if 判斷題目的特殊情況或規則分支。
    if ch == '"':
        out.append("``" if open_quote else "''")
        open_quote = not open_quote
    # else 處理前面條件都不成立時的情況。
    else:
        out.append(ch)
# print 負責輸出答案；字串格式要完全符合題目，空格和大小寫都很重要。
print("".join(out), end="")

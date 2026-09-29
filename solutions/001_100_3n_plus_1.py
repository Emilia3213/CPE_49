"""
UVA 100 - The 3n + 1 problem

題目中文意思：
給你兩個整數 i 和 j，請看 i 到 j 之間每一個數字的 3n+1 循環長度，
最後輸出這個區間裡「最大的循環長度」。

3n+1 規則：
1. 如果 n 是奇數，下一個數字變成 3*n + 1
2. 如果 n 是偶數，下一個數字變成 n / 2
3. 一直做到 n 變成 1 為止
4. 循環長度 = 從原本的 n 到 1 總共出現幾個數字

例子：
n = 22
22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
所以 22 的循環長度是 16。

輸入：
每一行有兩個整數 i j，可能有很多行，讀到 EOF 結束。

輸出：
每一行輸出：原本的 i 原本的 j 區間內最大循環長度
注意：就算 i > j，輸出時也要照原本輸入順序印出 i j。

解法：
1. 對區間 min(i,j) 到 max(i,j) 每個數字都算 cycle length。
2. 取最大的 cycle length。
3. 使用 cache 記憶化，算過的數字不用再重算，速度會快很多。
"""

import sys


# cache 用來記錄「某個數字的循環長度」。
# 因為很多數字在做 3n+1 時會走到同樣的中間數字，
# 例如 22 會走到 11，別的數字也可能走到 11。
# 如果 11 的答案已經算過，就可以直接拿來用，不用整段重算。
cache = {1: 1}  # 1 的循環長度就是 1，這是遞迴停止點。


def cycle_len(n):
    """回傳 n 的 3n+1 循環長度。"""

    # 如果 n 已經算過，直接回傳。
    # 這就是「記憶化」：用空間換時間，避免重複計算。
    if n in cache:
        return cache[n]

    # 題目規則：奇數下一步是 3*n + 1。
    # 目前這個 n 也算一個數字，所以長度要 +1。
    if n % 2 == 1:
        cache[n] = 1 + cycle_len(3 * n + 1)

    # 題目規則：偶數下一步是 n / 2。
    # Python 的 // 是整數除法，這裡要用 //，不要用 /，
    # 因為 / 會變成小數 float，後面當整數處理會比較麻煩。
    else:
        cache[n] = 1 + cycle_len(n // 2)

    return cache[n]


# sys.stdin 會一行一行讀取輸入，適合 UVA / CPE 這種「讀到 EOF」的題目。
for line in sys.stdin:
    # 避免空白行造成 split 後沒有資料。
    if not line.strip():
        continue

    # map(int, line.split())：
    # line.split() 先把一行切成字串，例如 "1 10" -> ["1", "10"]
    # map(int, ...) 再把它們轉成整數。
    a, b = map(int, line.split())

    # 題目要求 i 到 j 的區間，但輸入可能是 10 1。
    # 所以計算時要用小的當開頭、大的當結尾。
    lo, hi = min(a, b), max(a, b)

    # 逐一計算區間內每個 x 的循環長度，max 取最大值。
    # range(lo, hi + 1) 要 +1，因為 Python range 的尾端不包含 hi。
    ans = max(cycle_len(x) for x in range(lo, hi + 1))

    # 輸出時必須印原本輸入的 a b，不能印排序後的 lo hi。
    print(a, b, ans)

count = 0

def max_joltage_from_bank(bank: str, k: int = 12) -> int:
    s = bank.strip()

   
    if len(s) <= k:
        return int(s) if s else 0

    to_remove = len(s) - k  
    stack = []

    for ch in s:
        while to_remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)

    if to_remove > 0:
        stack = stack[:-to_remove]

    result_str = "".join(stack[:k])
    return int(result_str)

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:

        count += max_joltage_from_bank(line ,k = 2)
print(count)


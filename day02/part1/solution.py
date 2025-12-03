with open("input.txt", "r") as file:
    content = file.read().strip() 

ranges = content.split(",")

range_list = [list(map(int, range.split("-"))) for range in ranges]

def is_invalid_id(n: int) -> bool:
    s = str(n)
    
    if len(s) % 2 != 0:
        return False
    
    mid = len(s) // 2
    first = s[:mid]
    second = s[mid:]
    
    return first == second

def invalid_ids_in_range(start: int, end: int) -> list:
    return [n for n in range(start, end + 1) if is_invalid_id(n)]

count = 0

for start, end in range_list:
    invalids = invalid_ids_in_range(start, end)
    for invalid in invalids:
        count += invalid

print(count)



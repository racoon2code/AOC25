import operator

def parse_columns(input_string: str) -> dict:
    number_rows = []
    operator_rows = []

    for line in input_string.splitlines():
        tokens = line.split()
        if not tokens:
            continue

        if all(not t.isdigit() for t in tokens):
            operator_rows.append(tokens)
        else:
            nums = [int(t) for t in tokens if t.isdigit()]
            number_rows.append(nums)

    number_cols = list(map(list, zip(*number_rows)))

    if operator_rows:
        operator_cols = list(map(list, zip(*operator_rows)))
    else:
        operator_cols = []

    return {
        "numbers": number_cols,
        "operators": operator_cols
    }

with open("input.txt", "r", encoding="utf-8") as f:
    content = f.read()             
    math_problem = parse_columns(content)

grand_total = 0

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

for index, number in enumerate(math_problem["numbers"]):
    total = 0
    
    op = math_problem["operators"][index][0]    

    for idx, i in enumerate(number):
        
        if idx == 0:
            total = i

        else:        
         total = OPS[op](total, i)

    grand_total += total
    
   
print(grand_total)
      
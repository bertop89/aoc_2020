def find_innermost_parenthesis(expr):
    max_level = current_level = 0
    for idx, char in enumerate(expr):
        if char == '(':
            current_level +=1
            start = idx
        elif char == ')':
            if current_level > max_level:
                max_level = current_level
                max_seq = (start+1, idx)
            current_level -=1
    if max_level == 0:
        return None
    else:
        return max_seq

# part 1

def eval_expression(expr):
    while True:
        inner_par = find_innermost_parenthesis(expr)
        if inner_par:
            splited = expr[inner_par[0]:inner_par[1]].split(" ")
        else:
            splited = expr.split(" ")
        splited = [x for x in splited if x != '']
        result = int(splited[0])
        idx = 1
        while idx < len(splited):
            if splited[idx] == '+':
                result = result + int(splited[idx+1])
            elif splited[idx] == "*":
                result = result * int(splited[idx+1])
            idx += 2
        if not inner_par:
            return result
        expr = expr[:inner_par[0]-1] + ' ' + str(result) + ' ' + expr[inner_par[1]+1:]

results = []
with open("input.txt", 'r') as file:
    for line in file.readlines():
        results.append(eval_expression(line[:-1]))
print(sum(results))

# part 2

def eval_expression(expr):
    while True:
        inner_par = find_innermost_parenthesis(expr)
        if inner_par:
            splited = expr[inner_par[0]:inner_par[1]].split(" ")
        else:
            splited = expr.split(" ")
        splited = [x for x in splited if x != '']
        while '+' in splited:
            found = splited.index('+')
            result = int(splited[found-1]) + int(splited[found+1])
            splited = splited[:max(0, found-1)] + [str(result)] + splited[found+2:]
        while '*' in splited:
            found = splited.index('*')
            result = int(splited[found - 1]) * int(splited[found + 1])
            splited = splited[:max(0, found - 1)] + [str(result)] + splited[found + 2:]
        if not inner_par:
            return result
        expr = expr[:inner_par[0]-1] + ' ' + str(result) + ' ' + expr[inner_par[1]+1:]

results = []
with open("input.txt", 'r') as file:
    for line in file.readlines():
        results.append(eval_expression(line[:-1]))
print(results)
print(sum(results))

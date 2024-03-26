symbol = {'|':1, '&':2, '>':3, ',':4, '[':5, ']':6, '(':7, ')':8, '∀':9, '∃':10}

# a function to get the list of variables in string list
def variables_list(v):
    result = set()
    # for each string if there is a variable append it in result
    for s in v:
        s = s.replace(' ', '')
        l = 0
        r = 0
        i = 0
        while i < len(s):
            if s[i] in symbol:
                i += 1
                continue
            l = i
            r = i
            while(r < len(s) and not s[r] in symbol):
                i += 1
                r += 1
            #print(r)
            if(r == len(s) or s[r] != '('):
                result.add(s[l:r])
            i += 1
    return list(result)

"""def variables_list_test():
    v = ['a', 'Ahmed|eats(x, y)', '∃x[eats(x, y)]']
    print(variables_list(v))"""

#variables_list_test()

def eliminate_implication(s):
    s = s.replace(" ", "")
    formula = ""
    for char in s:
        if char == '>':
            formula += '|'
        else:
            formula += char
    index = formula.index('|')

    open_bracket = None
    for i in range(index - 1, -1, -1):
        if formula[i] == ']':
            open_bracket = i
        elif formula[i] == '[':
            if open_bracket is not None:
                formula = formula[:i] + '~' + formula[i:open_bracket] + formula[open_bracket:]
                break  # Stop after adding '~' before the '['
        elif formula[i] == ')':
            open_bracket = i
            #not completed 
                
    return formula

s = "[eat(x) > play(y)]"
res = eliminate_implication(s)
print(res)

def move_negation_inward(formula):
    formula = formula.replace(" ", "")
    formula = formula.replace("~~", "")  # Remove double negations
    
    while "~[" in formula:
        start_index = formula.index("~[")
        end_index = start_index + 2  # Start from the character after "~("
        count = 1
        while count != 0 and end_index < len(formula):
            if formula[end_index] == "[":
                count += 1
            elif formula[end_index] == "]":
                count -= 1
            end_index += 1
        # sub_formula: the formula after the negation '~[' and before the closing parenthesis ']'
        sub_formula = formula[start_index + 2 : end_index - 1]
        negated_sub_formula = ""

        for char in sub_formula:
            if char == "|":
                negated_sub_formula += "&"
            elif char == "&":
                negated_sub_formula += "|"
            elif char == "[":
                negated_sub_formula += "~["
            elif char == "]":
                negated_sub_formula += "]"
            elif char == "~":
                negated_sub_formula += ""
            else:
                negated_sub_formula += "~" + char

        formula = formula[:start_index] + formula[end_index:]
    return formula

formula = "~[eat(x) | play(y)]" 
result = move_negation_inward(formula)
print(result)

def standardize(formula):
    None
def Move_to_the_left(formula):
    None


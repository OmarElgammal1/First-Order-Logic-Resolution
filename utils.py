symbol = {'|':1, '&':2, '>':3, ',':11, '[':5, ']':6, '∀':7, '∃':8, '(':9, ')':10}

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

def eliminate_implication(formulas):
    result = []
    for s in formulas:
        s = s.replace(" ", "")
        formula = ""
        for x in range(len(s)):
            if s[x] == '>':
                s = s[:x] + '|' + s[x + 1:]
                i = x - 1
                open = 0
                if(s[x - 1] == ']'):
                        open += 1
                        while(open != 0):
                            i -= 1
                            if(s[i] == ']'):
                                open += 1
                            elif(s[i] == '['):
                                open -= 1
                else:
                    while(i >= 0 and not (s[i] in symbol.keys() and symbol[s[i]] < 9)):
                        i -= 1
                    i += 1
                s = s[:i] + '~' + s[i:]
        result.append(s)
    return result

# s = ["[eat(x) > play(y)]", "[~[eat(x) ^ y] > play(y)]>"]
# res = eliminate_implication(s)
# for i in range(len(s)):
#     print(s[i], " ----> ", res[i])

def remove_double_not(formulas):
    for f in formulas:
        f = f.replace(" ", "")
        f = f.replace("~~", "")  # Remove double negations
    return formulas

def move_negation_inward(formulas: list[str]):
    formulas = remove_double_not(formulas)
    for formula in formulas:
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
    return formulas

# formula = "~[eat(x) | play(y)]" 
# result = move_negation_inward(formula)
# print(result)

def standardize(formula):
    None
def Move_to_the_left(formula):
    None


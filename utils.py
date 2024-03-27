import re
import random
import string
symbol = {'~':0, '|':1, '&':2, '>':3, ',':11, '[':5, ']':6, '∀':7, '∃':8, '(':9, ')':10}

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
    v = ['a', 'Ahmed|eats(x, y)', 'x[eats(x, y)]']
    print(variables_list(v))"""

#variables_list_test()

def eliminate_implication(formulas):
    for j in range(len(formulas)):
        s = formulas[j].replace(" ", "")
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
        formulas[j] = s
    return formulas


def remove_double_not(formulas):
    for i in range(len(formulas)):
        formulas[i] = formulas[i].replace(" ", "")
        formulas[i] = formulas[i].replace("~~", "")  # Remove double negations
    return formulas


# s = ["[eat(x) > play(y)]", "[~[eat(x) & y] > play(y, Mohsen)]>x"]
# res = eliminate_implication(s)
# res = remove_double_not(res)
# for i in range(len(s)):
#     print(s[i], " ----> ", res[i])


def move_negation_inward(formulas: list[str]):
    for x in range(len(formulas)):
        formula = formulas[x].replace(" ", "")
        sz = len(formula)
        i = 0
        open_brackets = 0
        negation_stack = []  # Stack to keep track of negations inside brackets
        negation_count = 0  # Counter to track the number of negations
        while i < sz:
            if formula[i:i + 2] == '~[':
                # remove negation symbol
                formula = formula[:i] + formula[i + 1:]  # Remove '~'
                negation_stack.append(True)
                negation_count += 1
                open_brackets += 1
                sz -= 1
            elif formula[i] == '[' and i < sz - 1:  # Ensure index is within range
                negation_stack.append(False)
                open_brackets += 1
            elif formula[i] == ']':
                if(negation_stack[-1]):
                    negation_count -= 1
                negation_stack.pop()
                open_brackets -= 1
                if negation_stack and not negation_stack[-1]:
                    negation_stack.pop()
            elif formula[i] in ['|', '&', '∃', '∀'] and negation_count % 2 == 1:
                if formula[i] == '|':
                    formula = formula[:i] + '&' + formula[i + 1:]
                elif formula[i] == '&':
                    formula = formula[:i] + '|' + formula[i + 1:]
                elif formula[i] == '∃':
                    formula = formula[:i] + '∀' + formula[i + 1:]
                elif formula[i] == '∀':
                    formula = formula[:i] + '∃' + formula[i + 1:]
            elif negation_count % 2 == 1 and formula[i] not in symbol:
                if formula[i - 1] in ['[', '&', '~', '|', ' '] and formula[i + 1] in ['(',']', '&','|', '~'] or formula[i - 2] in ['∀', '∃']:
                    # Add negation before i
                    formula = formula[:i] + '~' + formula[i:]
                    sz += 1
                    i += 1
            i += 1
        formulas[x] = formula
    return remove_double_not(formulas)

formulas = ["~[P & ~Q]", "~[P | ~Q]", "~[∃x P(x)]", "~[∀x P(x)]"]
result = move_negation_inward(formulas)
for i in result:
    print(i)



# # helper function
# def find_closing_bracket_index(formula, open_index):
#     stack = []
#     for i, char in enumerate(formula):
#         if char == '(':
#             stack.append(i)
#         elif char == ')':
#             if stack[-1] == open_index:
#                 return i
#             stack.pop()
#     return -1

# def random_var(letters):
#     available_letters = set(string.ascii_lowercase) - set(letters)
#     if available_letters:
#         return random.choice(list(available_letters))
#     else:
#         return None  # all letter are used
    
def standardize(formulas: list[str]):
    return None
s = ["[∀xeat(x) > play(y)]", "[~∀x[eat(x) & y] > play(y, Mohsen)]"]
res = Standardize(s)
print(s)


def eliminate_universal(formulas: list[str]):
    eliminated_formulas = []
    for formula in formulas:
        formula = formula.replace(" ", "")

        # Find quantifier and replace quantifier with ''
        formula = re.sub(r'∀\s*[a-z]', '', formula)
        eliminated_formulas.append(formula)
    return eliminated_formulas


s = ["[∀xeat(x) > play(y)]", "[~∀x[eat(x) & y] > play(y, Mohsen)]"]
res = eliminate_universal(s)
print(res)



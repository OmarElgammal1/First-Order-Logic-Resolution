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
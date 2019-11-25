def balanced_parenthesis(input):
    open = ["[", "{", "("]
    n = len(input)
    res = []
    for i in input:
        if i in open:
            res.append(i)
        else:
            if len(res) > 0:
                res.pop()
                return "unbalanced"

    return "balanced"



input = "{[]{()}}"
print(balanced_parenthesis(input))
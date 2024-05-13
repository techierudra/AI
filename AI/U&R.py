def unify_var(var, x, s):
    if var in s:
        return unify(s[var], x, s)
    else:
        return extend(s, var, x)


def unify(x, y, s):
    if s is None:
        return None
    elif x == y:
        return s
    elif is_var(x):
        return unify_var(x, y, s)
    elif is_var(y):
        return unify_var(y, x, s)
    else:
        return None


def is_var(x):
    return isinstance(x, str) and x.startswith('?')


def extend(s, var, val):
    s2 = s.copy()
    s2[var] = val
    return s2
s = {}
x = '?x'
y = 'John'
result = unify(x, y, s)
print(result)  # Output: {'?x': 'John'}
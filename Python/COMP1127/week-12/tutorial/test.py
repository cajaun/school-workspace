# print(list(map(lambda x: x[0], ["let", "me", "know"])))
# x = ['ab', 'cd']
# print(len(list(map(list, x))))
def apply_fn(f, x):
    return f(f(f(x)))

print(apply_fn(lambda x: x + 1, 3))
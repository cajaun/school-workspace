def stack():
    # Write your code here
    return ("stack", [])

def contents(stk):
      # Write your code here
    if is_stack(stk):
        return stk[1]

def top(stk):
      # Write your code here
    if is_stack(stk) and not stack_empty(stk):
        return stk[1][-1]

def is_stack(obj):
    return isinstance(obj, tuple) and len(obj) == 2 and obj[0] == "stack" and isinstance(obj[1], list)

def stack_empty(stk):
      # Write your code here
    if is_stack(stk):
        return len(stk[1]) == 0
        

def push(stk, el):
      # Write your code here
    if is_stack(stk):
        stk[1].append(el)

def pop(stk):
      # Write your code here
    if is_stack(stk) and not stack_empty(stk):
        stk[1].pop()
        

st = stack()  

# Push elements to the stack
push(st, 1)
push(st, 2)
push(st, 3)
push(st, 4)
print(st) 

# Check the contents of the stack
print(contents(st))  

# Check the top element
print(top(st))  

# Check if it's a valid stack
print(is_stack(st))  

# Check if the stack is empty
print(stack_empty(st))  

# Push more elements
push(st, 5)
push(st, 6)
print(top(st))  
print(st)  

# Pop the top element
pop(st)
print(top(st))  
print(st)  
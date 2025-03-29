from question1 import post_order
from question2 import stack, push, top, pop
def isOperator(obj):
    # Write your code here
    return obj in ["+", "-", "*", "/"]


def applyOperator(operator, operand2, operand1):
    # Write your code here
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    if operator in operations:
        return operations[operator](operand2, operand1)
    else:
        raise ValueError("Invalid operator")



def eval_Postfix(tree):
    # Write your code here
    post_order_list = post_order(tree)
    
    # print(f"post order lst {post_order_list}")
    stk = stack()
    

    for element in post_order_list:
        
        if not isOperator(element):
            push(stk, element)
        else:  
            operand1 = top(stk) 
            pop(stk)
            operand2 = top(stk) 
            pop(stk)
            result = applyOperator(element, operand2, operand1)
            push(stk, result)
    

    return top(stk)


tree1 = ['btree', '/', 
          ['btree', 40, ['btree'], ['btree']], 
          ['btree', 5, ['btree'], ['btree']]]

print("Sample Input 0:")

print(f"Sample Output 0: {eval_Postfix(tree1)} \n")


tree2 = ['btree', '/', 
          ['btree', '+', 
           ['btree', 40, ['btree'], ['btree']], 
           ['btree', 5, ['btree'], ['btree']]], 
          ['btree', '*', 
           ['btree', 3, ['btree'], ['btree']], 
           ['btree', '-', 
            ['btree', 7, ['btree'], ['btree']], 
            ['btree', 2, ['btree'], ['btree']]]]]

print("Sample Input 1:")

print(f"Sample Output 1: {eval_Postfix(tree2)} ")
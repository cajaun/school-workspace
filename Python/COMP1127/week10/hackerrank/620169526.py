def make_empty_tree(root):
    return ("DT", [root, [], []])

def makeTree(root, left, right):
    return ("DT", [root, left, right])

def root(DT):
    return DT[1][0]

def left_subtree(DT):
    return DT[1][1]

def right_subtree(DT):
    return DT[1][2]

def is_empty(DT):
    return len(DT[1][1]) == 0 and len(DT[1][2]) == 0

def is_DT(DT):
    return isinstance(DT, tuple) and DT[0] == "DT" and isinstance(DT[1], list) and len(DT[1]) == 3

def make_leaf(value):
    return makeTree(value, [], [])


decision_tree = makeTree("HGC", 

    makeTree("DB", 
        make_leaf("HRL"), 
        make_leaf("MRL")
    ),
    makeTree("HBP", 
         makeTree("DBF", 
            
            makeTree("BMI", 
                make_leaf("HRL"), 
                make_leaf("MRL")
            ),
            make_leaf("LRL")
        ),
             
        makeTree("DBF", 
            
            makeTree("EH", 
                make_leaf("MRL"), 
                make_leaf("LRL")
            ),
            makeTree("SM", 
                makeTree("DB", 
                make_leaf("MRL"), 
                make_leaf("LRL")
                ),
                make_leaf("LRL"), 
                
            ), 
        ), 
       
    ), 
)



def diagnose(tree, hist_lst):
  
    if is_empty(tree):
        return root(tree)  

    condition = root(tree)

    conditionMap = {
        "HGC": 0,  
        "DB": 1,  
        "HBP": 2,  
        "DBF": 3,  
        "EH": 4,   
        "SM": 5,  
        "BMI": 6   
    }

    index = conditionMap[condition]
  
    if hist_lst[index] == "True":
        subtree = left_subtree(tree)
    else:
        subtree = right_subtree(tree)
 
    return diagnose(subtree, hist_lst)
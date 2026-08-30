lines = int(input())

is_balanced = True
last_bracket = ""

for _ in range(lines):
    string = input()
    
    if string == "(":
        if last_bracket == "(":
            is_balanced = False
        last_bracket = "("
        
    elif string == ")":
        if last_bracket != "(":
            is_balanced = False
        last_bracket = ")"

if last_bracket == "(":
    is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
    
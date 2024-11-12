from token import Token

NUM = "#"
TIMES = "*"
MINUS = "-"
PLUS = "+"
DIVIDED = "/"
OPEN = "("
CLOSE = ")"
OP = "operation"

OPS = [TIMES, MINUS, PLUS, DIVIDED, OPEN, CLOSE]

def tokenize(input_str):
    input_str = input_str.replace(" ", "")  # Remove spaces from the input string
    tokens = []

    i = 0
    while i < len(input_str):
        if input_str[i].isdigit():
            j = i + 1
            while j < len(input_str) and input_str[j].isdigit():
                j += 1
            tokens.append(Token(NUM, input_str[i:j]))
            i = j
        elif input_str[i] in OPS:
            tokens.append(Token(OP, input_str[i]))
            i += 1
        else:
            # Handle invalid characters or unexpected input here
            raise ValueError(f"Invalid character: {input_str[i]}")

    return tokens

# Convert tokens to a string for printing
def restring(tokens):
    out = ""
    for token in tokens:
        out += token.tokenData
    return out

def deparenthesize(tokens):
    for i in range(0,len(tokens)):
        if(tokens[i].tokenType==OPEN):
            for j in range(i,len(tokens)):
                if tokens[j].tokenType==CLOSE:
                    deparenthesize(tokens[i+1:j])
    #this section of code will be reached iff there are no parentheses in the input string.
    return(eval(restring(tokens)))
                    
        
input_str = "(44*3)"
tokens = tokenize(input_str)
print(restring(tokens))

print(deparenthesize(tokens))
def python_food():
    width = 80
    text = "pram and heggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

def center(*args, sep =" "): #parameter
    text = ""
    for arg in args:
        text+= str(arg) + sep
    left_margin = ( 131 - len(text)) // 2
    return " " * left_margin + text

# with open("center", mode='w') as center_file:
print(center("pram and heggs")) #arguments
print(center("pram, pram and heggs"))
print(center(12))
print(center("pram, pram, pram and pram"))

print(center("first", "second", 3, 4, "pram", sep = ":"))

print("=" + str(12 * 3))
print(sorted(["b","d","c","a"]))



mark_list = []
line_num = 0
with open('test.txt') as file:
    lines = file.readlines()
    print(f"quantity of lines:{len(lines)} \n")
    for line in lines:
        line = line.strip()
        line_num += 1
        print(f"\tquantity of symbols in line {line_num}:{len(line)}\n")
        words = line.split(" ")
        print(f"\t\tquantity of words:{words}>{len(words)} words\n")
gr1 = ["😀️","️😝","️😄"]
gr2 = ["😍️","😃️","😘"]
gr3 = ["🥰","🤪","😜️️"]
map = [gr1, gr2, gr3]
print(f"{gr1}\n{gr2}\n{gr3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

# original is easy to read
# selected_row = map[vertical-1]
# selected_row[horizontal-1] = "x"
map[vertical - 1][horizontal - 1] = "X" #select outermost and then innermost

print(f"{gr1}\n{gr2}\n{gr3}")


# console input: column > row
# code: select row, and then column



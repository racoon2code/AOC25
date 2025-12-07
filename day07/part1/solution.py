
tachyon_positon = []
count = 0

with open("input.txt", "r", encoding="utf-8") as f:
    
    for line in f:

        for index, char in enumerate(line):

            if char == "S":
                tachyon_positon.append(index)

            elif char == "^":

                if index in tachyon_positon:

                    count += 1

                    tachyon_positon.remove(index)

                    if index - 1 >= 0 and (index - 1) not in tachyon_positon:
                        tachyon_positon.append(index - 1)

                    if (index + 1) not in tachyon_positon:
                        tachyon_positon.append(index + 1)
                
            

print(count)
      
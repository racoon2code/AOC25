id_ranges = []
ingredients = []
finish_ranges= False
fresh_counter = 0

with open("input.txt", "r", encoding="utf-8") as f:
   for line in f:
      
      if line != "\n" and not finish_ranges:
         start, end = map(int, line.strip().split("-"))
         id_ranges.append([start, end])
    
      elif finish_ranges:
         ingredients.append(int(line.strip()))

      else:
        finish_ranges = True
         
       
for id in ingredients:
   
   for start, end in id_ranges:
    if id in range(start, end):
      fresh_counter += 1
      break
      

print(fresh_counter)  
 

def symbolCounter(s: str):
    syms_counter = {}
for i in s:
   syms_counter[i] = syms_counter.get(i, 0) + 1
return syms_counter 
       
print(symbolCounter())

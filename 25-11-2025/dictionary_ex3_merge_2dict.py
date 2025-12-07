d1={"a":1,"b":2}
d2={"b":3,"c":4}

merged={}

for key,value in d1.items():
    merged[key]=value

for key,value in d2.items():
    if key in merged:
        if isinstance(merged[key],list):
            merged[key].append(value)
        else:
            merged[key] = [merged[key], value]
    else:
        merged[key] = value

print(merged)



#lambda arguments: expression

# square=lambda x: x*x
# print(square(5))
#
# add=lambda a,b : a+b
# print(add(3,7))


#example2
generate_line=lambda user: f"Hello {user}, welcome to Python Training."

def write_dynamic_line(user,filename):
    with open(filename,"w") as f:
        f.write(generate_line(user))

write_dynamic_line("Rahul","welcome.txt")
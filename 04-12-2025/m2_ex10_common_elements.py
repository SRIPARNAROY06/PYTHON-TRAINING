def common_of_three(a: set, b: set, c: set):
    return a & b & c

s1 = {1, 2, 3, 4}
s2 = {2, 3, 5}
s3 = {0, 2, 3, 9}
print(common_of_three(s1, s2, s3))

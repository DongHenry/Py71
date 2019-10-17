# file1 = open('name.txt')
# print(file1.readline())

# file2 = open('name.txt')
# for line in file2.readlines():
#     print(line)
#     print('===========')

file3 = open('name.txt')
print(file3.tell())
file3.read(1)
print(file3.tell())

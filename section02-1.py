#Section02-1
#print

#print
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

#separator
print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T',sep='')
print('2019', '12', '24', sep='-')
print('userName', 'gmail.com', sep='@')

print()

#end
print('Welcome to', end=' ')
print('the Python', end=' ')
print('!!')

print()

#format
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))
# %s : 문자, %d : 정수, %f : 실수 (추가적인 것은 검색)
print("%s's favorite number is %d" % ('Pack', 7))
print("Test1 : %5d, Price : %4.2f" % (776, 6543.123))
print("Test1 : {0: 5d}, Price : {1: 4.2f}".format(776, 6543.123))
print("Test1 : {a: 5d}, Price : {b: 4.2f}".format(a=776, b=6543.123))

print()

#Escape
print("'You'")
print('\'You\'')
print('"You"')
print("""'You'""")
print('\\You\\\n')
print('\t\t\tTest')
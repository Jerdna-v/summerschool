try:
    print()
except Exception as Arg:
    print("arg")
else:
    print()
finally:
    print()

with open('hehe.csv', 'w') as file:
    file.write("hehe")
    file.writelines(['111111\n','2222222\n'])
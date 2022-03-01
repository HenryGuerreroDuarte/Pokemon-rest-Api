#This is to see the use of .isdigit() to take away numbers from strings
#x = '123abc'
#y = 'abc'
#z = '123'

#print([i for i in x if not i.isdigit()])

#print("Before " + x)
#x = ''.join([i for i in x if not i.isdigit()])
#print("After " + x)


file_list = ["12butterfree1920x1200.jpg", "134Toaster1920x1200.jpg", "13Pringlez1920x1200.jpg"]
#2 rename the files
for file_name in file_list:
    file_name = ''.join([i for i in file_name if not i.isdigit()])
    print("New file name:" + file_name)

print('New file name"',file_name)

#file_name_removed_last_five = [x[:-1] for x in file_name]

#print(file_name_removed_last_five)

#os.chdir(saved_path)


file_list = ["12butterfree1920x1200.jpg", "134Toaster1920x1200.jpg", "13Pringlez1920x1200.jpg"]
newtest = [x[:-9] for x in file_list]
print(newtest)




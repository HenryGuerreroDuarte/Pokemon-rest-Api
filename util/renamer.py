from fileinput import filename
import os
#File Directory -- C:\Users\Chartres\Documents\workspace-Api\PokemonFile\Pictures-names

#1 to get the file names
file_list = os.listdir(r"/Users/Chartres/Documents/workspace-Api/PokemonFile/Pictures-names")
print(file_list)
saved_path = os.getcwd()
print(" the current working directory is :" + saved_path)
os.chdir(r"/Users/Chartres/Documents/workspace-Api/PokemonFile/Pictures-names")


#2 rename the files--
#first takes out first 9 characters at the end
#file_list_re = [x[:-9] for x in file_list]
for file_name in file_list:
    #then takes out all the Int's
    new_name = ''.join([i for i in file_name[:-9] if not i.isdigit()]) + '.jpeg'
    print(f'Renamed {file_name} to {new_name}')
    os.rename(file_name, new_name)


os.chdir(saved_path)
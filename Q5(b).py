colour_list=['Red','Green', 'White', 'Black', 'Pink', 'Yellow']
#To remove several elememts we use del function
del colour_list[3:5]            
#To add an element we use insert function 
colour_list.insert(3,"Purple")
print('The updated colour list after removing "Black" and "Pink" and replacing them with "Purple" :-', colour_list)

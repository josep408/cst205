import pprint

pp = pprint.PrettyPrinter(indent=4)
#task 1
color_dictionary = {
	'red' : 	(255,	0,	0),
	'green' : (0, 128,	0), 
	'blue' : 	(0,	0,	255), 
	'magenta' : (255, 0, 255) , 
	'cyan' :  (0, 255, 255), 
	'yellow' : (255, 255, 0) , 
	'purple' : (128, 0, 128), 
	'pink' : (255, 192, 203) 
}
print("Task 1:")
pp.pprint(color_dictionary)

#Task 2 
print("\nTask 2:")
print(f"The blue channel of magenta has value {color_dictionary['magenta'][2]}.")
print(f"The green channel of yellow has value {color_dictionary['yellow'][1]}.")
print(f"The red channel of cyan has value {color_dictionary['cyan'][0]}.")

for color in color_dictionary:
	if color[1] == 'e':
		print(color, color_dictionary[color])

#Task 3
tineye_sample = {
    "status": "ok",
    "error": [],
    "method": "extract_collection_colors",
    "result": [
        {
            "color": (141, 125, 83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35, 22, 19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]
}

print("\nTask 3:")
print(f"The red channel of Clay Creek has value {tineye_sample['result'][0]['color'][0]}.")
print(f"The blue channel of Seal Brown has value {tineye_sample['result'][1]['color'][2]}.")

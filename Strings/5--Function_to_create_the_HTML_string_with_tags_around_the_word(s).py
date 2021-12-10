# Write a Python function to create the HTML string with tags around the word(s)

def add_tags(tag, word):
    final_string = ""
    boiler_plate_list = ["<", "", ">", "", "</", "", ">"]
    
    boiler_plate_list[1] = tag
    boiler_plate_list[3] = word
    boiler_plate_list[5] = tag

    for chars in boiler_plate_list:
        final_string += chars

    return final_string

print(add_tags("b", "Frustrated Learner"))
    
# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

# Example:

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# returns 'Bart'

# namelist([])
# returns ''

def namelist(names):
    the_string = ""

    for index, dicts in enumerate(names):
        if len(names) == 1:
            return dicts['name']
        else :
            if index == len(names) - 1:
                the_string += f" & {dicts['name']}"
                break
            elif index == len(names) - 2:
                the_string += f"{dicts['name']}"
                continue
            
            the_string += f"{dicts['name']}, "

    return the_string

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Arnold'} ]))
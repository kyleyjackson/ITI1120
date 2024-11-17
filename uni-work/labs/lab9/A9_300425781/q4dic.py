def reverse(dict):
    '''
    (dict) => dict
    
    Takes a phonebook dictionary where the phone numbers are mapped to the names
    '''

    names = []
    nums = []
    dict0 = {}

    for person in dict:
        names.append(person)
        nums.append(dict[person])
    
    for i in range(len(names)):
        dict0.update({ nums[i] : names[i] })

    return dict0

dict = {
    'Smith, Jane' : '123-45-67',
    'Doe, John' : '987-65-43',
    'Baker, David' : '567-89-01'
}

print(reverse(dict))
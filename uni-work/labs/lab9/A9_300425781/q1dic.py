# part 1
def letter2number(grade):
    '''
    (str) => int/None

    Returns the CGPA value correspoding to the inputted grade according to uOttawa grading system
    Returns None if the grade is invalid
    '''
    grades = ['A+', 'A', 'A-', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'E', 'F', 'ABS', 'EIN']
    cgpa = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0]

    if grade not in grades:
        return 

    index = grades.index(grade)

    return cgpa[index]

# part 2
def letter2number1(grade):
    '''
    (str) => int/None

    Returns the CGPA value correspoding to the inputted grade according to uOttawa grading system
    Returns None if the grade is invalid
    '''

    dic = {
        'A+' : 10,
        'A' : 9,
        'A-' : 8,
        'B+' : 7,
        'B' : 6,
        'C+' : 5,
        'C' : 4, 
        'D+' : 3, 
        'D' : 2, 
        'E' : 1,
        'F' : 0,
        'ABS' : 0,
        'EIN' : 0
    }

    return dic[grade]
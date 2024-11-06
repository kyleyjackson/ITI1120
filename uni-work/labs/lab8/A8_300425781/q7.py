def create_books_2Dlist(fileName):
    '''
    (str) => [[]]
    
    Converts file text into a 2D list with each row being one line of file text
    '''

    arr = open(fileName).read().splitlines()

    books = []

    for i in arr:
        i = i.split('\t') # make separate lists

        title = i[0].strip()
        author = i[1].strip()
        publisher = i[2].strip() 

        # reformat date
        date = i[3].strip()
        date = date.replace('/', '-')

        if len(date) < 10: # add zeroes to month
            date = '0' + date
        
        year = date[len(date) - 4 :]

        date = year + '-' +  date[: len(date) - 5]
        
        if len(date) < 10: # add zeros to days
            date = date[: len(date) - 1] + '0' + date[len(date) - 1]
        
        genre = i[4].strip()

        books.append([date, title, author, publisher, genre])
    
    return books

def search_by_year(books, year1, year2):
    '''
    ([[]], int, int) => None
    
    '''

    if year1 == year2:
        print('All titles from ' + str(year1) + ':')
    
    else: 
        print('All titles from ' + str(year1) + ' to ' + str(year2) + ':')

    print()

    noTitles = True

    for book in books: # check if no books
        if int(book[0][: 4]) >= year1 and int(book[0][: 4]) <= year2:
            noTitles = False

    if noTitles:
        print('No titles found in this range.')
        return
            
    for book in books:
        if int(book[0][: 4]) >= year1 and int(book[0][: 4]) <= year2:
            print(book[1] + ', by ' + book[2] + ' (' + book[0] + ')')

# main
fileName = input('Enter the name of the file: ')
fileName = fileName.strip()
books = create_books_2Dlist(fileName)

search_by_year(books, 0000, 1000)
search_by_year(books, 2005, 2005)
search_by_year(books, 1945, 1999)
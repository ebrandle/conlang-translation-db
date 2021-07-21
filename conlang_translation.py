# Code creator: E. Brandle
# Made free to the public: 2021/07/20

##################
''' TO DO LIST '''
##################
'''
+++ Completed +++
+ save english & conlang translations of words
+ list all words or all groups
+ search for translation of word in either direction
+ export database
+ add words to various categories (noun, verb, weather, etc)
+ list all words in a category
+ delete word/category

--- To Do ---
- list all categories for a certain word
- update word/category
- find rhymes
'''

###################
''' INTRO STUFF '''
###################
import sqlite3
import csv

menutext = """
0) Exit program
A) Add word or category
C) Categorize word
L) List words or available categories
LBC) List words by selected category
S) Search for word translation
D) Delete word or category
X) Export dictionary to conlang_dictionary.csv/.txt
"""

connection = sqlite3.connect('conlang.db')
cursor = connection.cursor()


###########
''' ADD '''
###########
def add():
    addType = input('\nDo you want to add a word or category (pick one): ').lower()
    if addType == 'word' or addType == 'words' or addType == 'w':
        add_word()
    elif addType == 'cat' or addType == 'category' or addType == 'c':
        add_cat()
    else:
        print('Invalid table name. Please try again.')

def add_word():
    con = input('>>> Conlang: ').lower()
    eng = input('>>> English: ').lower()
    eng2 = input('>>> Optional 2nd translation: ').lower()
    values = (con, eng, eng2)
    cursor.execute('INSERT INTO words (conlang, english, eng_def_2) VALUES (?,?,?)', values)
    connection.commit()

def add_cat():
    c = input('>>> Category: ').lower()
    values = (c,)
    cursor.execute('INSERT INTO categories (cat) VALUES (?)', values)
    connection.commit()


##################
''' CATEGORIZE '''
##################
def categorize_word():
    # choose word
    lstWords = input('>>> List all available words? ').lower()
    if lstWords == 'y' or lstWords == 'yes':
        list_words()
        print()
    wordToAdd = input('>>> Word to categorize: ').lower()
    
    # word validation
    wordLs = []
    for row in cursor.execute('SELECT * FROM words'):
        wordLs.append(row[0])
    if wordToAdd not in wordLs:
        print("\n!! Word validation error !!")
        return

    # choose category
    lstCat = input('\n>>> List all available categories? ').lower()
    if lstCat == 'y' or lstCat == 'yes':
        list_cat()
        print()
    catToAddTo = input('>>> Category to add to: ').lower()

    # cat validation
    catLs = []
    for row in cursor.execute('SELECT * FROM categories'):
        catLs.append(row[0])
    if catToAddTo not in catLs:
        print("\n!! Category validation error !!")
        return
    
    values = (wordToAdd, catToAddTo,)
    cursor.execute('INSERT INTO link_words_cat (con_link, cat_link) VALUES (?, ?)', values)
    connection.commit()


############
''' LIST '''
############
def list_stuff():
    listType = input('\nDo you want to list words or categories? ').lower()
    if listType == 'w' or listType == 'word' or listType == 'words':
        list_words()
    elif listType == 'c' or listType == 'cat' or listType == 'categories':
        list_cat()
    else:
        print('Invalid table name. Please try again.')

def list_words():
    print("\n<< Conlang: English >>")
    for row in cursor.execute('SELECT * FROM words'):
        tmpRow = row[0] + ': ' + row[1]
        if row[2] != '':
            tmpRow = tmpRow + ', ' + row[2]
        print(tmpRow)

def list_cat():
    print("\n<< Current categories >>")
    for row in cursor.execute('SELECT * FROM categories'):
        print(row[0])

def list_link():
    print("\n<< List of links >>")
    for row in cursor.execute('SELECT * FROM link_words_cat'):
        print(row[0],row[1])

def list_by_cat():
    # choose category
    lstCat = input('\n>>> List all available categories? ').lower()
    if lstCat == 'y' or lstCat == 'yes':
        list_cat()
        print()
    cat = input('Cateogory to list words from: ').lower()

    # category validation
    catLs = []
    for row in cursor.execute('SELECT * FROM categories'):
        catLs.append(row[0])
    if cat not in catLs:
        print("\n!! Invalid category !!")
        return

    # find words in category
    print('\n<<',cat.upper(),'>>')
    catVal = (cat,)
    for link_row in cursor.execute('SELECT * FROM link_words_cat WHERE cat_link=?',catVal).fetchall():
        #print('link row:',link_row)
        linkVal = (link_row[0],)
        for row in cursor.execute('SELECT * FROM words WHERE conlang=?',linkVal).fetchall():
            #print('row:',row)
            tmpRow = row[0] + ': ' + row[1]
            if row[2] != '':
                tmpRow = tmpRow + ', ' + row[2]
            print(tmpRow)


##############
''' SEARCH '''
##############
def look_up():
    lang = input('Search by language: ')
    word = input('Word to search: ')
    value = (word,)

    # english
    if lang == 'e' or lang == 'eng' or lang == 'english':
        for row in cursor.execute('SELECT conlang,english FROM words WHERE english=?',value):
            print('\nIn conlang,',row[1],'is',row[0]+'.')

    # conlang
    elif lang == 'c' or lang == 'con' or lang == 'conlang':
        for row in cursor.execute('SELECT conlang,english FROM words WHERE conlang=?',value):
            print(row[0],'means',row[1])
    else:
        print('\nInvalid language code.')


##############
''' DELETE '''
##############
def delete():
    addType = input('\nDo you want to delete a word or category? ').lower()
    if addType == 'word' or addType == 'words' or addType == 'w':
        delete_word()
    elif addType == 'cat' or addType == 'category' or addType == 'c':
        delete_cat()
    else:
        print('Invalid table name. Please try again.')

def delete_word():
    con = input('>>> Conlang: ').lower()
    val = (con,)
    cursor.execute('DELETE FROM words WHERE conlang=?', val).fetchall()
    cursor.execute('DELETE FROM link_words_cat WHERE con_link=?', val).fetchall()
    connection.commit()

def delete_cat():
    c = input('>>> Category: ').lower()
    val = (c,)
    cursor.execute('DELETE FROM categories WHERE cat=?', val).fetchall()
    cursor.execute('DELETE FROM link_words_cat WHERE cat_link=?', val).fetchall()
    connection.commit()


##############
''' EXPORT '''
##############
def export_csv():
    with open('conlang_dictionary.csv', 'w', newline='') as csvfile:
        fieldnames = ['conlang', 'english', 'eng_2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in cursor.execute('SELECT * FROM words'):
            writer.writerow({'conlang': row[0], 'english': row[1], 'eng_2': row[2]})

    print('CSV export to "conlang_dictionary.csv" complete.')

def export_dict():
    fullDict = {}
    f = open('conlang_dictionary.txt','w')
    for row in cursor.execute('SELECT * FROM words'):
        fullDict[row[0]] = {'Conlang': row[0], 'English': row[1], 'Eng_2': row[2]}
    f.write(str(fullDict))
    f.close()
    
    print('Dictionary export to "conlang_dictionary.txt" complete.')


######################
''' CALL FUNCTIONS '''
######################
while True:
    print(menutext)
    selection = input('>>> ').lower()

    # exit
    if selection == '0' or selection == 'q':
        break

    # add
    elif selection == 'a':
        add()
    elif selection == 'aw':
        add_word()
    elif selection == 'ac':
        add_cat()

    # categorize
    elif selection == 'c':
        categorize_word()
    
    # list
    elif selection == 'l':
        list_stuff()
    elif selection == 'lw':
        list_words()
    elif selection == 'lc':
        list_cat()
    elif selection == 'll':
        list_link()
    elif selection == 'lbc':
        list_by_cat()

    # find
    elif selection == 's':
        look_up()

    # delete
    elif selection == 'd':
        delete()
    elif selection == 'dw':
        delete_word()
    elif selection == 'dc':
        delete_cat()

    # export
    elif selection == 'x':
        export_csv()
        export_dict()
    elif selection == 'xc':
        export_csv()
    elif selection == 'xd':
        export_dict()
    elif selection == 'xt':
        export_dict()
        
    else:
        print('\nInvalid menu selection. Please try again.')


#######################
''' DATABASE FORMAT '''
#######################
'''
CREATE TABLE words (
    conlang text PRIMARY KEY,
    english text NOT NULL,
    eng_def_2 text
);

CREATE TABLE categories (
    cat text PRIMARY KEY
);

CREATE TABLE link_words_cat (
   con_link text NOT NULL,
   cat_link text NOT NULL,
   FOREIGN KEY (con_link) REFERENCES words (conlang),
   FOREIGN KEY (cat_link) REFERENCES categories (cat)
);
'''

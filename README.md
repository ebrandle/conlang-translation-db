# Python-SQLite Translation Database
Creator: E. Brandle

Last update: 2021/07/20

Link to original code: https://github.com/ebrandle/conlang-translation-db/

## Description
This is a simple python/sqlite interactive database designed to help authors, worldbuilders, and conlangers keep track of the words in their created language.

As of last update, this program only supports single-word translation. Multi-word/phrase translation can be done in a roundabout way by entering the phrase as a new "word"\*, but sentence translation must be completed by the user since conlang grammar often diverges from English grammar.

Note: While not at all required, I would love to be told if anyone uses my code. I love helping people and it's nice to know when my work pays off.

\*If you take this path, adding a category called "phrases" is recommended.

## Commands
- 0/Q: Exit program
- A: Add word or category
- - AW: Shortcut to add_word()
- - AC: Shortcut to add_cat()
- C: Categorize word
- L: List words or available categories
- - LW: Shortcut to list_words()
- - LC: Shortcut to list_cat()
- - LL: Unlisted path to list_link() (troubleshooting aid function)
- LBC: List words by selected category
- S: Search for word translation
- D: Delete word or category
- - DW: Shortcut to delete_word()
- - DC: Shortcut to delete_cat()
- X: Export dictionary to conlang_dictionary.csv/.txt
- - XC: Shortcut to export_csv() (.csv)
- - XD/XT: Shortcut to export_dict() (.txt)

## Abbreviations
- cat: category
- csv: comma separated values
- con: conlang
- conlang: constructed language
- eng: English
- ls: list
- lst: list
- tmp: temporary
- .txt: plain text file

## Legal
### The Unlicense
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

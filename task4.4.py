with open('book.txt', 'r') as file:
    text = file.read()
    symbols = [',', '.', '-', "»", '«','\n']
    text = text.strip()

    for symbol in symbols:
        text = text.replace(symbol, '')
    list_of_text = text.split(' ')
    total_words=len(list_of_text)
    x_word = list_of_text.count('слово')
    print(str(total_words) + ' слов')
    print(str(x_word) + ' раза')
# 1) удалить из текста все символы кроме алфавитных
# 2) разделить текст через пробелы на список
# 3) найти обшее количество слов в списке
# 4) найти количество определеннргр слово
# 5) вычислить процент опр слова

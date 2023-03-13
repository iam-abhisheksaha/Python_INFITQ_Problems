def translate():

    bil_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

    eng_list = input('Enter a sentence in English: ').split()
    swed_list = []

    for word in eng_list:
        swed_list.append(bil_dict.get(word))

    print(swed_list)

translate()
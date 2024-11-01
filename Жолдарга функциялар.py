# # Жай жол жасау
# s = "Сәлем, Python!"
# print(s)

#
# # Жолды бос орын арқылы бөлу
# text = "Python тілін,үйрену ,өте,# қызық"
# words = text.split() #split - перевод болу
# print(words)  # ['Python', 'тілін', 'үйрену', 'өте', 'қызық']
#

"""find() және replace()
find() әдісі белгілі бір символ немесе сөздің орын ретін табуға көмектеседі.
replace() әдісі жолдағы символды немесе сөзді басқаға ауыстырады"""

# # Белгілі бір сөзді табу
# text = "Python тілінде программалау"
# index = text.find("программалау")
# print(index)  # 14
#
# # Сөзді ауыстыру
# new_text = text.replace("Бекжан", "C++")
# print(new_text)  # C++ тілінде программалау

#
# """
# f-string форматы
# f-string көмегімен жолға мәндерді оңай енгізуге болады."""
#
# name = "Есімхан"
# age = 27
# info = f"Менің атым {name}, мен {age} жастамын."
# print(info)


"""isalpha(), isdigit(), isalnum()
isalpha() — жолдың тек әріптерден тұратынын тексереді.
isdigit() — жолдың тек цифрлардан тұратынын тексереді.
# isalnum() — жолдың әріптер мен цифрлардан тұратынын тексереді"""
#
# text = "Python"
# print(text.isalpha())    # True, тек әріптерден тұрады
#
# num = "12345"
# print(num.isdigit())     # True, тек цифрлардан тұрады
#
# mixed = "@#"
# print(mixed.isalnum())   # True, әріптер мен цифрлардан тұрады
#




#upper
text = 'bekzhan focus online grant'
a = text.upper() #upper() upper
#isupper
print(a.isupper())
if a.isupper():
    print("Барлык ариптер улкен")

#lower
# name = 'GULSHYRYN'
# print(name.lower())
# #capitalize
# print(text.capitalize())
# print(text.title())
#islower(),
"""Берілген жолда (text) үлкен және
кіші әріптер санын есептеңіз. Функция жолдағы әріптерді үлкен және кіші деп екіге бөліп санап,
нәтижені қайтарады.
"""
text = 'Grant 2024 Online only Focus'
bas_sozder = 0
kishi_sozder = 0

for i in text:
    if i.isupper():
        bas_sozder += 1
    elif i.islower():
        kishi_sozder += 1

print(f'Киши ариптер: {kishi_sozder}, Улкен ариптер: {bas_sozder}')



"""Жолда бас әріппен басталатын барлық сөздерді тауып, оларды тізім ретінде қайтарыңыз.
"""
# text = 'Grant 2024 Online only Focus'
# tizim = []
#
# for i in text.split():
#     if i.istitle():
#         tizim.append(i)
# print(tizim)
#


"""Шарты: Берілген жолдағы барлық кіші әріптерді бас әріпке айналдырыңыз.
"""
# text = 'GRANT 2024 online only focus'
# print(text.upper())
# print(text.lower())
#

"""Шарты: Жолдағы белгілі бір сөзді басқа сөзбен алмастырыңыз.
"""
# text = 'Bekzhan, salem!'
# print(text.replace('Nursultan', 'Aruzhan'))

"""Шарты: Жолдың басындағы және соңындағы артық бос орындарды алып тастаңыз.
"""
# text = 'focus online'
# print(text.strip('e'))

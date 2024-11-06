try:
    with open('text.txt', 'w+') as file:
        #     file_content = file.read()
        #     print(file_content)
        # with open('text.txt') as file:
        #     # print(file.readline())
        #     # print(file.readline())
        #     print(file.readlines())
        # for line in file.readlines():
        #     print(line)
        file.write('Paulina\n')
        file.write('Dominik\n')
        file.write('Truskawka\n')
        file.seek(0)
        print(file.read())
except FileNotFoundError:
    print('Plik niedostepny')

# ale lepiej tak nie dzialac na plikach:
# file = None
#
# try:
#     file = open('text.txt)')
#     file_content = file.read()
#     print(file_content)
#
# except Exception:
#     pass
# finally:
#     if file is not None:
#         file.close()
#
#         #ale lepiej tak nie dzialac na plikach

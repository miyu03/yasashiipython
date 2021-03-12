while True:
    command = input('pybot> ')
    if 'こんにちは' in command:
        print('ハロー')
    elif 'ありがと' in command:
        print('ドウいたしまして')
    elif 'さようなら' in command:
        print('バイバイ')
        break
    else:
        print('何言ってるかわからない')

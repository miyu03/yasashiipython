bot_dict = {
    'こんにちは': 'コンニチハ',
    'ありがと': 'ドウいたしまして',
    'さようなら': 'バイバイ',
    }

while True:
    command = input('pybot> ')
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break

    if not response:
        response = '何言ってるかわからない'
    print(response)

    if 'さようなら' in command:
        break

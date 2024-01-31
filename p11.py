# 文件系统
import time
import json
import requests


def main():
    # f = None
    # try:
    #     f = open('res/geci.txt', 'r', encoding='utf-8')
    #     print(f.read())
    # except FileNotFoundError:
    #     print("文件不存在")
    # except UnicodeDecodeError:
    #     print('读取文件时解码错误')
    # finally:
    #     if f:
    #         f.close

    # try:
    #     with open('res/geci.txt', 'r', encoding='utf-8') as f:
    #         print(f.read())
    # except FileNotFoundError:
    #     print('文件不存在')

    # with open('res/geci.txt', mode='r', encoding='utf-8') as f:
    #     for line in f:
    #         print(line, end='')
    #         time.sleep(0.5)
    # print()

    # with open('res/geci.txt') as f:
    #     lines = f.readlines()
    # print(lines)

    # with open('res/geci.txt', mode='a') as f:
    #     f.write('测试写入' + '\n')

    # with open('res/4444.jpeg', mode='rb') as f:
    #     data = f.read()
    # with open('res/4444_copy.jpeg', mode='wb') as f:
    #     f.write(data)

    # mydict = {
    #     'name': '骆昊',
    #     'age': 38,
    #     'qq': 957658,
    #     'friends': ['王大锤', '白元芳'],
    #     'cars': [
    #         {'brand': 'BYD', 'max_speed': 180},
    #         {'brand': 'Audi', 'max_speed': 280},
    #         {'brand': 'Benz', 'max_speed': 320}
    #     ]
    # }
    # try:
    #     with open('res/data.json', 'w', encoding='utf-8') as fs:
    #         json.dump(mydict, fs)
    # except IOError as e:
    #     print(e)

    # try:
    #     with open('res/data.json', 'r', encoding='utf-8') as fs:
    #         mydict = json.load(fs)
    # except IOError as e:
    #     print(e)
    # print(mydict)

    headers = {'x-api-key': '2222'}
    response = requests.put(
        'https://engine-api.apis.io/engine/apisjson', headers=headers)
    data_model = json.loads(response.text)
    print(data_model)


if __name__ == '__main__':
    main()

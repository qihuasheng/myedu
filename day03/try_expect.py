if __name__ == '__main__':
    print('3'in'35')
    print('3'not in'35')
    try:
        assert '3'not in'35'
        print(777)
    except:
        print(555)


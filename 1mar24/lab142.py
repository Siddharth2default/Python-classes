try:
    with open("testdata.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(e)
finally:
    file.close()
def test_function():

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()

#inner_function()
# При вызов функции вызывает ошибку, потому что она определена внутри функции "test_function" и не может быть доступна за ее пределами
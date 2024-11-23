calls = 0

def count_calls():
    global  calls
    calls += 1

def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return  tuple_

def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        if string.lower() in item.lower():
            return True
    return False


print(string_info("sas"))
print(is_contains('Urban', ['urBAN', 'hello', 'world']))  # True
print(is_contains('Urban', ['urBN', 'hello', 'world']))  # True
print(is_contains('nabrU', ['urBAN', 'hello', 'world']))  # True
print(calls)

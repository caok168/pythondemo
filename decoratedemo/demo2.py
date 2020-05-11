
def func(message):
    def get_message(message):
        print('Got a message:{}'.format(message))
    return get_message(message)

func('hello world')

def func_closure():
    def get_message(message):
        print('Got a message:{}'.format(message))
    return get_message

send_message = func_closure()
send_message('hello world')
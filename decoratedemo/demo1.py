def func(message):
    print('Got a message:{}'.format(message))

send_message = func

send_message('Hello world')

def get_message(message):
    return 'Got a message: '+message

def root_call(func,message):
    print(func(message))

root_call(get_message,'Hello world')
import easygui
import easygui as g

message = 'who are you'
message1 = 'i am ck'

def uiShow(message):
    while(1):
        Yes_or_No = easygui.buttonbox(title=" love ",msg=message, choices=['Yes', 'No'])
        if Yes_or_No == 'Yes': break
        if Yes_or_No == 'No':
            uiShow(message1)
        else:
            uiShow(message1)

if __name__ == '__main__':
    uiShow(message)
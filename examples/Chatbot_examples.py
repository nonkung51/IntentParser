import intentparser as ip
import datetime
import random

__author__ = 'Nonthakon Jitchiranant'

allIntent = []

HelloIntent = ip.intentParser({
    'description' : {
                    "type" : 'HelloIntent',
                    "args" : [],
                    "keyword" : [
                    (ip.REQUIRE, "hello_keyword"),
                    ]},
    'hello_keyword' : ['hello', 'hi'],
})
HelloIntent.teachWords(["Hello, How are you?", "Hi, Mr.John", "Hello, nice to meet you!"])
allIntent.append(HelloIntent)

ByeIntent = ip.intentParser({
    'description' : {
                    "type" : 'ByeIntent',
                    "args" : [],
                    "keyword" : [
                    (ip.REQUIRE, "bye_keyword"),
                    ]},
    'bye_keyword' : ['bye'],
})
ByeIntent.teachWords(["Good bye.", "Bye, Josh.", "Good bye, Be safe."])
allIntent.append(ByeIntent)

TimeIntent = ip.intentParser({
    'description' : {
                    "type" : 'TimeIntent',
                    "args" : [(ip.OPTIONAL, "scopes")],
                    "keyword" : [
                    (ip.REQUIRE, "time_keyword"),
                    (ip.OPTIONAL, "scopes")
                    ]},
    'time_keyword' : ['is', 'are', 'what', 'how', 'clock', 'how\'s'],
    'scopes' : [
        "day",
        "time"
        ]
})
TimeIntent.teachWords(["What time is it?", "How's the clock", "What is this day"])
allIntent.append(TimeIntent)

while True:
    text = input('User said : ')
    temp = []

    for i in allIntent:
        _temp = i.getResult(text)
        try:
            temp.append((_temp['confidence'], _temp['type']))
        except Exception as e:
            pass
    try:
        candidate = max(temp)
        if candidate[1] == 'HelloIntent':
            print(random.choice(['Chatbot said : Hello!',
                                'Chatbot said : How are you?',
                                'Chatbot said : What\'s up!']))
        elif candidate[1] == 'ByeIntent':

            print(random.choice(['Chatbot said : Good bye!',
                                'Chatbot said : Good Luck!',
                                'Chatbot said : See ya!']))
        elif candidate[1] == 'TimeIntent':
            typeOfTime = TimeIntent.getResult(text)['args']
            typeOfTime = [item for item in typeOfTime if item[0] == 'scopes'][0][1]
            now = datetime.datetime.now()
            if typeOfTime == 'day':
                print("Today is {}/{}/{}".format(now.day, now.month, now.year))
            else:
                print("now is {}:{}:{}".format(now.hour, now.minute, now.second))
            del typeOfTime, now
        else:
            print('error')
        del text, temp, _temp, candidate
    except Exception as e:
        print('Error')

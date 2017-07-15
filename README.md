# IntentParser
Simple intent parser for python 3

This is incredibly simple intent parser. Easy to use and hackable.

Installation
===============
    $ git clone https://github.com/nonkung51/IntentParser.git
    $ cd IntentParser
    $ python setup.py install

Examples
===============
this is a simple intent parser for parsing favourite music genre.

   
    import intentparser as ip

    if __name__ == "__main__":
        intent = ip.intentParser({
            'description' : {
                            "type" : 'FavMusicIntent',
                            "args" : [(ip.OPTIONAL, "musics_types")],
                            "keyword" : [
                            (ip.REQUIRE, "musics_keyword"),
                            (ip.OPTIONAL, "musics_types")
                            ]},
            'musics_keyword' : ['is', 'are', 'music', 'favourite', 'genre'],
            'musics_types' : [
                "pop",
                "rock",
                "jazz",
                "country",
                "reggae"
                ]
        })
        intent.teachWords(["I love Reggae music.", "Rock is my favourite.", "I love Country music genre."])
        print(intent.getResult("I love Rock music."))
        print(intent.getResult("Jazz is my favourite."))

result

    {'type': 'FavMusicIntent', 'args': [('musics_types', ['rock'])], 'confidence': 0.75}
    {'type': 'FavMusicIntent', 'args': [('musics_types', ['jazz'])], 'confidence': 0.6666666666666666}

this one is for parsing weather and location for weather forecasting



    import intentparser

    if __name__ == "__main__":
        intent = intentparser.intentParser({
        # 1 for optinal 2 for regex
            'description' : {
                            "type" : 'WeatherIntent',
                            "args" : [(ip.REGEX,"location"), (ip.OPTIONAL, "weather_types")],
                            "keyword" : [
                            (ip.REQUIRE, "weather_keyword"),
                            (ip.OPTIONAL, "weather_types"),
                            (ip.REGEX, "location")
                            ]},
            'weather_keyword' : ['is', 'are', 'weather', 'sleet', 'rain', 'humid'],
            'weather_types' : [
                "snow",
                "rain",
                "wind",
                "sleet",
                "sun"
                ],
            'location' : ' in (?P<location>.*)'
        })
        intent.teachWords(["Weather in Bangkok?", "Good weather in Canada?", "Is it rain in North California?"])
        print(intent.getResult("Rain in Khon Kaen?"))
        print(intent.getResult("Is it rain in California?"))

result

    {'type': 'WeatherIntent', 'confidence': 0.5, 'args': [('location', 'Khon Kaen?'), ('weather_types', ['rain'])]}
    {'type': 'WeatherIntent', 'confidence': 0.8571428571428571, 'args': [('location', 'California?'), ('weather_types', ['rain'])]}

And this is the previous one but use gensim sentence comparison instead of jaccard comparison

    import intentparser as ip

    if __name__ == "__main__":
        intent = intentparser.intentParser({
            'description' : {
                            "type" : 'WeatherIntent',
                            "args" : [(ip.REGEX,"location"), (ip.OPTIONAL, "weather_types")],
                            "keyword" : [
                            (ip.REQUIRE, "weather_keyword"),
                            (ip.OPTIONAL, "weather_types"),
                            (ip.REGEX, "location")
                            ]},
            'weather_keyword' : ['is', 'are', 'weather', 'sleet', 'rain', 'humid'],
            'weather_types' : [
                "snow",
                "rain",
                "wind",
                "sleet",
                "sun"
                ],
            'location' : ' in (?P<location>.*)'
        }, typeOfSim='gensim')
        intent.teachWords(["Weather in Bangkok?", "Good weather in Canada?", "Is it rain in North California?"])
        print(intent.getResult("Rain in Khon Kaen?"))
        print(intent.getResult("Is it rain in California?"))

result

    {'confidence': 0.95491028, 'args': [('location', 'Khon Kaen?'), ('weather_types', ['rain'])], 'type': 'WeatherIntent'}
    {'confidence': 0.95491028, 'args': [('location', 'California?'), ('weather_types', ['rain'])], 'type': 'WeatherIntent'}
    

Usage
===============
https://medium.com/@nonthakon/making-a-chatbots-in-python-67e9e6a8317b <=== making a chatbot. check it out!

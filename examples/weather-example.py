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

# IntentParser
Simple intent parser for python 3

This is incredibly simple intent parser. Easy to use and hackable

Examples

this is a simple intent parser for parsing favourite music genre.

```
  import intentparser
  if __name__ == "__main__":
      intent = intentparser.intentParser({
          'description' : {
                          "type" : 'FavMusicIntent',
                          "args" : [(1, "musics_types")],
                          "keyword" : [
                          (0, "musics_keyword"),
                          (1, "musics_types")
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
```

this one is for parsing weather and location for weather forecasting

```
import intentparser

intent = intentparser.intentParser({

    'description' : {
                    "type" : 'WeatherIntent',
                    "args" : [(2,"location"), (1, "weather_types")],
                    "keyword" : [
                    (0, "weather_keyword"),
                    (1, "weather_types"),
                    (2, "location")
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
```

And this is the previous one but use gensim sentence comparison instead of jaccard comparison

```
import intentparser

intent = intentparser.intentParser({

    'description' : {
                    "type" : 'WeatherIntent',
                    "args" : [(2,"location"), (1, "weather_types")],
                    "keyword" : [
                    (0, "weather_keyword"),
                    (1, "weather_types"),
                    (2, "location")
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
```

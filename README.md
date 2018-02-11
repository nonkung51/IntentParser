# IntentParser for Python

This is simple intent parser for using with chatbots, natural language processing ,etc.

## Getting Started

What you have to do is declare your intent parser -> teach it -> Done!
```
intent = ip.intentParser({
        'description' : {
         #Type aka. Name of the intent parser
         "type" : 'FavMusicIntent',
         
         #arguement that need to be parse.
         "args" : [(ip.OPTIONAL, "musics_types")],
         
         #define all keyword you need to use.
         "keyword" : [(ip.REQUIRE, "musics_keyword"),(ip.OPTIONAL, "musics_types")] 
        },
        'musics_keyword' : ["is", "are", "music", "favourite", "genre"], #require keywords
        'musics_types' : ["pop","rock", "jazz", "country", "reggae"] #optional keywords
    })
```
This is all you have to do to set up your intent parser. Now how to train it is pretty easy.
```
intent.teachWords(["I love Reggae music.", "Rock is my favourite.", "I love Country music genre."])
#use teachWords() fill with list of sentence just simple as that.
#also you could train as many time as you want!
```
What it could do?
```
print(intent.getResult("I love Rock music."))
print(intent.getResult("Jazz is my favourite."))
```
Result
```
{'type': 'FavMusicIntent', 'args': [('musics_types', ['rock'])], 'confidence': 0.75}
{'type': 'FavMusicIntent', 'args': [('musics_types', ['jazz'])], 'confidence': 0.6666666666666666}
```
Cool! huh?!

### Installing

To install it you just need to.

```
$ git clone https://github.com/nonkung51/IntentParser.git
$ cd IntentParser
$ python setup.py install
```

## Usage

* [Making chatbot in python](https://medium.com/@nonthakon/making-a-chatbots-in-python-67e9e6a8317b) <=== making a chatbot. check it out!

## Contributing
This module is contributing by myself(nonkung51). If you want to contributing just contact me!

## Authors

* **Nonthakon Jitchiranant** - *Initial work* - [nonkung51](https://github.com/nonkung51)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details

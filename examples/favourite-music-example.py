import intentparser

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

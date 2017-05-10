import intentparser

if __name__ == "__main__":
    intent = intentparser.intentParser({
    # 1 for optinal 2 for regex
        'description' : {
                        "type" : 'ถามเพลงโปรด',
                        "args" : [(2,"ชื่อเพลง"), (1, "แนวเพลง")],
                        "keyword" : [
                        (0, "คำบอก"),
                        (1, "weather_types"),
                        (2, "location")
                        ]},
        'คำบอก' : ['ผม', 'ชอบ', 'เจ๋ง', 'โปรด', 'เพลง', 'แนว'],
        'แนวเพลง' : [
            "ป๊อป",
            "ร็อค",
            "แจ๊ส",
            "คันทรี",
            "เพลงไทย"
            ],
        'ชื่อเพลง' : ' เพลง (?P<location>.*)'
    })
    intent.teachWords(["ผมชอบเพลง Yellow", "ฉันรักเพลงแจ๊ส", "เพลงไทยสนุกมาก"])
    print(intent.getResult("ผมชอบเพลงร็อต"))
    print(intent.getResult("เพลงคันทรีสนุกมาก"))

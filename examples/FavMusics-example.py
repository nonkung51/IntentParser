import intentparser as ip

if __name__ == "__main__":
    intent = ip.intentParser({
    # 1 for optinal 2 for regex
        'description' : {
                        "type" : 'ถามเพลงโปรด',
                        "args" : [(ip.REGEX,"ชื่อเพลง"), (ip.OPTIONAL, "แนวเพลง")],
                        "keyword" : [
                        (ip.REQUIRE, "คำบอก"),
                        (ip.OPTIONAL, "แนวเพลง"),
                        (ip.REGEX, "ชื่อเพลง")
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

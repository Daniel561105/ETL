with open("name_url.txt","r",encoding="utf-8") as f:
    for text in f:
        text = text.split()
        book = text[0]
        name = f"{text[0]}_{text[1]}"
        print(book)
        print(name)
for  i in range(5):
    print("")
    meme_dict = {    
        "CRINGE": "Garip ya da utandırıcı bir şey",
        "LOL": "Komik bir şeye verilen cevap",
        "OMG": "şaşırdığımız bir şey olduğunda verdiğimiz bir cevap",
        "MEME": "komik bir olay olduğu videolara verilen isim ama Türkçede aynı değil",
        "jsjsjsj": "arkadaşımız bize komik bir video gönderdiğinde veya komik bir mesaj attığında verdiğimiz tepki",
    }

    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else: 
        print("Sözlükte yok")

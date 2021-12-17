import re


WEIGHTED_WORDS = {
    1: [
        #"i ", "i'm", "i am", "i've", "i have", "i'd", "i had", "i'll", "i will",
        " my ", "myself", " he ", " she ", " his ", " her ", " you ", "you'", #"you'll", "you will",
        "think", "thinking", "feeling", "beautiful", "happy", "sad ",
        re.compile("oo*ps"), "paradox", "worry",
        "days", "hours", "headache", "yesterday", "tomorrow",
        "music", "personal",
    ],
    2: [
        re.compile(" a+h+ "), re.compile(" o+h+ "),
        re.compile(" a+r+g+h* "), re.compile(" mm+h* "),
        re.compile(" ba*h* "),
    ],
    3: [
        "funny", "hilarious", "ridiculous", "amazing",
        "love", "hate", "fuck", "stupid", "awful", "silly", "curse", "damn", "joy ",
        "frustrati", "humbug",
        "ugly", "moral", " boy", "girl", "friend", "shame", "thoughts",
        "evil", " god ", "god's", "church", " verse", "faith ", "cthulhu",
        "cheat", "breakfast", "life", "dream", "grief", "gosh", "god"
        "heaven", "hell ", "hellish", "fantasy", "mystery", "magic",
        "paranoia", "paranoid", "society", "social", "forgive", "forgiving",
        "sister", "brother", "bless", "shit", "mama", "papa", "cock", "ascetic",
        "stunned", "stunning", "horribl", "yeah",
        "humiliate", "inspiration", "experience", "darkness", "misery", "suffering",
        "struggling", "obsess", "female", "ignorant",
    ]
}

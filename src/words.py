import re


WEIGHTED_WORDS = {
    0.1: [
        "i ", "i'm", "i am", "i've", "i have", "i'd", "i had", "i'll", "i will",
    ],
    1: [
        " my ", "myself", " he ", " she ", " his ", " her ", " you ", "you'",
        "think", "thinking", "feeling", "beautiful", "happy", " sad ",
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
        "yeah",

        "funny", "hilarious", "ridiculous", "amazing",
        "stupid", "awful", "silly", "ugly",
        "sadness",

        "love", "hate", "fuck", "curse", "damn", "joy ",
        "frustrati", "humbug", "gosh", "shit",
        "evil", " god ", "god's", "church", " verse", "faith ", "cthulhu",
        "bless", "ascetic",
        "heaven", " hell", "hellish", "fantasy", "mystery", "magic",
        "moral", " boy", "girl", "friend", "shame", "thoughts",
        "female", " male ", "cock",

        "life", "dream", "grief",
        "paranoia", "paranoid", "society", "social", "forgive", "forgiving",

        "cheat", "breakfast",

        "sister", "brother", "mama", "papa",
        "stunned", "stunning", "horribl",
        "humiliate", "inspiration", "experience", "darkness", "misery", "suffering",
        "struggling", "obsess", "ignorant",
    ]
}

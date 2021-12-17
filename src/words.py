import re


WEIGHTED_WORDS = {
    0.1: [
        "i ", "i'm", "i am", "i've", "i have", "i'd", "i had", "i'll", "i will",
    ],
    1: [
        " my ", "myself", " he ", " she ", " his ", " her ", " you ", "you'",
        "think", "thinking", "feeling", "beautiful", "happy", " sad ",
        re.compile("oo*ps"), "paradox", "worry",
        "days", "hours", "headache", "yesterday", "today", "tomorrow",
        "music", "personal", "brain", "cool", "interesting",
    ],
    2: [
        re.compile(" a+h+ "), re.compile(" o+h+ "),
        re.compile(" a+r+g+h* "), re.compile(" mm+h* "),
        re.compile(" ba*h* "),
        "pandemic",
    ],
    3: [
        "yeah",

        "funny", "hilarious", "ridiculous", "amazing",
        "stupid", "awful", "silly", "ugly", "clunky", "creep",
        "sadness", "emotion",

        "love", "hate", "fuck", "curse", "damn", "joy ",
        "frustrati", "humbug", "gosh", "shit", "blood", "annoy",
        "evil", " god ", "god's", "church", " verse", "faith ", "cthulhu",
        "bless", "ascetic", "spirit",
        "heaven", " hell", "hellish", "fantasy", "mystery", "magic",
        "moral", " boy", "girl", "friend", "acquaintance",
        "shame", "thoughts",
        "female", " male ", "cock",

        "life", "dream", "grief",
        "paranoia", "paranoid", "society", "social", "forgive", "forgiving",

        "cheat",
        "breakfast", "dinner", "lunch",

        "sister", "brother", "mama", "papa",
        "stunned", "stunning", "horribl",
        "humiliate", "inspiration", "experience", "darkness", "misery", "suffering",
        "struggling", "obsess", "ignorant",
    ]
}

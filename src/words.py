import re


WEIGHTED_WORDS = {
    1: [
        "i ", "i'm", "i am", "i've", "i have", "i'd", "i had", "i'll", "i will",
        " my ", "myself", " he ", " she ", " his ", " her ", " you ", "you'd", "you'll", "you will",
        "think", "thinking", "feeling", "beautiful", "happy", "sad ",
        "oops", "paradox", "worry",
        "days", "hours", "headache", "yesterday", "tomorrow",
        "remember", "music", "personal", "game",
    ],
    3: [
        "funny", "hilarious", "ridiculous", "amazing",
        "love", "hate", "fuck", "stupid", "awful", "silly", "curse", "damn", "joy ",
        "ugly", "moral", "immoral", " boy", "girl", "friend", "shame", "thoughts",
        re.compile(" a+h+ "), re.compile(" o+h+ "),
        re.compile("a+r+g+h*"),
        "evil", "god's work", "cthulhu",
        "cheat", "breakfast", "life", "dream", "grief", "gosh", "god"
        "heaven", "hell ", "hellish", "fantasy", "mystery", "magic",
        "paranoia", "paranoid", "society", "social", "forgive", "forgiving",
        "sister", "brother", "bless", "shit", "mama", "papa", "cock", "ascetic",
        "stunned", "stunning", "horribl", "yeah",
        "humiliate", "inspiration", "experience", "darkness", "misery", "suffering",
        "struggling", "obsess", "female", "ignorant",
    ]
}

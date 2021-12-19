import re

"""

These are the words that filter the commit messages. 

Punctuations and new-lines are removed from the messages and
the following strings are searched in the whole message.

Each matching string increases the rank-counter **once**
and messages with rank >= 10 are included.

"""


WEIGHTED_WORDS = {
    0.15: [
        " i m ", " i am ", " i ve ", " i have", " i d ", " i had ",
        " i ll ", " i will ", " i won't ", " i wont ",

        " today",
    ],
    1: [
        " i want ",
        " my ", " myself", " he ", " she ", " his ", " her ", " you ", " you d ", " you ll ",
        " we ", " we ll ", " we d ",
        " we should ", " i should", " he should", " she should",
        " think", " thinking", " feeling", " beautiful", " happy", " sad ",
        "paradox", " worry", " wise", " sane ", " weird ", " wierd "  # !sic
        " days ", " hours ", " yesterday", " tomorrow", " year",
        "music", " personal", " cool ", " interesting",
        " offend", " frankly", " fortunate", " however ",
        "didn't help", "thanks", "thank you", "anyway", " enjoy ",
        re.compile(" a+h+ "), re.compile(" o+h+ "), re.compile(" oo+ps "),
        " do the tricks ", " garbage", " depressing ",
        " love", "love ", " appease ",
    ],
    2: [
        re.compile(" a+rr+g+h* "), re.compile(" mm+h+ "),
        re.compile(" ba+h+ "),
        re.compile(" ha\s*ha "),re.compile(" ha\s*ha\s*ha "),
        re.compile(" har\s*har "),
        " my brain",
        "pandemic", " war ", "science", "scientist",
        " hack", " hacks", " wild ", " claw", " crazy ", " beast ",
        "drinking", " exhaustive", " headache",
        " poorly", " unreadable", " theory", " theorize",
        " diary", " wonder ", " depression ", " revenge ",
        " intelligent machine", "psychedelic", " deeply ",
    ],
    3: [
        " yeah", re.compile(" yah+ "),
        " my opinion", " not that", "kinda ", "to be honest", "honestly",
        " doesn't make sense", " confess", " remember",
        " funny", " hilarious", " ridiculous", " amazing", " wonky",
        " stupid", " awful", " silly", " ugly", " clunk", " creep",
        " shut up", " suck", " sucking", " sick ", " screw you", " idiot", " idiotic",
        " sadness", " emotion", " pain", " miracle", " despair", " despar",  # !sic
        " insane", " insanit", " rage ", " die ", " lynch",

        " lovely", " hate ", " hateful", " hating", " curse", "damn", " joy ",
        " frustrati", "humbug", " gosh ", " blood", " annoy", " trouble",
        " evil", " god ", " devil ", " god s ", "praise", " holy ", "church", " verse ", " faith ",
        re.compile(" omg+ "),
        " bless", "ascetic", " spirit", "demonic", " demon ",
        " heaven", " hell ", " hellish", "fantasy", " mystery", " magic",
        " moral", " immoral", " boy", " girl", "friend", "acquaintance",
        " shame", "thoughts", "sorry",
        " female", " male ", " cock", " ass ", " arse ", "bitch",

        " life ", " dream", " grief", " tears",
        "paranoia", "paranoid", " society", " social", " forgive", " forgiving",

        " cheat", "singularity", " hot potato",
        " breakfast", " dinner", " lunch", " morning", " evening", "night ",

        " sister", " brother", " mama ", " papa ",
        " stunned", " stunning", " horribl",
        " humiliate", " inspiration", "experience", " darkness", " misery", " suffering",
        " struggling", " obsess", "ignorant",
        " please understand",
    ],
    4: [
        "fuck", " shit", "bullshit", " sin ", "facepalm",
        "cthulhu",
        re.compile("notes? to .*self"), " hate myself",
        "dear diary",
    ],
    10: [
        " hate my life", "fuck you",
    ]
}

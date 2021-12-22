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

        " today ", " fairly ",
    ],
    .3: [
        " wrong ", " extremely ", " hope ", " why ",
        " enough ", " free ", " good ", " wouldn t ",
    ],
    1: [
        " my ", " myself", " he ", " she ", " his ", " her ",
        " you ", " you d ", " you ll ", " you re ",
        " we ", " we ll ", " we d ", " we re ",
        " we should ", " i should", " he should", " she should",
        " think", " thinking", " feeling", " opinion ", " beautiful",
        " happy", " sad ", " sadly ",
        "paradox", " worry", " wise", " sane ", " weird ", " wierd "  # !sic
        " days ", " hours ", " yesterday", " tomorrow", " year",
        " summer", " winter", " autumn",
        "music", " personal", " cool ", " interesting",
        " offend", " frankly", " fortunate", " however ",
        "didn't help", "thanks", "thank you", "anyway", " enjoy ",
        re.compile(" a+h+ "), re.compile(" o+h+ "), re.compile(" oo+ps "),
        " do the tricks ", " garbage", " depressing ",
        " love", "love ", " appease ", " suspicion ", " deeply ",
        " buttload ", " dunno ", " quirk ",
        " literally ", " giant ", " illusion ", " brute ",
        " turf ", " turfs ", " outright ", " repetitious ", " adware ",
        " bugged ", " heart ", " sleep ", " poor ", " juicy ", " facts ",
    ],
    2: [
        re.compile(" a+rr+g+h* "), re.compile(" mm+h+ "),
        re.compile(" ba+h+ "),
        re.compile(" ha\s*ha "),re.compile(" ha\s*ha\s*ha "),
        re.compile(" har\s*har "),
        " i want ", " my brain", " shot ",
        "pandemic", " war ", "science", "scientist",
        " hack", " hacks", " wild ", " claw", " crazy ", " beast ",
        "drinking", " exhaustive", " headache", " shocked ", " puzzled ",
        " poorly", " unreadable", " theory", " theorize",
        " diary", " wonder ", " depression ", " revenge ",
        " intelligent machine", "psychedelic", " exciting ", " angel ",
        " quirky ", " mistake ", " fluctuation", " twinkle ", " twinkling ", " hookin ", #! sic
        " enjoy ", " artists ",
    ],
    3: [
        " yeah", re.compile(" yah+ "),
        " my opinion", " not that", "kinda ", "to be honest", "honestly",
        " doesn't make sense", " confess", " remember",
        " funny", " hilarious", " ridiculous", " amazing", " wonky",
        " stupid", " awful", " silly", " ugly", " ugliness ", " clunk", " creep",
        " shut up", " suck", " sucking", " sick ", " screw you", " idiot", " idiotic",
        " sadness", " emotion", " pain", " miracle", " despair", " despar",  # !sic
        " insane", " insanit", " rage ", " die ", " lynch",
        " commercialized ", " ideology ", " suicid", " revolution ",
        " joke ", " joking ", " jokes ", " laugh", " lousy ", " guru",

        " lovely", " hate ", " hateful", " hating", " curse", "damn", " joy ",
        " frustrati", "humbug", " gosh ", " blood", " annoy", " trouble",
        " evil", " god ", " devil ", " god s ", "praise", " holy ", "church", " verse ", " faith ",
        re.compile(" omg+ "), " salvation ", " terror",
        " bless", "ascetic", " spirit", "demonic", " demon ",
        " heaven", " hell ", " hellish", "fantasy", " mystery", " magic",
        " moral", " immoral", " boy", " girl", "friend", "acquaintance",
        " shame", "thoughts", " sorry",
        " female", " male ", " cock", " ass ", " arse ", "bitch",
        " smoker ", " violent",
        " life ", " dream", " grief", " tears", " angels ",
        "paranoia", "paranoid", " society", " social", " forgive", " forgiving",

        " cheat", "singularity", " hot potato", " crisis ", " espionage ",
        " breakfast", " dinner", " lunch", " morning", " evening", "night ",
        " my parents"
        " sister", " brother", " mama ", " papa ",
        " stunned", " stunning", " horribl",
        " humiliate", " inspiration", "experience", " darkness", " misery", " suffering",
        " struggling", " obsess", "ignorant",
        " please understand", " armageddon",
    ],
    4: [
        "fuck", " shit", "bullshit", " sinner ", "facepalm",
        "cthulhu", " junkie",
        re.compile("notes? to .*self"), " hate myself",
        "dear diary", " tinfoil ",
        " should be sleep", " my parents", " why me ",
    ],
    10: [
        " hate my life", "fuck you",
    ]
}

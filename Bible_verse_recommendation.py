print("BIBLE VERSE RECOMMENDATIONS :)")

sad = {
    "Psalm 9:9": "The LORD is a refuge for the oppressed, a stronghold in times of trouble.",
    "Psalm 18:2": "The LORD is my rock, my fortress and my deliverer; my God is my rock, in whom I take refuge. He is my shield and the horn of my salvation, my stronghold.",
    "Psalm 22:24": "For he has not despised or disdained the suffering of the afflicted one; he has not hidden his face from him but has listened to his cry for help.",
    "Proverbs 14:32": "When calamity comes, the wicked are brought down, but even in death the righteous have a refuge.",
    "Isaiah 54:10": "\"Though the mountains be shaken and the hills be removed, yet my unfailing love for you will not be shaken nor my covenant of peace be removed,\" says the LORD, who has compassion on you."
}

happy = {
    "John 16:22": "So also you have sorrow now, but I will see you again, and your hearts will rejoice, and no one will take your joy from you.",
    "Psalm 4:7": "You have put more joy in my heart than they have when their grain and wine abound.",
    "John 15:11": "These things I have spoken to you, that my joy may be in you, and that your joy may be full.",
    "Psalm 16:11": "You make known to me the path of life; in your presence there is fullness of joy; at your right hand are pleasures forevermore.",
    "1 Chronicles 16:27": "Splendor and majesty are before him; strength and joy are in his place."
}

angry = {
    "Psalm 37:8": "Refrain from anger, and forsake wrath! Fret not yourself; it tends only to evil.",
    "Proverbs 15:1": "A soft answer turns away wrath, but a harsh word stirs up anger.",
    "Proverbs 22:24": "Make no friendship with a man given to anger, nor go with a wrathful man.",
    "Ephesians 4:31": "Let all bitterness and wrath and anger and clamor and slander be put away from you, along with all malice.",
    "James 1:19": "Know this, my beloved brothers: let every person be quick to hear, slow to speak, slow to anger..."
}

emotions = input("How are you feeling?: ").lower()

if emotions == "sad" or emotions == "grief":
    print("HERE ARE SOME COMFORTING BIBLE PASSAGES FOR YOU:")
    for key, value in sad.items():
        print(key, value)

elif emotions == "happy" or emotions == "joyful" or emotions == "excited":
    print("HERE ARE SOME BIBLE PASSAGES FOR YOU:")
    for key, value in happy.items():
        print(key, value)

elif emotions == "angry" or emotions == "upset":
    print("HERE ARE SOME BIBLE VERSES TO CHEER YOU UP:")
    for key, value in angry.items():
        print(key, value)
else:
    print("JESUS LOVES YOU! <3")

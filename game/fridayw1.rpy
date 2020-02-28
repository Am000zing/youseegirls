label Friday_One_withMio:
"Ugh..."
"I stayed up all night gaming with Mio."
"He's really good at the game!"
"Or maybe I just suck."
"Oh, shoot, it's Friday. I have class!"
"I checked the time."
N "Ah, shoot."
Mio "zzz..."
"I ran out quickly to my room and got ready."
"Morning routine over and out!"
jump Friday_One_AfterClass

label Friday_One:
show dorm morning with Fade(1.0,0,1.0)
"I wake up early, somewhat tired from the first day of class yesterday."
"It wasn't too bad at least. The jet lag is wearing off, and my sleep schedule has improved greatly."
"It's time to get to class though!"
"Morning routine over and out!"
jump Friday_One_AfterClass

label Friday_One_AfterClass:
"After class, I walked back my dorm wearily."
"Ah, this week has been quite the ride. I've met so many people, and all this social interaction has really tired me out."
"What should I do now?"
menu:
    "Study":
        "I should probably study for my classes."
        "I can't afford to slack off, even if I'm no longer in high school!"
        "Ah, I'm so worn out."
        "I should probably shower and sleep..."
        "zzz..."
    "Go Sleep":
        "I'm so worn out from this week and from classes."
        "I should just get some rest."
        "I should probably shower and sleep..."
        "zzz..."
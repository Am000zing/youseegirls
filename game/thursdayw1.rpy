label Thursday_One:

scene dorm inside
with Fade(1.0, 0.0, 1.0)
"I woke up and found a piece of paper that had been slid under the door."
"I picked it up."
"It reads:"
"I picked it up. It reads:"
"Hey [name]!"
"I think you could use a break from me today, since your legs are probably tired and class is about to start for you."
"Message me if you need anything! Your dear RA, Mio (951)XXX-XXXX"
"Well, it would be nice to take a break today, especially since I've been flung into action as soon as I stepped off the plane."
"Time to get ready for the day..."
#time skip
"Okay, I think I'm about ready to go out now."
"Hmm...should I see if Mio's up?"
menu:
    "Knock on Mio's door.":
        #knock knock knock
        "No one answered. There's no noise from inside."
        jump knock_once
    "Leave":
        jump leave_for_class

label knock_once:
menu:
    "Knock again?":
        #knock knock knock
        "Still quiet."
        jump knock_twice
    "Leave.":
        jump leave_for_class

label knock_twice:
menu:
    "Knock again?":
        #knock knock knock
        jump knock_thrice
        "There's no response."
    "Leave.":
        jump leave_for_class

label knock_thrice:
menu:
    "Knock again?":
        #knock knock knock
        Mio "Hey, I'm trying to sleep! I'll talk to you later."
        jump after_knocking_thrice
    "Leave":
        jump leave_for_class

label after_knocking_thrice:
menu:
    "Leave":
        jump leave_for_class

label leave_for_class:
"I should probably leave him alone. It's pretty early."
"As I near the exit, my phone buzzes. It's a text from Auntie."
Auntie "Good morning sweetie!"
Auntie "I was thinking that your Uncle and I might come to visit you for lunch."
Auntie "How has your time been at UCJJ?"
menu:
    "It's been fun.":
        "I text her back:"
        N "It's really fun! I've become good friends with the tour guide."
        Auntie "That's great to hear!"
    "It's been great!":
        "I text her back:"
        N "It's been great! The students here are interesting."
        N "I've met a some new girls that I think I might get along with."
        Auntie "Oh my! Well, make sure you stay focused on your studies."
    "It's been fine.":
        N "It's been fine. I'm not sure that I've found anything I'm interested in yet."
        Auntie "Oh, that's alright."
        Auntie "You just need to spend more time getting to know things, and then you'll figure out what you like."

Auntie "Anyways, good luck with school! I'll talk to you more at lunchtime."
N "Okay, Auntie. Thanks!"
"Ahh, it's nice to know that I also have family here."
"I should really call Mom though..."
"Ah, I need to get to class! Shouldn't be late for my first day!"
# time skip
show dorm afternoon with dissolve
"Class wasn’t too bad. The teacher seems really nice and understanding, so I think I’ll have a good time here!"
"Especially since I have Auntie taking care of me."
"It was nice to see her for lunch."

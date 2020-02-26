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
A "{i}Good morning sweetie!{/i}"
A "{i}I was thinking that your Uncle and I might come to visit you for lunch.{/i}"
A "{i}How has your time been at UCJJ?{/i}"
menu:
    "It's been fun.":
        "I text her back:"
        N "{i}It's really fun! I've become good friends with the tour guide.{/i}"
        A "{i}That's great to hear!{/i}"
    "It's been great!":
        "I text her back:"
        N "{i}It's been great! The students here are interesting.{/i}"
        N "{i}I've met a some new girls that I think I might get along with.{/i}"
        A "{i}Oh my! Well, make sure you stay focused on your studies.{/i}"
    "It's been fine.":
        N "{i}It's been fine. I'm not sure that I've found anything I'm interested in yet.{/i}"
        A "{i}Oh, that's alright.{/i}"
        A "{i}You just need to spend more time getting to know things, and then you'll figure out what you like.{/i}"

A "{i}Anyways, good luck with school! I'll talk to you more at lunchtime.{/i}"
N "{i}Okay, Auntie. Thanks!{/i}"
"Ahh, it's nice to know that I also have family here."
"I should really call Mom though..."
"Ah, I need to get to class! Shouldn't be late for my first day!"
# time skip
show dorm afternoon with Fade(1.0,0,1.0)
"Class wasn’t too bad. The teacher seems really nice and understanding, so I think I’ll have a good time here!"
"Especially since I have Auntie taking care of me."
"It was nice to see her for lunch."
"Huh, now that I think about it, I wonder if Mio’s still in his room."
"He was probably sleeping in the morning, but now it’s the afternoon."
"He should be awake by now, right?"
"He did give me his contact details. I could message him if I want to…"
"Message Mio?"
menu:
    "Yes":
        jump annoyMio_optionyes1
    "No":
        "He's probably not going to respond anyways."

label annoyMio_optionyes1:
N "Hey Mio, you awake?"
"..."
"No response."
N "Sorry for bothering, but I just wanted to know if you wanted to hang out."
"..."
N "I'm bored."
"..."
"I think he’s sleeping."
"Even though it’s well in the afternoon, he did mention that he enjoys napping after classes."
"I decide to head back to the dorm. Maybe I could knock on his door when I get there…"
scene dorm night with Fade(1.0,0,1.0)
"I lay back in my chair, trying to relax."
"I’m kind of tired now that I think about it."
"Maybe I should take a nap with Mio too."
"Or should I go knock on Mio’s door?"
label Monday_One:

show dorm inside
with Fade(1.0, 0.0, 1.0) 

"I woke to the sunlight streaming through the blinds and the loud sound of machinery outside the window."
"*Yawn*"
"I stretched and peeked through the blinds. There was a man mowing the lawn, and another blowing leaves away."
"I checked the time"
"It's 8 AM! I woke up so early..."
"Man, jet-lag is one hell of a sucker."

#jump: Agenda

"I did my morning routine: brushing my teeth, washing my face, did my hair..."
"I'm so excited what might happen today!"
"I exited the dorms, and made my way to the parking lot where I supposed to meet up with Mio."
show parking lot with Fade(2.0,0,2.0) 
"Oh? He isn't here yet?"
"I checked the time..."
"It's 9:50AM."
"Maybe he's running a bit late. I'll just wait around for him."

"Close by, a car screeched into a parking space."
"Wow! It's so glossy-looking..."
"And a Mercedes? S-Class? I didn't realize people enjoyed their wealth on their sleeve, not that it's up to me to decide."
"A girl stepped out, dressed in her school uniform with a large oversized jacket on top."
"Her large sunglasses covered half her face. How could she possibly hold her head up with such large, heavy glasses?"
"In her hand was a cup of boba milk tea."
"She took a sip as she shut her car door, but then suddenly she sounded like she, quite loudly, had a hard time breathing."

menu:
    "Check out if she's okay.":
        "I head over to check on her. Maybe she choked on her drink!"
    "Stay where you are.":
        "Her lurching sounds grow louder. I think she's choking!"
        "I decide to head over to her and not be a degenerate bystander."
label after_checking:
N "Hey, are you alright?"
"She looks up, her face becoming a bit blue and tears in her eyes."
"Oh no, she's dying!"
"Thinking fast, I come up with a solution to attempt to save her."
N "Okay, this might hurt a bit, but I'll try to help you!"
"I slapped her back with all my might-"

$ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
show parking lot with sshake

"-And out came a tapioca pearl!"
"Her sunglasses nearly came off with how hard I slapped her back but god knows what would've happened if I didn't help though..."
"She slowly straightened herself up, adjusting her glasses and her jacket."
"She's breathing a bit heavily..."
"Oh no, maybe I hit her too hard?"

menu:
    "Apologize for hitting her.":
        N "Sorry about suddenly hitting you so hard."
        unknown "It's fine."
        unknown "My back has a dull sting to it, but at least you tried to help me."
        "Tried to help her...?"
    "Ask if she's okay.":
        N "Are you okay?"
        unknown "Yeah, I'm fine."
        unknown "My back does have a dull sting to it though."
label after_firstIrene:
N "Well, I'm glad you're not choking anymore! I was really concerned when I saw you suddenly nearly fall over..."
unknown "I'm sorry you had to see something so disgraceful... please don't speak of this to anyone else."
N "Uh... okay?"
"Not that I'd have anyone to talk about this to..."
unknown "Here."
"She hands me a $20 bill."
"..."
"What?"
N "W-why? It's fine I don't need it"
unknown "No, I insist. It's for saving my life."
"O-okay then."
"I guess I just got $20...?"
unknown "By the way, what's your name?"
unknown "There aren't many people attending the UCJJ summer school sessions, so it's easy to spot new faces."
N "Ah, I'm [name]! It's very nice to meet you."
unknown "I see."
Irene "Well, I'm Irene. Hope to see you around sometime."
N "Yeah, see you around!"
"She left the parking lot and walked into campus, sipping on her boba."
"How interesting. She seems like she means well, but she can't seem to express it in a...nice manner?"
"Ah, well, it's not up to me to judge."
"I hear a voice from behind"
Mio "Hey!"
show mio neutral
Mio "Wow, you were really on time. Sorry for being late."
menu:
    "It's no problem.":
        Mio "No problem, huh?"
        show mio teasing
        Mio "What, you met someone cool while I was gone? Without me?"
    "What held you up?":
        show mio teasing
        Mio "I'll be honest, there was a really good book that I never thought about reading before that I ended up getting hooked on."
        menu:
            "What book were you reading?":
                $Mio_LP += 1
                Mio "Well, uh..."
                Mio "It was more of, um, a manga."
                Mio "It's a bit embarassing to talk about right now, but just know it was insane."
                Mio "So bizarre, in fact, that I ended up staying up all night reading!"
            "That's cool.":
                Mio "Indeed!"
    "How unprofessional.":
        $ Mio_LP -= 1
        show mio upset
        Mio "Ah, man, cut me some slack."
        Mio "I'm a student, just like you."

show mio neutral
Mio "Anyways, let's get going!"
hide mio neutral with dissolve
#Time-Skip. prob just say something like the tour guide lasted up til lunch
show parking lot with Fade (2.0,0,2.0)

show mio neutral with dissolve
Mio "~And that's it for today's tour!"
Mio "Let's head over to the dining hall. You're probably starving!"
"Huh, I didn't even realize that I hadn't eaten anything since the tour began."
"But I don't want to stretch Mio's time more than I need to."
N "Ah, I think I'll just head back to my room. I'm not that hungry."
$ sshake = Shake((0, 0, 0, 0), 2.0, dist=15)
show parking lot with sshake
"GROOOOWWWLWLLLWWHWWH~"
#probably have some sound effect for a very long stomach rumble
"I gasped and I clutched my stomach in embarrassment."
#"Mio stopped and turned to me."
show mio teasing
Mio "Heeeey, don't lie to me now. I thought we were good buddies, yeah?"
N "Haha, yeah..."
"He motioned towards the dorm's dining hall."
show mio laugh
Mio "Then let's go get something to eat! Clearly your stomach has a mind of its own."
"Meekly, I followed him."
hide mio laugh with dissolve
"Why do stomach growls always have to happen at the worst moment possible?!"
label dininghall_introduction:
show dining hall with Fade(2.0,0,2.0)
cashier "Have a nice day!"
N "Thank you!"
"I pocketed my ID card as I caught up with Mio who was waiting in the walkway."
show mio neutral with dissolve
Mio "The dining hall here is like a buffet, so you can really pick and choose what you wanna eat!"
Mio "The theme of the cuisine varies every other day as well so that there's as many options as possible."
N "Ohh, that's pretty cool!"
Mio "I'll have you look around by yourself first."
"He motions to the corner of the dining hall."
Mio "Find me at one of the tables there when you're done!"
N "Sounds good."
hide mio neutral with dissolve
"I stared at the onslaught of entrées and sides available to me."
"Wow, there's so many options!"
"I do feel a bit overwhelmed by everything, so I should narrow down what seems good."
menu:
    "Kale Feta Salad":
        "I grabbed the tongs and heaped a helping of kale feta salad onto my plate. I feel healthier already!"
        "As I contemplated over salad dressings, I overhear someone rapidly asking the chefs a bunch of questions."
        unknown "Is this dish vegetarian friendly?"
        unknown "So this isn't cooked in like animal fat either, right?"
        unknown "Like butter?"
        unknown "Where do you get your veggies from?"
        Chef "Uhh, miss, it says right there on the label that it is a vegetarian dish..."
        unknown "I know, but I'm just making sure. I promised myself that I'd eat less animal stuff."
        unknown "Sorry for all the questions!"
        Chef "Ah, it's no problem, miss!"
        "The girl turned and saw me watching her."
        "I nervously looked back at the salad dressings, hoping she didn't notice."
        show dany neutral
        with dissolve
        unknown "How's the salad?"
        unknown "Is it good here?"
        unknown "We didn't have kale on my farm, dad was never too big on it."
        N "Uhh...I haven't tried it yet."
        "This is kinda awkward...I don't even know who she is!"
        show dany concern
        unknown "Oh, I'm so sorry. I haven't even told you who I am!"
        show dany laugh
        Dany "My name's Dany."

    "Roast Chicken & Rice":
        "I heaped a spoonful of rice onto my plate. Can't ever go any meal without rice!"
        "I eyed the large pan of roast chicken, which laid next to a pan of mashed potatoes and a separate pan of gravy."
        "As I grabbed the tongs to reach for the chicken, I overhear someone rapidly asking the chefs a bunch of questions."
        unknown "Is this dish vegetarian friendly?"
        unknown "So this isn't cooked in like animal fat either, right?"
        unknown "Like butter?"
        unknown "Where do you get your veggies from?"
        Chef "Uhh, miss, it says right there on the label that it is a vegetarian dish..."
        unknown "I know, but I'm just making sure. I promised myself that I'd eat less animal stuff."
        unknown "Sorry for all the questions!"
        Chef "Ah, it's no problem, miss!"
        "The girl turned and saw me watching her."
        "I nervously tried to hide my plate full of chicken from her sight, but she came over anyways."
        show dany concern
        with dissolve
        unknown "You don't have to hide meat from me just 'cause I'm trying to be a vegetarian, you know. Even I can't resist it sometimes!"
        N "Really?"
        show dany happy
        unknown "Yeah. My dad makes *the best* ribs."
        show dany laugh
        Dany "Oh, my name's Dany, by the way."

show dany neutral
N "I'm [name]."
#"Give Dany a gift?"
#menu:
#    "Yes":
#        jump danygift
#    "No":
#        jump aftergiftgiving
#label aftergiftgiving:
Dany "Nice to meet you, [name]! Wanna eat with me?"
"I see Mio waving at me from his table."
N "Ah, no, sorry. I'm already sitting with someone."
Dany "Alrighty. I'll see you later then, [name]!"
hide dany happy with dissolve
scene dorm afternoon with Fade(2.0, 0.0, 2.0) with Pause(1)

"I laid back in my bed, still full from that heavy buffet."
"I thought that I would be able to take it...but it's really hard to stop yourself when you know you could keep going!"
"I yawned loudly, physical and mental fatigue setting in."
"I'm so tired...I haven't had some solid sleep since coming back."
"I'll just...close my eyes...for a bit..."
"zzz..."

jump Tuesday_One
label quad_encounters:
#show quad

#RYVER ENCOUNTERS
#RYVER ENCOUNTER ONE
label e_Ryver_1:
$ ryver_encounter = True
#Ryver is outside in the Quad.
"She’s sitting on the lawn with two library books lying open in front of her, scribbling in a notebook on her lap."
menu:
    "Approach Ryver?"
    "Yes":
        jump e_Ryver_1_A
    "No":
        #return to the quad options
        "She looks really busy. I shouldn't disturb her."
        jump quad_people
#(A.)
label e_Ryver_1_A:
$ Ryver_LP += 1.0
"As I walk closer, Ryver notices me approaching and looks up from her writing."
show ryver laughing with dissolve
Ryver "Hi, [name]! What’s up?"
N "Hey, Ryver! I just wanted to chat."
show ryver neutral
Ryver "Cool! How’s university life treating you?"
N "It’s been fine. Mind if I sit with you?"
show ryver laughing
Ryver "Of course not!"
show ryver neutral
"She starts putting her books away to make space for me beside her."
N "What were you working on?"
Ryver "I’m trying to get a head start on my ethnic studies paper so I have more free time later."
menu:
    "Wow, a paper already?":
        $ Ryver_LP += 0.5
        jump e_Ryver_1_A1
    "Ethnic Studies is an interesting subject.":
        $ Ryver_LP += 1.5
        jump e_Ryver_1_A2
    "What do you like to do in your free time?":
        $ Ryver_LP += 1.0
        jump e_Ryver_1_A3

#[“Wow, a paper already?”]
label e_Ryver_1_A1:
show ryver annoyed
Ryver "Yes. It’s not due yet, but I don’t like when my workload piles up."
show ryver neutral
menu:
    "I'm a procrastinator myself.":
        $ Ryver_LP -= 1.0
        show ryver annoyed
        Ryver "But don’t you end up feeling really stressed? I can direct you to a time-management workshop, if you want. That really helped me."
        jump e_Ryver_1_A_End
        #Relationship Result: -0.5
    "Homework can be stressful.":
        $ Ryver_LP += 1.0
        show ryver neutral
        Ryver "Right? I’m glad you get it. You probably have some coping tips of your own. Maybe we can share later."
        jump e_Ryver_1_A_End
        #Relationship Result: 1.5

#[“Ethnic Studies is an interesting subject.”]
label e_Ryver_1_A2:
show ryver laughing
Ryver "It is! I’m glad UCJJ is making it a requirement for new students."
Ryver "I think everyone should open their minds to the diverse perspectives of the world."
menu:
    "You sound really passionate about that.":
        $ Ryver_LP += 1.0
        show ryver laughing
        Ryver "Yeah, I am pretty passionate about equality and human rights. I want to do something with that after I graduate."
        jump e_Ryver_1_A_End
        #Relationship Result: 3.5
    "I agree. Education is important.":
        $ Ryver_LP += 0.5
        show ryver neutral
        Ryver "Haha, yeah! There really should be more people like you."
        jump e_Ryver_1_A_End
        #Relationship Result: 2.5

#[“What do you like to do in your free time?”]
label e_Ryver_1_A3:
show ryver neutral
Ryver "Oh, just hang out with my friends and chill. Maybe go to a concert from time to time."
menu:
    "Do you have a lot of friends?":
        $ Ryver_LP += 0.5
        show ryver neutral
        Ryver "Yeah. A lot of them are from this club I’m in. Speaking of..."
        #Relationship Result: 2.5
    "What kind of music do you listen to?":
        $ Ryver_LP += 1.0
        show ryver neutral
        Ryver "Music? I like EDM. And lo-fi, sometimes."
        #Relationship Result: 3.0
    "That's cool.":
        jump e_Ryver_1_A_End
        #Relationship result: 2.0

label e_Ryver_1_A_End:
"Ryver shoulders her bookbag and stands up."
show ryver neutral
Ryver "Anyways, I have to run to a meeting now. It was nice seeing you!"
N "See you later!"
"Ryver waves enthusiastically as she leaves."
hide ryver neutral with dissolve
jump menu_areas

###################################################
#RYVER ENCOUNTERS
#RYVER ENCOUNTER TWO
label e_Ryver_2:
$ ryver_encounter = True
"Ryver is talking with a group of people in the Quad. I hear them saying goodbyes as they start to disperse."
menu:
    "Approach Ryver?"
    "Yes":
        jump e_Ryver_2_A
    "No":
        #return to the quad options
        "She’s still chatting with someone. I don’t want to interrupt them."
        jump quad_people
#(A.)
label e_Ryver_2_A:
$ Ryver_LP += 1.0
N "Hey Ryver!"
show ryver laughing with dissolve
Ryver "Oh, hey, [name]!"
"She seems really bubbly after socializing with those people."
N "What’re you up to?"
show ryver neutral
Ryver "I just got out of a club meeting."
menu:
    "Which club?":
        jump e_Ryver_2_A1
    "Does that mean you're free now?":
        jump e_Ryver_2_A2
    "How was it?":
        jump e_Ryver_2_A3

#[“Which club?”]
label e_Ryver_2_A1:
$ Ryver_LP += 0.5
Ryver "Oh, the LGBTQ+ Club."
menu:
    "Oh, I didn't know you were...":
        jump e_Ryver_2_A1a
    "What do you do there?":
        jump e_Ryver_2_A1b

#["Oh, I didn't know you were..."]
label e_Ryver_2_A1a:
$ Ryver_LP += 0.5
show ryver concerned
Ryver "... Um, gay?"
show ryver laughing blushing
Ryver "Haha, no. I’m just an ally."
menu:
    "So, you still like guys?":
        $ Ryver_LP -= 1.0
        show ryver annoyed blushing
        Ryver "Yeah. Well, actually, if I’m being honest, I’m bi. I just think that everyone deserves a chance, you know?"
        #Relationship Result: 1.0
        jump e_Ryver_2_End
    "That’s really cool.":
        $ Ryver_LP += 0.5
        show ryver neutral blushing
        Ryver "Yeah, it’s nice to be able to support others."
        #Relationship Result: 2.5
        jump e_Ryver_2_End

#[“What do you do there?”]
label e_Ryver_2_A1b:
$ Ryver_LP += 0.5
show ryver neutral
Ryver "Mostly we just hang out and talk. Sometimes we plan movie or game nights. It’s chill."
menu:
    "Wow, sounds fun.":
        $ Ryver_LP += 0.5
        show ryver laughing
        Ryver "Yeah. It is. You should join!"
        N "I’ll think about it, for sure."
        #Relationship Result: 2.5
        jump e_Ryver_2_End
    "Sounds like I should join.":
        $ Ryver_LP += 1.0
        show ryver laughing
        Ryver "You totally should! It’ll be extra exciting with you there. The more the merrier!"
        #Relationship Result: 3.0
        jump e_Ryver_2_End

#["Does that mean you're free now?"]
label e_Ryver_2_A2:
$ Ryver_LP += 0.5
show ryver neutral
Ryver "Just for a minute. I have plans with some friends."
menu:
    "How’s your Ethnic Studies paper?":
        $ Ryver_LP += 0.5
        show ryver neutral
        Ryver "Done! I submitted it already."
        Ryver "Too bad early turn-in extra credit isn’t a thing in college, otherwise I might actually get a good grade on that paper, ha."
        #Relationship Result: 2.0
        jump e_Ryver_2_End
    "Where are you going?":
        $ Ryver_LP -= 1.0
        show ryver annoyed
        Ryver "Nosy much?"
        show ryver neutral
        Ryver "We’re just gonna chill a friend’s house, that’s all."
        #Relationship Result: 0.5
        jump e_Ryver_2_End

#["How was it?"]
label e_Ryver_2_A3:
$ Ryver_LP += 1.0
show ryver neutral
Ryver "It was good! A lot of people came. It’s nice to see everyone finding a place where they feel welcomed."
menu:
    "Wow, sounds fun.":
        $ Ryver_LP += 0.5
        show ryver laughing
        Ryver "Yeah. It is. You should join!"
        N "I’ll think about it, for sure."
        #Relationship Result: 2.5
        jump e_Ryver_2_End
    "Sounds like I should join.":
        $ Ryver_LP += 1.0
        show ryver laughing
        Ryver "You totally should! It’ll be extra exciting with you there. The more the merrier!"
        #Relationship Result: 3.0
        jump e_Ryver_2_End

label e_Ryver_2_End:
unknown "HEY, RYVER! Are you coming?"
#I see a girl beckoning Ryver over. She’s standing by a few other members of the LGBTQ+ club.
show ryver concerned
Ryver "Sorry. I gotta go. I promised I’d hang out with them."
N "It’s no problem."
Ryver "See you later?"
N "Yeah! See you."
hide ryver concerned with dissolve
jump menu_areas


###################################################
#RYVER ENCOUNTERS
#RYVER ENCOUNTER THREE
label e_Ryver_3:
$ ryver_encounter = True
"Ryver is laying on the lawn in the Quad."
"She has earphones in and her eyes are closed. It looks like she’s relaxing or taking a nap."
menu:
    "Yes":
        jump e_Ryver_3_A
    "No":
        "I think I just heard a little snore. I better let her relax in peace."
        jump quad_people
label e_Ryver_3_A:
"As I come closer, I hear music faintly blaring from her earphones. She couldn’t be asleep with the volume that loud, could she?"
N "Hey, Ryver?"
"She doesn’t respond. Maybe a little louder…"
N "Ryver!"
"She still can’t hear me. I should..."
menu:
    "She still can't hear me. I should..."
    "Pull an earphone out of her ear.":
        jump e_Ryver_3_A1
    "Yell at the top of my lungs.":
        jump e_Ryver_3_A2
    "Nudge her side with my foot.":
        jump e_Ryver_3_A3

#["Pull an earphone out of her ear."]
label e_Ryver_3_A1:
"She sits up suddenly and tries to yank the earphone from my hand."
show ryver annoyed with dissolve
$ Ryver_LP -= 1.0
Ryver "Hey! That’s not cool, bro."
menu:
    "Apologize.":
        jump e_Ryver_3_A1a
    "See what she's listening to.":
        jump e_Ryver_3_A1b

label e_Ryver_3_A1a:
N "I’m sorry. I only wanted to get your attention."
show ryver neutral
$ Ryver_LP += 1.0
Ryver "Oh, that’s alright. Sorry for snapping."
N "You’re fine."
menu:
    "What're you listening to?":
        $ Ryver_LP += 1.0
        Ryver "This cool EDM artist, Skill-Rex. I listen to them a lot, especially at, uh, parties."
        Ryver "I just went to one last night, so I’m trying to catch up on sleep out here between classes."
        show ryver concerned
        Ryver "So as much as I’d like to talk with you, I don’t have a lot of time..."
        #Relationship Result: 1.0
        jump e_Ryver_3_end
    "How are you?":
        $ Ryver_LP += 0.5
        Ryver "Oh, I’m fine. I’m pretty tired though. I had an eventful night, so I’m just trying to catch up on sleep out here between classes."
        Ryver "What’s new with you?"
        N "I’ve been getting to know the people here more. I think I’m going to make some lasting relationships."
        show ryver laughing
        Ryver "Awesome!"
        show ryver neutral blushing
        Ryver "I hope I’m one of those people."
        show ryver concerned
        Ryver "I hate to cut our bonding time short, but I’m really exhausted, so..."
        #Relationship Result: 0.5
        jump e_Ryver_3_end

####
label e_Ryver_3_A1b:
$ Ryver_LP -= 1.0
"I quickly put the earphone to my ear and hear the wub wubs of some hardcore dubstep."
show ryver annoyed
Ryver "Knock it off."
menu:
    "Start headbanging to the music.":
        show ryver laughing
        Ryver "What are you doing?!"
        N "Jammin’! Is this Skill-Rex?"
        $ Ryver_LP += 3.0
        show ryver neutral
        Ryver "Heck yeah! I didn’t know you liked them. With those moves, I bet you’re fun at parties."
        show ryver concerned
        Ryver "But right now, I’m totally partied out and need a nap, so..."
        #Relationship Result: 2.0


#["Yell at the top of my lungs."]
label e_Ryver_3_A2:
"I take a deep breath-"

#["Nudge her side with my foot."]
label e_Ryver_3_A3:
"I gently kick the toe of my shoe against Ryver’s side."

######
label e_Ryver_3_end:
N "I see. I guess I’ll leave you to your nap, then. See you tomorrow?"
"Ryver waves her hand in a silent goodbye as she lays back down, music loud in her ears."
"Almost instantly she’s out."
"I think I just heard her snort! It’s kind of endearing..."
"Argh, I should stop being such a creeper, watching her sleep."
jump quad_people
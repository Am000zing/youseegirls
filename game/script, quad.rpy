label quad_encounters:
scene Quad with dissolve

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
#[Apologize]
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
#[See what she's listening to.]
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
        jump e_Ryver_3_end
        #Relationship Result: 2.0
    "Give her the earphone back.":
        N "Here."
        $ Ryver_LP += 0.5
        Ryver "Thanks, [name]."
        show ryver concerned
        Ryver "Listen, I’d like to chat, but I’m really tired right now. Another time, maybe?"
        jump e_Ryver_3_end
        #Relationship Result: -1.5

#["Yell at the top of my lungs."]
label e_Ryver_3_A2:
"I take a deep breath-"
N "RYVER!!!"
"Some students walking by give me weird looks."
"Well, at least Ryver woke up. She looks both annoyed and confused."
show ryver annoyed
Ryver "[name]?"
"She suddenly sits up and the earphones fall out of her ears. She looks around, noticing the people staring and whispering."
$ Ryver_LP -= 1.0
show ryver annoyed blushing
Ryver "Why did you do that?"
N "I thought it was the best way to get your attention."
Ryver "Well, you really shouldn’t have."
menu:
    "I'm sorry.":
        $ Ryver_LP += 1.0
        Ryver "You should be. That was really embarrassing."
        Ryver "I don’t like that kind of attention. I just prefer to... stay out of the spotlight."
        jump e_Ryver_3_A21
    "What's your problem?":
        $ Ryver_LP -= 1.0
        Ryver "What’s my problem?"
        Ryver "You, at the moment."
        "She stuffs her earphones back in her ears and crosses her arms, refusing to look at me."
        "I guess I should go..."
        jump e_Ryver_3_end
        #Relationship Result: -2.0


label e_Ryver_3_A21:
menu:
    "So you're introverted?":
        show ryver annoyed
        Ryver "Well, if you have to put a label on it, I suppose I am introverted."
        show ryver concerned
        Ryver "Sometimes it feels like people forget I’m there... but I still like hanging out with them."
        Ryver "Anyways, right now I’d like to be alone and get a nap in before class. Nothing personal, [name]."
        jump e_Ryver_3_end
        #Relationship Result: 0.0
    "Really? You seem so sociable.":
        $ Ryver_LP += 0.5
        Ryver "I do try to be sociable, but I’m not exactly extroverted."
        show ryver concerned
        Ryver "Like, I still enjoy being around people, but, I wonder, do they like being around me?"
        "Ryver shakes her head."
        Ryver "That’s just the sleep-deprivation talking..."
        jump e_Ryver_3_end
        #Relationship Result: 0.5

#["Nudge her side with my foot."]
label e_Ryver_3_A3:
"I gently kick the toe of my shoe against Ryver’s side."
"She starts to wake up and blinks groggily at me."
"With a yawn, she sits up and takes the earphones out."
show ryver neutral
Ryver "Hey, [name]."
N "Good morning."
Ryver "Yeah, yeah."
menu:
    "What're you listening to?":
        Ryver "This cool EDM artist, Skill-Rex. I listen to them a lot, especially at, uh, parties."
        jump e_Ryver_3_A31
    "Rought night?":
        Ryver "You could say that."
        jump e_Ryver_3_A32

label e_Ryver_3_A31:
menu:
    "What kind of parties do you go to?":
        $ Ryver_LP += 2.0
        Ryver "Oh, a lot of college house parties, cool concerts with friends, and-"
        show ryver neutral blushing
        "She pauses to lean in closer, as if to tell a secret."
        Ryver "... my favorite are those raves that go hardcore, you know? The kind that ends up getting shut down because it gets too out of hand. They’re so much fun!"
        show ryver neutral
        Ryver "I may or may not have gone to one last night, so I’m super exhausted right now."
        jump e_Ryver_3_end
        #Relationship Result: 2.0
    "We should party sometime.":
        show ryver concerned
        Ryver "Oh yeah? I dunno. I think I’d have to see your dance moves first. I go pretty hard sometimes."
        "I focus on the faint music coming out from the earphones and start bobbing my head and grooving, showing off some of my best moves."
        show ryver laughing blushing
        $ Ryver_LP += 3.0
        Ryver "Woah, [name]! That’s cool stuff."
        show ryver neutral blushing
        Ryver "Alright, maybe we can vibe. I’ll think about it."
        Ryver "But I’m all partied out for now and need a big nap. I’ll be down to talk to you tomorrow, ‘kay?"
        jump e_Ryver_3_end
        #Relationship Result: 3.0

label e_Ryver_3_A32:
menu:
    "Is everything alright?":
        $ Ryver_LP += 1.0
        Ryver "Oh, yeah, totally. Nothing bad happened; don’t worry."
        Ryver "It’s just that I may have partied a little too hard last night and my head still hurts."
        N "Do you need anything?"
        Ryver "No, I think I just need to rest up. Thanks for asking, though."
        jump e_Ryver_3_end
        #Relationship Result: 1.0
    "More schoolwork?":
        $ Ryver_LP += 0.5
        Ryver "No..."
        N "No more ethnic studies papers?"
        Ryver "Not yet, but that one paper I worked on earlier was so that I could go to a party last night."
        N "A party? Oh, cool."
        Ryver "Yep. Maybe if you’re free next time we can go together."
        show ryver concerned
        Ryver "Ooh... My head is still kind of pounding. I should lay back down..."
        jump e_Ryver_3_end
        #Relationship Result: 0.5

######
label e_Ryver_3_end:
N "I see. I guess I’ll leave you to your nap, then. See you tomorrow?"
"Ryver waves her hand in a silent goodbye as she lays back down, music loud in her ears."
"Almost instantly she’s out."
"I think I just heard her snort! It’s kind of endearing..."
"Argh, I should stop being such a creeper, watching her sleep."
jump quad_people



#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#MERCIE ENCOUNTERS
#MERCIE ENCOUNTER ONE
label e_Mercie_1:
$ mercie_encounter = True
"Mercie is sitting alone at a table, aimlessly staring at her phone. She doesn't look very busy. If anything, she looks bored."
menu:
    "Approach Mercie?"
    "Yes":
        $ Mercie_LP += 1.0
        jump e_Mercie_1_A
    "No":
        "I shouldn't bother her."
        jump quad_people

label e_Mercie_1_A:
N "Hey, Mercie! Can I sit with you?"
show mercie concern with dissolve
"She looks up and blinks like I spoke gibberish to her."
Mercie "... Y-You want to sit? With {i}me{/i}?"
"Huh? That's a silly question. I just wanted to talk to her."
N "Well, I don't have any other plans. And you're fun to talk to."
N "Why?"
show mercie concern blush
Mercie "Ah!"
Mercie "N-No reason. I'm just..."
Mercie "..."
show mercie neutral
Mercie "Um, thanks."
"What's she thanking me for?"
"She moved her things aside and we chatted for a bit..."
hide mercie neutral with dissolve
scene quad with Fade(1.0,0,2.0)
show mercie happy with dissolve
Mercie "Well, I should get going. I've got class in a couple of minutes."
N "Okay! It was nice talking to you."
show mercie concern
Mercie "Yeah! I'll...see you later?"
show mercie happy
N "Yeah, see you!"
"She scurries away, a bounce in her step."
hide mercie happy with dissolve
jump menu_areas

#######################################################
#MERCIE ENCOUNTER TWO
label e_Mercie_2:
$ mercie_encounter = True
"She's sitting alone, this time twiddling her thumbs, almost as if she's expecting someone."
menu:
    "Approach Mercie?"
    "Yes":
        jump e_Mercie_2_A
    "No":
        "She's probably waiting for someone else."
        jump quad_people

label e_Mercie_2_A:
N "Hey, Mercie!"
show mercie happy
Mercie "Hey, [name]! Come here, I saved you a seat!"
"As I made my way over, I noticed she had notes out on her lap. Is she studying?"
menu:
    "Observe her work.":
        $ Mercie_LP += 1.0
        "I point to her lap."
        N "Is this for a class?"
        Mercie "Oh! This? It's for my breadth requirement."
        Mercie "But I...I kind of like the class though."
        "Wow. She looks super passionate about this type of stuff. Maybe I should ask her-"
    "Ask her what she's studying for.":
        $ Mercie_LP += 0.5
        N "Are you studying for something?"
        Mercie "H-Huh? Oh, um- Yeah."
        Mercie "I sit all the way in the back. And this really tall guy sits in front of me... "
        Mercie "I-I tend to fall behind..."
        N "I can try to help you if you want. What class is this for?"
        Mercie "R-Really? You don't have to."

Mercie "Wait- I just remembered."
Mercie "I-I have a meeting in five minutes!"
Mercie "{i}Ugh, why am I always so forgetful!{/i}"
N "O-Oh, okay! Good luck!"
Mercie "Thanks! See ya!"
N "See you later too..."
"Well, that was abrupt."
jump menu_areas

#######################################################
#MERCIE ENCOUNTER THREE
label e_Mercie_3:
if Mercie_LP >= 2:
    jump e_Mercie_3_alt
else: 
    jump e_Mercie_3_start

label e_Mercie_3_alt:
$ mercie_encounter = True
"I feel someone poke my arm."
Mercie "Hey, are you busy? If not, do you want to chat for a bit?"
menu:
    "Chat with Mercie?"
    "Yes":
        N "Yeah, I've got time to spare."
        "We ended up walking around the Quad aimlessly and complained about our classes..."
        scene Quad with Fade (2.0,0,2.0)
        "It sounds like she's really into plants and wildlife. It's the total opposite of what I expected...but also somehow not surprising."
        "Eventually, we got tired and decided to sit down."
        jump e_Mercie_3_A
    "No":
        $ Mercie_LP -= 1.0
        N "Sorry, not now."
        Mercie "Oh, um, okay. I'll see you around then."
        "She seems disappointed."
        jump menu_areas

label e_Mercie_3_start:
$ mercie_encounter = True
"She's leaning against a wall, toeing the ground aimlessly."
"She looks like she's expecting someone."
menu:
    "Approach Mercie?"
    "Yes":
        N "Hey, Mercie."
        show mercie happy with dissolve
        Mercie "Hi, [name]!! How has your day been?"
        N "It's been good. You seem excited."
        show mercie neutral
        Mercie "Haha, yeah..."
        show mercie concern
        Mercie "Hey, do you want to walk a little with me a bit?"
        N "I don't see why not."
        "I'm already here anyways."
        show mercie laugh
        Mercie "Cool!"
        hide mercie laugh with dissolve
        "We ended up walking around the Quad aimlessly and complained about our classes..."
        scene Quad with Fade (2.0,0,2.0)
        show mercie laugh with dissolve
        "It sounds like she's really into plants and wildlife. It's the total opposite of what I expected...but also somehow not surprising."
        "Eventually, we got tired and decided to sit down."
        jump e_Mercie_3_A
    "No":
        jump menu_areas

label e_Mercie_3_A:
menu:
    "Where should we sit?"
    "On the grass.":
        $ Mercie_LP += 2.0
        show mercie neutral
        N "You don't mind sitting on the grass, right?"
        Mercie "Not at all! I love the smell of fresh-cut grass!"
    "At a table.":
        $ Mercie_LP += 1.0
        show mercie neutral
        N "Let's go find a table."
        Mercie "Let's just hope it's clean, haha."
        N "Clean?"
        show mercie happy
        Mercie "Oh, yeah. Some people just don't clean after themselves. So, careful where you sit, newbie."

"We found a spot and settled down. We laid out our textbooks."
show mercie annoyed
Mercie "Ugh! It's always crowded this time of year. I can't wait 'til break!"
menu:
    "What are your plans for break?":
        $ Mercie_LP += 0.5
        show mercie concern
        "She sighs."
        Mercie "Probably go home and help my family."
        "Oh, your family owns a business?"
        Mercie "It's not exactly like that. Just kind of have a lot of cows."
    "God, I can't wait either.":
        $ Mercie_LP += 1.0
        show mercie neutral
        Mercie "Dude, you JUST started. Haha."
        N "I mean- I could always catch up on some games I bought."
        show mercie laugh
        Mercie "Pft- NERD."
        show mercie concern
        Mercie "I guess compared to you though, my break would be kind of boring."
"Huh? She doesn't look really happy..."
"Should I say something?"
menu:
    "Should I say something?"
    "You don't look so psyched.":
        $ Mercie_LP += 0.5
        N "Is there a reason?"
        Mercie "Well... It's remote, covered in fields. And every so often, you see a stray horse walking around."
        show mercie neutral
        Mercie "It's reaaally boring... But you know, it's home."
    "I'm sure you'll have fun!":
        $ Mercie_LP += 1.0
        N "Plus, you have a lot of cool friends to hang out with!"
        show mercie neutral
        Mercie "I guess you're right. I just wished I didn't live so far away from everything."

menu:
    "Well, if it's any consolation, I would definitely talk to you if you ever get bored.":
        show mercie neutral blush
        Mercie "..."
        show mericie happy
        Mercie "Thanks. I appreciate it."

show mercie neutral
"My phone rings."
##Ring Ring
"Oh, this phone call looks important."
N "O-Oh, sorry, Mercie. I really have to take this."
Mercie "Don't worry about it. I'm just about to run home anyway."
N "Ah, I see. I'll see you around then!"
Mercie "Bye!"
N "See you later!"
hide mercie neutral with dissolve
jump menu_areas
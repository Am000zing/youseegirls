label quad_encounters:

#RYVER ENCOUNTERS
#RYVER ENCOUNTER ONE
label e_Ryver_1:
$ ryver_encounter = True
#Ryver is outside in the Quad.
stop music fadeout 3.0
"She’s sitting on the lawn with two library books lying open in front of her, scribbling in a notebook on her lap."
menu:
    "Approach Ryver?"
    "Yes":
        $ c_Ryver += 1.0
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
stop music fadeout 3.0
"Ryver waves enthusiastically as she leaves."
hide ryver neutral with dissolve
if AP == 0:
    jump dayendings
else:
    jump menu_areas

###################################################
#RYVER ENCOUNTERS
#RYVER ENCOUNTER TWO
label e_Ryver_2:
$ ryver_encounter = True
stop music fadeout 3.0
"Ryver is talking with a group of people in the Quad. I hear them saying goodbyes as they start to disperse."
menu:
    "Approach Ryver?"
    "Yes":
        $ c_Ryver += 1.0
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
        play sound "audio/bad choice.mp3"
        show ryver annoyed blushing
        stop music fadeout 3.0
        Ryver "Yeah. Well, actually, if I’m being honest, I’m bi. I just think that everyone deserves a chance, you know?"
        #Relationship Result: 1.0
        jump e_Ryver_2_End
    "That’s really cool.":
        $ Ryver_LP += 0.5
        show ryver neutral blushing
        stop music fadeout 3.0
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
        stop music fadeout 3.0
        #Relationship Result: 2.5
        jump e_Ryver_2_End
    "Sounds like I should join.":
        $ Ryver_LP += 1.0
        play sound "audio/good choice.mp3"
        show ryver laughing
        Ryver "You totally should! It’ll be extra exciting with you there. The more the merrier!"
        stop music fadeout 3.0
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
        stop music fadeout 3.0
        #Relationship Result: 2.0
        jump e_Ryver_2_End
    "Where are you going?":
        $ Ryver_LP -= 1.0
        play sound "audio/bad choice.mp3"
        show ryver annoyed
        Ryver "Nosy much?"
        show ryver neutral
        Ryver "We’re just gonna chill a friend’s house, that’s all."
        stop music fadeout 3.0
        #Relationship Result: 0.5
        jump e_Ryver_2_End

#["How was it?"]
label e_Ryver_2_A3:
$ Ryver_LP += 1.0
play sound "audio/good choice.mp3"
show ryver neutral
Ryver "It was good! A lot of people came. It’s nice to see everyone finding a place where they feel welcomed."
menu:
    "Wow, sounds fun.":
        $ Ryver_LP += 0.5
        show ryver laughing
        Ryver "Yeah. It is. You should join!"
        N "I’ll think about it, for sure."
        stop music fadeout 3.0
        #Relationship Result: 2.5
        jump e_Ryver_2_End
    "Sounds like I should join.":
        $ Ryver_LP += 1.0
        play sound "audio/good choice.mp3"
        show ryver laughing
        Ryver "You totally should! It’ll be extra exciting with you there. The more the merrier!"
        stop music fadeout 3.0
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
if AP == 0:
    jump dayendings
else:
    jump menu_areas


###################################################
#RYVER ENCOUNTERS
#RYVER ENCOUNTER THREE
label e_Ryver_3:
$ ryver_encounter = True
stop music fadeout 3.0
"Ryver is laying on the lawn in the Quad."
"She has earphones in and her eyes are closed. It looks like she’s relaxing or taking a nap."
menu:
    "Approach Ryver?"
    "Yes":
        $ c_Ryver += 1.0
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
play sound "audio/bad choice.mp3"
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
play sound "audio/good choice.mp3"
Ryver "Oh, that’s alright. Sorry for snapping."
N "You’re fine."
menu:
    "What're you listening to?":
        $ Ryver_LP += 1.0
        play sound "audio/good choice.mp3"
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
        show ryver neutral
        Ryver "But I’m all partied out for now and need a big nap. I’ll be down to talk to you tomorrow, ‘kay?"
        jump e_Ryver_3_end
        #Relationship Result: 3.0

label e_Ryver_3_A32:
menu:
    "Is everything alright?":
        $ Ryver_LP += 1.0
        play sound "audio/good sound.mp3"
        show ryver 
        Ryver "Oh, yeah, totally. Nothing bad happened; don’t worry."
        Ryver "It’s just that I may have partied a little too hard last night and my head still hurts."
        N "Do you need anything?"
        show ryver neutral
        Ryver "No, I think I just need to rest up. Thanks for asking, though."
        jump e_Ryver_3_end
        #Relationship Result: 1.0
    "More schoolwork?":
        $ Ryver_LP += 0.5
        show ryver concerned
        Ryver "No..."
        N "No more ethnic studies papers?"
        show ryver neutral
        Ryver "Not yet, but that one paper I worked on earlier was so that I could go to a party last night."
        N "A party? Oh, cool."
        Ryver "Yep. Maybe if you’re free next time we can go together."
        show ryver concerned
        Ryver "Ooh... My head is still kind of pounding. I should lay back down..."
        show ryver neutral
        jump e_Ryver_3_end
        #Relationship Result: 0.5

######
label e_Ryver_3_end:
N "I see. I guess I’ll leave you to your nap, then. See you tomorrow?"
stop music fadeout 5.0
hide ryver neutral with dissolve
"Ryver waves her hand in a silent goodbye as she lays back down, music loud in her ears."
"Almost instantly she’s out."
"I think I just heard her snort! It’s kind of endearing..."
"Argh, I should stop being such a creeper, watching her sleep."
if AP == 0:
    jump dayendings
else:
    jump menu_areas

###################################################
#RYVER ENCOUNTERS
#RYVER ENCOUNTER FOUR
label e_Ryver_4:
$ ryver_encounter = True
stop music fadeout 3.0
"Ryver is laying on her back on the grass in the Quad."
"She’s awake this time, watching the cumulus clouds drift in the sky."
menu:
    "Approach Ryver?"
    "Yes":
        $ c_Ryver += 1.0
        jump e_ryver4
    "No":
        "I just don’t feel like talking to Ryver right now. Besides, she’s probably tired of seeing me all week."
        jump dayendings

label e_ryver4:
$ Ryver_LP += 1.0
play sound "audio/good choice.mp3"
"I take a few steps towards her and she notices me right away."
"Was she expecting me?"
show ryver neutral
Ryver "Hi, [name]!"
"She pats the grass next to her."
Ryver "Lie down with me?"
menu:
    "Sure":
        $ Ryver_LP += 1.0
        play sound "audio/good choice.mp3"
        jump e_ryver4a
    "I'd rather not.":
        $ Ryver_LP -= 1.0
        play sound "audio/bad choice.mp3"
        jump e_ryver4b
    "Why?":
        jump e_ryver4c

label e_ryver4a:
N "The grass looks almost soft."
show ryver laughing
Ryver "Right? It’s really comfy. That’s why you always find me chilling out here."
show ryver neutral
"I stretch out on my back next to Ryver."
"The grass feels cool against my skin and smells clean and fresh."
"As I take a deep breath, I catch a whiff of something citrusy...oranges?"
"This is the first time I’ve been this close to Ryver, enough to smell her perfume."
menu:
    "Now what?":
        jump e_ryver4a1
    "You smell nice.":
        $ Ryver_LP -= 1.0
        play sound "audio/bad choice.mp3"
        jump e_ryver4a2

label e_ryver4a1:
Ryver "Now we cloud-gaze. It's a beautiful day and the clouds are big and fluffy."
N "Yep, certainly beautiful."
"For a few minutes, we are relaxing in a peaceful quiet, gazing up at the sky."
"I feel so comfortable in this moment."
show ryver laughing
Ryver "Hey! That one-"
"She pointed up at a particular cloud."
show ryver neutral
Ryver "What does that look like to you?"
N "That one looks like..."
menu:
    "A fluffy bear!":
        $ Ryver_LP += 0.5
        Ryver "Oh yeah, it does look like a bear if it were on it’s back."
        Ryver "I was thinking it kinda looked like a heart."
        Ryver "But bears are cool too! They’re actually my favorite animal."
        show ryver laughing
        Ryver "They’re strong and fierce...{i}grahhh{i/}!"
        "She growls intimidatingly with her hands as claws."
        show ryver laughing blushing
        Ryver "But also cute and cuddly!"
        #Relationship Result: 2.5
    "A lovely heart!":
        $ Ryver_LP += 1.0
        play sound "audio/good choice.mp3"
        Ryver "That’s what I was thinking!"
        Ryver "Some people believe cloud formations are omens."
        Ryver "{i}I wonder if that heart means anything?{/i}"
        "We lie in silence for a little longer."
        "After a while, her hand brushes against mine."
        show ryver neutral blushing
        Ryver "Oops! Sorry."
        N "I-It’s no big deal."
        #Relationship Result: 3.0

label e_ryver4a2:
$ Ryver_LP -= 1.0
play sound "audio/bad choice.mp3"
show ryver annoyed
Ryver "What?"
N "You smell nice, like oranges."
Ryver "Oh, uh, thanks."
"Ryver subtly shifts away from me."
"Awkward. I guess she didn’t like the compliment."
menu:
    "So...":
        $ Ryver_LP -= 1.0
        play sound "audio/bad choice.mp3"
        Ryver "So...wanna cloud-gaze with me?"
        N "Sure."
        Ryver "It’s nice weather we’re having."
        N "Yep, very nice."
        "For a few minutes, we relax quietly, staring up at the sky."
        "The silence is a bit uncomfortable..."
        #Relationship result: -1.0
    "Why oranges?":
        $ Ryver_LP += 0.5
        Ryver "It reminds me of home. There were a lot of citrus groves near where I lived."
        N "Do you miss home?"
        Ryver "Not too much, only because I have made such good friends here that UCJJ’s almost like a second home to me now."
        N "Am I one of those friends?"
        show ryver neutral blushing
        Ryver "Maybe!"
        #Relationship Result: 0.5

label e_ryver4b:
Ryver "Oh... well, that’s okay."
"I squat down next to Ryver, making sure not to touch the grass."
"Ryver sits up."
N "You don't have to..."
Ryver "Nah, it’s alright."
menu:
    "So, now what?":
        jump e_ryver4b1
    "Nice weather.":
        jump e_ryver4b2

label e_ryver4b1:
$ Ryver_LP += 0.5
show ryver concerned
Ryver "So... wanna cloud-gaze with me?"
N "Sure."
show ryver neutral
Ryver "The clouds are big and fluffy today."
N "Yeah, they look nice."
"For a few minutes, we relax quietly, staring up at the sky."
Ryver "Hey! That one-"
"Ryver pointed up at a particular cloud."
Ryver "What does that look like to you?"
menu:
    "A fluffy bear!":
        $ Ryver_LP += 0.5
        Ryver "Oh yeah, it does look like a bear if it were on it’s back."
        Ryver "I was thinking it kinda looked like a heart."
        Ryver "But bears are cool too! They’re actually my favorite animal."
        show ryver laughing
        Ryver "They’re strong and fierce...{i}grahhh{i/}!"
        "She growls intimidatingly with her hands as claws."
        show ryver laughing blushing
        Ryver "But also cute and cuddly!"
        hide ryver laughing blushing with dissolve
        jump e_ryver4end
    "A lovely heart!":
        $ Ryver_LP += 1.0
        play sound "audio/good choice.mp3"
        Ryver "That’s what I was thinking!"
        Ryver "Some people believe cloud formations are omens."
        Ryver "{i}I wonder if that heart means anything?{i/}"
        "We lie in silence for a little longer."
        "After a while, her hand brushes against mine."
        show ryver neutral blushing
        Ryver "Oops! Sorry."
        N "I-It’s no big deal."
        hide ryver neutral blushing with dissolve
        jump e_ryver4end

label e_ryver4b2:
show ryver laughing
Ryver "It is! The UCJJ campus is really beautiful too. How are you liking it here?"
N "It’s great, honestly. Classes are, well, you know. But I’ve been having a lot of fun getting to know the other students...like you!"
Ryver "Aw, thanks! I like you too."
menu:
    "You like me?":
        $ Ryver_LP += 1.0
        play sound "audio/good choice.mp3"
        show ryver concerned blushing
        Ryver "Uh- well- yes! Who doesn’t!"
        hide ryver concerned blushing
        "We sit and talk for a long while, but it only feels like minutes."
        jump e_ryver4end
    "Check out that cool cloud!":
        $ Ryver_LP += 0.5
        N "Hey, check out that cloud! It looks like..."
        show ryver laughing
        Ryver "A heart! Aw, how cute."
        "She points at a different cloud."
        show ryver neutral
        Ryver "-And that one kind of looks like a poodle."
        N "No way! It does not!"
        hide ryver neutral with dissolve
        "We joke and laugh the day away."
        jump e_ryver4end

label e_ryver4c:
show ryver concerned
Ryver "Why?"
Ryver "I thought you wanted to hang out with me."
menu:
    "You're not upset?":
        jump e_ryver4c1    
    "Of course I do!":
        jump e_ryver4c2

label e_ryver4c1:
show ryver neutral
Ryver "Upset with you? Of course not!"
Ryver "I’m not one to hold grudges."
show ryver annoyed
Ryver "Unless you’ve really made me mad...then you’ll know!"
menu:
    "What's something that'd make you mad?":
        show ryver neutral
        $ Ryver_LP += 0.5
        Ryver "People taking advantage of each other. Like racial discrimination, or toxic relationships, or even students that cheat. It’s just horrible."
        N "You’re really passionate about human rights. I admire that."
        Ryver "Thanks. If only everyone could, then we wouldn’t have a problem."
        hide ryver neutral
        jump e_ryver4end
    "Phew! Guess I'm lucky.":
        $ Ryver_LP += 0.5
        show ryver laughing
        Ryver "Fortunately! Otherwise you’d get some of this!"
        "She punches me playfully in the shoulder."
        hide ryver laughing with dissolve
        "We joke and laugh with each other during the time we had."
        #Relationship Result: 1.0
        jump e_ryver4end

label e_ryver4c2:
$ Ryver_LP += 0.5
show ryver neutral
Ryver "Oh, that’s good. Got me worried for a second."
N "Don’t worry about that! I’m a good friend, I promise."
N "I just wanted to know what we were doing is all."
Ryver "Well, what do you want to do?"
menu:
    "Whatever you want.":
        $ Ryver_LP += 0.5
        Ryver "Wanna cloud-gaze with me?"
        N "Sure."
        #Ryver plays some chill lo-fi music from her phone speaker.
        Ryver "The sky is pretty today."
        N "It’s nice out too. Not too hot."
        hide ryver neutral with dissolve
        "We relax quietly, staring up at the sky."
        "Every so often we point out a funny-looking cloud and laugh about it."
        #Relationship Result: 1.5
        jump e_ryver4end
    "Let's just talk.":
        $ Ryver_LP += 0.5
        Ryver "Sure. What’d you want to talk about?"
        N "How’s school going for you? Have you met any other people?"
        show ryver laughing
        Ryver "School’s good. I feel really passionate about learning."
        show ryver neutral
        Ryver "Some of friends I have here are Bella and Mercie. They’re cool. Maybe you’ve met them."
        N "Yeah, I've bumped into them."
        hide ryver neutral with dissolve
        "We chat about whatever we can think of. I think we learn a lot about each other."
        #Relationship Result: 1.5
        jump e_ryver4end

label e_ryver4end:
stop music fadeout 3.0
"After hours of fascinating conversation fly by, we both say goodbye and go our separate ways."
if AP == 0:
    jump dayendings
else:
    jump menu_areas

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
stop music fadeout 5.0
"Mercie is sitting alone at a table, aimlessly staring at her phone. She doesn't look very busy. If anything, she looks bored."
menu:
    "Approach Mercie?"
    "Yes":
        $ Mercie_LP += 1.0
        $ c_Mercie += 1.0
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
scene qquad with Fade(1.0,0,2.0)
show mercie happy with dissolve
Mercie "Well, I should get going. I've got class in a couple of minutes."
N "Okay! It was nice talking to you."
show mercie concern
Mercie "Yeah! I'll...see you later?"
show mercie happy
stop music fadeout 5.0
N "Yeah, see you!"
"She scurries away, a bounce in her step."
hide mercie happy with dissolve
if AP == 0:
    jump dayendings
else:
    jump menu_areas

#######################################################
#MERCIE ENCOUNTER TWO
label e_Mercie_2:
$ mercie_encounter = True
stop music fadeout 3.0
"She's sitting alone, this time twiddling her thumbs, almost as if she's expecting someone."
menu:
    "Approach Mercie?"
    "Yes":
        $ c_Mercie += 1.0
        jump e_Mercie_2_A
    "No":
        "She's probably waiting for someone else."
        jump quad_people

label e_Mercie_2_A:
N "Hey, Mercie!"
show mercie happy with dissolve
Mercie "Hey, [name]! Come here, I saved you a seat!"
"As I made my way over, I noticed she had notes out on her lap. Is she studying?"
menu:
    "Observe her work.":
        $ Mercie_LP += 1.0
        play sound "audio/good choice.mp3"
        "I point to her lap."
        N "Is this for a class?"
        show mercie neutral
        Mercie "Oh! This? It's for my breadth requirement."
        show mercie concern
        Mercie "But I...I kind of like the class though."
        show mercie neutral
        "Wow. She looks super passionate about this type of stuff. Maybe I should ask her-"
    "Ask her what she's studying for.":
        $ Mercie_LP += 0.5
        N "Are you studying for something?"
        show mercie concern
        Mercie "H-Huh? Oh, um- Yeah."
        show mercie annoyed
        Mercie "I sit all the way in the back. And this really tall guy sits in front of me... "
        Mercie "I-I tend to fall behind..."
        show mercie neutral
        N "I can try to help you if you want. What class is this for?"
        show mercie concern
        Mercie "R-Really? You don't have to."

show mercie concern
Mercie "Wait- I just remembered."
Mercie "I-I have a meeting in five minutes!"
Mercie "{i}Ugh, why am I always so forgetful!{/i}"
N "O-Oh, okay! Good luck!"
show mercie neutral
stop music fadeout 5.0
Mercie "Thanks! See ya!"
N "See you later too..."
hide mercie neutral with dissolve
"Well, that was abrupt."
if AP == 0:
    jump dayendings
else:
    jump menu_areas

#######################################################
#MERCIE ENCOUNTER THREE
label e_Mercie_3:
if Mercie_LP == 2:
    jump e_Mercie_3_alt
else: 
    jump e_Mercie_3_start


label e_Mercie_3_alt:
$ mercie_encounter = True
stop music fadeout 3.0
"I feel someone poke my arm."
show mercie neutral with dissolve
Mercie "Hey, are you busy? If not, do you want to chat for a bit?"
menu:
    "Chat with Mercie?"
    "Yes":
        $ c_Mercie += 1.0
        N "Yeah, I've got time to spare."
        hide mercie neutral with dissolve
        "We ended up walking around the Quad aimlessly and complained about our classes..."
        scene qquad with Fade (2.0,0,2.0)
        "It sounds like she's really into plants and wildlife. It's the total opposite of what I expected...but also somehow not surprising."
        "Eventually, we got tired and decided to sit down."
        jump e_Mercie_3_A
    "No":
        $ Mercie_LP -= 1.0
        play sound "audio/bad choice.mp3"
        N "Sorry, not now."
        Mercie "Oh, um, okay. I'll see you around then."
        "She seems disappointed."
        hide mercie neutral with dissolve
        if AP == 0:
            jump dayendings
        else:
            jump menu_areas

label e_Mercie_3_start:
$ mercie_encounter = True
stop music fadeout 3.0
"She's leaning against a wall, toeing the ground aimlessly."
"She looks like she's expecting someone."
menu:
    "Approach Mercie?"
    "Yes":
        $ c_Mercie += 1.0
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
        scene qquad with Fade (2.0,0,2.0)
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
        play sound "audio/good choice.mp3"
        show mercie neutral
        N "You don't mind sitting on the grass, right?"
        Mercie "Not at all! I love the smell of fresh-cut grass!"
    "At a table.":
        $ Mercie_LP += 1.0
        play sound "audio/good choice.mp3"
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
        play sound "audio/good choice.mp3"
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
        play sound "audio/good choice.mp3"
        N "Plus, you have a lot of cool friends to hang out with!"
        show mercie neutral
        Mercie "I guess you're right. I just wished I didn't live so far away from everything."

menu:
    "Well, if it's any consolation, I would definitely talk to you if you ever get bored.":
        show mercie neutral blush
        Mercie "..."
        show mercie happy
        Mercie "Thanks. I appreciate it."

show mercie neutral
play sound "audio/Phone Ring.mp3"
"My phone rings."
"Oh, this phone call looks important."
N "O-Oh, sorry, Mercie. I really have to take this."
Mercie "Don't worry about it. I'm just about to run home anyway."
N "Ah, I see. I'll see you around then!"
Mercie "Bye!"
N "See you later!"
hide mercie neutral with dissolve
if AP == 0:
    jump dayendings
else:
    jump menu_areas

#######################################################
#MERCIE ENCOUNTER FOUR
label e_Mercie_4:
$ mercie_encounter = True
stop music fadeout 3.0
"Mercie waves at you excitedly, motioning for you to sit with her."
menu:
    "Sit with her?"
    "Yes":
        $ c_Mercie += 1.0
        jump e_Mercie4
    "No":
        $ Mercie_LP -= 3.0
        play sound "audio/bad choice.mp3"
        "I can't today, Mercie. I'll make it up to you, I promise."
        "Her face falls and I can tell she's really upset."
        Mercie "I-It's okay! I'll see you around!"
        "She scurries away, looking down."
        jump menu_areas

label e_Mercie4:
N "Hey, Mercie! How are you?"
show mercie happy with dissolve
Mercie "Haha, I'm doing gre- "
define sshake = { "master" : Shake((0, 0, 0, 0), 3.0, dist=15)}
show mercie concern with sshake
"Some guys sit down on her end laughs and jostles her backpack."
"Wow. They're acting like she doesn't even exist."
"She looks uncomfortable. Is she too afraid to say anything?"
menu:
    "Sit next to her.":
        $ Mercie_LP += 1.0
        play sound "audio/good choice.mp3"
        "I plop myself in the space between Mercie and the other guys."
        "I lean on the guy next to me and obnoxiously pool my belongings onto him."
        unknown "Ugh!"
        "Eventually, he and his friends pick up their things and leave in a huff."
        N "What a load of jerks."
    "Move somewhere else.":
        $ Mercie_LP += 0.5
        N "It's a little stuffy here. Wanna find a different table?"
        Mercie "Y-Yes, please."
        "We grab her things and find a nice patch of grass to sit on."
        N "We should be fine over here."
Mercie "I-I'm sorry it had to come to that. Thanks for helping."
menu: 
    "Don't feel sorry.":
        $ Mercie_LP += 1.0
        play osund "audio/good choice.mp3"
        N "That guy was overstepping your boundaries. Someone's got to teach him a lesson eventually."
        Mercie "I guess so. Either way, I'm grateful."
        N "Don't worry about it. What are friends for?"
    "It's okay.":
        $ Mercie_LP += 0.5
        N "That guy was overstepping your boundaries. I thought getting you out of there would be better than making you uncomfortable."
        show mercie happy
        Mercie "You're right. Maybe I should start kicking people in the-"
        show mercie neutral
        N "I-I wouldn't go that far."
show mercie annoyed
Mercie "I don't know. I feel like I should have like... done something too. "
Mercie "I mean- People tend to do this all the time."
show mercie concern
"All the time?"
menu:
    "I don't see why.":
        $ Mercie_LP += 1.0
        play sound "audio/good choice.mp3"
        show mercie neutral
        "I can spot you a mile away. They'd have to be blind to not see you. "
        show mercie neutral blush
        Mercie "..."
        N "I mean, it's true."
    "Then, assert yourself!":
        $ Mercie_LP += 0.5
        show mercie laugh
        Mercie "What if they decide to rough me up? What then?"
        show mercie neutral
        N "Your friends will back you up. Including me!"
        Mercie "..."
show mercie happy blush
Mercie "T-thanks. I really appreciate it."
hide mercie happy blush with dissolve
scene qquad with Fade(1.0,0,2.0)
stop music fadeout 10.0
"Ah, it's gotten pretty late. We had an intense conversation about acceptable forms of pizza consumption, and I lost track of time."
show mercie neutral with dissolve
Mercie "The next shuttle is leaving in fifteen minutes. I better get going."
N "No problem! I'll walk you there."
"We walked over to the shuttle stop."
Mercie "W-well...I'll catch you later?"
N "Yeah! Definitely."
hide mercie neutral with dissolve
"She waves goodbye as she boards the shuttle."
if AP == 0:
    jump dayendings
else:
    jump menu_areas
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#BELLA ENCOUNTERS
#BELLA ENCOUNTER ONE
label e_Bella_1:
$ bella_encounter = True
stop music fadeout 3.0
"She has a series of notebooks on the table and her lap. She fans herself while she reads."
menu:
    "Approach Bella?"
    "Yes":
        $ c_Bella += 1.0
        jump e_Bella_A
    "No":
        "Hm, I think I should leave her alone now. She could be busy."

label e_Bella_A:
$ Bella_LP += 1.0
N "Hey! Bella, right?"
show bella neutral with dissolve
Bella "Oh, hey. I remember you. [name], right?"
N "Yeah! That’s me, haha."
Bella "You still getting out of breath when you run?"
"Oof, she remembered that too. How should I respond...?"
menu:
    "Lie to her":
        $ Bella_LP += 0.5
        N "Actually, I’ve been running since last we met."
        show bella smile
        Bella "Oh really?"
        N "..."
        N "Okay, maybe I’m lying."
        show bella neutral
        Bella "Don’t feel bad about it. You’re not the first guy to try to impress me through athleticism."
        N "Sorry. You’re really cool. I didn’t want you to think I was like...some kind of dweeb."
        show bella laugh
        Bella "Haha, too late for that!"
    "Tell the truth":
        $ Bella_LP += 1.0
        play sound "audio/good choice.mp3"
        N "I’ve been walking around campus a lot, but I don’t exercise as much as I should."
        N "I’ll likely get used to it though. Eventually."
        show bella laugh
        Bella "Haha, that’s the spirit!"
        show bella neutral
        Bella "Oh, I’m so sorry. Did you want to sit next to me? I have plenty of room."
        N "O-Oh, thank you!"
        Bella "No problem."
        Bella "Just don’t trip over yourself trying to sit down."
scene qquad with Fade(2.0,0,2.0)
show bella neutral
stop music fadeout 3.0
Bella "I’ve gotta go now. It takes a bit to return to my place, and I’d rather go now than later."
N "Okay, see you later then?"
Bella "Yeah, see you!"
hide bella neutral with dissolve
if AP == 0:
    jump dayendings
else:
    jump menu_areas

#########################################################################
#########################################################################
#BELLA ENCOUNTERS
#BELLA ENCOUNTER TWO
label e_Bella_2:
$ bella_encounter = True
stop music fadeout 3.0
"Bella’s sitting on a bench trying to fit a whole bagel into her mouth."
menu:
    "Approach Bella?"
    "Yes":
        $ c_Bella += 1.0
        jump e_Bella_2A
    "No":
        "Hm, I should leave her alone for now. She seems busy."
        jump menu_areas

label e_Bella_2A:
N "Hey, Bella. What’re you up to?"
Bella "{i}Whan shum?{/i}"
"Huh? What was that? I can’t hear her over the bagel."
N "D-Did I catch you at a bad time?"
"She hurriedly gulps the bagel."
show bella neutral with dissolve
Bella "Urk- Not at all! Want some?"
menu:
    "Sure!":
        $ Bella_LP += 1.0
        play sound "audio/good choice.mp3"
        jump e_Bella_2A1
    "Uh, I think I'm good.":
        $ Bella_LP += 0.5
        jump e_Bella_2A2

label e_Bella_2A1:
"She breaks off a piece and hands it to me. I chomp into the bagel piece and sit down next to her."
N "{i}Thish ish preddy goo.{/i}"
show bella laugh
Bella "Pft- Dude. You spilled some over your, err...Let me help."
show bella neutral
N "!!!"
"Bella leans over with a napkin. It’s inches from my face..."
menu:
    "Let her.":
        $ Bella_LP += 1.0
        play sound "audio/good choice.mp3"
        "I couldn’t look her in the eyes. The napkin glides over my face."
        N "O-Oh, uhhh...Thanks."
        Bella "You’re welcome!"
        show bella neutral blush
        Bella "You had crumbs on your face."
        N "O-Oh, thank you..."
        hide bella neutral blush with dissolve
        jump e_Bella_2end
    "Take the napkin.":
        $ Bella_LP += 0.5
        N "T-Thanks, Bella."
        "She stares unblinkingly, then smiles."
        show bella neutral blush
        Bella "Oops, sorry. Personal space. Forgot about that."
        N "N-No, you did nothing wrong."
        hide bella neutral blush with dissolve
        jump e_Bella_2end

label e_Bella_2A2:
show bella neutral
Bella "Suit yourself!"
"I sat down next to her as she finished the rest of her bagel."
N "Did you just get out of class?"
Bella "Yup. I forgot to pack myself lunch, so I went straight to the JJ Store."
show bella concern
Bella "I’m {i}starving{/i}."
menu:
    "Offer to give her something.":
        $ Bella_LP += 1.0
        play sound "audio/good choice.mp3"
        N "I have a protein bar in my bag, if you'd like."
        show bella smile
        Bella "No, it’s okay! Save it for yourself."
        N "It’s fine, really."
        "Bella laughs and she waves her hand in dismissal."
        show bella laugh
        Bella "I’m not going to DIE, dude. That’s something I would expect from you, running out of breath so easily."
        jump e_Bella_2end
    "Offer to buy her something.":
        $ Bella_LP += 1.0
        play sound "audio/good choice.mp3"
        N "Why don’t we stop by a vending machine? It’s on me."
        Bella "Aw, I’d really appreciate that. But why?"
        N "As a thank you. You know, for when we met. I technically owe you."
        show bella smile
        Bella "You’re too sweet."
        Bella "Are you single?"
        N "Um..."
        show bella laugh
        Bella "Haha, I’m just joking around. Let’s go!"
        hide bella laugh with dissolve
        jump e_Bella_2end

label e_Bella_2end:
scene qquad with Pause(2.0)
"After eating, we walked around the quad together for a bit. She eventually had to leave though."
stop music fadeout 3.0
show bella neutral with dissolve
Bella "See you sometime?"
N "Yeah, see you!"
hide bella neutral with dissolve
if AP == 0:
    jump dayendings
else:
    jump menu_areas
#########################################################################
#########################################################################
#BELLA ENCOUNTERS
#BELLA ENCOUNTER THREE
label e_Bella_3:
$ bella_encounter = True
stop music fadeout 3.0
"Bella is sitting alone, but staring intently at her laptop."
menu:
    "Approach her?"
    "Yes":
        $ c_Bella += 1.0
        jump bella3
    "No":
        "She’s probably doing an online class or something. I should leave her alone." 
        jump menu_areas
label bella3:
N "Skipping out on lunch today?"
show bella neutral with dissolve
Bella "Haha, hey. I didn’t have class, so I ate a little earlier. Why? You hungry?"
N "Err, no. Not particularly."
"Bella stares at me a little too intensely."
"She pulls out a sandwich from her purse. My stomach grumbles."
show bella smile
Bella "You should have a snack. At least."
menu:
    "Decline her sammich.":
        $ Bella_LP -= 0.5
        N "I think I can hold out until dinner."
        Bella "Hm, Suit yourself! I have a purse full, but I guess I'll just share them with my friends tonight."
        N "You have something planned?"
        Bella "Yeah. I bought this new multiplayer game and we wanted to mess around with it."
        N "You play?"
        Bella "Haha, only with friends! But that’s besides the point. I have something {i}very{/i} important to ask you..."
        "My stomach knots up. She says it so seriously..."
        Bella "Do you have Uno on Xbox?"
        "..."
        "Huh?"
        jump bellaUNO
    "Eat it.":
        $ Bella_LP += 1.0
        play sound "audio/good choice.mp3"
        N "I guess a little piece wouldn’t hurt."
        Bella "Hell yeah! Here, I’ll give you the best part."
        "She hands me a square. I reach down to take it, but-"
        show bella laugh
        Bella "Say ‘ah’!"
        "She’s holding the sandwich and slowly looming it over my mouth."
        jump bellasammich

label bellaUNO:
menu:
    "Of course.":
        $ Bella_LP += 1.0
        play sound "audio/good choice.mp3"
        N "Of course I have Uno on Xbox. It came free with the console."
        show bella laugh
        Bella "Yeah!"
        show bella smile
        Bella "You should play with us some time. The more, the merrier."
        show bella neutral
        N "I’m actually pretty bad at playing any form of card games. I always get dealt a bad hand."
        Bella "Damn- Must be hard to have the odds stacked against you."
        show bella laugh
        Bella "Is there {i}anything{/i} you’re good at?"
        "Now that I think about it, I don’t think I really have any character-defining hobbies..."
        N "Uhhh, I make...really good friends?"
        show bella laugh
        "Bella laughs."
        show bella smile
        Bella "Hmm, yeah. I guess that’s true."
        jump e_Bella_3end
    "No, I don't.":
        $ Bella_LP -= 0.5
        N "Sorry, I don't have Uno."
        show bella annoyed
        Bella "Um, yeah, you do. Every Xbox came with Uno for free."
        N "My Xbox didn't come with Uno."
        Bella "You have Uno. When you get home, check it out."
        N "Errr, I don’t know, I can’t really-"
        Bella "You have Uno."
        N "I don’t have-"
        define sshake = { "master" : Shake((0, 0, 0, 0), 3.0, dist=15)}
        show bella annoyed with sshake
        Bella "YOU HAVE UNO."
        show bella annoyed
        #(hella funny if she just zoomed in really dramatically lol)
        N "O-Okay. I guess I have Uno! Y-You can back up now."
        show bella smile
        Bella "Cool. Now we can play it some time!"
        N "S-Sure."
        "Well, this is a new side of Bella I didn’t expect."
        jump e_Bella_3end

label bellasammich:
menu:
    "Open up.":
        $ Bella_LP += 1.0
        play sound "audio/good choice.mp3"
        show bella smile
        "My cheeks blaze up into flames and I open up."
        "..."
        "The sandwich is REALLY good, though."
        Bella "It rocks, right? My last class had a party and I have like… a buttload in my bag."
        "She unfastens her duffel bag and reveals a stack of sandwiches."
        N "Can...Can I take some?"
        show bella neutral
        Bella "No, man! Find your own stash!"
        N "Aw, man. Not even just one?"
        show bella laugh
        Bella "Okay, okay! Here."
        "She laughs and playfully throws me one."
        hide bella laugh with dissolve
        jump e_Bella_3end

    "Close those chompers.":
        $ Bella_LP += 0.5
        "I close my mouth. I don’t want her to think I’m a little kid."
        N "T-Thank you, but I can eat by myself."
        show bella concern
        Bella "Huh?"
        show bella concern blush
        Bella "O-Oh, right." 
        show bella neutral
        Bella "S-Sorry. I keep forgetting. I have a habit of overstepping people’s personal space."
        N "It’s okay! My mom has done worse things."
        Bella "So, I’m one step away from being your mom?"
        N "T-That’s not what I meant!"
        "Bella laughs and hits my shoulder."
        hide bella neutral with dissolve
        jump e_Bella_3end

label e_Bella_3end:
"We spent the rest of our time talking about upcoming game releases. She’s got good taste!"
show bella neutral with dissolve
stop music fadeout 3.0
Bella "Well, I better get going. I have class soon."
N "Alright, see you!"
Bella "Yeah, see you!"
hide bella neutral with dissolve
if AP == 0:
    jump dayendings
else:
    jump menu_areas
#########################################################################
#########################################################################
#BELLA ENCOUNTERS
#BELLA ENCOUNTER FOUR
label e_Bella_4:
$ bella_encounter = True
stop music fadeout 3.0
"She’s zipping up her bag when she notices me."
Bella "Hey, [name]!"
"She waves me over. Is she inviting me to walk with her?"
menu:
    "Go to her?"
    "Yes.":
        $ c_Bella += 1.0
        jump e_Bella_4A
    "No.":
        $ Bella_LP -= 4.0
        N "Uh, I really can’t. Sorry."
        Bella "Okay. Have fun then!"
        "She scurried off before I could say anything else."
        jump menu_areas

label e_Bella_4A:
$ Bella_LP += 0.5
"I jog over. As I’m approach...is that chlorine?"
"Before I can think too much of it, Bella taps my shoulder playfully."
show bella neutral
Bella "Fancy seeing you here, [name]. Heading to class?"
N "No. I’m actually free 'til like...3?"
Bella "Oh cool. Mind if we sit down for a bit? I wanted to go through my notes."
N "Yeah, I don't mind."
"We walk further into the quad and find an empty table."
menu:
    "Where should I sit?"
    "Across from her.":
        $ Bella_LP += 1.0
        play sound "audio/good choice.mp3"
        jump e_Bella4A1
    "Next to her.":
        $ Bella_LP += 0.5
        jump e_Bella4A2

label e_Bella4A1:
show bella neutral
"I sit across from her, avoiding her notes. She’s pulling a lot of markers and pens from her bag."
N "You have a test or something coming up?"
show bella smile
Bella "Nah. I like to doll up what I’ve written down, you know? It’s easier to remember."
show bella neutral
"Now that I’m looking at her papers, little flowers are doodled in the corners."
menu:
    "I lean over and draw a..."
    "Cowboy":
        $ Bella_LP += 0.5
        "I draw a cute little mustache and a wide hat, but she isn’t looking up from her notes. "
        show bella neutral
        show bella laugh with dissolve
        Bella "Aw! That’s cute!"
        show bella neutral
        "She reaches over and doodles a bandana over his eyes."
        hide bella neutral with dissolve
        #"Hm, he has an air of mystery now. I wonder what his backstory would be if we fleshed it out..."
        jump e_Bella4end
    "Racoon":
        $ Bella_LP += 1.0
        play sound "audio/good choice.mp3"
        show bella laugh
        Bella "Haha, how cute! I love raccoons!"
        show bella neutral
        "I look up from my drawing and she's staring at the doodle."
        N "Are they your favorite animal?"
        Bella "Yeah! They’re such cute little trash babies!"
        "Her face lights up with a smile as she pulls out her phone."
        Bella "I have a bunch of photos of my neighborhood raccoon. Here, I’ll show you."
        hide bella neutral with dissolve
        jump e_Bella4end

label e_Bella4A2:
$ Bella_LP += 0.5
show bella smile
Bella "Oh, let me move these for you."
show bella neutral
"She reaches over and gathers up her stuff. Pens, highlighters, post-it notes, markers, etc."
N "That’s a lot of uhh, pens you got there."
show bella smile
Bella "Nice deduction there, Sherlock. I just like making my notes pretty, you know?"
N "Can I look?"
show bella laugh
Bella "Sure, go for it!"
show bella neutral
"I glance down at her notes and-"
"Whoa. There’s that chlorine smell again."
menu:
    "Maybe I should ask about her..."
    "Wet hair.":
        $ Bella_LP += 1.0
        play sound "audio/good choice.mp3"
        show bella concern
        N "Did you go to the gym this morning?"
        Bella "Huh? Why?"
        N "Well, your hair is still wet. And you look a bit flushed."
        show bella smile
        Bella "Oh! I was just at the pool. I wanted to swim for a bit. "
        "There’s a pool here?"
        show bella neutral
        Bella "Do you know how to swim?"
        N "Errr, I can, but nothing amazing.”"
        show bella smile
        Bella "Maybe I can take you there some time. Show you around some more?”"
        N "Yeah, I wouldn't mind that."
        hide bella smile with dissolve
    "Smell":
        $ Bella_LP -= 1.0
        play sound "audio/bad choice.mp3"
        N "Did you buy a new perfume?"
        show bella concern
        Bella "A new what?"
        N "O-Oh, it’s just- Before, you had vanilla and now you smell...pool-y."
        show bella annoyed blush
        Bella "You’ve...smelled me before?"
        "Oh. That doesn’t sound right out loud. "
        N "I-I mean, I don’t smell you intentionally. It just wafts around!"
        show bella annoyed
        Bella "Yeah, right..."
        hide bella annoyed with dissolve
        #"Damn- I’m never going to live this down, huh."

label e_Bella4end:
"We spend the rest of the evening talking about upcoming classes."
"Before heading home, Bella asked if I knew what the flying spaghetti mosnter was."
"I had {i}no{i/} idea how to respond."
if AP == 0:
    jump dayendings
else:
    jump menu_areas
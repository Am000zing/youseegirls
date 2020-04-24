label coffeeshop_encounters:
scene coffeeshop with Fade(1.0,0,1.0)
#BERKLY ENCOUNTERS
#BERKLY ENCOUNTER ONE
label e_Berkly_1:
$ berkly_encounter = True
#Berkly is sitting with a cup of coffee beside her laptop.
"She’s sitting at one of the tables with a couple other students who, like her, are all staring intensely at their screen typing away."
menu:
    "Approach Berkly?"
    "Yes":
        $ Berkly_LP += 0.5
        N "Hey, Berkly! How’s your studying going?"
        Berkly "Oh! Hey, [name]. It’s going well. Would you like some studying tips?"
        jump e_Berkly_1_A
    "No":
        "Berkly seems busy. I better not interrupt her studying."
        jump coffeeshop_people

label e_Berkly_1_A:
menu:
    "Sure":
        $ Berkly_LP += 0.5
        Berkly "One thing you could do is study in sessions instead of all at once. Doing that several days in advance is best."
        Berkly "Another thing that helps is studying in a group so you feel more motivated. You can join us if you want to. After all, being a transfer student must be difficult."
        N "Well..."
        jump e_Berkly_1_A_menu
    "No thanks, I'm good.":
        $ Berkly_LP -= 0.5
        Berkly "Well, that's a shame."
        Berkly "Anyways, I should get going."
        N "Do you have more classes?"
        Berkly "Well, not just that. I've got other errands to run."
        N "Ah, I see. Catch you later then."
        Berkly "See ya."
        #Result: 0
        jump menu_areas


label e_Berkly_1_A_menu:
menu:
    "No thanks.":
        $ Berkly_LP -= 1.0
        jump e_Berkly_1_A1
    "Really? Thanks!":
        $ Berkly_LP += 1.0
        jump e_Berkly_1_A2
    "I'll think about it.":
        $ Berkly_LP += 0.5
        jump e_Berkly_1_A3

########################

#[No thanks.]
label e_Berkly_1_A1:
Berkly "Bummer. Are you sure you don’t want to spend even a little bit of time with us?"
N "Umm…"
menu:
    "You've convinced me":
        $ Berkly_LP += 1.0
        Berkly "Hehe. I guess my skills in convincing aren’t too bad, yeah?"
        "The other people studying glance over at Berkly and nod tersely before continuing their own work."
        "Maybe this is why she wasn’t very communicative during the library. She’s exactly like the people studying at this table. Might as well utilize this time to ask for help..."
        N "Berkly, could I get some advice for my classes?"
        Berkly "Sure! What do you need help on?"
        "I stayed in the coffee shop for a while until Berkly had to head to wherever she needed to go."
        jump e_Berkly_1_A_End
        #Result: 1
    "I don't want to be a bother.":
        $ Berkly_LP -= 1.0
        N "I stopped by for a bit, but your studying seems important."
        "She seemed kind of disappointed that I didn’t sit with her. I really don’t want to bother her though."
        jump menu_areas
        #Result: -1.0

#[Really? Thanks!]
label e_Berkly_1_A2:
Berkly "We study on the weekdays here whenever we aren’t in class or in the dorms. You can stop by anytime you need some help."
N "Thanks, I really appreciate it."
Berkly "No problem. Hey, could you watch my stuff for me? I think I'm gonna order another coffee."
menu:
    "Sure!":
        $ Berkly_LP += 1.0
        Berkly "Cool, thanks!"
        "Berkly gets up and goes to order a coffee. When she comes back, she’s carrying two cups."
        Berkly "Here! For you."
        N "Oh! Thank you, you didn’t have to."
        Berkly "Of course I didn’t {i}have{/i} to. I wanted to."
        jump e_Berkly_1_A_End
        #Result: 3
    "Sorry, I was going leave to study as well.":
        $ Berkly_LP += 0.5
        Berkly "Its ok. I’ll ask one of my study buddies. If you have any questions, you can rely on me."
        N "Thanks, Berkly."
        Berkly "No problem."
        jump menu_areas
        #Result: 2.5
    "Another cup?":
        $ Berkly_LP -= 1.0
        Berkly "Well, I didn't ask for you to judge my life choices."
        Berkly "Anyways, I should get going."
        N "Do you have more classes?"
        Berkly "Well, not just that. I've got other errands to run."
        N "Ah, I see. Catch you later then."
        Berkly "See ya."
        jump menu_areas
        #Result: 2

#[I’ll think about it.]
label e_Berkly_1_A3:
Berkly "Well, if you're able to, you are welcome to join us."
N "Okay."
Berkly "Later."
menu:
    "Bye":
        jump menu_areas
        #Result: 1.5
    "On second thought...":
        $ Berkly_LP += 1.0
        N "I think I’ll join, actually. My grades weren’t the best in high school, so I should take this as an opportunity for a fresh start."
        Berkly "It's alright. I wasn’t the best in high school either."
        N "Really?"
        "I would’ve thought someone like her would be at the top of her class in high school."
        jump e_Berkly_1_A_End
        #Result:2.5

#################################
label e_Berkly_1_A_End:
show coffeeshop with Fade(1.0,0,1.0)
Berkly "I should get going."
N "Do you have more classes?"
Berkly "Well, not just that. I've got other errands to run."
Berkly "I’m glad you decided to join us."
N "I’m glad as well. I got a lot of work done."
Berkly "Catch you later then."
N "Let's meet up again"
Berkly "Yeah!"
if AP == 0:
    jump dayendings
else:
    jump menu_areas

######################################################################################################
######################################################################################################
#BERKLY ENCOUNTERS
#BERKLY ENCOUNTER TWO
label e_Berkly_2:
$ berkly_encounter = True
"Berkly's sitting alone this time. She’s typing with one hand and sipping on coffee with the other."
menu:
    "Approach Berkly?"
    "Yes":
        N "Is it just you this time?"
        Berkly "You sound like you have a problem with that."
        N "No, but none of your other friends are here."
        Berkly "I think they’re just busy with their own stuff."
        N "I see."
        "Nice to see she’s warming up to me."
        Berkly "Wanna join me for a short walk? Taking a short break from studying is always good."
        jump e_Berkly_2_A
    "No":
        jump coffeeshop_people

label e_Berkly_2_A:
menu:
    "Nah, I'm good.":
        jump e_Berkly_2_A1
    "Sure, I could use some exercise.":
        jump e_Berkly_2_A2

label e_Berkly_2_A1:
$ Berkly_LP += 0.5
Berkly "Really? I have reason to doubt your health."
N "I don’t know what you’re talking about. I’m perfectly healthy!"
Berkly "You say that after that extra sweetened coffee you just bought."
N "Haha, way to put me on the spot."
Berkly "Also I’m trying to help you. Come on, we can go for a quick walk."
menu:
    "Alright.":
        jump e_Berkly_2_A11
    "Sorry, no.":
        jump e_Berkly_2_A12

label e_Berkly_2_A11:
$ Berkly_LP += 1.0
#[Alright]
N "So we’re just going to take a walk around campus?"
Berkly "No, that’s too long. We’ll just take a short one around the perimeter of the coffeeshop."
"Oh, thank God."
Berkly "So…wanna play 20 questions?"
N "Um, sure."
"Her phone rings."
#Ring Ring Ring
Berkly "Sorry, I gotta take this call."
N "Go ahead."
Berkly "Sorry about that. Do you wanna ask the first question?"
N "You can go first."
Berkly "Okay, what are your thoughts on President X?"
"This isn’t what I had in mind when I agreed to this…"
menu:
    "I don’t really have an opinion":
        jump e_Berkly_2_A111
    "Can we do different questions?":
        jump e_Berkly_2_A112
    "Sorry, I don’t really follow politics.":
        jump e_Berkly_2_A113


##############################################################
label e_Berkly_2_A12:
$ Berkly_LP -= 1.0
#[Sorry, no.]
Berkly "I see."
Berkly "...Wanna play 20 questions?"
N "Yeah, sure. Let me finish this coffee first."
"Her phone rings."
#Ring Ring Ring
B "Sorry, I gotta take this."
N "It's fine, go ahead."
#pause
B "Sorry about that."
N "It's fine. Besides, I finished."
B "You already finished?! Didn’t you just buy it?"
N "It was pretty good."
N "Alright, let’s start."
B "Hmm...What do you think about President X?"
"This isn’t what I had in mind when I agreed to this…"
menu:
    "I don’t really have an opinion":
        jump e_Berkly_2_A111
    "Can we do different questions?":
        jump e_Berkly_2_A112
    "Sorry, I don’t really follow politics.":
        jump e_Berkly_2_A113


#####################################################################
label e_Berkly_2_A2:
$ Berkly_LP += 1.0
#[Sure, I could use some exercise]
B "Great, let’s go!"
N "Gimme a sec, just need to finish this coffee."
B "Didn't you just get it? Wouldn’t-"
N "-Done."
"I can’t tell if she’s amazed with disgust or interest."
B "Wow."
B "You just downed like a million calories in an instant."
N "That much?"
B "You wanna hit the gym and do some exercising later?"
menu:
    "Sure.":
        jump e_Berkly_2_A21
    "Sorry, I have plans later.":
        jump e_Berkly_2_A22

label e_Berkly_2_A21:
$ Berkly_LP += 1.0
#[Sure]
Berkly "Sweet. Do you have any exercises in mind?"
"Her phone rings."
#Ring Ring Ring
Berkly "Sorry, gotta take this call."
"She walks out briefly."
"Must be important."
Berkly "Sorry, there’s been a change in plans. Looks like we aren’t gonna workout together today."
N "It's fine. I think I could start using the student recreation center without a guide."
Berkly "So, do you want to ask first?"
N "You can go ahead."
Berkly "Hmm...So what do you think about President X?"
"This isn’t what I had in mind when I agreed to this…"
menu:
    "I don’t really have an opinion":
        jump e_Berkly_2_A111
    "Can we do different questions?":
        jump e_Berkly_2_A112
    "Sorry, I don’t really follow politics.":
        jump e_Berkly_2_A113

label e_Berkly_2_A22:
$ Berkly_LP += 0.5
#[Sorry, I have plans for later today.]
B "No problem."
"Her phone rings."
#Ring Ring Ring
Berkly "Sorry, gotta take this call."
"She walks out briefly."
"Must be important."
B "Sorry about that. Looks like even if we were going to workout together today, we wouldn’t have been able to."
N "It's fine. I think I could start using the student recreation center without a guide."
Berkly "So, do you want to ask first?"
N "You can go ahead."
Berkly "Hmm...So what do you think about President X?"
"This isn’t what I had in mind when I agreed to this…"
menu:
    "I don’t really have an opinion":
        jump e_Berkly_2_A111
    "Can we do different questions?":
        jump e_Berkly_2_A112
    "Sorry, I don’t really follow politics.":
        jump e_Berkly_2_A113

############################################################
label e_Berkly_2_A111:
$ Berkly_LP -= 1.0
#[I don’t really have an opinion]
Berkly "Wanna try asking me a question then?"
N "Well, I guess why ask about politics? It seems like a pretty intimidating topic to ask about with someone you barely know?"
Berkly "Huh, really? Sorry, I didn’t mean to put you on the spot like that."
Berkly "I just really enjoy discussing lots of different topics and putting my opinion out there, you know."
"She wasn't very talkative when we first met...so this is nice."
jump e_Berkly_2_end

label e_Berkly_2_A112:
$ Berkly_LP += 0.5
#[Can we do different questions?]
Berkly "Sure. What kind of coffee do you enjoy? Without all the extra sweeteners."
N "Uhh, new question?"
Berkly "So as long as it’s sweetened, you’d like any coffee?"
"Oh man, put on the spot twice in a day about my coffee habits."
N "Okay, fine. As long as it is sweetened coffee, I’ll drink it."
Berkly "Seems like we might have to do a couple extra laps."
"Ah, jeez."
Berkly "Haha, just kidding! I’m just teasing."
N "Well, now it’s my turn. I won’t hold back, you know."
Berkly "I could critique your eating habits more, you know."
N "Okay, okay, I’ll hold back."
jump e_Berkly_2_end

label e_Berkly_2_A113:
$ Berkly_LP -= 1.0
#[Sorry, I don’t really follow politics.]
Berkly "Don’t you think that we should be keeping track of politics?"
N "Well, since I’m from Japan, I don’t know if you should expect me to understand American politics as well."
Berkly "Ugh, I guess."
Berkly "Do you have any questions for me?"
N "Do you only follow American politics?"
Berkly "Mostly just here. I think it's important to be informed on a general level for most things. For politics, I think it’s important to be able to express your opinions, especially for the country you live in."
jump e_Berkly_2_end



######################################################################################################
label e_Berkly_2_end:
show coffeeshop with fade
B "Thanks for waiting while I pack up."
N "It's no biggie."
B "Later."
N "Bye."
if AP == 0:
    jump dayendings
else:
    jump menu_areas

######################################################################################################
######################################################################################################
#BERKLY ENCOUNTERS
#BERKLY ENCOUNTER THREE
label e_Berkly_3:
$ berkly_encounter = True
"Berkly is sitting alone again. She’s reading a book and relaxed. Steam rises from the cup of coffee beside her."
menu:
    "Approach Berkly?"
    "Yes":
        jump e_Berkly_3A
    "No":
        jump menu_areas
label e_Berkly_3A:
N "I’m sorry if I come off as rude, but shouldn’t your other friends be here by now?"
Berkly "Did you have the impression that they were here on a daily basis?"
N "Yea, I thought that this was going to be a study group."
Berkly "This {i}is{/i} a study group though?"
N "What?"
N "Isn’t a study group a group that meets on a daily basis and helps each other with work?"
Berkly "Well for us, this is a study group."
Berkly "We usually meet up once a week."
N "Oh, sorry."
N "Was I being a bother showing up everyday?"
Berkly "No, it's fine. I appreciate the company."
Berkly "That wouldn’t happen to be another extra sweetened coffee, would it?"
N "Uh..."
menu:
    "I can't help it.":
        $ Berkly_LP -= 1.0
        jump e_Berkly_3A1
    "Maybe...":
        $ Berkly_LP += 0.5
        jump e_Berkly_3A2
    "You want some?":
        $ Berkly_LP += 0.5
        jump e_Berkly_3A3

label e_Berkly_3A1:
B "Really? I thought I already told you about how it isn’t healthy to drink something like that so often."
N "I might have a slight appreciation for the taste of it."
B "You should say that after you buy one that isn’t extra sweetened."
"Not this again."
N "Alright, next time I’ll get one that isn’t extra sweetened."
B "Good."
B "I don’t have much to do for homework today what about you?"
menu:
    "I don’t have much to do either.":
        $ Berkly_LP += 1.0
        jump e_Berkly_3A11
    "I think I have a test to study for.":
        $ Berkly_LP += 0.5
        jump e_Berkly_3A12

###
label e_Berkly_3A2:
B "Really? I thought I already told you about how it isn’t healthy to drink something like that so often?"
N "I might have a slight appreciation for the taste of it."
B "You should say that after you buy one that isn’t extra sweetened."
"Not this again."
N "I think next time I’ll buy one that isn’t extra sweetened"
B "Good."
B "I don’t have much to do today. What about you?"
menu:
    "I don’t have much to do either.":
        $ Berkly_LP += 1.0
        jump e_Berkly_3A11
    "I think I have a test to study for.":
        $ Berkly_LP += 0.5
        jump e_Berkly_3A12


###
label e_Berkly_3A3:
B "I’m not going to be bribed. I thought I already told you about how it isn’t healthy to drink something like that so often?"
N "I might have a slight appreciation for the taste of it."
B "You should say that after you buy one that isn’t extra sweetened."
"Not this again."
N "Alright, next time I’ll get one that isn’t extra sweetened"
B "Good."
B "I don’t have much to do for homework today. What about you?"
menu:
    "I don’t have much to do either.":
        $ Berkly_LP += 1.0
        jump e_Berkly_3A11
    "I think I have a test to study for.":
        $ Berkly_LP += 0.5
        jump e_Berkly_3A12


label e_Berkly_3A11:
Berkly "Great! Is there anything that you want to do then?"
N "Well, I don’t really want to do anything too academically intensive."
Berkly "Hmmm..."
Berkly "Ah, do I have your number?"
N "No."
Berkly "Okay, let’s exchange then."
"The phone she pulls out looks like a much older model."
N "Have you ever thought about upgrading your phone?"
Berkly "No, I only use my phone for simple communication."
N "What about games or watching videos?"
B "I can do that on my laptop or some other computer."
jump e_Berkly_3A1end

label e_Berkly_3A12:
Berkly "Let me help you study then. For what class?"
N "Actually, I changed my mind. I don’t really want to do anything too academically intensive right now."
Berkly "Too tired?"
N "Yeah."
Berkly "Hmmm..."
Berkly "Ah, do I have your number?"
N "No."
Berkly "Okay, let’s exchange then."
"The phone she pulls out looks like a much older model."
N "Have you ever thought about upgrading your phone?"
Berkly "No, I only use my phone for simple communication."
N "What about games or watching videos?"
B "I can do that on my laptop or some other computer."
jump e_Berkly_3A1end

label e_Berkly_3A1end:
menu:
    "Wanna watch a movie together then?":
        $ Berkly_LP -= 1.0
        Berkly "Um, no thanks. Going to a movie theater is a bit out of the way."
        N "Sorry, I meant just right now on my phone or laptop."
        Berkly "..."
        "She seems speechless. I better change the subject."
        N "I also have a snack if you want any?"
        Berkly "No, I’m good..."
        Berkly "I’m sorry, I must have misunderstood what you meant."
        "Does that mean she wanted to watch something...?"
        N "So...you wanna watch something?"
        Berkly "Well, you were the one who asked."
        Berkly "What movie did you have in mind?"
        N "An old romcom."
        B "Oh, yeah, I’m in."
        Berkly "Hey, I’m still curious about your interest in politics, by the way. Don’t you think you should keep track of what’s going on here?"
        N "Well, I don’t really see how it’s necessary to keep track of the politics here since I’m not really from here."
        Berkly "I guess."
        scene coffeeshop with Fade(2.0,0,2.0)
        B "That was a fun movie."
        N "That scene with the stone mask always gets me."

    "Let me introduce you to this game I play on my phone!":
        $ Berkly_LP += 0.5
        Berkly "What kind of game is it?"
        N "It’s a rhythm game. You try and press the key at the right time in order to progress further in the song."
        Berkly "I see."
        N "Not interested?"
        Berkly "Not really. I thought you meant like chess or some board game that could be played on the phone."
        N "Sorry. I’m not interested in those games. Do you have a deck on you then?"
        Berkly "Yeah. Do you like Uno?"
        N "Yeah, I do."
        "Huh, she conveniently has an Uno deck on her?"
        Berkly "Hey, I’m still curious about your interest in politics, by the way. Don’t you think you should keep track of what’s going on here?"
        N "Well, I don’t really see how it’s necessary to keep track of the politics here since I’m not really from here."
        Berkly "I guess."
        scene coffeeshop with Fade(2.0,0,2.0)
        B "That was a fun!"
        N "Yeah!"

    "We never talked about music. What is your favorite?":
        $ Berkly_LP -= 1.0
        Berkly "Um, where did that come from?"
        Berkly "Hey, I’m still curious about your interest in politics, by the way. Don’t you think you should keep track of what’s going on here?"
        N "Well, uh, I don’t really see how it’s necessary to keep track of the politics here since I’m not really from here."
        Berkly "I guess."

Berkly "Are you coming by tomorrow as well?"
N "If I don’t have any other plans, then sure."
Berkly "I see. Well, catch you later?"
N "Yeah, Later!"

if AP == 0:
    jump dayendings
else:
    jump menu_areas

######################################################################################################
######################################################################################################
#BERKLY ENCOUNTERS
#BERKLY ENCOUNTER FOUR
label e_Berkly_4:
$ berkly_encounter = True
"She's sitting at the same table and same spot. She seems busy."
"Ah, man. I had nothing to do so I came here. Maybe I shouldn’t have come."
"Berkly looks up and waves to me. She gestures towards the seat that I usually sit at."
menu:
    "Approach Berkly?"
    "Yes":
        jump e_Berkly_4A
    "No":
        "I wave back, but turn around. I shouldn't bother her..."
        jump menu_areas
label e_Berkly_4A:
N "Sorry for bothering you. I didn't really have anything else to do and..."
"Where was I going with this?"
Berkly "Wanna keep me company then?"
N "Sure."
Berkly "Thanks, [name]."
N "Just think of this as a repayment for all the times you let me hang around."
Berkly "Are you perhaps thinking of leaving?"
N "Well, kinda. I was actually thinking that I would be bothering you if I stuck around too much."
Berkly "No, no! You’re not bothersome at all."
Berkly "{i}I actually really appreciate it.{/i}"
Berkly "..."
"She suddenly seems really...down?"
N "Everything alright?"
Berkly "I..."
Berkly "The study group is done. It’s just you and me."
menu:
    "What happened?":
        Berkly "The other group members I guess decided that this wasn’t really their thing. I tried convincing them, but they just left with lame excuses."
        "She looks particularly frustrated about this."
        N "You seem like you care a lot about this study group."
    "I see.":
        N "Do you want to talk about it?"
        Berkly "I guess."
        Berkly "I tried convincing them, but they just left with lame excuses."
        N "..."
        "I feel like butting in, but I think I should let her keep talking."

Berkly "This isn’t the first study group I tried to create. The first one started off great, but there was no meaningful relationship."
Berkly "It’s like everyone disappeared once it no longer became convenient."
Berkly "This time, it was basically over in just a week. I don’t know when it all went wrong."
N "Did you try asking them why they didn’t feel like going?"
Berkly "Yes, of course I tried! I asked, but they never respond!"
N "Did you ask them why they don’t go or were you trying to convince them to go?"
Berkly "Well… I did both."
jump e_Berkly_4A1

label e_Berkly_4A1:
menu:
    "Give her constructive criticism.":
        $ Berkly_LP += 1.0
        N "I’m not sure how to say this nicely, but you’re way too fixated on small things."
        Berkly "Huh?!"
        N "You mentioned politics even when I said I wasn’t interested in it earlier?"
        Berkly "Yea..."
        N "People usually don’t appreciate it when you keep on bringing up things that they don’t want to talk about."
        Berkly "Okay. But was it really that often?"
        N "You also mentioned me liking extra sweetened coffee a lot of times."
        Berkly "But that’s because-"
        N "-You care. I know. You do this because you care."
        N "It’s just that not everyone thinks the same way you do. Your overbearing kindness can be misunderstood by others."
        N "You also really love to talk, but let the people you’re with talk as well."
        Berkly "..."
    "Give her shallow advice.":
        $ Berkly_LP -= 1.0
        N "I’m not sure what you did wrong. I thought that all the actions you did were pretty reasonable for others."
        Berkly "You...nevermind."

Berkly "The study group is officially disbanded. I don’t want to be a leader of something when I can’t even be a good one."
Berkly "Thanks for listening to me, [name]."
N "Of course."
Berkly "I'm gonna get going. See you later, maybe."
N "Yeah, see you."
if AP == 0:
    jump dayendings
else:
    jump menu_areas

############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
#CHRISTINE ENCOUNTERS
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
#DANY ENCOUNTERS
#DANY ENCOUNTER ONE
label e_Dany_1:
$ dany_encounter = True
"Dany is sitting in the coffee shop."
"She’s sitting next to the window, seemingly staring off into space."
menu:
    "Approach Dany?"
    "Yes":
        jump e_Dany1
    "No":
        "I should probably leave her alone."
        jump menu_areas

label e_Dany1:
$ Dany_LP +=1.0
#When I walk up to her, Dany doesn’t seem to hear me coming.
N "Uh...Hello?"
show dany concerned
Dany "O-Oh! Hey, there, [name]!"
"Oh, it seems like she didn’t hear me."
N "Hey, Dany! I just wanted to chat."
show dany neutral
Dany "Sounds good to me. How’re you adjustin’?"
N "I think I’m doing alright. Mind if I sit with you?"
Dany "By all means!"
"Huh...The table’s kind of empty."
N "Working on anything important?"
Dany "Nah. I got a little burnt out, so I’m just daydreamin’."
menu:
    "Do you have a lot of work?":
        $ Dany_LP +=0.5
        jump e_Dany1a
    "What were you daydreaming about?":
        $ Dany_LP += 1.0
        jump e_Dany1b

label e_Dany1a:
Dany "Not a whole lot! I just...don’t even wanna think about it, y’know?"
N "Yeah, I get that."
Dany "..."
N "..."
Dany "Do you have any stuff to do?"
menu:
    "Yeah":
        N "I’ve gotta figure out where everything is. There’s just... {i}so much.{i/}"
        Dany "No kiddin’."
        Dany "I think you’ll get the hang of it pretty quick, though!"
        N "Haha, thanks."
        "*ring ring*"
        #ring ring
        Dany "Oh, shoot! It’s already this late?"
        Dany "I forgot I was supposed to meet up with someone... but how ‘bout this? Come see me again, and I’ll tell ya all about it!"
        N "Sounds like a dat- I mean plan!"
        "Did I almost call it a...nevermind."
        jump e_Danyend
    "No":
        N "I got everything figured out ahead of time, so I’m good for now."
        Dany "Well, lookit you. Might wanna relax now before the burnout gets to ya!"
        N "B-burnout...?"
        Dany "Jeez, don’t be so serious! I’m just joshin’ ya."
        N "R-right..."
        "*ring ring*"
        #ring ring
        Dany "Oh, shoot! I forgot I was supposed to meet up with my friend today!"
        Dany "Okay, let’s hang out again soon. Next time I see you, I’ll tell you all about it!"
        jump e_Danyend

label e_Dany1b:
Dany "Ah, nothin’ too special. I wouldn’t wanna bore you with all that fluff."
Dany "Besides, you’ve probably got your own stuff to think on!"
N "What, you think I can’t think about different things?"
Dany "No, nothin’ like that! It’s just...It’s silly."
menu:
    "Aw, come on! Just a bit?":
        N "I promise I won’t tell anyone."
        Dany "Aw, you’ve just got such an honest face... Alright, fine!"
        "Her face is red right now! What could it be...?"
        Dany "I was daydreamin’ about..."
        #-ring ring-!
        Dany "Oh, shoot! It’s already this late?"
        Dany "I forgot I was supposed to meet up with someone... but how ‘bout this? Come see me again, and I’ll tell ya all about it!"
        N "Sounds like a dat- I mean plan!"
        "Did I almost call it a...nevermind."
        jump e_Danyend
    "It can’t be that bad.":
        Dany "I mean, it ain’t bad, but..."
        Dany "Tell ya what. If you promise not to tell anybody, I’ll tell you. Deal?"
        N "Deal!"
        Dany "Alright! So, ever since I-"
        #-ring ring-!
        Dany "Oh, shoot! I forgot I was supposed to meet up with my friend today!"
        Dany "Okay, let’s hang out again soon. Next time I see you, I’ll tell you all about it!"
        jump e_Danyend

label e_Danyend:
if AP == 0:
    jump dayendings
else:
    jump menu_areas

######################################################################################################
######################################################################################################
#DANY ENCOUNTERS
#DANY ENCOUNTER TWO
label e_Dany_2:
$ dany_encounter = True
"Dany is sitting in the cafe, daydreaming again. She seems pretty into it."
menu:
    "Approach Dany?"
    "Yes":
        jump e_Dany2
    "No":
        "I should probably leave her alone."
        jump menu_areas

label e_Dany2:
N "Hey, Dany."
Dany "Hey, there!"
"That’s a complete 180 from last time."
Dany "How’s it goin’, partner?"
N "It’s going well, thanks. You?"
Dany "Can’t complain a lick, myself."
Dany "Wanna sit down?"
menu:
    "Sure!":
        $ Dany_LP += 1.0
        jump e_Dany2a
    "I'm good.":
        $ Dany_LP += 0.5
        jump e_Dany2b

label e_Dany2a:
"I take a seat next to her. The more I look, the more I notice she seems a bit down."
"Dany turns her eyes to the window. They kind of get stuck there, as if she’s daydreaming again."
N "Daydreaming again?"
Dany "Yeah, just a little bit."
"I then remember that we were supposed to follow up on that from the last time we talked."
menu:
    "What were you daydreaming about?":
        $ Dany_LP += 0.5
        jump e_Dany2aa
    "Talk about something else.":
        $ Dany_LP += 0.5
        jump e_Dany2ab

label e_Dany2aa:
Dany "Right! We were supposed to talk about my daydream."
Dany "Okay, so... I’m just daydreamin’ about feedin’ the animals back on the farm."
N "You grew up on a farm?"
Dany "Sure did! Chickens, cows, pigs... I know each one of ‘em by name."
Dany "The oldest cow, Cat, was like a best friend to me before college. A couple of months ago, though..."
"...Oh."
menu:
    "I'm really sorry to hear that.":
        $ Dany_LP += 1.0
        Dany "I appreciate it."
        Dany "Still kind of gets to me sometimes, y’know?"
        N "Yeah..."
        "Dany’s wiping her eyes."
        Dany "Enough of that."
        Dany "Sorry you had to see that! Honestly, I’m still kind of a softie."
    "You can get another cow, right?":
        $ Dany_LP -= 1.0
        show dany annoyed
        Dany "..."
        Dany "Pardon?"
        "Uh...whoops."
        Dany "Look, I know you’re still gettin’ used to things around here, but that’s definitely uncool."
        N "I’m sorry. Where I’m from, it’s just uncommon to have cows as pets."
        N "Though, we treat them with great respect."
        Dany "I’d sure hope so."
        Dany "Sorry, I think I just need some time to myself."
        N "No worries. I’ll catch you later."
        Dany "See ya!"

label e_Dany2ab:
$ Dany_LP += 0.5
"Whatever’s bothering Dany, I don’t want her to dwell on it if she doesn’t have to."
N "How’re classes?"
Dany "Well, ain’t you the charmer."
N "Huh?"
Dany "Never mind. They’re okay. Nothin’ special."
menu:
    "You see really out of it today.":
        $ Dany_LP += 0.5
        Dany "Honestly, I am."
        N "Wanna talk about it?"
        Dany "Not really. It’s kind of a heavy subject."
        N "No problem."
        Dany "Thanks for being so understanding. I think I’ll take the day for myself, if you don’t mind."
        N "No worries. I’ll catch you later."
        Dany "See ya!"
    "Why so moody?":
        $ Dany_LP -= 1.0
        Dany "That’s really dismissive of you."
        N "Sorry. You just seem like you’re in a bad mood."
        Dany "You’re certainly not helpin’ that."
        Dany "Look. I’m going to take the rest of the day for myself. I’ll catch you another time."
        N "Alright."

label e_Dany2b:
"Dany shrugs her shoulders, then looks out the window. She seems really down today."
"Whatever’s bothering Dany, I don’t want her to dwell on it if she doesn’t have to."
N "How’re classes?"
Dany "Well, ain’t you the charmer."
N "Huh?"
Dany "Never mind. They’re okay. Nothin’ special."
menu:
    "You see really out of it today.":
        $ Dany_LP += 0.5
        Dany "Honestly, I am."
        N "Wanna talk about it?"
        Dany "Not really. It’s kind of a heavy subject."
        N "No problem."
        Dany "Thanks for being so understanding. I think I’ll take the day for myself, if you don’t mind."
        N "No worries. I’ll catch you later."
        Dany "See ya!"
    "Why so moody?":
        $ Dany_LP -= 1.0
        Dany "That’s really dismissive of you."
        N "Sorry. You just seem like you’re in a bad mood."
        Dany "You’re certainly not helpin’ that."
        Dany "Look. I’m going to take the rest of the day for myself. I’ll catch you another time."
        N "Alright." 

label e_Dany2end:
if AP == 0:
    jump dayendings
else:
    jump menu_areas


######################################################################################################
######################################################################################################
#DANY ENCOUNTERS
#DANY ENCOUNTER THREE
label e_Dany_3:
"Huh."
"I look around for Dany, but it seems like she isn't here today..."
menu:
    "Sit at a table?"
    "Yes":
        $ dany_encounter = True
        define e_dany3end2 = False
        jump e_dany3
    "No":
        "I'll just leave. Not much of a point."
        jump menu_areas

label e_dany3:
"I decide to take a seat at a table and relax for a bit. The last time with Dany was a little weird. Maybe she’s-"
Dany "[name]! I’ve been lookin’ all over for you."
"She looks out of breath as she stands there in front of me."
Dany "{i}*huff*{i/} I just wanted to {i}*huff*{i/} apologize for the other day."
Dany "It’s just... She meant a lot to me."
Dany "She may have been “just some animal” to a lotta folks, but..."
menu:
    "It's okay.":
        $ Dany_LP += 1.0
        jump e_dany3a
    "...":
        jump e_dany3b

label e_dany3a:
Dany "Thanks, [name]. I appreciate it."
"She sits across from me and takes a moment to collect herself."
Dany "How’ve you been, though?"
N "I’ve been okay. Just getting through the day."
N "You seem really out of breath, though."
N "Do you want me to grab you something to drink?"
"Dany stares at me incredulously."
Dany "Actually, I was intendin’ for it to be on me."
N "What? Why?"
Dany "It’s part of the apology, silly!"
Dany "‘Round these parts, it’s pretty customary to give a ‘lil something extra as a thank you."
"Thank you?"
menu:
    "Thanks for what?":
        $ Dany_LP += 0.5
        Dany "For bein’ such a good friend!"
        #note should make dialogue flexible in light of other choices in future builds
        N "Ah...you don’t have to thank me for that, you know."
        Dany "Ugh, stop being so tight! Haha."
        Dany "I promise my intentions are pure and noble."
        N "That wasn’t the point-"
        Dany "C’mon. Let’s get some iced coffees."
        N "O-okay..."
        "Despite my reluctance, we had a lot of fun!"
        "We talked about the animals on her farm, my old friends from back home, and enjoyed iced coffees."
        "It was nice..."
        jump e_dany3end1
    "Oh, got it.":
        $ Dany_LP += 0.5
        Dany "There we go!"
        "I'm still a little confused"
        N "So, do you want me to pay you back, or..."
        Dany "Ask me that again, I dare you."
        Dany "Haha, just kidding!!"
        Dany "We’re gonna have a lot of fun today, so just let me take care of everything, okay?"
        "It felt a little weird letting her pay for me, but I vowed that it’s definitely gonna be on me next time."
        N "Alright, then. Lead the way!"
        "We had a lot of fun! We talked about the animals on her farm, my old friends from back home, and enjoyed some iced coffees."
        "It was...nice."
        jump e_dany3end1

label e_dany3b:
Dany "Um, [name]?"
"She seems worried about what I’ll say next."
Dany "Look, I know I wasn’t greatest the other day, but I really am sorry."
"I’m trying to process what she’s saying. How am I supposed to respond to this?"
Dany "Anything?"
"It seems like she wants me to respond."
menu:
    "Uh...sike?":
        $ Dany_LP -= 0.5
        jump e_dany3ba
    "...":
        $ Dany_LP -= 1.0
        play sound "audio/bad choice.mp3"
        jump e_dany3bb

label e_dany3ba:
$ Dany_LP -= 1.0
"She’s absolutely flabbergasted."
show dany annoy blush
Dany "DAMMIT, [name]! That’s not funny at all."
"And even though she’s saying that, I can hear her chuckling under her frustration."
Dany "Ugh, you had me worried."
Dany "Never do that again, or I’ll hogtie you and throw you into the river!"
N "Alright, alright. I promise I won’t do it again."
Dany "Hey, lemme buy you a drink. We can just hang out today and catch up."
menu:
    "You really don't have to.":
        Dany "Already getting up!"
        N "Wait!"
        Dany "Better tell me what you like before I get that caramel latte!"
        "That doesn’t sound bad, actually..."
        "We had a lot of fun! We talked about the animals on her farm, my old friends from back home, and enjoyed some iced coffees."
        "It was...nice."
    "That sounds like a lot of fun!":
        Dany "No hesitation, huh?"
        N "Well I-"
        Dany "Kidding! C’mon, I want you to try a cool flavor I discovered..."
        "We had a lot of fun! We talked about the animals on her farm, my old friends from back home, and enjoyed some iced coffees."
        "It was...nice."

label e_dany3bb:
Dany "I see."
"She looks like she’s on the verge of tears."
Dany "Alright, I guess I’ll just talk to you later, then."
"She’s getting up and leaving. I still don’t know what to say, but if I can stop her, I should."
menu:
    "Grab her arm.":
        $ Dany_LP += 1.0
        Dany "Huh...?"
        N "I’m not sure how to respond."
        N "I’m sure it’s not proper to say “it’s okay” because it feels dismissive."
        N "And I feel like I should also apologize, but...should I answer an apology with an apology...?"
        show dany mouth smile
        Dany "You goof."
        "She has a little smile on her face as she’s wiping her eyes."
        Dany "It’s always okay to say “it’s okay.” It’s short and simple."
        show dany annoy
        Dany "And doesn’t keep people anxiously waiting around!"
        N "Sorry about that."
        show dany neutral
        Dany "No, no! It’s fine."
        hide dany neutral with dissolve
        "We had a lot of fun! We talked about the animals on her farm, my old friends from back home, and enjoyed some iced coffees."
        "It was...nice."
        jump e_dany3end1
    "Let her go.":
        $ Dany_LP -= 1.0
        $ e_dany3end2 = True
        "And she’s gone. All that time I spent trying to figure out how to assure her I wasn’t angry...wasted."

label e_dany3end1:
if AP == 0:
    jump dayendings
else:
    jump menu_areas

######################################################################################################
######################################################################################################
#DANY ENCOUNTERS
#DANY ENCOUNTER FOUR
label e_Dany_4:
if e_dany3end2 == True:
   jump e_dany4bad
else:
   jump e_dany4ok

label e_dany4ok:
"Dany's sitting by the window."
Dany "Hey, [name]!"
"She waves me over. Seems like she’s looking to have me sit next to her."

label e_dany4bad:
"Dany's sitting by the window."
"She turns her head and we make eye contact. But she just turns around and stares out the window."
"I should probably go to not make things awkward..."
jump dayendings
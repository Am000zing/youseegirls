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
        Berkly "Oh! Hey, [Name]. It’s going well. Did you want any study tips?"
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
        "Berkly Sure! What do you need help on?"
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
jump menu_areas



######################################################################################################
######################################################################################################
#BERKLY ENCOUNTERS
#BERKLY ENCOUNTER ONE
######################################################################################################
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
jump menu_areas

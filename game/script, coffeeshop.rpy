label coffeeshop_encounters:
show coffeeshop with Fade(1.0,0,1.0)

#BERKLY ENCOUNTERS
#BERKLY ENCOUNTER ONE
label e_Berkly_1:
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

#########################

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
label e_Berkly_1_A3
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


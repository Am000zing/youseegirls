label Monday_Two: 
$ AP = 3
"Ugh...it's Monday."
"Sluggishly, I get up out of bed."
"I'm changing into other clothes until-"
# Knock knock knock

"Strange. I wonder who’s knocking on the door?"
Mio "Open up [name], I’ve got an important announcement for you!"
N "Alright, alright."
play sound door_open
scene dorm inside with dissolve
show mio laugh with dissolve
Mio "Thanks for letting me in. Check this out!"
"In shining letters on the screen of his phone was the title {b}UC Girls{/b}."
show mio neutral
Mio "I found this game while browsing through the app store on my phone."
show mio laugh
Mio "I think you’ll really enjoy it [name]!"
"This was his important announcement...?"
N "Um, sure. I’ll check it out soon."
show mio teasing
Mio "I think you should check it out right now!"
show mio neutral
Mio "I mean, look at this amazing Activity Point system that exists in the game!"
hide mio neutral

menu:
    "Activate NPC Mio? {fast}"
    "Yes":
        jump Mio_AP_NPC_yes
    "No":
        jump Mio_AP_NPC_no

#(Yes)
label Mio_AP_NPC_yes:
# show Mio at left with move
# show AP tutorial slide 1 at right with dissolve
NPCM "There is a system in the game called “Activity Points.” Activity Points will be referred to as AP."
NPCM "You have a set amount of AP per day, but there might be instances where you might have more or less."
NPCM "It really depends on how you, our protagonist, is feeling for the day."
NPCM "AP is only impacted when you decide to talk to someone. Going to an area will {b}not{/b} change how much AP you have."
NPCM "You are not required to use up all of your AP for the day."
NPCM "You can end the day without using up all your AP."
NPCM "Lastly, the amount of days you decide to talk to someone will help you move along in your bond with them."
NPCM "Would you like me to explain the Love Point system?"
"Would you like to know about the Love Point System?"
menu:
    "Yes":
        jump Mio_LP_NPC_yes
    "No":
        jump Mio_LP_no

#(No)
label Mio_AP_NPC_no:
# show Mio at left with move
# show AP tutorial slide 1 at right with dissolve

Mio "So in the game UC Girls, there’s a system called “Activity Points.” Activity Points is referred to as AP."
Mio "You have a set amount of AP per day, but there might be instances where you might have more or less."
Mio "It really depends on how you’re feeling for the day."
Mio "AP is only impacted when you decide to talk to someone. Going to an area will {b}not{/b} change how much AP you have."
Mio "You are not required to use up all of your AP for the day."
Mio "You can end the day without using up all your AP."
Mio "Lastly, the amount of days you decide to talk to someone will help you move along in your bond with them."
Mio "Would you like me to explain the Love Point system?"
"Would you like to know about the Love Point System?"
menu:
    "Yes":
        jump Mio_LP_yes
    "No":
        jump Mio_LP_no

#(Yes)
label Mio_LP_NPC_yes:
# show Mio at left with move
# show LP tutorial slide 1 at right with dissolve
NPCM "There is a system in this game called Love Points (LP) and Love Points will be referred to as LP."
NPCM "LP can be gained or lost with any of the UC Girls you interact with"
NPCM "Any time you make a decision that is relatively neutral with a UC Girl, you will gain a little LP and there will be no sound."
NPCM "If you make a bad decision, you will lose LP, along with a sound indicating that she didn’t like what you said."
NPCM "Lastly, if you make a good decision, you will gain LP, along with a sound indicating that she liked what you said."
NPCM "There might be instances where either decision she will actually like, so sometimes you don’t even need to stress about what you want to say!"
jump after_Mio_LP

#(Yes)
label Mio_LP_yes:
Mio "So in the game UC Girls, there is a system called Love Points (LP) and Love Points will be referred to as LP."
Mio "LP can be gained or lost with any of the UC Girls you interact with."
Mio "Any time you make a decision that is relatively neutral with a UC Girl, you will gain a little LP and there will be no sound."
Mio "If you make a bad decision, you will lose LP, along with a sound indicating that she didn’t like what you said."
Mio "Lastly, if you make a good decision, you will gain LP, along with a sound indicating that she liked what you said."
Mio "There might be instances where either decision she will actually like, so sometimes you don’t even need to stress about what you want to say!"
jump after_Mio_LP

#(No)
label Mio_LP_no:
show mio neutral
Mio "Well, if you ever want a refresher on anything, you can go into your agenda and check your notes!"
N "Cool, I'll keep it in mind."
jump after_Mio_LP

#################################

label after_Mio_LP:
Mio "Anyways, I should let you get going."
show mio laugh
Mio "Good luck this week!"
N "Ahah, thanks!"
hide mio laugh with dissolve
play sound door_close
"Alright, let's get ready and get going as soon as we can..."

show outdoor hall with Fade(1.0,0,2.0)
"I'm done with classes, but walking back seems so far..."
"Hmm...what should I do?"
$ ryver_encounter = False
$ bella_encounter = False
$ mercie_encounter = False
$ berkly_encounter = False
$ dany_encounter = False
$ christine_encounter = False
$ lola_encounter = False
$ irene_encounter = False
$ diana_encounter = False
jump menu_areas


label End_Monday:
"Well, I should get going."
scene dorm night with Fade(1.0,0,2.0)
"Ah, what an eventful day."
"I should get some sleep..."
jump Tuesday_Two

############################

label Tuesday_Two:
$ AP = 3
$ ryver_encounter = False
$ bella_encounter = False
$ mercie_encounter = False
$ berkly_encounter = False
$ dany_encounter = False
$ christine_encounter = False
$ lola_encounter = False
$ irene_encounter = False
$ diana_encounter = False
show dorm inside with Fade(2.0,0,2.0) 
"Wow, I actually kinda woke up before my alarm."
"I get up out of bed, and get ready for class..."

show outdoor hall with Fade(1.0,0,2.0)
"I'm done with classes, but walking back seems so far..."
"Hmm...what should I do?"
jump menu_areas

if AP == 0:
    jump End_Tuesday
else:
    "Hey, you shouldn't be seeing this. Please give us a bug report!"
#=else:
#    "Are you sure you want to end the day?"
#    menu:
#        "Yes":
#        "No":

label End_Tuesday:
"Well, I should get going."
show dorm night with Fade(1.0, 0, 1.0)
"Ah, what an eventful day."
"I should get some sleep..."
jump Wednesday_Two

############################

label Wednesday_Two:
$ AP = 3
$ ryver_encounter = False
$ bella_encounter = False
$ mercie_encounter = False
$ berkly_encounter = False
$ dany_encounter = False
$ christine_encounter = False
$ lola_encounter = False
$ irene_encounter = False
$ diana_encounter = False
show dorm inside with Fade(2.0,0,2.0) 
"Halfway through the week!"
"Well, I know it is but it doesn't really feel like it."
"Whatever, I should get ready to go to class..."

show outdoor hall with Fade(1.0,0,2.0)
"I'm done with classes, but walking back seems so far..."
"Hmm...what should I do?"
jump menu_areas

#if AP == 0:
#    jump End_Wednesday
#else:
#    "Are you sure you want to end the day?"
#    menu:
#        "Yes":
#        "No":

label End_Wednesday:
"Well, I should get going."
show dorm night with Fade(1.0,0,2.0)
"Ah, what an eventful day."
"I should get some sleep..."

############################

label Thursday_Two:
$ AP = 1
$ ryver_encounter = False
$ bella_encounter = False
$ mercie_encounter = False
$ berkly_encounter = False
$ dany_encounter = False
$ christine_encounter = False
$ lola_encounter = False
$ irene_encounter = False
$ diana_encounter = False
show dorm inside with Fade(2.0,0,2.0) 
"..."
"Ah, shoot."
"My alarm went off like 20 minutes ago but I hit the wrong button."
"Class is about to start in 10 minutes..."
"Sigh."
"I rush out of bed and rush to get ready to go to class."

show outdoor hall with Fade(1.0,0,2.0)
"Ugh, I'm so worn out..."
"I'm done with classes, but walking back seems so far."
"I think I only have enough energy to talk to one person..."
jump menu_areas
#if AP == 0:
#    jump End_Thursday
#else:
#    "Are you sure you want to end the day?"
#    menu:
#        "Yes":
#        "No":

label End_Thursday:
"Well, I should get going."
show dorm night with Fade(1.0,0,2.0)
"Ah, what an eventful day."
"I should get some sleep..."

############################

label menu_areas:
menu:
    "Go to the Quad":
        "Maybe I can just chill for a little in the Quad before I head back."
        #show quad with Fade(1.0,0,1.0)
        "Oh?"
        "There's some people I recognize..."
        "Should I talk to them?"
        jump quad_people
    "Go to the Coffeeshop":
        "Maybe I can get something at the coffeeshop before I head back."
        show coffeeshop with Fade(1.0,0,1.0)
        "Oh?"
        "There's some people I recognize..."
        "Should I talk to them?"
        jump coffeeshop_people
    "Go to the Bookstore":
        "Maybe I can check out some stuff in the bookstore before I head back."
        #show bookstore with Fade(1.0,0,1.0)
        "Oh?"
        "There's some people I recognize..."
        "Should I talk to them?"
        jump bookstore_people
    "Go back to the dorm":
        $ ED = 0
        "I'm not really feeling it right now."
        "I'll just head back."
        if ED == 0:
            $ ED += 1
            jump End_Monday
        elif ED == 1:
            $ ED += 1
            jump End_Tuesday
        elif ED == 2:
            $ ED += 1
            jump End_Wednesday
        elif ED == 3:
            $ ED += 1
            jump End_Thursday
        else:
            "Hey, you shouldn't be seeing this. Give us a Bug Report!"
            jump menu_areas

label quad_people:
menu:
    "Bella":
        #$ AP -= 1
        #if e_Bella == 0:
        #    $ e_Bella += 1
        #    jump e_Bella_1
        #elif e_Bella == 1:
        #    $ e_Bella += 1
        #    jump e_Bella_2
        #elif e_Bella == 2:
        #    $ e_Bella += 1
        #    jump e_Bella_3
        #elif e_Bella == 3
        #    $ e_Bella += 1
        #    jump e_Bella_4
        #else:
            "Hey, you shouldn't be seeing this. Give us a Bug Report!"
            jump menu_areas
    "Mercie" if mercie_encounter == False:
        $ AP -= 1
        if e_Mercie == 0:
            $ e_Mercie += 1
            jump e_Mercie_1
        elif e_Mercie == 1:
            $ e_Mercie += 1
            jump e_Mercie_2
        elif e_Mercie == 2:
            $ e_Mercie += 1
            jump e_Mercie_3
        elif e_Mercie == 3:
            $ e_Mercie += 1
            jump e_Mercie_4
        elif e_Mercie == 4:
            $ e_Mercie += 1
            jump e_Mercie_CFS
        else:
            "Hey, you shouldn't be seeing this. Give us a Bug Report!"
            jump menu_areas
    "Ryver" if ryver_encounter == False:
        $ AP -= 1
        if e_Ryver == 0:
            $ e_Ryver += 1
            jump e_Ryver_1
        elif e_Ryver == 1:
            $ e_Ryver += 1
            jump e_Ryver_2
        elif e_Ryver == 2:
            $ e_Ryver += 1
            jump e_Ryver_3
        #elif e_Ryver == 3
        #    $ e_Ryver += 1
        #    jump e_Ryver_4
        else:
            "Hey, you shouldn't be seeing this. Give us a Bug Report!"
            jump menu_areas
    "Go somewhere else.":
        jump menu_areas
        
label coffeeshop_people:
menu:
    "Berkly":
        #$ AP -= 1
        #if e_Berkly == 0:
        #    $ e_Berkly += 1
        #    jump e_Berkly_1
        #elif e_Berkly == 1:
        #    $ e_Berkly += 1
        #    jump e_Berkly_2
        #elif e_Berkly == 2:
        #    $ e_Berkly += 1
        #    jump e_Berkly_3
        #elif e_Berkly == 3
        #    $ e_Berkly += 1
        #    jump e_Berkly_4
        #else:
            "Hey, you shouldn't be seeing this. Give us a Bug Report!"
            jump menu_areas
    "Dany":
        #$ AP -= 1
        #if e_Dany == 0:
        #    $ e_Dany += 1
        #    jump e_Dany_1
        #elif e_Dany == 1:
        #    $ e_Dany += 1
        #    jump e_Dany_2
        #elif e_Dany == 2:
        #    $ e_Dany += 1
        #    jump e_Dany_3
        #elif e_Dany == 3
        #    $ e_Dany += 1
        #    jump e_Dany_4
        #else:
            "Hey, you shouldn't be seeing this. Give us a Bug Report!"
            jump menu_areas
    "Christine":
        #$ AP -= 1
        #if e_Christine == 0:
        #    $ e_Christine += 1
        #    jump e_Christine_1
        #elif e_Christine == 1:
        #    $ e_Christine += 1
        #    jump e_Christine_2
        #elif e_Christine == 2:
        #    $ e_Christine += 1
        #    jump e_Christine_3
        #elif e_Christine == 3
        #    $ e_Christine += 1
        #    jump e_Christine_4
        #else:
            "Hey, you shouldn't be seeing this. Give us a Bug Report!"
            jump menu_areas
    "Go somewhere else.":
        jump menu_areas
label bookstore_people:
menu:
    "Diana":
        #$ AP -= 1
        #if e_Diana == 0:
        #    $ e_Diana += 1
        #    jump e_Diana_1
        #elif e_Diana == 1:
        #    $ e_Diana += 1
        #    jump e_Diana_2
        #elif e_Diana == 2:
        #    $ e_Diana += 1
        #    jump e_Diana_3
        #elif e_Diana == 3
        #    $ e_Diana += 1
        #    jump e_Diana_4
        #else:
            "Hey, you shouldn't be seeing this. Give us a Bug Report!"
            jump menu_areas
    "Lola":
        #$ AP -= 1
        #if e_Lola == 0:
        #    $ e_Lola += 1
        #    jump e_Lola_1
        #elif e_Lola == 1:
        #    $ e_Lola += 1
        #    jump e_Lola_2
        #elif e_Lola == 2:
        #    $ e_Lola += 1
        #    jump e_Lola_3
        #elif e_Lola == 3
        #    $ e_Lola += 1
        #    jump e_Lola_4
        #else:
            "Hey, you shouldn't be seeing this. Give us a Bug Report!"
            jump menu_areas
    "Irene":
        #$ AP -= 1
        #if e_Irene == 0:
        #    $ e_Irene += 1
        #    jump e_Irene_1
        #elif e_Irene == 1:
        #    $ e_Irene += 1
        #    jump e_Irene_2
        #elif e_Irene == 2:
        #    $ e_Irene += 1
        #    jump e_Irene_3
        #elif e_Irene == 3
        #    $ e_Irene += 1
        #    jump e_Irene_4
        #else:
            "Hey, you shouldn't be seeing this. Give us a Bug Report!"
            jump menu_areas
    "Go somewhere else.":
        jump menu_areas
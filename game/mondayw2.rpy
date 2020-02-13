label Mondayw2: 

# Knock knock knock

"Strange. I wonder who’s knocking on the door?"
Mio "Open up [name], I’ve got an important announcement for you!"
N "Alright, alright."
# door open sound
Mio "Thanks for letting me in. Check this out!"
"In shining letters on the screen of his phone was the title UC Girls."
Mio "I found this game while browsing through the app store on my phone."
Mio "I think you’ll really enjoy it [name]!"
N "Um, sure. I’ll check it out soon."
Mio "I think you should check it out right now!"
Mio "I mean, look at this amazing Activity Point system that exists in the game!"

menu:
    "Activate NPC Mio?":
        "Yes"
            jump Mio_AP_NPC_yes
        "No"
            jump Mio_AP_NPC_no

#(Yes)
label Mio_AP_NPC_yes:
# show Mio at left with move
# show AP tutorial slide 1 at right with dissolve
Mio "There is a system in the game called “Activity Points.” Activity Points will be referred to as AP."
Mio "You have a set amount of AP per day, but there might be instances where you might have more or less."
Mio "It really depends on how you, our protagonist, is feeling for the day."
Mio "AP is only impacted when you decide to talk to someone. Going to an area will <b>not</b> change how much AP you have."
Mio "You are not required to use up all of your AP for the day."
Mio "You can end the day without using up all your AP."
Mio "Lastly, the amount of days you decide to talk to someone will help you move along in your bond with them."
Mio "Would you like me to explain the Love Point system?"
menu:
    "Would you like to know about the Love Point System?":
        "Yes"
            jump Mio_LP_NPC_yes
        "No"
            jump Mio_LP_no

#(No)
label Mio_AP_NPC_no:
# show Mio at left with move
# show AP tutorial slide 1 at right with dissolve

Mio "So in the game UC Girls, there’s a system called “Activity Points.” Activity Points is referred to as AP."
Mio "You have a set amount of AP per day, but there might be instances where you might have more or less."
Mio "It really depends on how you’re feeling for the day."
Mio "AP is only impacted when you decide to talk to someone. Going to an area will <b>not</b> change how much AP you have."
Mio "You are not required to use up all of your AP for the day."
Mio "You can end the day without using up all your AP."
Mio "Lastly, the amount of days you decide to talk to someone will help you move along in your bond with them."
Mio "Would you like me to explain the Love Point system?"
menu:
    "Would you like to know about the Love Point System?":
        "Yes"
            jump Mio_LP_yes
        "No"
            jump Mio_LP_no

#(Yes)
label Mio_LP_NPC_yes
# show Mio at left with move
# show LP tutorial slide 1 at right with dissolve
Mio "There is a system in this game called Love Points (LP) and Love Points will be referred to as LP."
Mio "LP can be gained or lost with any of the UC Girls you interact with"
Mio "Any time you make a decision that is relatively neutral with a UC Girl, you will gain 0.5 LP and there will be no sound effect."
Mio "If you make a bad decision, you will lose 1 LP, and there will be a sound indicating that she didn’t like what you said."
Mio "Lastly, if you make a good decision, you will gain 1 LP and there will be a sound indicating that she liked what you said."
Mio "There might be instances where either decision she will actually like, so sometimes you don’t even need to stress about what you want to say!"

#(Yes)
label Mio_LP_yes:
Mio "So in the game UC Girls, there is a system called Love Points (LP) and Love Points will be referred to as LP."
Mio "LP can be gained or lost with any of the UC Girls you interact with."
Mio "Any time you make a decision that is relatively neutral with a UC Girl, you will gain 0.5 LP and there will be no sound effect."
Mio "If you make a bad decision, you will lose 1 LP, and there will be a sound indicating that she didn’t like what you said."
Mio "Lastly, if you make a good decision, you will gain 1 LP and there will be a sound indicating that she liked what you said."
Mio "There might be instances where either decision she will actually like, so sometimes you don’t even need to stress about what you want to say!"


#(No)
label Mio_LP_no:
Mio "Well, if you ever want a refresher on anything, you can go into your agenda and check your notes!"
N "Cool, I'll keep it in mind."

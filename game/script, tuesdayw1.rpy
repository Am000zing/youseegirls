label Tuesday_One:

scene dorm morning with Fade(1.0, 0.0, 1.0)
"Ugh...I'm so tired. I didn't realize how much Orientation was going to drain me out."
"I wonder what the plans are for the day..."
"I thought about the girls I met yesterday.  The people on campus are rather... unique."
"..."
"Ah, I should get my head out of the clouds and concentrate on getting ready."
"I quickly brushed my teeth, showered and got dressed. I don't want to be late, so I ran out the door without any breakfast."
"Even though Mio said not to worry about being late, I didn't want to disappoint him."
"I don't want all his kindness to go unnoticed!"
play sound "audio/door open.mp3"
play sound "audio/door close.mp3"

scene parking lot with Fade(2.0,0,2.0)
with Pause(1)
"Oh, god...I think...I pushed myself...too much. I think I'm gonna throw up."
"I leaned on a nearby tree and panted like a dog."
"I probably look like an idiot, but that's the least of my worries..."

unknown "Are you okay?"
"I looked up and my eyes fluttered under the sun."
"My heart nearly shot out of my mouth as someone straight out of a romance novel appeared in front of me. Her hair swept up against the breeze and I caught the faintest smell of vanilla."
"Now {i}this{/i} is a woman I can {i}respect{/i}."
#"I didn't know where she came from, but at this point, do I care?"
show bella neutral with dissolve
play music "audio/Casual.mp3" fadein 10.0
unknown "Are you not feeling good? I have something that can help..."
"She stepped closer. She reached into her purse and rummaged through her bag."
menu:
    "Don't worry! I do this all the time!":
        "I stood up and puffed out my chest. I leaned against a tree, sniffing."
        N "Oh, this? This is nothing."
        N "I do this all the time. It's part of my morning. You know, running and stuff."
        show bella neutral with dissolve
        "She smiled and crossed her arms as she looked at me up and down."
        "I don't think she's convinced."
    "Sorry. I don't do this often...":
        N "I, uhhh-"
        N "I was just running too much is all! You don't have to do that."
        show bella smile with dissolve
        unknown "No, I insist!"
        N "No, really! I'm just not used to it."
        show bella concern
        unknown "Are you sure? You look pale..."
        N "I'll get over it, don't worry."
    "No, it's okay!":
        N "No, it's okay, really!"
        "I stepped forward and sub-consciously reached for her wrist."
        N "!!!"
        "Immediately, my face got hot as realization set in."
        show bella concern blush
        unknown "Um..."
        N "I-I'm so sorry."
        "I quickly let go of her wrist."
        "The first person who comes to help me and I grab them? What was I thinking?"
        show bella neutral
        N "Oh, oh god, I'm sorry. I don't mean to be too forward or anything."

N "I'm sorry, I'm afraid I haven't got your name?"
unknown "Ah, I'm sorry too! I can't believe I just barged in like that."
show bella laugh
Bella "I'm Bella."
N "It's good to meet you, Bella!"
show bella neutral
Bella "It seems like you don't really run much. I wouldn't mind giving you some pointers."
menu:
    "I don't really know how to pace myself yet.":
        Bella "I could help you out!"
        show bella smile
        Bella "We should run together some time! There's a beach I know we can run at!"
        N "Oh, really? That sounds cool."
        Bella "Yeah, let's run together! It's more fun with friends anyways, yeah?"
    "That'd be really nice, thanks!":
        show bella smile
        Bella "Of course! Breathing is obviously important, so knowing how to breathe well when you run is number one."
        Bella "Number Two: Don't start off running too fast. You'll get too tired. Try keeping an even pace the whole distance."
        N "Should I be taking notes?"
        show bella laugh
        Bella "Ahaha, if you want I guess!"
    "Is that a date?":
        $ Bella_LP -= 1
        show bella annoyed
        Bella "Um...No? I just wanted to give you advice, that's all."
        "Oh."
        "Oops."
        "I swallowed the butterflies of embarrassment crawling up my throat and-"

show bella neutral
Mio "Hey, [name]!"
"I turn around, and see Mio waving his arms at me."
show bella neutral
Bella "It looks like you're running just as late as I am. I should head to class too..."
"She readjusted the strap of her purse and walked toward campus with a smile."
N "O-oh, um-"
Mio "[name]!"
"She waved goodbye and disappeared into a crowd of students."
hide bella neutral with dissolve
N "Hope to see you around."
"I jogged over to Mio."
show mio neutral with dissolve
Mio "You're late."
N "Y-yeah. I figured. Thanks for waiting."
show mio teasing
Mio "If this is a habit of yours, maybe I'll swing by your place and wake you up myself."
"Blood rushed to my cheeks, but I tried to laugh it off."
N "Haha. Please don't."
stop music fadeout 10.0
hide mio teasing with dissolve

show outdoor hall with Fade(2.0,0,2.0)
"As students filed out of their evening classes, campus buzzed with small-talk."
"I'm a little tired from today's events, but I think it's something I can get used to."
show mio neutral with dissolve
Mio "Man, it's already this late. How you holding up, [name]?"
N "Uhhhh..."
"My mind went blank as a taco truck parked directly behind Mio."
"The windows swung open and carried the greasy, meaty smell of fresh burritos and chips."
"While trying to form an answer, I could feel my mouth watering."
Mio "We'll take an hour break to recuperate from the tour. Feel free to eat anything from the Dining Hall."
N "What about you?"
show mio smile
Mio "Don't worry about it. I already grabbed a snack before I left."
show mio neutral
Mio "You should head over there before rush hour."
N "Thanks!"
hide mio neutral with dissolve
show dining hall with Fade(1.0,0,1.0)
"I looked around in the Dining Hall, trying to narrow down what kind of foods I wanted..."
menu:
    "Stir-Fried Tofu and Veggies.":
        "I scooped up some good looking Tofu and Veggies."
        unknown "Hey, that looks good, whatcha getting?"
        "I jerked my head, a sudden breathy voice by my ears."
        play music "audio/Casual.mp3" fadein 10.0
        show christine neutral with dissolve
        N "O-oh just some stir fried tofu and veggies. Planning to get some rice with it too."
        unknown "That sounds really good. I'll probably get a scoop of that too."
        show christine happy
        Christine "Sorry for surprising you like that. I'm Christine, by the way."
        N "Oh, uh, I'm [name]."
        show christine neutral
        "On her plate was an entire mountain of fries."
        "Her lax and standoffish demeanor contrasted with her sharp eyes."
        "It was like she was silently judging me..."
        jump choice_ChristineIntroA
    "BBQ Pulled Pork Sliders":
        unknown "Ooh, that smells so good, what'd you get?"
        "I jerked my head, a sudden breathy voice by my ears."
        play music "audio/Casual.mp3" fadein 10.0
        show christine neutral with dissolve
        N "A-ah, I got a BBQ Pulled Pork Slider. It smelled so good, I couldn't resist."
        "She gave a long look at me and the slider on my plate."
        "She had an intense stare, despite her lax and standoffish demeanor."
        "It was like she was silently judging me..."
        show christine happy
        Christine "Sorry for surprising you like that. I'm Christine, by the way."
        N "Oh, uh, I'm [name]."
        show christine neutral
        unknown "I guess I can't judge you for desiring it, considering that the aroma is absolutely divine."
        unknown "But just so you know, the American meat industry, especially when it comes to pork, can be especially cruel."
        jump choice_ChristineIntroB

label choice_ChristineIntroA:
menu:
    "Are you going to eat all of those fries?":
        show christine annoyed
        Christine "How dare you assume I'd be able to finish all of these fries by myself! Who do you think I am?"
        jump choice_ChristineIntroA1
    "Where'd you get those fries?":
        show christine happy
        Christine "They're on the rightmost side of the dining hall. Can't miss 'em."
        jump choice_ChristineIntroFinal

label choice_ChristineIntroA1:              
menu: 
    "A self-loathing university student":
        show christine annoyed
        Christine "..."
        show christine neutral
        Christine "Well, you're not wrong."
        jump choice_ChristineIntroFinal
    "Your name is Christine, so I assume Christine.":
        show christine annoyed
        Christine "Ugh, you think you're so funny and snarky, huh."
        jump choice_ChristineIntroFinal

label choice_ChristineIntroB:
menu:
    "I wasn't aware of that.":
        N "O-oh, I see. I wasn't aware of that."
        $Christine_LP += 1
        jump choice_ChristineIntroFinal
    "How does this apply to me?":
        N "How does this apply to me now though?"
        $Christine_LP -=1
        show christine annoyed
        Christine "Ugh, by picking this item up at the buffet, you directly support the demand of dining hall pork, which in turn will cause more pigs to die."
        N "I'm not directly killing them though..."
        Christine "Whatever, I can explain this some other time."
        jump choice_ChristineIntroFinal

label choice_ChristineIntroFinal:
show christine neutral
Christine "Well, it's a pleasure to meet you."
Christine "I'm sure we'll be seeing each other around often considering how few people attend this summer session."
Christine "Well, I'm gonna go. My friends are nearly done with their food, so I should finish mine too."
N "Uhh, yeah! Hope to see you around!"
stop music fadeout 10.0
hide christine neutral with dissolve

scene dorm afternoon
with Fade(1.0,0,2.0)
"The day ended with Mio walking me back to my room."
"He answered a lot of my questions, and we realized we had a lot in common."
"I wonder if all guys are as cool and chill as Mio."
show mio neutral with dissolve
N "Ugh, my feet are sore."
Mio "Hm? Was the pace today a bit rough?"
N "Just a little."
show mio teasing
Mio "I'll keep that in mind tomorrow, then.... Unless you decide to be late for that too."
N "Um, yeah, it won't happen again."
show mio neutral
Mio "Whatever you say, dude. Just know I'll be here if you need help getting out of bed."
N "Haha. Thanks, man. Have a good night!"
show mio smile
Mio "Good night, [name]!"
hide mio smile with dissolve
scene dorm night with dissolve
with Pause(2.0)
#"I closed my door as he waved goodbye."
"As the silence settled in, I realized that like it here a lot."
"I changed into my pajamas, washed, and plopped myself into bed."
"As I slowly drifted to sleep, I wondered what might happen tomorrow..."
jump Wednesday_One
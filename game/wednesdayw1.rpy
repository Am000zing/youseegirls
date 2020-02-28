label Wednesday_One:
define Upstairs = False
define Downstairs = False

scene dorm inside
with Fade(1.0, 0.0, 1.0)
#birds chirping sound
"..."
"Ah, I woke up before my alarm..."
"I rolled out of bed and sluggishly trudged into my bathroom."
"My eyes drooped as I peered at myself in the mirror."
"My sleep schedule's been really off lately."
"Jet lag has really been killer, considering that I kept waking up at odd hours and then falling back asleep."
"I slapped on some clothes and munched on a banana that conveniently was on my desk."
"I don't even remember when I got it, but I probably grabbed it before I left the dining hall yesterday."
"The door slammed behind me as I made my way to the parking lot."
#sound of door closing
"I wonder what today would bring me..."
"Mio's been super helpful so far, not to mention, I've met so many people so far!"
"Whatever life throws at me, I feel like I can take it!"
show parking lot with Fade(1.0,1.0,2.0)
"I made it to the parking lot. Now I have plenty of time to arrive earl-"
#*SMACK*
#bumping into someone sound
$ sshake = Shake((0, 0, 0, 0), 0.5, dist=15)
show parking lot with sshake
"I toppled over, but barely caught my balance at the last second."
unknown "Ow! Shoot, I'm so sorry. Are you okay?"
N "Y-yeah, I'm fine...?"
"I looked around for whoever had bumped into me, but there was no-one in front of me."
N "Huh? I swear I was bumped into."
unknown "Ah, yeah, I'm so sorry, let me get out of your way."
"I turned around."
show mercie concern with dissolve
"She had already brushed herself off and gathered herself ready to leave."
N "W-wait!"
show mercie concern blush
"She halted, quietly staring at me with almost a worried look on her face."
N "I'm sorry, I'm new to this school, so I'm trying to get to know people."
show mercie concern
N "May I ask what your name is?"
show mercie happy
unknown "Y-you want to know my name?"
"She was aghast, almost amazed...for someone wanting to know who she is?"
N "U-uh, yeah. I'm [name]."
show mercie laugh
unknown "Oh wow, that's so cool! It's so nice to meet you!!"
Mercie "I'm Mercie!"
N "I'm [name]. It's nice to meet you too!"
show mercie neutral
"Mercie quickly brushes her hair back, and exhales in relief."
Mercie "Well, I'm off now! Hope to see you around, if you want to of course."
hide mercie neutral with dissolve
"Before I can respond, she's off in the distance."
"She seems really hesitant in social encounters..."
"I wonder if she's scared of me?"
"My train of thought is abruptly cut by the sight of Mio fast-walking towards me."
Mio "Hey, [name]! I was more on time this time, wasn't I?"
Mio "Well anyways, let's get going, shall we? There's not much left to show you around."

scene purple bubble bg
with Fade(1.0,0.0,1.0)
"I started to get hungry as noontime came about."
N "Hey, Mio, when are we going to the Dining Hall?"
Mio "Oh! I actually brought lunch for us to share. It's not as large of portions as the dining hall, but it should be better than dining hall food!"
N "Wow, you can cook?"
Mio "I do what I can."
N "Woah, thanks, I-"
"!!!"
"In his hands, he held a decorated bento you'd purchase anywhere. But..."
N "Uh, Mio..."
Mio "Yeah, what's up?"
N "Look, I appreciate all you've done for me but..."
N "Why is it in this kind of container?"
"Mio darted his eyes between the bento and me."
Mio "Oh, it was the cheapest one at the market, so I decided on it."
Mio "It's an old container, don't sweat it!"
N "U-uh, yeah."
Mio "Anyways, eat up! We still got a place to go to, and it's pretty big, so you'll need your energy."
N "Alright, got it!"

#scene library
show library_2 with Fade(1.0,0,2.0)

"Mio stopped us by the library, which was absolutely huge."
Mio "Downstairs is the research archives, while upstairs is the literature section."
Mio "Take your time to look around anywhere."
"Mio's phone dings, and he takes his phone out and stares at the screen."
Mio "I'm gonna have to leave you here for a minute."
N "Okay? What's up?"
Mio "Nah, something just came up."
Mio "You can probably ask someone to help you out in the places you're checking out."
N "Oh, uh-"
"Before I could reason with him, he's already out the door."
"Well..."
"Where should I go?"


label menu_library:
menu:
    "Downstairs to the Research Archives":
        jump Downstairs
    "Upstairs to the Literature Section":
        jump Upstairs

label Downstairs:
$ Downstairs = True
show library_1 with Fade(1.0,0,2.0)
"I head downstairs, curious about the various research the university has done."
"Wow, there's so many files and articles...how do I know what's good and what's not?"
"I notice that there's two others also perusing the archives."
menu:
    "Approach the one staring intently at the file she's going through.":
        jump choice_betweenBL_Berkly
    "Approach the one also staring at the file she's going through, but less enthusiastically than the other girl.":
        jump choice_betweenBL_Lola

label choice_betweenBL_Berkly:
N "Excuse me, I was-"
unknown "Yes, you are excused."
"Maybe I should ask someone else for help..."
unknown "Ah, sorry. I'm a little stressed so I'm a bit on edge."
"She doesn't look up from her file."
N "I’m a transfer student here, and I wanted to ask if you could introduce me around the archives."
"She's going to help me...right?"
show berkly concerned with dissolve
unknown "Oh, I see. I’ll help you, but my time is a bit limited."
N "That's be great, thanks!"
N "I'm [name], by the way."
show berkly neutral
Berkly "Berkly, good to meet you."
Berkly "Well, let's get going then."
hide berkly neutral with dissolve
#TIME SKIP
show library_1 with Fade(1.0,1.0,1.0)
show berkly neutral with dissolve
Berkly "~I mean isn’t it obvious that all organic coffee is better than non-organic?"
"I tiredly nod in agreement."
Berkly "If you need more help, I can introduce someone else to you."
N "Oh, sure! That'd be cool."
"She taps on the shoulder of the other girl in the room."
Berkly "Could you help him, please?"
show berkly concerned
"Berkly looks up at the clock on the wall. Her eyes widen in shock, and quickly gathers her belongings."
show berkly annoyed
Berkly "Oh dear, I haven't been keeping track of time."
show berkly neutral
Berkly "I've gotta rush, so I'll see you around campus, probably."
N "Oh, y-yeah, see you around!"
"She was already out the door by the time I had waved bye."
hide berkly neutral with dissolve
"She's quite moody... pretty cool to talk to, but also very easy to annoy."
"I sigh in both tiredness and relief."
unknown "Yeah, she's a real charmer, isn't she?"
N "Oh!"
"I forgot there was still another person in the room."
show lola neutral with dissolve
Lola "I'm Lola! You're certainly a new face around here."
N "Haha, yeah, I just wanted to check out the library and stuff."
"Especially since Mio kinda ditched me..."
Lola "So I'm guessing Berkly went over things really quickly, yeah?"
show lola laugh
Lola "Don’t worry I’ll just go over everything that you need clarification on."
N "Yeah, sure, I appreciate it."
show lola neutral
Lola "Hmm..."
"She takes out a tin of Altoids."
Lola "Here's a mint!"
"Crap...did my breath smell bad?"
N "Uh, thanks."
show lola laugh
Lola "Heh, your breath doesn't smell by the way. This is just my icebreaker."
"The mint is an icebreaker..."
show lola concern
Lola "Don’t stare at me like I'm some alien! I swear these are just to lighten the mood!"
N "Sorry, I just didn't expect-"
show lola laugh
Lola "The constant joking? Like I always say, don’t worry about it!"
hide lola laugh with dissolve
show library_1 with Fade(1.0,1.0,1.0)
show lola neutral with dissolve
Lola "~And this is the place where you can find the records specifically researched by our professors."
N "Thanks for your help!"
show lola laugh
Lola "Remember if you need anything, I’m your gal."
show lola neutral
N "Of course, I’ll keep it in mind."
"Lola waves goodbye, and leaves the archives."
hide lola neutral with dissolve
###
jump if_else_updown
###

label choice_betweenBL_Lola:
N "Excuse me, I was wondering if I could get a brief introduction to the archives?"
show lola neutral with dissolve
unknown "Sure, I don't see why not."
N "Thank you!"
unknown "You new around here?"
N "Yeah, I'm trying to get a feel of the library and the school right now."
unknown "That's really cool!"
Lola "Lola, by the way."
N "I'm [name]. It's nice to meet you!"
show library_1 with Fade(1.0,1.0,1.0)
show lola neutral with dissolve
Lola "-And this is the place where you can find the previous research done by JJ alumni."
N "That's pretty cool."
"It's kind of boring around here..."
Lola "It’s nice having someone willing to listen to me, you know."
menu:
    "Yeah, you've been really helpful and informative.":
        N "Yeah, you've been really helpful and informative."
        Lola "I'm glad to help!"
    "Well, I guess.":
        Lola "Better some than none."
    "I don't really have a choice.":
        show lola annoyed
        Lola "Well, you didn't have to ask me if you didn't want to."
        $Lola_LP -= 1
show lola neutral
"Lola looked up at the clock on the wall. Her jaw dropped, and quickly gathered her belongings."
show lola concern
Lola "Hey, [name], I gotta blast."
Lola "If you need more help, you can ask Berkly over there."
"She motions to the girl intently perusing files."
N "The one with the glasses?"
show lola neutral
Lola "Yep, just make sure to mention that I recommended you to her or else she might ignore you."
hide lola neutral with dissolve
"She enthusiastically waved goodbye to me, and I returned the gesture."
"I went over to the person she mentioned."
N "Hi, could you give me a quick rundown of this place? Lola told me you could help me."
show berkly neutral with dissolve
Berkly "You're the new student, yeah?"
N "Yeah, I am."
Berkly "Alright then, let's get started."
hide berkly neutral with dissolve
show library_1 with Fade(1.0,1.0,1.0)
show berkly neutral with dissolve
Berkly "This is the area where you can access vinyl records and VCRs."
N "It's pretty dusty here..."
$ sshake = Shake((0, 0, 0, 0), 0.5, dist=15)
show library_1 with sshake
N "A-ACHOO!"
"I sneezed hard, and dust particles flew up around me."
Berkly "I should really go. I've got plans later, so I can't stay for much longer."
N "Oh, don't worry about me! You've been really helpful."
show berkly happy
Berkly "It’s no problem. I know some secret places and hidden areas in the library too, if you're interested of course."
N "Uh... yeah that'd be cool some time."
"I guess that's cool?"
show berkly neutral
N "Thanks for the info!"
Berkly "Of course, it's no problem."
hide berkly neutral with dissolve
"Before I can wave goodbye, she's out the door."

#########################
label if_else_updown:
if not Upstairs:
    jump go_upstairs
else:
    jump after_library_intro

#########################

label go_upstairs:
"Well, I guess I should check out what's upstairs."
jump Upstairs

label go_downstairs:
"Well, I guess I should check out what's downstairs."
jump Downstairs


######################

label Upstairs:
$ Upstairs = True
show library_3 with Fade(1.0,0,2.0)
"I head upstairs, curious about the type of books the university has in inventory."
"Wow, these stairs are kind of treacherously steep. I better watch my step!"
"As I approached the top of the staircase, I noticed someone leaning over a mess of books and papers."
"She looks tired and erratic."
"Maybe I should help her..."
menu:
    "Help her":
        jump choice_helpRyver_help
    "Walk past her":
        jump choice_helpRyver_nohelp

label choice_helpRyver_help:
"I walked over and picked up some strewn papers near the top of the steps."
N "Here you go."
show ryver neutral with dissolve
unknown "Oh, thank you! I could've used an extra hand."
N "No problem! I'm not really doing anything right now."
unknown "Really? Are you new around here?"
N "Yeah. I'm actually just looking around."
show ryver concerned
unknown "Oh, I hope I'm not taking too much of your time."
N "Oh, no, it's no problem. I'm pretty free right now."
"I reached for a piece of paper and her hands grazed against mine." #uwu
N "S-Sorry!"
show ryver laughing
unknown "Haha, don't be so nervous. It's okay."
"I suppose Americans make friends easily? She didn't seemed bothered about me intervening at all..."
hide ryver laugh with dissolve
jump choice_helpRyver_after

label choice_helpRyver_nohelp:
"She seems like she's got it under control, so I continued making my way up."
"I took one step up the stairs and a girl brushed passed me."
unknown "Oh my god, Ryver! Are you okay?"
"I stopped mid-step and turned around. Two girls squatted and hunched over the strewn about papers."
unknown "What happened?!"
unknown "I'm fine, don't worry! I just forgot to zip my backpack and everything just-"
"A few small papers fell out between bigger pieces."
unknown "-Scattered, you know? You should get to class though. You're late, right?"
unknown "I mean, I am but...."
unknown "Go to class! I got this."
"A few seconds of silence passed by until her friend sighed."
unknown "I'll see you later then! Maybe ask someone for help."
"The girl scurried off and I looked up the stairs. Then, back down."
"I should probably help her."
"I walked back down the steps. I stood hesitantly beside her."
N "D-Do you need any help?"
"The first girl, Ryver, took one look at me and moved aside with a big smile."
show ryver laughing with dissolve
unknown "Oh my god, yes. Please. Thank you so much."
"I knelt on the floor next to her and helped pick up her papers."
hide ryver laughing with dissolve
jump choice_helpRyver_after

label choice_helpRyver_after:
scene library_3 with Fade(1.0,1.0,2.0)
show ryver neutral with dissolve
"We gathered all her papers into a messy pile and shuffled them into a semi-neat stack."
show ryver concerned
unknown "Phew, well that took forever. "
unknown  "Hey, thank you sooo much for the help!"
unknown "You're a lifesaver, errr...."
N "Oh, I'm so sorry. I'm [name].  Pleased to meet you!"
show ryver laughing
Ryver "Nice to meet you, [name]. The name's Ryver."
show ryver concerned
"She stared at her own stack and then back at mine."
"She looks a little concerned."
show ryver neutral
Ryver "Hey, do you mind coming along with me? I don't think I can carry all of these on my own without them like, flapping all over the place."
N "Yeah! No problem!"
hide ryver neutral with dissolve
"With a smile, she raced ahead of me and led me up the flight of stairs. "
"She'd change topics so often that the conversation seemed erratic, yet I felt like she really wanted to know more about me."
"I wonder if she's always this friendly with complete strangers."
show library_3 with Fade(2.0,0,1.0)
show ryver laughing with dissolve
Ryver "Here we are! You can put them next to the bag over there."
"I walked to where she pointed, and I find a schoolbag and laptop laid on a table."
"Does...Does she just...leave her bag out like this?"
"I placed the stack over on the table."
show ryver neutral
Ryver "Sooo, you're a new student, huh?"
N "Yeah. I've been taking tours around campus, and I haven't gone around to looking at the huge library here."
Ryver "Well, you're in luck! I just so happen to be in here ALL the time."
show ryver laughing
Ryver "Yours truly can give you a tour."
N "Really? You'd do that?"
show ryver neutral
Ryver "Yeah! I'll even buy you a drink as a thank you!"
N "O-oh, no, it's okay! Really, I'm fine-"
"She rolled her eyes and tugged me away."
hide ryver neutral with dissolve
"Next thing I knew, we were exploring the library together."

show library_3 with Fade(1.0,1.0,2.0)
show ryver neutral with dissolve
Ryver "... And this vending machine tends to eat your money."
"I don't really eat a lot of snacks, but I suppose this is some useful information?"
N "Haha, I'll keep that in mind if I ever need a quick snack."
"I gripped the soda she bought me.  I felt weird just taking something."
N "A-Again, I can pay you for the drink. All I did was pick up some papers."
show ryver laughing
Ryver "Don't sweat it. Anything to help a fellow student. We need to stick together, after all!"
"Ryver’s words died out as a finger tapped her back. She quirked her brow and looked over her shoulder."
show ryver neutral at left with move
show diana concerned at right with dissolve
unknown "Hey, Ryver, mind keeping it down over there?"
"A girl emerged from a series of bookcases, nervously looking at us."
unknown "Um, sorry to intrude, but you're talking a bit loudly."
Ryver "Sorry, Diana. I was talking to one of the new students here."
show diana neutral at right
Diana "Oh, uh— it’s alright! It’s very pleasant to, uh, make your acquaintance."
Diana "I-I'm Diana. What's your name?"
show ryver concerned at left
Ryver "Jeez, Diana, you make introducing yourself seem like the most life-threatening thing in the world."
#((Diana blushes))
show diana neutral blushing at right
N "I’m [name]. It's nice to meet you!"
show diana annoyed blushing at right
Diana "I-I'm only asking your name. N-No need to be so sudden..." #>///~///>
"H-Huh? Did I say something she didn't like?"
show ryver neutral at left
Ryver "By the way, what were you doing on your laptop? You looked like you were staring at your screen pretty intensely earlier."
show diana neutral at right
Diana "I was just really busy, um, catching up on something."
"I'm pretty sure she was watching anime when we walked past her a few minutes ago..."
menu:
    "Call her out.":
        N "But you were just staring at your laptop the whole time with headphones in..?"
        show diana annoyed at right
        Diana "So what?!"
        show diana annoyed blushing at right
        Diana "It was VERY important business!"
        show ryver annoyed
        Ryver "..."
        N "Oh, uh, sorry..."
        "Her shoulders hiked up to her ears and her eyes darted to the door."
        Diana "I-I-I-"
        Diana "I have to go now. See you all later!"
        hide diana annoyed blushing with dissolve
        Ryver "See ya."
    "Pretend you didn't see anything.":
        N "Well, if you were catching up, it must've been very important."
        N "We need more dedicated people like you!"
        show diana concerned blushing at right
        Diana "O-oh, um..."
        show diana happy blushing at right
        Diana "Y-Yeah! More people like me! Of course! Definitely!"
        Ryver "Um, what are you on about?"
        show diana happy at right
        Diana "A-Anyways, I-I-I have another class. I'll see you around, Ryver!"
        show diana happy blushing at right
        Diana "A-And you- I'll see you! Yes! B-Bye!"
        hide diana happy blushing at right
        Ryver "Uh, see ya!"
"Diana left in a hurry, mumbling and quickly packing up her things."
"She didn’t look back as she quickly exited the premise."
"I turned to Ryver and she placed a hand at her hip and heaved a sigh."
show ryver concerned at center with move
Ryver "I’m sorry. She gets really anxious whenever it comes to strangers."
"I mean, that sounds understandable..."
show ryver neutral
Ryver "Which reminds me. I've gotta go before it gets dark."
Ryver "Thanks so much for helping, by the way."
N "Well, thank you for the tour."
N "If I ever have any questions, I hope I find a tour guide as cool as you."
"Ryver laughed and punched my arm playfully."
Ryver "See you around!"
hide ryver neutral with dissolve
"She disappeared behind a row of bookcases and I was alone."

############
if not Downstairs:
    jump go_downstairs
else:
    jump after_library_intro
############

label after_library_intro:
"..."
"Oh man, I didn't even think about messaging Mio this whole time to check on him!"
"He did kind of just abandon me and left me to fend for myself, though."
Mio "Hey, [name]!"
"I turn around and see Mio rushing towards me."
N "Well, took you long enough."
Mio "Ah, sorry. It was a pretty urgent call."
Mio "Were you able to get around?"
menu:
    "Yeah":
        N "Yeah, I was able to. I found some nice people who showed me around some places."
        $ Mio_LP += 0.5
        Mio "That's great! Sorry I wasn't able to help more."
    "Yeah, no thanks to you":
        $ Mio_LP -= 1.0
        Mio "Dang, dude. I can't help it when I have emergencies."

Mio "Anyways, let's head back if there's nothing else to do."
N "Okay."

scene dorm night with Fade(1.0, 0, 1.0)
with Pause(2.0)

"I returned to my room that night and tidied up my bag for tomorrow."
"I've got my first day of class, so I should try to prepare in advance."
#N "Huh?"
#"I picked up my cellphone and found a text message from Mio."
#"It says:"
#"Rest up, dude. You have a big day tomorrow!"
"I checked the time and-"
"Whoa! It's already this late???"
#"I shoot him a quick response."
#N "Thanks \(^ - ^)/!"
#"After sending it, I sat down on my bed."
"I quickly set my bag on my chair, turned off the lights, and sat down on my bed."
"I sighed and my mind drifted off."
"I'm exhausted beyond belief, but I think i've made a lot of new friends."
"I drifted off to sleep, wondering when I'd meet them again."

jump Thursday_One
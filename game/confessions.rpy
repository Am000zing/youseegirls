label Friday_2:
#"confessions page"
#Here things are labeled as CFS - confession scene :D
scene dorm morning with Fade(2.0,0,2.0)
"Sunlight streamed into my room as I groggily turned off my alarm."
"Finally..."
"It's the end of the week."
"It always feels relieving knowing you've made it through the rough of it."
"I've had a good time though."
"I think I've met some really cool people here on campus."
"Well, I should get going to class. I started strong, so now I should end strong!"

scene outdoor hall with Fade(2.0,0,2.0)
"As I make my way to class, I start thinking about the people I've talked to..."
"I hope I'll be able to make lasting relationships while I'm here!"


play music "audio/confession.mp3" fadein 6.0
scene Romance hall with Fade(2.0,0,2.0)
"It's quite lovely outside at this time of day."
"UCJJ has been really fun so far."
"Maybe I'll just stay here."
"From behind me, I hear someone-"

if e_Mercie == 4:
    jump e_Mercie_CSF
elif e_Ryver == 4:
    jump e_Ryver_CSF
elif e_Berkly == 4:
    jump e_Berkly_CSF
elif e_Bella == 4:
    jump e_Bella_CSF
elif e_Dany == 4:
    jump e_Dany_CSF
elif e_Christine == 4:
    jump e_Christine_CSF
elif e_Lola == 4:
    jump e_Lola_CSF
elif e_Diana == 4:
    jump e_Diana_CSF
elif e_Irene == 4:
    jump e_Irene_CSF
else:
    jump e_Mio

label e_Mercie_CSF:
Mercie "H-Hey, [name]. I wanted to talk to you. If that’s okay."
N "Huh?"
show mercie concern with dissolve
play music "audio/confession.mp3"
"I turn around and notice Mercie nervously standing behind me."
N "Oh, yeah. That’s fine."
show mercie neutral
Mercie "Do..."
show mercie neutral blush
Mercie "Do you have a cellphone?"
N "Y-"
show mercie annoyed
Mercie "Wait! No- Ugh! Of course, you’d have a cellphone."
Mercie "Everyone has a cellphone. What am I even saying? Geez!"
"...Is she okay?"
N "Hey, is everything alright?"
show mercie concern
Mercie "..."
Mercie "I-I screwed up."
Mercie "It’s just..."
show mercie neutral
Mercie "You’re the first person who hasn’t forgotten I existed."
Mercie "And you’re the only person outside of my friends who has even so much as talked to me."
Mercie "{i}Not that I’ve had many friends to begin with.{/i}"
show mercie concern
Mercie "I-I don’t know..."
Mercie "What I’m trying to say is..."
show mercie neutral blush
Mercie "C-Can I get your number?"
"Oh?"
show mercie concern
Mercie "N-Not as like, an ‘asking you out’ thing! Haha, because that would be...um..."
Mercie "..."
show mercie concern blush
Mercie "F-Forget it. Pretend I didn’t say anything!"
N "N-No! Come back! I think you’re really great too!"
show mercie concern
Mercie "..."
Mercie "Really?"
show mercie smile
Mercie "{i}It wasn’t all in my head..?{/i}"
N "Yeah! Here. Put your number in my phone and I’ll text you."
show mercie concern
Mercie  "..."
N "Haha, now that I think about it… You’ll be the first American contact I have!"
"Apart from the family here, at least."
show mercie cg with Fade(2.0,0,2.0)
Mercie "{i}I’ve never really been the first for anything...{/i}"
#show mercie cg blush with dissolve
Mercie "You’re a really weird guy, [name]."
show black bg with Fade(2.0,0,2.0)
"You've unlocked special images in your Journal."
jump Credits

#label e_Ryver_CSF:

label e_Berkly_CSF:
"I turn around and spot a familiar face. Except instead of being alone, she was with a couple others."
"She spots me and walks over to me."
play music "audio/confession.mp3"
show berkly neutral with dissolve
Berkly "[name], good to see you again."
N "Yeah, good to see you too."
B "Listen, I was thinking over some things...and I realized theres areas I can really improve myself on."
"I opened my mouth to speak-"
#show berkly cg
"-but Berkly quickly shushed me."
B "Sorry, I just want to get all this off my chest at once."
B "I know that you were right, but improving on my own is difficult. Which is why I wondered if you were open to the possibility of hanging out- no."
B "I wanted to know if you would like to go on a date on the weekend of the last week of the month."
N "I, uh."
B "Don't worry, you don’t have to decide right now."
B "I’ll be waiting for your response."
show black bg with Fade(2.0,0,2.0)
"You've unlocked special images in your Journal."
jump Credits


#label e_Bella_CSF:
#label e_Dany_CSF:
#label e_Christine_CSF:
#label e_Lola_CSF:
#label e_Diana_CSF:
#label e_Irene_CSF:

label e_Mio:
#"u got that"
Mio "[name]?"
N "Huh?"
show mio neutral with dissolve
play music "audio/confession.mp3"
Mio "You alright? You kinda seemed spaced out."
N "Oh, uh, yeah. I'm fine."
Mio "If you say so."
show mio teasing
Mio "Don't make me worry about you."
N "Haha, you? Worry about me?"
show mio upset
Mio "Hey, that's kinda rude. Why can't I?"
show mio neutral
menu:
    "I just seem just out of your league.":
        Mio "Haha, what do you mean?"
        show mio teasing
        Mio "You sayin' you interested?"
        N "Huh? N-no, that's not what I'm-"
        show mio neutral
        "Mio suddenly leans in really close."
    "I don't think I should be worried about.":
        show mio upset
        Mio "What do you mean?"
        Mio "Am I not allowed to care for a dear friend?"
        N "No, I never said that! I just-"
        show mio teasing
        Mio "Just what?"
        show mio neutral
        "Mio suddenly leans in really close."
"I suddenly feel really self-conscious."
N "Um, you're really close-"
hide mio neutral with dissolve
"I lose my balance and fall backwards."
"Mio tries to reach out for me but it's too late."
"I fall on my butt on the lawn."
N "Ugh..."
Mio "You alright?"
scene mio cg with Fade(1.0,0,2.5)
N "Um, yeah."
Mio "Haha, did you get nervous?"
N "N-no, that isn't it. I just-"
Mio "You don't gotta give me an answer now."
Mio "We can just progress naturally, as most do."
N "..."
Mio "Won't we now, [name]?"
jump Credits

label Credits:
scene ysg with Fade(2.0,0,2.0)
"Thank you so much for playing!"
"It's incomplete right now, but I hope you'll look forward to seeing what we continue to develop!"
label Friday_2:
#"confessions page"
#Here things are labeled as CFS - confession scene :D
scene dorm inside with Fade(2.0,0,2.0)
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
"at age 6 she was born without a face"
Mercie "H-Hey, MC. I wanted to talk to you. If that’s okay."
N "Huh?"
N "Oh, yeah. That’s fine."
#Mercie (blush)
Mercie "Do..."
Mercie "Do you have a cellphone?"
N "Y-"
Mercie "Wait! No- Ugh! Of course, you’d have a cellphone."
Mercie "Everyone has a cellphone. What am I even saying? Geez!"
"...Is she okay?"
N "Hey, is everything alright?"
Mercie "..."
Mercie "I-I screwed up."
Mercie "It’s just..."
Mercie "You’re the first person who hasn’t forgotten I existed."
Mercie "And you’re the only person outside of my friends who has even so much as talked to me."
Mercie "{i}Not that I’ve had many friends to begin with.{/i}"
Mercie "I-I don’t know..."
Mercie "What I’m trying to say is..."
Mercie "C-Can I get your number?"
"Oh?"
Mercie "N-Not as like, an ‘asking you out’ thing! Haha, because that would be...um..."
Mercie "..."
#Mercie (blush) “....”
Mercie "F-Forget it. Pretend I didn’t say anything!"
N "N-No! Come back! I think you’re really great too!"
Mercie "..."
Mercie "Really?"
Mercie "{i}It wasn’t all in my head..?{/i}"
N "Yeah! Here. Put your number in my phone and I’ll text you."
Mercie  "..."
N "Haha, now that I think about it… You’ll be the first American contact I have!"
"Apart from the family here, at least."
#show mercie cg1 with fade
Mercie "{i}I’ve never really been the first for anything...{/i}"
#Mercie (smiles while blushing)
"You’re a really weird guy, [name]."
#I’ve obtained Mercie’s number!
#jump Credits



#label e_Ryver_CSF:
#label e_Berkly_CSF:
#label e_Bella_CSF:
#label e_Dany_CSF:
#label e_Christine_CSF:
#label e_Lola_CSF:
#label e_Diana_CSF:
#label e_Irene_CSF:
label e_Mio:
"u got that"
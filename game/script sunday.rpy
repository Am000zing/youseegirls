# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


label start:
python:
    name = renpy.input("Before we start, what's your name?", default="Haru")
    name.strip()

if name == "Dio" or name == "dio" or name == "Mio" or name == "mio":
    define dio = Character("[name]", color="F8B900")
    dio "I'm sorry, but you cannot have that name."
    jump start
elif name == "owo" or name == "uwu" or name == "0w0" or name == "OwO" or name == "OWO" or name == "UWU" or name == "uWu" or name == "UwU" or name == "oWo" or name == "0W0":
    define owo = Character("[name]", color="9D00F9")
    owo "Choose a different name, you degenerate."
    jump start
elif name == "Bulge" or name == "bulge":
    define bulge = Character("[name]", color="9D00F9")
    bulge "But there was nothing to notice."
    jump start
elif name == "Game Spawn" or name == "gamespawn" or name == "Gamespawn" or name == "GameSpawn" or name == "game spawn":
    menu:
        "The club that you should join."
        "Yes":
            jump sunday
        "No":
            jump start
elif name == "agenda":
    window hide
    show screen agenda with dissolve
    "hi"


menu:
    "Your name is [name], right?"
    "Yes": 
        jump sunday
    "No":
        jump start

label sunday:
# Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
scene purple bubble bg
with dissolve


"I stepped out of the plane into the passenger boarding bridge, feeling the immediate difference between the dry California breeze and the warm Japan humidity."
"As I walked into passport control, I quickly texted my family friends that it would only take about 10 to 15 more minutes before I could go to the terminal where I should be exiting."
"Luckily I don't have too much luggage to pick up from the baggage claim."
"I prefer traveling light anyways."

#scene fuwafuwa bubble bg

"I took a placement test against my classmates to earn an opportunity to come to the United States to visit a university of my choice there."
"The school that stood out to me the most was The University of California: JJ, or UCJJ, for short."
"The {b}JJ{/b} is supposed to be the initials of the founder of the school, but the founder chose to keep his name hidden from the world, as well as his face."
"How admirable! He clearly values upholding the highest standards of education rather than chasing money or fame."
"I studied and worked really hard to get here... "
"I better take advantage of the opportunity when I can!"

#scene bubble bg


"I stepped out of the International Airport, luggage dragging at my side."
#show airport arrivals 
"I blinked and squinted under the sunlight."
"I don't know what'll happen in this foreign land, but I believe I'm going to make it!"


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
#show eileen happy

unknown "Hey, [name]! Over here!"

"My luggage chugged behind me as a lone figure waving enthusiastically came into view."
"I squinted and started a light jog towards their car."
"I waved to them as I got closer, shaking in excitement."

N "Hey Auntie! Uncle! Sorry I took a bit."

show auntie neutral at right
with dissolve
A "Oh no worries, [name]. We're just glad you landed safely!"
U "Here, let me put your luggage in the back. We gotta get out of this airport before the traffic makes me lose my mind."
A "How was your flight, [name]? I hope you were able to get some sleep on the plane."
menu:
    "It was bearable.":
        N "It was a little bumpy here and there, plus the occasional crying child."
        A "Oh my, were you able to sleep for a little?"
        N "Yeah, kinda."
        A "Well, you can sleep in the car ride on the way to UCJJ, okay?"
    "I had a nice time sleeping.":
        N "I had my headphones, so the flight wasn't horrible."
        A "So you were able to sleep on the plane?"
        N "Yeah, I got a bit of sleep, but I might rest in the car for a little bit."
        A "Of course! Get as much energy as you can. We'll be here to help you move in too!"
    "Well...":
        N "There was a kid who could NOT stop crying. I felt really bad for their parents... they seemed like they were trying their best to deal with it."
        A "Oh dear, poor thing."
        U "Poor thing? More like poor passengers stuck in there for 15 hours listening to that."
        A "That's so rude! I'm sure the child and parents were trying their best."
        U "Which is exactly why I think toddlers and babies should be banned from planes."
        A "Well, [name], you can sleep in the car ride on the way to UCJJ if you need to, okay?"
label after_menu:
    hide auntie neutral
    with dissolve
    "Finally leaving the airport, I leaned back the car seat and relaxed."
    "My eyes feel a bit heavy... maybe I should get some rest."
    "I closed my eyes..."

scene black bg
with dissolve
with Pause(1)

U "Hey, [name]. Wake up! We're here now."
U "Luckily the drive wasn't too bad as soon as we left the airport."
"Groggily, I stretched my arms out. Oh man, already at the school?"
U "You can rest some more as soon as we move in."
A "Take out your passport. It's your only piece of ID for your dorm keys right now."

scene dorm inside
with dissolve

"Getting the keys didn't take too long, but the moving in process felt like lifetimes."
"ESPECIALLY since I just got off the plane about an hour ago."
"But I am feeling a little more energized now though."
"I'm so excited!"

unknown "Hey, you're [name], right?"

"I turned and saw a tall man by my doorway."
"He was wearing a shirt that shouted UCJJ pride all over it."

N "Hello! I'm afraid we haven't met yet."
unknown "It's alright! I just got a notification that you moved in, so I wanted to introduce myself since we're likely going to seeing each other a lot."

"He sticks out his hand in greeting."
"As I return the gesture, I realize how strong his grip is. My hand kind of hurts..."

Mio "The name's Mio."
Mio "I'm your Resident Advisor, so if you need anything, just knock at my door!"
"He motions down the hall. There's a door with a big name-tag labeled: MIO Brandon."
"Mio straightens up, wide smile on his face."
"His smile is so bright it's blinding..."
Mio "I didn't come over just to introduce myself though."
Mio "I also came to remind you that I'll be taking you on campus tours during your orientation."
Mio "You do remember, right?"
N "Ah, yes! I did know about the tours but I wasn't sure who I was supposed to meet."
"Well, NOW I know, anyways."
#insert Mio smile
Mio "Well, now you know!"
Mio "I'll let you settle in and move in now. Meet me at the parking lot that you came in from at 10 AM."
"He backed out of the room waving."
Mio "See you tomorrow! 10 AM, Parking lot!"
N "Ahaha, yeah! See you!"
"He leaves the room."
A "He seems like a nice boy! I hope you two will get along."
"Yeah, he seems nice. I feel like I can trust him..."

scene desk bg
with Fade(0.5, 0.0, 0.5)
"I slurped on my cup noodles tiredly, finally finished with settling in."
"Auntie and Uncle already left about 2 hours ago."
N "Well, I have to be a little more productive now so that I can just get some sleep."
"I cleaned up, muscles feeling a little stiff from all the sitting in the plane."
"I wonder what school here is... going to be like...zzz"
N "zzz..."

jump Monday_One

label quad_encounters:
#show quad

#RYVER ENCOUNTERS
#RYVER ENCOUNTER ONE
label e_Ryver_1:
#Ryver is outside in the Quad.
"She’s sitting on the lawn with two library books lying open in front of her, scribbling in a notebook on her lap."
menu:
    "Approach Ryver?"
    "Yes":
        jump e_Ryver_1_A
    "No":
        #return to the quad options
        "She looks really busy. I shouldn't disturb her."
        jump quad_people
#(A.)
label e_Ryver_1_A:
$ Ryver_LP += 1.0
"As I walk closer, Ryver notices me approaching and looks up from her writing."
show ryver laughing with dissolve
Ryver "Hi [name]! What’s up?"
N "Hey Ryver! I just wanted to chat."
show ryver neutral
Ryver "Cool! How’s university life treating you?"
N "It’s been fine. Mind if I sit with you?"
show ryver laughing
Ryver "Of course not!"
show ryver neutral
"She starts putting her books away to make space for me beside her."
N "What were you working on?"
Ryver "I’m trying to get a head start on my ethnic studies paper so I have more free time later."
menu:
    "Wow, a paper already?":
        $ Ryver_LP += 0.5
        jump e_Ryver_1_A1
    "Ethnic Studies is an interesting subject.":
        $ Ryver_LP += 1.5
        jump e_Ryver_1_A2
    "What do you like to do in your free time?":
        $ Ryver_LP += 1.0
        jump e_Ryver_1_A3

#[“Wow, a paper already?”]
label e_Ryver_1_A1:
show ryver annoyed
Ryver "Yes. It’s not due yet, but I don’t like when my workload piles up."
show ryver neutral
menu:
    "I'm a procrastinator myself.":
        $ Ryver_LP -= 1.0
        show ryver annoyed
        Ryver "But don’t you end up feeling really stressed? I can direct you to a time-management workshop, if you want. That really helped me."
        jump e_Ryver_1_A_End
        #Relationship Result: -0.5
    "Homework can be stressful.":
        $ Ryver_LP += 1.0
        show ryver neutral
        Ryver "Right? I’m glad you get it. You probably have some coping tips of your own. Maybe we can share later."
        jump e_Ryver_1_A_End
        #Relationship Result: 1.5

#[“Ethnic Studies is an interesting subject.”]
label e_Ryver_1_A2:
show ryver laughing
Ryver "It is! I’m glad UCJJ is making it a requirement for new students."
Ryver "I think everyone should open their minds to the diverse perspectives of the world."
menu:
    "You sound really passionate about that.":
        $ Ryver_LP += 1.0
        show ryver laughing
        Ryver "Yeah, I am pretty passionate about equality and human rights. I want to do something with that after I graduate."
        jump e_Ryver_1_A_End
        #Relationship Result: 3.5
    "I agree. Education is important.":
        $ Ryver_LP += 0.5
        show ryver neutral
        Ryver "Haha, yeah! There really should be more people like you."
        jump e_Ryver_1_A_End
        #Relationship Result: 2.5

#[“What do you like to do in your free time?”]
label e_Ryver_1_A3:
show ryver neutral
Ryver "Oh, just hang out with my friends and chill. Maybe go to a concert from time to time."
menu:
    "Do you have a lot of friends?":
        $ Ryver_LP += 0.5
        show ryver neutral
        Ryver "Yeah. A lot of them are from this club I’m in. Speaking of..."
        #Relationship Result: 2.5
    "What kind of music do you listen to?":
        $ Ryver_LP += 1.0
        show ryver neutral
        Ryver "Music? I like EDM. And lo-fi, sometimes."
        #Relationship Result: 3.0
    "That's cool.":
        jump e_Ryver_1_A_End
        #Relationship result: 2.0

label e_Ryver_1_A_End:
"Ryver shoulders her bookbag and stands up."
show ryver neutral
Ryver "Anyways, I have to run to a meeting now. It was nice seeing you!"
N "See you later!"
"*Ryver waves enthusiastically as she leaves."
hide ryver neutral with dissolve
jump menu_areas


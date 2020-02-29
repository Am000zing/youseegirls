default Berkly_LP = 0
default Dany_LP = 0
default Lola_LP = 0
default Mercie_LP = 0
default Bella_LP = 0
default Christine_LP = 0
default Diana_LP = 0
default Ryver_LP = 0
default Irene_LP = 0
default Mio_LP = 0
default danyrng = 0

# +1: Standard choice to have dialogue w/ someone (every dialogue choice is +1 if there's no special effect)
# +1.5: Sending a gift
# +2: Choosing liked responses
# +2.5: Sending a loved gift
# +3: Choosing loved responses
# +0: Choosing disliked responses

menu Gifts:
    "Who do you want to send a present to:"
    "Berkly":
        $ Berkly_LP += 1.5
    "Lola":
        $ Lola_LP += 1.5
    "Dany":
        $ Dany_LP += 1.5
        jump danygift
    "Christine":
        $ Christine_LP += 1.5
    "Diana":
        $ Diana_LP += 1.5
    "Bella":
        $ Bella_LP += 1.5
    "Irene":
        $ Irene_LP += 1.5
    "Ryver":
        $ Ryver_LP += 1.5
    "Mercie":
        $ Mercie_LP += 1.5

label danygift:
    if Dany_LP >= 3:
        $ danyrng = renpy.random.randint (1,3)

        if danyrng == 3:
            "wow, thanks!"

        else:
            "uh...."
    else:
        Dany "wow, thanks!"
jump aftergiftgiving
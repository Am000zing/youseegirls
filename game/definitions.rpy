define Berkly = Character("Berkly", color="#FC74A9")
define Dany = Character("Dany", color="#FC74A9")
define Lola = Character("Lola", color="#FC74A9")
define Mercie = Character("Mercie", color="#FC74A9")
define Bella = Character("Bella", color="#FC74A9")
define Christine = Character("Christine", color="#FC74A9")
define Diana = Character("Diana", color="#FC74A9")
define Ryver = Character("Ryver", color="#FC74A9")
define Irene = Character("Irene", color="#FC74A9")
define Mio = Character("Mio")
define NPCM = Character("NPC Mio")
define A = Character("Auntie")
define U = Character("Uncle")
define unknown = Character("???")
define cashier = Character("Cashier")
define student = Character("Student")
define Chef = Character("Chef")
define Mom = Character("Mom")

define config.menu_include_disabled = True
# The game starts here.


define narrator = Character(None, what_italic=True)
define N = Character("[name]", color="#228cc9")

define fade = Fade(0.5, 0.0, 0.5)

init python:

    saturation = 1.0

    def bwImage(st,at,path):
        return im.MatrixColor(Image(path),im.matrix.saturation(saturation)),None

define e_Berkly = 0
define e_Dany = 0
define e_Lola = 0
define e_Mercie = 0
define e_Bella = 0
define e_Christine = 0
define e_Diana = 0
define e_Ryver = 0
define e_Irene = 0
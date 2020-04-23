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

init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
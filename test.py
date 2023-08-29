import spacy

nlp = spacy.load("en_core_web_sm")

quote = """
MATT: Welcome to Wildemount. The year is 835 P.D.,
or post-Divergence. This continent is divided both

by jagged terrain and political powers. The
Menagerie Coast, a collection of city-states

united under the Clovis Concord, monopolizes the
southwestern shores and ports of Wildemount,

thriving on open trade and cultural freedom.
Beyond the Cyrios Mountains lies the massive

region known as Wynandir, bisected by the
Ashkeeper Peaks. Eastern Wynandir houses the

expansive wastes and turbulent badlands of
Xhorhas, overrun with all manner of beasts and

terrors, relics from the final battles of the
Calamity that ruined that scarred landscape.

Northward, you would find the Greying Wildlands, a
lawless realm harboring a curse that has kept it

unconquered by human hands. However, this story
begins in the territory of Western Wynandir,

within the boundaries of the Dwendalian Empire.
Emerging 13 generations before, the Dwendalian

Empire has slowly spread to encompass the
surrounding societies of the region, absorbing the

peoples of the Zemni Fields and the Marrow Valley,
before finally conquering the Julous Dominion and

taking the whole of Western Wynandir for the
Empire.

SAM: There will be no test.

MATT: No. This is– let me continue. Under the
rule of the current King Bertrand Dwendal, now in

his 68th year, most are left to their own devices.
You live as you did before. The crown only takes a

tithe of what you produce and earn. You follow its
laws, worship its gods, and bow to its installed

local leadership. In return, denizens of the
Empire are protected from the chaotic horrors and

shadowed evils that stalk the edges of the
civilized lands. This accord has led to a

prosperous century for the Empire, or at least the
political elite. Tensions brew beneath the

chafing watch of the Crown’s Guard. Every temple
is government-owned and run, and worship outside

the approved idolatry is met with imprisonment.
Rumors of military clashes at the eastern border

near Xhorhas have many common folk on edge. Our
story, however, begins much smaller. Here in the

southern reaches of the Marrow Valley, beyond the
entry gates of the Wuyun Gorge, lies the small

rural town of Trostenwald. Bordering the blue
waters of the Ustaloch, this town came to

prominence near the turn of this recent century,
when the surrounding fertile farmlands were

discovered to produce a unique type of grain and
wheat, leading to a boom of breweries. When the

glut subsided, three large families stood
triumphant in the local business of fermented

delights. Now Trostenwald thrives on their exports
of fish, crops, and ale. Here in this sleepy trade

stop along the Amber Road, a handful of wandering
destinies slowly begin to intersect.

We begin in the early hours of the morning on the
day of Grissen in a messy room on the second floor

of the Nestled Nook Inn. A bleary-eyed, bruised
man in a tattered coat slowly wakens from his

lengthy sleep, catching his small, snoring ally
curled at the foot of the bed.
"""
doc = nlp(quote)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

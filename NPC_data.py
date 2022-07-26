from tools.Tools import *

# Add new entries within the string separated by a line break

races = """Dwarf
Halfing
Dragonborn
Human
Half-Elf
Tiefling
Tortle
Half-Orc
Elf"""
raceList = lineBreakList(races)

pronouns = """She/Her/Hers
He/Him/His
They/Them/Theirs
No pronouns, only a name"""
pronounList = lineBreakList(pronouns)

age = """A child
A teen
A young adult
An Adult
Elderly
Extremely old"""
ageList = lineBreakList(age)

hair = """Short dark/black hair
Short blonde/white hair
Short red hair
Shoulder-length dark hair
Shoulder-length blonde hair
Shoulder-length red hair
Flowing dark hair
Flowing blonde hair
Flowing red hair
Colorful hair(green/purple/blue/etc), length at GM discretion
Bald
Wigged (Roll again)"""
hairList = lineBreakList(hair)

build = """Tall and lean
Tall and ripped
Tall and rotund
Medium Height and build
Medium Height and slim
Medium Height and out of shape
Short and thin
Short and sturdy
Short and stout
Sickly (Roll again)"""
buildList = lineBreakList(build)

firstName = """Aer
Ali
Archer
Azar
Brook
Briar
Balin
Berieve
Carmen
Chidi
Chardane
Cyrille
Dane
Desta
Devon
Dian
Eidar
Eli
Erin
Evrim
Fabian
Farah
Flynn
Fatima
Gabi
Grey
"Gums"
Goose
Hadley
Helle
Hisoka
Hunter
Imani
Indiana
Irati
Ike
Jaden
Jamal
Joprani
Jack
Kaari
Kyra
Kagiso
Kalin
Lin
Lucian
Lumi
Lloyal
Maayan
Makota
Moriah
Nesim
Nico
Nyyk
Noose
Ori
Olley
Ophilia
Oban
Piper
Poe
Pal
Perrin
Quinn
Quora
Quinene
Rayyan
Ren
Roux
Rowan
Samar
Siya
Skye
Slaine
Tal
Tierney
Toiv
Tumelo
Umber
Umut
Urg
Val
Vanja
Vivian
Varek
Wanda
West
Weezy
Wooster
Xen
Xuan
X'ian
Yael
Yagmur
Yannik
Yuck
Zein
Zeke
Zaya"""
firstNameList = lineBreakList(firstName)

lastName = """Aberrich
Aefrim
Atlas
Avilseer
Baelmai
Bingletrite
Blackreed
Bronzestein
Carter
Claymore
Cogturner
Crysalis
Datesi
Darksteele
Deepstone
Dwandra
Eeaves
Excellente
Emallo
E'tellor
Faemoira
Firsel
Flintheart
Frostarm
Geasfoot
Gigak
Gnazbright
Goldcask
Huneldth
Hutchrice
Hoover
Honeyeater
Iasbex
Igrild
Illynmah
Importan
Jarvalsa
Jaytai
Jeffries
Justice
Kavius
Keystina
Khilltahrn
Koahath
Leagallow
Lillfritz
Lukewill
Luckdodger
Mavcius
Merigu
Mishala
Mogumir
Neriya
Nialinva
Neeves
Noosecatcher
Oakfury
Ootati
Oldfur
Orgulas
Polaan
Plackard
Puddlewish
Poutine
Questar
Quid
Reebsa
Reyhana
Rivershale
Rosenmer
Sarberos
Shatterblade
Sindasalt
Srob
Thanar
Thermobolt
Therundlin
Tighfield
Underbough
Ugdough
Us
Valarnith
Venderform
Volto
Vainweather
Wapronk
Wolfsbane
Woolyboon
Wheelmaiden
Xas
Xeran
Xencord
Yesvyre
Yahsquin
Yeoman
Yearender
Zeagan
Zimet
Zytal"""
lastNameList = lineBreakList(lastName)

description = """Shaggy hair and slight overbight
Deep-set eyes and an upturned nose
Wide smile and a fashionable mole
Steady gaze and pursed lips
Deep facial scar and a gruff exterior
Pug nose and lots of freckles
Round face and rosy cheeks
Few hairs springing out of a wart on their face
Heavy limp and a can-do attitude
Kind face and a slow drawl
Shifting eyes and a hushed voice
Few missing teeth and a hungry gaze
Massive nose and a tight mouth
Hooded eyes and a casual tone
Wild hair and a covered in sweat
Oily skin and whistling breaths
Large ears and an oval face
Strong jaw and a hearty laugh
Slack jaw and a tendency to mouthbreathe
Gap-toothed grine and dead eyes
Pot Belley and an infectiuous giggle
Blank expression and wild ear-hair
Face full of piercings and extremely kind eyes
More tattoos than uninked skin
Buns of steel and the armor to match
Scarred and scabby knuckles they always seem to be cracking
Sick pompadour haircut
Wearing a corset of a much slimmer person
Slack face on one side impeding on their speech
Tongue seemingly too big for their mouth
Posh attitude and clothes to match
Posh attitude without the clothes to match
Biggest head in the room
Broad shoulders and lowcut tunic
Hunched back and sores
Flirty eyes and the grace of a dancer
Devoid of eyebrows and a sense of humor
Soot-covered face
Dent in their skull that has healed over
Purple Tunic, ascot, and patent leather boots
Covered in black tar and white feathers
Broken arrow stuck in the side of their head
Black eyes and irises
Face Buried in a book about Wild Turkeys
Holding a tiny dog and fighting back tears
Humming to themselves and scratching flaky skin
Narrow face and fine, almost too perfect features
Bruised eye and a busted lip
Lumpy nose that looks a bit infected
Beehive hairdo that makes them seem taller
Neck twice as thick as their face
Face that appears to be stitched together
Looks like they're about to vomit
Dripping in sweat
Expertly juggling a trio of daggers
Drippy nose and red cheeks
Wearing clothes that are three sizes too big
Looks twice their age
Pretty face and big ideas
Wearing goggles and chomping a smoldering cigar
Has the energy of an overstimulated child
Has bangs that everyone agrees do not suit their face
Nervously chewing their lower lip
Blind, but making it work
Still sporting scars from a rogue Owlbear attack
Just has one of those faces...
Has a chin that could block out the sun
Whisper-quiet voice
Cute smile and a belt of knives
Wearing far too many belts and silver jewelry
Biggest beard in the room
Blessed with lavish curves
Scythe-wielding farmer
Armor that shines like the sun
With an almost hypnotic voice and an air of importance
Looks like they just woke up
In a tight-fitting, red-scaled jakcet
Wearing temple robes and a surprised expression
Greasy hair and hands to match
Hard, weathered face with eyes that tell a story
Walks with the grace of a dancer
Wearing a crop top to show off their abs
Wearing black leather and a pair of sharp heeled boots
Has a permanent squint and a stiff upper lip
Who appears as if they were struck by lightning
With a smile that's all teeth and no joy
Has a smell that is off-putting
Has bloody nail-free fingertips
Wearing a hat that is half as tall as they are
Wearing droopy robes, obscurring their body
No arms, but two Mage Hands instead
Bare-feet and seems to be in a hurry
Dressed in a patchwork coat of dozens of fabrics
One leg, and a hamgman's scar on their neck
Deaf and uses gestures to communicate
Shaggy hair, baggy clothin and a chill attitude
Has cheekbones that could cut glass and eyes that pierce
Wearing a hood that they can't remove
Handsome face and a sure, kind smile"""
descriptionList = lineBreakList(description)

wants_needs = """Could really use a hug
Could use a bath
Who literally and figuratively has no sense of direction
Begging for help to find their kidnapped father
Compelled to smell everyone they meet
Just need directions/ride to the next town
Thinks they're possessed by a vengeful warrior
Needs a cure for their incessant hiccups
Has developed a taste for human flesh
Just trying to get through the day, man...
Knows of a nearby cave filled with treasure
Hasn't slept in eight days
Hasn't been sobr in two weeks
Will do pretty much anything for a silver piece
Repeats the full names of everyone they meet
Can't stop talking about the end of the world
Constantly on the lookout for grooming tips
Compulsively says what they're thinking
Wants to do right by their god, no matter what the cost
Attracted to a member of the party
Brother was wrongfully accused for a crime the party committed
Thinks they have a rat infestation
Can't find their horse
Needs a set of blacksmiths tools
Lost their mother's wedding band
Needs to be the centre of attention
Needs help with a dance off
Had a dream where they saw the party die
Needs a rare coin to complete their collection
Loves to talk about food
Owns the town paper
Wants to be left alone
Worried they might have unleashed a curse
Needs human contact
Says their family has been possessed
Just wants to own their own pastry shop
Needs a place to hide
Looking for the witch of the woods
Trapped in the friend zone
Is saving to start a restaurant
Once this uptight town to legalize dancing
Suspects their house is haunted
Wants to clean up the local pond
Says their sister has been turned into a dog
Wants to know if you've seen a man named Web
Has a standup performance tonight
Need some help dealing with local thugs
Once the party to protect them
Needs an invitation to tonight's ball
Is looking for a cure to a contagious disease
Is searching for the power of a wish spell
Has been challenged to a rap battle
Just inherited an orphanage
Is raising money for wizard school
Can't find their glasses
Is on the hunt for a red dragon egg in the area
Needs to catch six fish
Needs everyone to wise up
Needs to acquire a rare chre jelly
Believes their friend might be a hag
Is looking for models for a fashion show
Wants to join the circus
Needs enough incense to bring back their familiar
Is looking for some drinking buddies
Can't unlock their basement
Refuses to bathe and talks to any stray dogs
Looking for the dream archive page 118
Seeks to kill the town guard who killed their dad
Would rather be listening to heavy lute tunes
Wants to learn to fight
Enjoys harmless flirting
Spreads propaganda against Shapeshifter's
En route to the Hall of the many gods page 144
Needs investors for their pyramid scheme
Can't find their watch
Is trying to sell a Dragon heart
Wants to spread the word about their God
Is trying to write a love ballad
Searching for redemption
Who wants to see the next sunrise
Longs to be the strongest person alive
Hired to kill a party member
Compulsively judges others fashion sense
Trying to build a Time machine
Is on a quest to kill monsters
Is trying to do good
It's trying to sell some fruit
Is on the run from prison
Needs the blood of 30 crows
Wants to learn common
Wants to go on in adventure
Is paddling bags of medicinal route
Needs to spread their father's ashes
Is hoping to run for public office
Seeks a new owner for their pet owl
Is looking for their dog. Have you seen their dog?
Doesn't let anyone get in their way
Is hunting for ancient relics in old forgotten tombs
Looking for inspiration for their new novel"""
wantsNeedsList = lineBreakList(wants_needs)

secrets_obstacles = """Has Sticky Fingers
Is an utter coward
Doesn't speak Common
Is tracking the party's movements for the spy's guild
Cannot walk on their own
Is plagued by a curse (page 248)
Has lost the will to live
Can't control the volume of their voice
Is in deep with a local crime boss
Is never wrong. Just ask them
Is always in a hurry
Gets distracted easily
Is addicted to a local drug
Doesn't believe in violence
Distrust at least one party member
Is also a Lycanthrope
Is allergic to something nearby
Is comically hot tempered
Is plagued with a small bladder
Has terrible judgment
Is a satyr in disguise
Six the perfect whiskey recipe
Is afraid of the dark
Is a stranded planar traveller
Is self obsessed
Struggles with their dad's expectations
Doesn't have teeth
Insults those in charge
A mind that's beginning to unravel
Is hopeless at negotiating
Is afraid of bats
As a part-time cult leader
Gets nervous near new people
Needs locks of hair from everyone
Despises being touched
Runs a multilevel marketing scam
Definitely a fiend but is making it work
Can't read
Is bad luck to everyone within 30 feet
Is possessed by a low level devil
Has a gambling problem
Has a problem with somnambulism
Can't remember their name
Is a goose that was true polymorphed
Lies for fun
Is a member of the assassins guild
Hasn't paid their tab in six months
Has never made a true friend
Is on the run for tax evasion
Is a long lost member of the royal family
Is struggling to get over the flu
Is a runaway zombie
On the treasure map to a secret island
Hates children
Is the definition of very chaotic evil
Is afraid of spell casters
Is working against the parties interests
Lacks Common sense
Is being blackmailed
Feels like an extra in someone else's story
Is wearing a hag's eye from a nearby coven
Is five months behind on all their bills
Can only tell the truth
Is immortal
Won't take no for an answer
Uses a puppet to talk
Has a habit of losing their false teeth
Can read minds reattach
May have made a pact with a demon
Is way more apathetic than you
Is missing their tongue
Fierce commitment
Assumes everyone they meet is a shifter
Is devoid of confidence
Is a compulsive liar
Is never on time
Is particularly awkward
Is afraid of heights. And depths
Speaks with wild gestures
Once ruled this land
Is a newly made vampire
Has crippling arthritis
Now has cold feet
Won't listen to human opinions
Is absolutely from the future
Serves a talking cow
Was, until today, a shut in
Thinks humans are useless
Is also a deva
Is a Magic School dropout
Is a warlock of The Great Old One
Is a total yes-man
Is a happy go lucky necromancer
Is a butting songwriter
Was an escaped convict in their youth
Is possessed by the spirit of a God
Owns a dog that can speak Common
Runs an illegal fighting ring nearby
Is an absolute kill joy
Once looked completely different
Once looked completely different"""
secretsObstaclesList = lineBreakList(secrets_obstacles)

carrying = """2gp, 5sp, 14cp. Beltknife, scyth, bundle of wheat
Empty moneypouch. A silver broach in the shape of a rabbit
1sp, 8cp. Small bag of butterfly wings. Pouch of herbs and a pipe
1gp, 15cp. A novel titled Through the Weave. One packet of beans
Nothing. And proud of it!
2sp, 17cp. A wooden cup they carved themselves
73cp painted to look like 73pp. A small jar of platinum paint.
32cp, 13sp. A hoope and a stick.
15sp. A necklace that contains a ball of yak hair
21cp, 2sp, 3gp. An incredibly smooth rock they enjoy tumbling
3sp, 8gp. A jar fullk of beef tallow. A crude map of the region
5cp, 9sp, 1gp. A vial of wyvern poison
4cp, 16sp. An oversized lollipop. A deck of cards
6cp, 8sp, 12gp. Loaded dice. A directories of local gambling halls
79cp, 2sp. Knitting needles and a half finish scarf
7cp. A large leather hat. A set of thieves tools
6sp, 1gp. A cup and ball game. A trout and butcher paper
4cp, 3sp, 1gp. A book about blacksmithing
85cp. A note that says, “Be careful, I love you. - Mum"
64sp. 12gp in loose gems. A rock hammer
14cp, 17sp, 4gp. A magnifying glass
10sp. Brewers kit and water skin of whiskey
32sp. A collection of dolls that looks like the party
Whistle only a badger named Jenny can hear
5cp, 30sp, 9gp. A very small hat
19cp, 2sp. A spy glass that can suck out an eyeball on command
14cp, 92sp. An error field map of the realm
A cursed penknife (role on the cursed table on page 248)
32cp, 7sp, 3gp. A pair of shoes in need of resoling
8cp. An IOU that reads "owe you three sacks of wool. - Ham"
94cp, 1gp. A mask that hides their face and hit list of local thugs
7cp, 8sp, 2gp. A dark artifact
34cp, 10sp. A broken lute. A crumpled love letter
3cp, 5sp, 7gp. A sack of dates. A pound of dried apricots. A fishing pole
4cp, 6sp. A set of wooden teeth
7cp, 92sp. A bottle of baby tears they want to sell
9cp, 53sp, 900gp. A dark leather tome titled How To Act Human
5cp, 5sp, 5gp. Five rings worth 55gp
3cp, 81sp. Joiners tools. A bloodsoaked rag
32cp, 5sp, 1pp. A crust of mouldy bread. Some salt pork
45cp, 2sp. An undead hand that is very important to them
61cp, 3sp. A forger's kit. A list of nobles names
92cp, 3gp. Cufflinks that can seal two doses of Drow poison
52sp. A sack of fingernails, each more precious than the next
89cp, 3sp. A belt buckle with a Hidden lock pick
62cp, 32sp. A diamond that appears to be worth 500 GP. It's not
25cp, 6sp, 24gp. A Spork, the first of its kind
6cp, 2gp. A sandwich made of nut butter and smashed jam
21cp, 5sp. An exquisite dagger carved from the bones of a dragon born
4cp, 74sp. A wine skin filled with a potion of haste
8cp, 53sp. A fake beard. A tome filled with gift ideas for hundreds of children
91sp. A recipe for pot pie. Small sack of peas. Spices in
3cp, 14sp. A jar of honey. A box containing a very large Queen bee
7cp, 13sp. A gate spell scroll
A pocket sized copy of the realms founding documents
A frog. Roll 1d6. On a 1, it was once a prince
31cp. A rudimentary colouring book. Some coloured wax pieces
4cp, 3sp, 2gp. A set of woodworker's tools
8sp. A minor gem worth 1gp
5gp. A +1 scimitar engraved with the name "Trevor"
42sp. A tub of grease. A wand of webs
55gp. A vial of de-aging serum that takes 20 years off of a creature's life
8sp, 4gp. A top hat concealing a dozen squirrels
3sp. A bottle of milk. An ornate quarterstaff
An unopened letter challenging them to a duel with a merchant
15cp. A jar capable of storing memories
8cp. A vile labelled "DO NOT OPEN” that contains the expelled gas of a king
90sp. A liniment that helps with insomnia
13cp. Directions to a guards house. A box of juice
Sheet music from a bard you've never heard of. A -1 charisma pinky ring
13pp. A jar of beard oil that is also flammable
29sp. A small painting of an Elven girl
35. A colourful piece of chewing taffy that never loses its flavour
A list of several gods with at least nine crossed out
14 vials of a potion it smells great but does nothing
A watch chain. A pair of fancy hair combs
A note with the location of a Dragon's layer
30sp. A pair of bi-lands readers. A sack of candies
A morning ring featuring the eye of their mother
1cp, 1sp, 1gp, 1pp. A deck of many things
390gp. A sack of grave dirt. A spade. A beret
42cp, 71sp. Three vials of a tonic that adds +2 to strength for one hour
62cp, 21sp, 92gp. A gag and a hood. Two vials of purple worm poison
3cp, 9sp, 21gp. An opal carved in the shape of a jawbone
5cp. A sports almanac
92sp. Manticore bait. A griffin call. Sacks of meat
20-percent off coupon for Mage You Look (page 128)
18cp, 4sp. A stuffed tiger. A tuna sandwich
3cp. A speckled egg. A broken music box new one
92gp. A small heart and a smaller cage
3gp. A bag of salt. A bag of pepper. A bag of octopus tentacles
A lyre that's missing all but one string
A glass orb. A raven's beak. A vial of tiger blood
5cp. A lump of coal. A small box filled with ashes
52sp. An herbalists kit. A neatly folded poster with their face on it
5,256. A notebook listing all the things they've done this year
13sp, 2gp. A few gnarled balls of thick cord and cloth
81cp, 3sp. A list of rules for something called “Brawl Joint”
Ink that disappears but it can be revealed with a little heat 
A 32 page booklet of so-called "haters "- a few names are crossed out"""
carryingList = lineBreakList(carrying)

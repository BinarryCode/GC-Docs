from ClassDefFunc import Define_ClassGuide, class_guides
# name, desc, main, alt, item, reloadBool, user1, user2, passive, wallJumps, airJumps

# DOOM
Define_ClassGuide("BaronOfHellClass", "Baron Of Hell", "temp description",
    "Baron Slash/Fireball\nUncharged, does two slashes.\nCharged, fires a fireball that summons gravity-affected fireballs\naround it when it hits a surface.",
    "Baron Grab\nDoes a dash that grabs opponents. On grab, they are instantly slammed.",
    "",
    False,
    "Baron Run\nDoes a ranged dash move that can hurt opponents.\nCan be cancelled into altfire.\nIf holding jump, thrusts you downwards and does a stomp upon landing. This can't be cancelled.",
    "", "", 0, 0
);
Define_ClassGuide("CyberdemonClass", "Cyberdemon", "temp description",
    "Cyberdemon Rocket\nFires rockets as long as you have ammo.",
    "Cyberdemon Grab\nGrabs opponents, and after a while, hits them and knocks them back.",
    "",
    False,
    "",
    "", "", 0, 0
);
Define_ClassGuide("RevenantClass", "Revenant", "temp description",
    "Revenant Rocket\nFires an exploding rocket that knocks opponents back.\nIf used during altfire, rapid-fires smaller bullets.",
    "Revenant Jetpack\nActivates Jetpack. Use again after activated to disable it.",
    "",
    False,
    "Revenant Punch\nA punch.",
    "Homing Rocket\nFire a rocket that homes in at the nearest player, or the player you aim at.",
    "", 0, 1
);
Define_ClassGuide("ArchvileClass", "Archvile", "temp description",
    "Archvile Fireball\nFires a ripping fireball. This explodes upon impact with surfaces.",
    "Archvile Pillar\nIf used close enough to an opponent, a flaming aura appears over them. If they don't try to escape it, they will get hit after some time.",
    "Demon Swap\nSwitches the demon spawned from User2.",
    False,
    "Archvile Aura\nFires a flaming aura. When allies touch it, they are given slight damage reduction.",
    "Demon Summon\nSpawns either an Imp or a Cacodemon, depending on which icon is outlined.",
    "", 0, 0
);

# JJBA
Define_ClassGuide("JotaroKujoClass", "Jotaro Kujo", "temp description",
    "Ora Ora\nStar Platinum unleashes a barrage of punches, pummeling enemies who come close to him.\nIn Stand Off Mode, you can control his detonation. In Stand On Mode, after some startup you gain a momentum boost and Star Platinum punches in front of you.",
    "Mach Ora\nStar Platinum launches forwards, unleashing a gut punch that knocks the enemy back.\nIn Stand On Mode, you can aim him, and the first use stops you in place.",
    "",
    False,
    "Stand Toggle\nToggles Stand On Mode, changing how the attacks work.",
    "Star Charge\nStar Platinum charges up, unleashing a different attack depending on input.\nMainfire is replaced with Star Finger, dragging them towards the player. In Stand On Mode, the projectile can be aimed.\nAltfire is replaced with Star Breaker, going in an arc (if in Stand On Mode, you also get the momentum); and spawning a shockwave that knocks players up when landing.",
    "Star Platinum regenerates his health during Stand Off Mode.\nIf he runs out of health, you take 15 damage and get stunned temporarily.",
    0, 0
);

Define_ClassGuide("WamuuClass", "Wamuu", "temp description",
    "Divine Sandstorm\nHold to rapid-fire gusts of wind that slow opponents on hit.",
    "Whoosh!\nDash forwards and release to blast nearby opponents with slowdown.",
    "",
    False,
    "Wind Mode\nTurs you slightly invisible, as well as buffing the speed of Whoosh!.\nUse again to charge up a flurry of powerful gusts that knock you back while firing.",
    "", "", 0, 0
);
Define_ClassGuide("YoshikageKiraClass", "Yoshikage Kira", "temp description",
    "Bubble\nFires a bubble that can be aimed with the cursor. Releasing the attack key makes it explode.",
    "Bites The Dust\nFires a short-ranged projectile. If it hits an opponent or surface, it will tick down to rewind them and nearby opponents (and you if nearby); a few seconds back.",
    "SHA Mode Swap\nSwaps the mode Sheer Heart Attack is on. The 3 modes are: Standby, Seek And Find, and CHASEDOWN.",
    False,
    "Sheer Heart Attack\nThrows out Sheer Heart Attack, instantly putting you on the first item mode.\nOn Seek And Find mode, if an opponent is not found it will look where you aim.\nOn CHASEDOWN mode, it runs forwards until it hits a wall or opponent.",
    "", "", 0, 0
);
Define_ClassGuide("SeccoClass", "Secco", "temp description",
    "Rock Darts\nWithout enough ammo, you have to charge the attack up first.\nHaving ammo makes you fire dirt, with full ammo it becomes a 3-way spread. Yes, the debris does damage.",
    "Deep Dive\nYou dig into the ground, not able to see opponents' positions until they make a sound.\nPressing mainfire fires a volley of pinpoint dirt.\nReleasing this attack lets you hurt opponents if nearby, as well as gain a speed boost. This attack also instantly refills mainfire ammo after emerging.",
    "",
    False,
    "Secco Punch\nDoes a short-ranged punch that can rebound off of walls.\nAfter it lands, you can use this again to rapid-fire a flurry of punches at the cost of speed.",
    "", "", 0, 0
);
Define_ClassGuide("FooFightersClass", "Foo Fighters", "temp description",
    "Plankton Bullets\nFires a fast bullet. When altfire is pressed (with enough ammo);, you can rapid-fire at the cost of ammo, slightly haulting vertical movement.\nIn Overfill mode, this fires a projectile that makes opponents' movement slippery on hit.",
    "Douplegangers\nTurns into the Actual FF, leaving the body as a corpse and spawning another clone.\nIn this form, mainfire is replaced with a bigger projectile that can be rapid-fired twice. Altfire teleports you to the corpse, turning you back into FF.",
    "",
    True,
    "Over Fill\nActivates Overfill mode, making you more slippery.",
    "", "Reload fills up ammo.", 0, 0
);
Define_ClassGuide("WekapipoClass", "Wekapipo", "temp description",
    "Wrecking Ball\nThrows a wrecking ball forwards. Can crawl on floors if it hits a floor. Otherwise, it falls if it hits a wall.",
    "Satellites\nUncharged, fires a bouncing spread of Satellites. Charged, fires a shotgun spread of Satellites.\nWith a Wrecking Ball out, using altfire makes them fire satellites.\nThese Satellites will half-blind opponents on hit.",
    "",
    True,
    "",
    "", "", 0, 0
);

# PvZ
Define_ClassGuide("CactusClass", "Cactus", "temp description",
    "Spike Shot\nFires a fast projectile.",
    "Potato Mine\nPlaces a potato mine in front of you.\nIf you get close enough to it, you can rocket jump.",
    "Zoom\nZoom in and out.",
    False,
    "Wall Nuts\nSummons a set of 3 wall nuts. You can place 2 at a time.",
    "", "", 0, 0
);

# TF2
Define_ClassGuide("ScoutClass", "Scout", "temp description",
    "Bullets\nNailgun: No Powershot ammo. Rapid-fire weak bullets that do headshot damage.\nScattergun: Requires 2 Powershot ammo. Fire a spread of 5 bullets that do no headshot damage. Gives 2 Powershot ammo if 2 shots hit.\nBeverage Of The Gods: Requires 48 Powershot Ammo. Fires a large laser.",
    "Bonk\nNailgun: No Powershot ammo. Activate Bonk Rush. You cannot attack during Bonk Rush.\nScattergun: Requires 2 Powershot ammo. Makes all Nailgun and Scattergun bullets do extra damage.\nBeverage Of The Gods: Requires 48 Powershot ammo. Activates an aoe attack. Upon hitting, opponents debuffed with it give health on hit.",
    "",
    False,
    "Bat Swing\nSwings a bat, knocking opponents back o hit.",
    "", "Double Jumping gives an extra momentum boost temporarily.", 0, 1
);
Define_ClassGuide("SoldierClass", "Soldier", "temp description",
    "Hyper American Rocket\nFires a rocket that deals both contact and explosion damage.\nCan rocket jump if used close to the player, but deals damage to them.",
    "Market Gardener\nUses a melee attack that does moderate damage. If used after rocket jumping, does much more damage.",
    "",
    False,
    "Buff Banner\nCharges up a horn that gives allies and the player a temporary attack or speed buff, depending on if mainfire or altfire was pressed.",
    "", "", 0, 0
);

# Shovel Knight
Define_ClassGuide("ShovelKnightClass", "Shovel Knight", "temp description",
    "Shovel Strike\nDoes a quick swipe that reflects projectiles.",
    "Shovel Drop\nActivates Shovel Drop, letting you bounce on opponents.\nAfter bouncing on a foe, you can use your other attacks.\nWhen used on the ground, you get an extra vertical boost.",
    "",
    False,
    "Dust Knuckles\nDoes a quick damaging dash.\nCan be used again if you have enough ammo.",
    "Chaos Sphere\nFires a sphere that can be moved around by you with mainfire and altfire.\nMore wall bounces speed up the projectile.",
    "", 0, 0
);
Define_ClassGuide("KingKnightClass", "King Knight", "temp description",
    "King Bash/King Tumble\nDash forward and bash into your enemies. Once you land a hit, you twirl up and get the opportunity to hit again. You can also tumble into your enemies instead by attacking again.",
    "Dueling Glove/Rat Bombardier/Scepter Of Swiftness/Horns of Heralding/Bubble Frog\nDueling Glove:\nKnocks a hit enemy back until they hit a wall. Can be held to go faster.\nRat Bombardier:\nSends a high damage rat to run around the stage. Press Altfire to turn the rat.\nScepter Of Swiftness:\nDoes a very quick dash, dealing ripper damage to anyone caught in it. Stops when hitting a wall, and can combo into King Bash.\nHorns of Heralding:\nSummons confetti-spewing horns that do damage to anyone caught in it.\nBubble Frog:\nSummons a bubble frog to give him a floating, invulnerable bubble. Once popped, you gain 3 seconds of invincibility. Ends after the duration, or once you attack.",
    "Rat Detonate\nDetonates Rat Bombardier.",
    False,
    "Propeller Rat\nEscape danger by flying up into the air with your propeller rat, but at the cost of 10 damage.",
    "", "", 0, 0
);
Define_ClassGuide("PropellerKnightClass", "Propeller Knight", "temp description",
    "Propeller Sword\nDoes a ripper slash. Damage depends on shield ammo.",
    "Propeller Spin\nSpins your sword, blocking projectiles. Blocking projectiles gives ammo.",
    "",
    False,
    "Propeller Blow\Propeller Dive\nOn the ground, you push opponents back. Press mainfire during this to pull them in for damage.\nIn the air, you fall down quickly and stomp the ground. This cancels your glide.",
    "",
    "Can double jump.\nIf you hold jump after jumping, you can glide.",
    0, 0
);
Define_ClassGuide("TreasureKnightClass", "Treasure Knight", "temp description",
    "Bejeweled Bubbles\nFires a rapid-fire burst of bubbles. If they hit an opponent, you instantly gain ammo.",
    "Treasure Slam\nGives the player a vertical boost in the air.\nWhen used again, the player falls down quickly, and spawns a 4-way shockwave when you land.\nIf you don't press altfire again, then you just spawn a shockwave.",
    "Anchor Hook\nWorks like Wire Adaptor, but pulls enemies in.\nIf it hits a surface, there is a delay before it pulls you in.",
    False,
    "Whirlpool Chest\nSpawns a chest that does stunning damage.\nWhen User1 is pressed again, it pulls in opponents and does more damage.",
    "", "", 0, 0
);
Define_ClassGuide("SpecterKnightClass", "Specter Knight", "temp description",
    "Specter Slash / Surf\nUncharged, does a short-ranged slash. Charged, lets you dash forwards for constant damage.",
    "Specter Dash / Judgement Rush\nUncharged, does a dash forwards. You can aim up or down to gain a vertical boost.\nCharged, fires a projectile that lets you dash towards the opponent it hits.",
    "",
    False,
    "Chronos Coin\nThrows a coin that slows opponents on hit.",
    "", "", 3, 0
);

# Pizza Tower
Define_ClassGuide("PeppinoClass", "Peppino", "temp description",
    "Peppino Stuffed Punch / Space Jam/Special Delivery\nWith full ammo: Does a medium-ranged grab. Press mainfire to punch them where you aim. Press altfire to slam and stun the opponent.\nWithout full ammo: Does a quick slap. Hitting opponents requires a second hit to give a combo point.",
    "Running Grease\nHold to gain speed. Loses all speed if released. If you hit a wall, you get stunned for 1 second. Hold jump to climb up walls.",
    "",
    False,
    "Peppino Shuffle\nDoes a random pose. If used with 5 combos, it does damage, but takes three combo points away.\nIf used with 3+ combos, you can parry projectiles that are about to hit you.",
    "", "Can pick up a shotgun weapon by finding AoE weapons.\nJumping in the air makes you stomp.", 0, 0
);
Define_ClassGuide("VigilanteClass", "Vigilante", "temp description",
    "Vigilante Pistol\nRapid-fires weak bullets. Tap mainfire again when the HUD flashes to rapid-fire.",
    "Dynamite\nIf uncharged or used without enough ammo, throws a dynamite. You can get a short boost by going close to it when it explodes.\nIf charged, does a jump in the air.",
    "Detonate\nDetonates any thrown dynamite.",
    False,
    "Dash\nDoes a dash forwards, doing damage if it hits an opponent.",
    "",
    "Move forwards for enough time to gain speed. This has a speed cap.",
    0, 0
);
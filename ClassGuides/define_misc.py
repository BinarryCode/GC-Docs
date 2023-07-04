from ClassDefFunc import Define_ClassGuide

Define_ClassGuide("DrJekyllAndMrHydeClass", "Dr. Jekyll", "temp description",
    "Corrosive Concoction / Ruthless Strike\nIn Dr. Jekyll Form: Fires a gravity-affected projectile that gives afterburn on hit.\nIn Mr. Hyde Form: Does a short-ranged punch.",
    "Daily Exercise / Cane Poke, Trample / Wail\nIn Dr. Jekyll Form: Uncharged, does a short-ranged poke that knocks opponents back. Charged, does a dash after placing a bomb down. If mainfire is pressed, the bomb is thrown with the cane. No this bomb does not have the ridiculous radius.\nIn Mr. Hyde Form: Uncharged, charges forwards while swinging the cane, doing ripper damage. Charged, does an explosion that removes some Hyde Potion ammo.",
    "Medicine / Bloodlust\nIn Dr. Jekyll Form: A quickheal item, heals you and allies depending on ammo.\nIn Mr. Hyde Form: Changes attacks to give health on hit.",
    False,
    "Hyde Potion / Trample\nIn Dr. Jekyll Form: Gives 1/3 of Hyde Form Ammo. At full ammo, you transform into Mr. Hyde.\nIn Mr. Hyde Mode: Does a quick dash forwards, constantly hurting opponents in the way.",
    "",
    "In Mr. Hyde Form, your health is drained (until at 1 HP);, and ammo is drained before turning back into Dr. Jekyll.\nAfter the first morph, Hyde Potion ammo regenerates, and there is less startup lag to turning into Mr. Hyde.",
    0, 0
);

Define_ClassGuide("PepsimanClass", "Pepsiman", "temp description",
    "Pepsi Can\nUncharged: Fires Pepsi cans that can fall after some time and then bounce off floors. While gravity-defying, they can roll on the ground if they hit a floor.\nCharged: Fires a large Pepsi can that bounces off walls and floors.",
    "Pepsi Slide / Soda Can\nDoes a damaging slide.\nIf used mid-air, fires a soda can that spews out soda bits on the ground.",
    "",
    False,
    "Pepsi Bash\nDoes a dash forwards, doing constant damage.",
    "", "", 0, 0
);

Define_ClassGuide("ScottClass", "Animdude", "temp description",
    "Alarm\nFires a spread of bullets that home in on release.",
    "Neon Shield\nActivates a shield. On block, a segmented wall is fired on release, and you cannot use it for a while.",
    "",
    False,
    "Mega-Virus\nFires a slow projectile that spawns an AoE. Opponents who are damaged in it get poisoned once they leave.",
    "", "", 0, 0
);

Define_ClassGuide("DiscordAppClass", "DiscordApp", "temp description",
    "Punches\nRapid-fire short ranged fists.",
    "Swift Gun\nFire a short-ranged, explosive bullet.",
    "Nitro Boost\nTurns on Nitro-Boosted mode, temporarily giving you and allies a speed boost as well as removing ammo requirement on your attacks.",
    False,
    "@ EVERYONE\nSpawn an @ e v e r y o n e laser. Freezes opponents in place.",
    "", "", 0, 0
);

Define_ClassGuide("CrabChampionClass", "Crab Champion", "temp description",
    "Crab Arsenal\nFires a projectile depending on the weapon selected.",
    "Aqua Defender\nHold to put a shield in front of you, but your movespeed is lowered.",
    "",
    False,
    "Crab Boost\nHold to move forwards faster.",
    "", "Gains upgrade ammo over time, and when hitting opponents with mainfire or blocking projectiles.\nWhen at full upgrade ammo, you can switch weapons to upgrade.\nThe last upgrade is temporary and will set you back to the previous weapon after the ammo is drained.", 0, 0
);
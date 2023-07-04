from ClassDefFunc import Define_ClassGuide, class_guides

Define_ClassGuide("MegamanClass", "Megaman", "DLN-001 The Blue Bomber",
    "Mega Buster\nA chargable attack. Can be synthfired for an uppercut by default. Can have varying properties depending on upgrades.",
    "Slide\nA slide boost by default. Uses Gear Ammo for a bigger boost.\nJet Boost\nGives you a boost in speed.\nPower (Adaptor) Gear\nActivates Power Gear, increasing charge time and making altfire a stomp or uppercut.\nNova Strike\nDoes a powerful dash forwards.",
    "",
    False,
    "Buster Swap\nSwitch between different buster types by pressing mainfire, altfire, or user1 again.",
    "",
    "Can grab copyweps, and obtain them upon killing an opponent.",
    0,
    0
);
Define_ClassGuide("ProtomanClass", "Protoman", "temp description",
    "Proto Buster\nA chargable attack. Press altfire on full charge to increase slot ammo.\nIf used with half slot ammo, instantly fires a powerful projectile, using that ammo.",
    "Proto Bash\nA bash attack that knocks opponents back",
    "",
    False,
    "", "", "",
    0, 0
);
Define_ClassGuide("BassClass", "Bass", "temp description",
    "Bass Buster\nA spread of bullets.\nIf used with Blue Evil Energy, it works like MM10 Bass Buster.\nIf used with Red Evil Energy, it fires a 2-way spread in a set pattern instead.",
    "Bass Dash\nA dash attack that lets you use Crescent Kick by pressing mainfire.",
    "Switch Evil Energy modes.",
    False,
    "Uses the selected Evil Energy mode.\nUpon using Red Evil Energy, you lose the double jump temporarily and become more vulnerable, but gain a speed boost and can do more damage overall.\nUpon using Blue Evil Energy, you gain damge reduction, but are slower.",
    "",
    "",
    0, 1
);
Define_ClassGuide("DuoClass", "Duo", "temp description",
    "Duo Fist\nFires a short-ranged projectile.\nWhen supercharged, it instead fires a fist forward, and can be charged to fire the Giga Fist.",
    "Justice Shield\nPuts a shield in front of you, giving ammo when blocking projectiles.",
    "Supercharge!\nTurns on a Supercharge mode. It can not be turned off.",
    False,
    "Duo Meteor\nAfter some startup, you can bounce on walls. Press user1 to cancel it (hold jump during this to get a boost), and press mainfire to slam to the ground, spawning a shockwave when landing.",
    "", "", 0, 0
);
Define_ClassGuide("QuintClass", "Quint", "temp description",
    "Quint Buster/Quint Arm/Sakugarne Leap\nNot in Double Gear Mode:\nUncharged, a standard buster shot will be fired. Charged, a fist will be fired. Once it hits an enemy, it will hook onto them and deal damage.\nCharged and altfire is pressed, a standard charge shot will be fired.\nIn Double Gear Mode:\nDoes a leap after spawning a shockwave.",
    "Sonic Dash/Sakugarne Dive\nNot in Double Gear Mode:\nPerforms a constant Dash that will end if the button is released or if the dash limit is full.\nIn Double Gear Mode:\nSakugarne slams the ground and creates a shockwave.",
    "",
    False,
    "Sakugarne/Double Gear\nNot in Double Gear Mode:\nWhen Ammo is full, summons or despawns Sakugarne.\nTouching it will make you enter Double Gear Mode.\nIn Double Gear Mode: Exits Double Gear Mode.",
    "",
    "Sakugarne Regen:\nSakugarne ammo passively regens, even when charging.\nWarpstone Energy Generation:\nGenerates one unit of Warpstone Gem Energy every 30 seconds.\nLedge Jump:\nJump after falling from a ledge. This cannot be done if you've already done a normal jump.\nWarpstone Gem Energizer:\nCan upgrade weapons by using the Gem Energizer.\nVulcan Burst: Adds damage and ability to ignite oil to Quint Arm.\nRecursive Bomber: Replaces Buster Charge Shot with a gravity-affected bomb\nthat creates a multi-hit explosion.\nDream Twins: Adds damage to Gear Mode Mainfire.\nSurge Binder: Adds damage to Gear Mode Altfire.\nDrill Shredder: Adds damage to Quint Arm.\nSonic Boomerang: Buster Charge Shot creates a boomerang upon impact.\nTime Wrap: Gear Mode Mainfire creates a spread of knives.\nSnake Commando: Adds damage to Gear Mode Altfire.\nGem Energy is dropped after a hit enemy is fragged within ten seconds.",
    0, 0
);
Define_ClassGuide("MaestroClass", "Maestro", "temp description",
    "Maestro Buster\nA chargable attack.\nIf a chip is selected, press to use said chip.",
    "Chip Selection\nSelects a chip to use.\nSword: Fires a short-ranged slash.\nKunai: Fires a flurry of exploding projectiles.\nTime Bomb: Fires a timed projectile. If it gets hit, the timer goes down. If it hits an opponent, then it explodes instantly. Can be chained together.\nPunch: Fires a flurry of punches where you aim.\nMet Shield: Spawns a shield in front of you that shoots where you aim when attacked.",
    "",
    False,
    "",
    "", "", 0, 0
);

Define_ClassGuide("RushClass", "Rush", "temp description",
    "Rush Buster\nFires a 3-way spread of bullets. When using Rush Bike, it instead fires an explosive projectile",
    "Rush Jet / Bike\nDepending on the weapon, turns on/off either Rush Jet or Rush Bike if used at full ammo.\nRush Jet gives you flight, and Rush Bike lets you move forward/backward faster.",
    "",
    False,
    "Rush Coil\nLifts opponents in the air and stunning them. When used in the air, you can spawn a shockwave when landing from a high enough height.",
    "", "", 0, 0
);
Define_ClassGuide("TangoClass", "Tango", "temp description",
    "Tango Slash\nSlashes opponents in front of you. This has a cooldown when used too much.",
    "Tango Roll\nCharges up a dash. When used mid-air, it acts like a drop dash.",
    "Meow\nA 'taunt' item.",
    False,
    "Tango Rage\nMakes the player bounce up and down, replacing mainfire with a bouncing projectile and altfire with an instant full-ammo drop dash.",
    "", "", 3, 0
);
Define_ClassGuide("TrebleClass", "Treble", "temp description",
    "Treble Bark/Buster\nFires a short-ranged burst that knocks opponents back.\nWhen used in Sentry Mode, rapidfires bullets.",
    "Treble Dash/Charge Shot\nCharge up a dash forwards. This has cooldown.\nWhen used in Sentry Mode, it fires a charge shot instead.",
    "Sentry Mode Toggle\nToggles Sentry Mode. This gives you 50% movespeed when active.",
    False,
    "",
    "", "", 0, 0
);
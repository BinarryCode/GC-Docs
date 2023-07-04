from ClassDefFunc import Define_ClassGuide, class_guides

Define_ClassGuide("GravitySniperClass", "GravitySniper", "temp description",
    "Gravitor Bullet\nRelease mainfire to make the bullet lose gravity.",
    "Grenade\nThrow an explosive grenade.\nYou get a vertical boost and wall jump if it explodes near you.\nDuring said boost, you can rapid-fire grenades.",
    "", True,
    "Punch\nA basic short-ranged punch.",
    "", "", 1, 0
);

Define_ClassGuide("RangedScanClass", "RangedScan", "temp description",
    "Chaingun\nRapid-fires weak bullets.",
    "Shotgun\nFires a bullet that splits into a spread-shot. You can aim where you are knocked back.",
    "", True,
    "Stealth Shot\nFire a slow and visible bullet that transitions into a fast and barely-visible bullet. This requires reloading.",
    "", "", 0, 0
);

Define_ClassGuide("BodyBuilderClass", "BodyBuilder", "temp description",
    "Punch\nA generic punch.",
    "Weight Throw\nHold to lift weights and gain more ammo over time.",
    "",
    False,
    "Body Tackle\nCannot be cancelled upon use.\nUpon use, does a tackle that runs on the ammo gained from altfire.",
    "", "Loses altfire ammo over time.", 0, 0
);

Define_ClassGuide("RandomizerClass", "Randomizer", "temp description",
    "Randomized Bullet\nFire a missile that increases in damage over time and homes in on opponents.\nHowever, the bullet has only one health.\nFire a bullet on another bullet to make it circle around.",
    "Loot Crate\nFire a ripping chest.\nOnce it hits the ground, you get a random item.\nBuddies:\nGrand Dad - Fires a random projectile at an opponent. Has 20 health.\nEddie Bomber - Throws itself at the opponent. Does explosive damage.\n\nWeapons:\nDrop Buster - A projectile that bounces alot, and is fast.\nBass Buster Clone - Summons a Bass Buster clone that rapid-fires 10 times.\nItems 1-3:\nSelf-Explanatory.",
    "", False, "", "", "", 0, 0
);

Define_ClassGuide("HexaGlitcherClass", "HexaGlitcher", "temp description",
    "Water Gun\nFires a spread of projectiles",
    "Thunder Beam?\nFires a Thunder Beam Projectile. When used again, the projectile is paused. Release altfire during that to teleport, making you very temporarily invulnerable to projectiles and unpausing the projectile, spawning glitched Magma Bazooka projectiles, as well as reversing the directions of any mainfire projectiles.",
    "Swingset of Death\nSummons a swingset in front of you. Stand on it and wait to get launched forwards, knocking opponents back on hit and spawning a spread of sparks when landing.",
    False,
    "Teleport\nInstantly does the altfire teleport. If used after the item launch, a projectile is fired.",
    "", "", 0, 0
);

Define_ClassGuide("BruhmanClass", "Bruhman", "temp description",
    "B-R-U-H\nFires a burst of B-R-U-H letters. Once an opponent get hits by 2 of the projectiles, they get 1/4 debuff. Once the debuff spells 'Bruh' or 'hurB', they recieve more damage from Bruh Man (Non-Team Modes); and his allies (Team Modes);.",
    "Bruh Blast\nFires an BRUHSPLOSIVE projectile.\nIf used during Bruh Moment, you are launched in the air and constantly fire weaker Bruh Blast projectiles until landing.",
    "Bruh Moment\nWhen used at full ammo, toggles flight.",
    False,
    "",
    "", "", 0, 0
);

Define_ClassGuide("RunemanClass", "Runeman", "temp description",
    "Rune Bullet\nFire a weak bullet.",
    "Rune Use\nUses the selected rune.",
    "",
    False,
    "",
    "", "", 0, 0
);

Define_ClassGuide("CoronamanClass", "Coronaman", "temp description",
    "MERS-CoV Touch\nFires a short-ranged puff that gives opponents a damage debuff.",
    "SARS-CoV Touch\nSimilar to mainfire, except it slows down opponents instead.",
    "",
    False,
    "Corona Blast\nCharges up a powerful blast AoE that lingers, debuffing opponents on hit.",
    "", "", 0, 0
);

Define_ClassGuide("DeathmanClass", "Deathman", "temp description",
    "Death Buster\nUncharged, fires a spread of bullets. Charged, fires a bullet that spawns a stationary spike after some time.",
    "Fake Death\nIf a projectile hits you during the attack duration, you fake your death temporarily.",
    "",
    False,
    "Death Rush\nDashes forwards, spawning spikes that split on impact with a surface.",
    "", "", 0, 0
);

Define_ClassGuide("SnatchmanClass", "Snatchman", "temp description",
    "Snatch Buster/Slash\nNormal: Fire a bullet that does headshot damage.\nDPS: Rapid-fire weak bullets. \nTank: Fire an explosive bullet.\nSpeed: Fire a short-ranged melee.",
    "Snatch Slide/Grenade/Leap/Dash\nNormal: Slide forwards.\nDPS: Fires a grenade.\nTank: Does an explosive leap.\nSpeed: Does a longer-ranged slide. Can be used mid-air as an airslide.",
    "Switch the user1 mode.",
    False,
    "Snatch\nIf in Normal Mode, use to get an item from hitting an opponent, depending on the item mode.\nIf used in non-normal mode, throws a headshotting projectile that gives 3/4 ammo back on hit and reverts you to normal mode.",
    "",
    "Normal: None\nDPS: Recieve more damage.\nTank: Armor given, lower movespeed.\nSpeed: Faster movespeed. Movespeed lowered and slide ammo regen slowed temporarily when Speed ends.",
    0, 0
);

Define_ClassGuide("MaceGuyClass", "MaceGuy", "temp description",
    "Mace Tackle / Punch\nCharge to tackle at opponents. If uncharged, fires a short-ranged bullet.\nDuring cooldown, you can rapidly punch.",
    "Burn Torch\nFires a flame that constantly does damage as it travels.",
    "",
    False,
    "Mace Aura\nUse normally to have damage go to the opponent on hit, attacking removes it.\nAfter hitting an opponent with mainfire, this instead gives you armor. You can stack both buffs.",
    "", "", 0, 0
);

Define_ClassGuide("TelelocatorClass", "Telelocator", "temp description",
    "Telelocator Sniper\nFire two projectiles twice, with different patterns for both.",
    "Sonic Boom\nCharge up a soundwave that blocks projectiles and does damage.",
    "",
    False,
    "Hefty Grab\nCharge forwards, swapping the opponent's position to where you initially used the attack on hit.",
    "", "", 0, 0
);

Define_ClassGuide("PoisonHealerClass", "PoisonHealer", "temp description",
    "Healer's Hands\nThrows one of your arms out. When it grapples an opponent, they get hurt over time, healing you and nearby allies.",
    "Health/Poison Pellet\nThrows a health or poison pellet depending on the weapon. The former heals allies, and the latter damages foes.",
    "",
    False,
    "Finger Guns\nFires a spread of fast bullets.\nIf used while arms are out, then they fire where you aim instead.",
    "", "", 0, 0
);
from ClassDefFunc import Define_ClassGuide

Define_ClassGuide("FiremanClass", "Fireman", "FLAMES OF JUSTICE!",
    "Fire Storm\nFires a basic projectile, charges user1 ammo.",
    "Flame Thrower\Releases a constant short range barrage.",
    "", True,
    "Activate Rage\nEmpowers all of your next attacks, power depends on the user1 ammo. Can be cancelled early if at level 2 or 3.",
    "", "", 0, 0
);
Define_ClassGuide("FiremanCrossXClass", "Fireman Cross X", "temp description",
    "Fire Storm CX\nFires a projectile that goes up or down if it hits a floor or ceiling",
    "Fire Uppercut\nDoes an uppercut that knocks opponents up.",
    "",
    False,
    "Storm Tackle\nCharge up a dash that pulls opponents near you when released. Requires half ammo.",
    "", "", 0, 0
);
Define_ClassGuide("ElecmanClass", "Elecman", "temp description",
    "Thunder Beam\nFires a basic piercing projectile.",
    "Electric Bolt\nReleases a constant short range barrage, syntfire to launch yourself in the opposite direction.",
    "", False,
    "Pinpoint Lightning\nInstantly drop lighting over your cursor.",
    "", "", 0, 0
);
Define_ClassGuide("BondmanClass", "Bondman", "temp description",
    "Bond Shot\nCharges a flurry of projectiles that slow opponents on hit.\nThe rapid-fire can be canceled by pressing manifire again, keeping your ammo.",
    "Bond Sprinkler\nFires a sprinkler that spews Bond Shots when it lands on a floor.",
    "",
    False,
    "Bond Bubble\nFires a flurry of bubbles, giving cooldown with each one fired.\nThey can be shot by you (or allies) to make it grow and eventually explode.\nIf opponents shoot it then it shrinks (and doesn't explode).",
    "", "", 0, 0
);
Define_ClassGuide("YellowDevilClass", "Yellow Devil", "temp description",
    "Devil Eye / Devil Laser\nDevil Eye: Rapid-fires 5 shots. Stops when out of ammo.\nDevil Laser: Fires a short-ranged laser.",
    "Devil Cube\nFires a bouncing cube.",
    "",
    False,
    "Devil Blobs\nOnly usable with full ammo. When used, activates a dash. While dashing, press again to cancel.",
    "", "", 0, 0
);
Define_ClassGuide("CopyRobotClass", "Copy Robot", "temp description",
    "Copy Buster\nA chargable attack, similar to Mega Buster. The charge shot fires a bouncing laser projectile.\nIf the Arrow Buster Upgrade was picked up, press altfire to fire Arrow Buster instead.",
    "Copy Slide\nA damaging slide.",
    "",
    False,
    "Copy Machine\nA pinpoint attack that has multiple effects.\nUse it on yourself to temporarily spawn 2 other clones at the cost of losing the charge shot. Use it on enemies to get their location, and use it on allies to give them a temporary damage and armor buff.",
    "", "", 0, 0
);

# MM2
Define_ClassGuide("MetalmanClass", "Metalman", "temp description",
    "Metal Blade, Rising Sun, Golden Metal Blade / Metal Forge\nFires a Metal Blade, Rising Sun, or Golden Metal Blade depending on the upgrade.\nMetal Upgrade:\nOn the second weapon, you can upgrade your Metal Blade into Rising sun, and Rising Sun into Golden Metal Blade.\nExtra upgrades give you 10 HP.",
    "Thrash Metal Blade\nDoes a leap forwards, then after landing the player does a melee attack.",
    "",
    False,
    "Metal Catcher\nActs like the Quint's Revenge copywep. Upon hitting an opponent, it returns to the player with health.",
    "", "", 0, 0
);
Define_ClassGuide("AirmanClass", "Airman", "temp description",
    "Air Shooter / Tornado Of Doom\nFires a spread of projectiles that fly up.\nCharge to fire a powerful tornado that moves forwards.",
    "Copipi Swarm\nFires a Copipi egg. Press again to shoot it down. Hold altfire when it drops to have them aim where you look, otherwise they home in.",
    "",
    False,
    "Tornado Platforms\nSpawns platforms that give a boost when you or allies get nearby.",
    "", "", 0, 0
);
Define_ClassGuide("QuickmanClass", "Quickman", "temp description",
    "Quick Boomerang(s);\nWeapon 1: Fires Quick Boomerangs that return to the player after a few tics. With enough ammo, boomerangs home in onto targets after a few tics.\nWeapon 2: Fires Quick Boomerangs at a faster fire rate.",
    "Quick Dash / Slugger\nWeapon 1: Dashes quickly, summoning boomerangs and consuming ammo.\nWeapon 2: Does a constant flurry of punches, requiring both ammo.",
    "",
    False,
    "",
    "", "", 4, 0
);
Define_ClassGuide("CrashmanClass", "Crashman", "temp description",
    "Crash / Impact\nCharge to fire a 3-way spread.\nNormal: Acts like Crash Bomb.\nSticky: Sticks to opponents. Can't be charged.",
    "Crash Mines\nAll projectiles become gravity-affected after a few tics of firing.\nNormal: Acts like Crash Bomb, but with mine mechanics.\nSticky: Detonating on ceilings makes it fall back down. Detonating on walls and floors spawn a Sticky Crash Bomb that moves where you aim.",
    "Detonate\nDetonate all placed mines.",
    False,
    "Megalo Bomb\nFires two large bombs from your shoulder cannons.",
    "Megalo Bomb Redirect\nSelf-explanatory.", "", 3, 0
);
Define_ClassGuide("AlienClass", "Alien", "temp description",
    "Alien Shot\nFires a basic projectile,it bounces and gains gravity on surfaces.",
    "Alien Technology\nFires one of following attacks, hold to change selection." + "\nMecha Dragon Fire\n A powerful projectile which deals afterburn damage.\n" + "\nPicopico Blocks\n Shoots two pico pico blocks, if they connect, it will form a homing projectile in the middle.\n" + "\nBoobeam Turret\n A boobeam turret appears over your head, after a slight delay it will automatically aim and rapidly fire many shots.\n",
    "", False,
    "",
    "Has low gravity", "", 0, 0
);

# MM3
Define_ClassGuide("ShadowmanClass", "Shadowman", "temp description",
    "Shadow Blade\nFires a burst-fire volley of Shadow Blade projectiles. These can headshot.",
    "Shadow Block / Shadow Dash\nDoes a block attack that uses up ammo. If mainfire is pressed, the player dashes forwards. If altfire is pressed or the ammo is empty, it is cancelled.",
    "",
    False,
    "",
    "", "Wall jumps don't instantly regenerate, requiring waiting a bit.", 10, 0
);
Define_ClassGuide("DocRobotClass", "Doc Robot", "temp description",
    "Doc Buster\nFires a basic projectile that fills user1 ammo on hit, can also Headshot.\nSpark Data:\nThrows a Metal Gear that crawls on floors and bounces on walls once.\nShadow Data:\nShoots a fully charged Atomic Fire.\nGemini Data:\nUses Bubble Lead.\nNeedle Data:\nFires a spread of Air Shooters.",
    "Data Beam\nReleases a shield in front of the user,attacks absorbed are converted into user1 ammo.\nSpark Data:\nRapidfires quick boomerangs and increases your speed.\nShadow Data:\nUnleashes Woodman's Leaf Rain.\nGemini Data:\nShoots a projectile that freezes opponents in place.\nNeedle Data:\nShoots a Crash Bomb that creates a circle of explosions or spreads into Crash Bombs depending on if it hits an opponent or surface.",
    "", False,
    "Serial Copy\nCompletely changes your moveset,each weapon gains a new mainfire and altfire.",
    "", "", 3, 0
);
Define_ClassGuide("DocRobotMark2Class", "Doc Robot Mark 2", "temp description",
    "Doc Buster Mark 2\nFires bullets that have small ripper shields orbiting around them.",
    "Doc Shield Mark 2\nSummons a shield. Hold altfire to keep the shield up.",
    "",
    False,
    "Doc Dash Mark 2\nDoes a quick dash where you aim.",
    "Doc Barrage Mark 2\nSpawns a Red Evil Energy effect temporarily, replacing mainfire with 4 very fast bullets that increase in damage if landed.\nIf you miss a shot, this form ends early.",
    "", 0, 0
);

# DOS
Define_ClassGuide("WavemanPCClass", "Waveman DOS", "temp description",
    "Water Shooter\nStarts out as a shootable projectile, then you fire three projectiles. These split projectiles summon waves upon hitting a floor. Gives altfire ammo if you hit an opponent.",
    "Waterlogger\nRapid-fires small projectiles that gives allies armor and foes a slowdown. Heals you upon hit.",
    "",
    False,
    "",
    "", "Can 'swim' in the air. ", 0, 0
);

# MM4
Define_ClassGuide("ToadmanClass", "Toadman", "temp description",
    "Blinding Fluid\nFires gravity-affected water projectiles that blind+slow opponents on hit.",
    "Toad Tongue\nA Thunder Claw eqsue attack, that lets you gain extra mobility when hitting surfaces.\nUser1 ammo is gained when it hits projectiles or players.",
    "",
    False,
    "Rain Missile\nFires an explosive projectile that spawns Rain Flush on hit.",
    "", "", 0, 0
);
Define_ClassGuide("PharaohmanClass", "Pharaohman", "temp description",
    "Tech Attacks\nInsanity Buster: Rapid-fire weak shots.\nSolar Shine: Fires a shootable projectile that grows when shot. Shooting it too much makes it explode.\nSun Shotgun: Fire a spread of Pharaoh Shots.\nSpark: Throws an arcing projectile that does damage in a massive radius and leaves behind lethal shrapnel. This also stuns opponents.\nTesla Sphere: Fire a projectile that zaps nearby opponents.\nIce Lances: Spawn 6 icicles where you aim.\nShadow Clone: Spawns a clone after turning invisible. This clone moves around and rapid-fires Insanity Buster at a lower fire rate. Lasts 3 seconds, but is deactivated early upon attacking.\nNanite Cloud: Fire a spread of poisonous clouds.",
    "Tech Give / Sell\nIf used on the main weapon with enough ammo, gains a different tech depending on how long altfire was held for. If a tech is selected, hold altfire for long enough to sell it for tech ammo.",
    "",
    False,
    "Easy Execute\nCreates a light sphere in front of you when held. Move close to the enemy and release to do a melee attack. Successful hits temporarily make the mainfire fire hitscan projectiles.",
    "", "", 0, 0
);
Define_ClassGuide("DivemanClass", "Diveman", "temp description",
    "Dive Missile\nHold mainfire to fire torpedos. If released, they go faster and do more damage, but can't be aimed.",
    "Submarine Charge\nDoes a strong tackle that can't be controlled.",
    "",
    False,
    "",
    "", "", 0, 0
);
Define_ClassGuide("SkullmanClass", "Skullman", "temp description",
    "Skull Buster / Shotgun Ribs\nNormal Mode: Fires a weak projectile that does headshot damage. Barrier Ammo is gained on hit. Fire rate is increased depending on Barrier Ammo. When spammed with enough ammo, the buster overheats and fires much slower. \nKill Mode: Fires a cqc shotgun.",
    "Skull Dash / Focused Skull Barrier Shot\nNormal Mode: Does a dash. There is a 24-tic cooldown between uses.\nKill Mode: Fire a Focused Skull Barrier shot. This does scaling damage depending on the barrier ammo. After use, Barrier ammo cannot be re-gained for a few seconds.",
    "Kill Mode Toggle\nToggles Kill Mode.",
    False,
    "",
    "", "Wall Jump angling is slightly different.", 3, 0
);

# MM5
Define_ClassGuide("GyromanClass", "Gyroman", "temp description",
    "Gyro Attack\nFires a Gyro Attack that slows down when it hits a floor.",
    "Flight Mode\nActivates flight. While flying, you summon mini-gyros beneath you. Hold to keep flying.",
    "Gyro Split\nSplits all of the gyros. This has a cooldown.",
    False,
    "",
    "", "", 0, 0
);
Define_ClassGuide("NapalmmanClass", "Napalmman", "temp description",
    "Napalm Vulcan\nWeak: Fires weaker shots that have infinite range.\nStrong: Fires stronger, explosive shots that have limited range.",
    "Napalm Bomb\nFire a Napalm Bomb projectile that spawns a ring once it hits a floor, or an explosion on impact.",
    "Napalm Dash\nToggle a constant dash forwards.",
    False,
    "",
    "", "", 0, 0
);
Define_ClassGuide("CrystalmanClass", "Crystalman", "temp description",
    "Crystalline Ring\nFires an explosive projectile.",
    "Crystal Eye\nChargable projectile that splits on impact with a surface, charging increases speed.\nPress mainfire while charging to make the projectile have gravity.",
    "",
    False,
    "Crystal Kick\nA kick that knocks opponents back.\nWhen used in the air, there is some startup to the attack, and it does more damage.",
    "", "", 0, 0
);
Define_ClassGuide("Darkman1Class", "Darkman 1", "temp description",
    "Berserker Rush\nRapid-fires bullets. This has a cooldown meter.\nLanding hits gives altfire ammo.",
    "Dark Ram\nCharges up a dash, blasting any nearby opponent.\nPress mainfire to be able to suplex an opponent 3 times in a row.",
    "",
    False,
    "Dark Leap\nCharges up a leap, using the same ammo as the altfire.",
    "", "", 0, 0
);
Define_ClassGuide("Darkman2Class", "Darkman 2", "temp description",
    "Dark Shields\nUncharged, fires a spread of mini-shields that pulls opponents in. Charged, fires a larger shield that moves forwards.",
    "Dark Mega-Shield\nPuts up a shield that blocks projectiles. Pressing mainfire throws the shield forwards, piercing through opponents.\nPress User1 after enough projectiles are blocked to give armor to you and nearby allies.",
    "",
    False,
    "Dark Run\nCharges up a dash that stops upon hitting an opponent or wall. Opponents are knocked back on hit.",
    "", "", 0, 0
);
Define_ClassGuide("Darkman3Class", "Darkman 3", "temp description",
    "Dark Sniper\nCan be charged. Speed is dependent on charge level. Does headshot damage.",
    "Dark Rings\nShoots 3 rings that stun players. If used without enough ammo, fires one ring.",
    "Jetpack\nJumps to hover for a short time.",
    False,
    "Zoom\nZoom in/out.",
    "", "", 0, 0
);
Define_ClassGuide("Darkman4Class", "Darkman 4", "temp description",
    "Dark Bullets\nNormal Mode: Tap to fire one strong bullet, or hold to rapid-fire weaker bullets with enough charge. Press altfire during charge to automatically do the uncharged mainfire.\nDisguise Mode: Rapid-fires the tapped mainfire.",
    "Dark Shield / Dark Proto Buster\nNormal Mode: Activate Dark Shield. Leaving it up gives you a speed boost. Press altfire again to fire two shots in front and behind you.\nDisguise mode: Charge a Proto Buster shot. The projectile does headshot damage.",
    "",
    True,
    "Disguise Mode\nNormal Mode: Activates Disguise Mode. Your sprite is temporarily changed to Proto Man's.\nDisguise Mode: Throw a fake Proto Buster icon on the ground. If opponents hit it, they get a damage debuff on all of Darkman4's projectiles.",
    "", "", 0, 0
);

# MMV
Define_ClassGuide("MarsClass", "Mars", "temp description",
    "Photon Auto-Cannon / Photon Missile / CannonBall\nWeapon 1: Rapid-fires short-ranged bullets.\nWeapon 2: Fires a short-ranged explosive missile. Charge to fire a gravity-affected cannonball.",
    "Photon Stream / Martian Tread\nWeapon 1: Fires a spread of gravity-affected cannon bullets.\nWeapon 2: Dash forwards, stunning opponents on hit.",
    "",
    False,
    "Photon Seeker\nFires a projectile that first moves upwards, then moves where you aim.",
    "", "", 0, 0
);
Define_ClassGuide("JupiterClass", "Jupiter", "temp description",
    "Electric Splasher / Electric Shock\nRapid-fires bullets. If used in Jet Mode, fires Electric Shock below the player, and makes them move forwards.",
    "Electric Zapper\nFires a stunning ripper shock. If used in Jet Mode, fires a projectile that splits into more upon hitting a floor.",
    "",
    False,
    "",
    "", "", 0, 0
);
Define_ClassGuide("SaturnClass", "Saturn", "temp description",
    "Void Lock\nFires a ring that returns on impact with a surface.\nIf it hits an opponent, their health is drained as long as you have ammo and mainfire is held. With half AMMO2, press altfire during this to drag opponents to you.",
    "Darkness inside of Darkness / Quazar Beam\nPulls out a Black Hole, sucking in projectiles (giving Quazar Beam ammo);. After the move ends, the player fires a Quazar Beam for a duration based on that ammo.",
    "",
    False,
    "Saturn Stopper\nFreezes opponents temporarily, and makes you invisible. After some time, you turn visible again and fire a flurry of bullets around you.",
    "", "", 0, 0
);
Define_ClassGuide("TerraClass", "Terra", "temp description",
    "Spark Trap\nThrow out a medium ranged trap that redirects to where you aim upon detonation.",
    "Flash Sweep\nFly forward quickly for a short period of time, swiping anyone close to you while deleting projectiles with the sweep.",
    "Spark Trap Detonate\nSelf-explanatory.",
    False,
    "Grapple Dash\nDash forward, grabbing anyone that you land on and kick them in the direction you are aiming in.",
    "", "", 0, 0
);

# MM6
Define_ClassGuide("CentaurmanClass", "Centaurman", "temp description",
    "Centaur Shot\nFires a spread of short-ranged projectiles.",
    "Centaur Arrow\nCharges up an arrow projectile that splits into bullets on impact. Time the charge right to make it faster.",
    "Clone Place\nPlaces a clone, use again to remove it.",
    False,
    "Headbutt Dash\nDoes a dash forwards, knocking opponents back (with wall slam); and giving ammo on hit.",
    "Centaur Flash\nSelf-explanatory, turn invisible and reappear after some frames. Using this gives ammo.\nIf a clone is placed, you are teleported to that before disappearing.",
    "", 0, 0
);
Define_ClassGuide("PlantmanClass", "Plantman", "temp description",
    "Plant Buster\nUncharged: Fires a rapid-fire burst.\nCharged: Fires a vine whip that stuns opponents.",
    "Plant Barrier\nActivates Plant Barrier. Upon attacking, you fire the barrier. If the barrier hits opponents, they get stunned.",
    "",
    False,
    "Tack Seed\nFire a tack seed that blooms into a flower. Fires shots at opponents.",
    "Poison Seed\nFire a spore seed that blooms into a Poison Plant. When opponents get close, it sprays poison on them.",
    "", 0, 0
);
Define_ClassGuide("TomahawkmanClass", "Tomahawkman", "temp description",
    "Silver Tomahawk\nFires a bouncing projecitle.\nCharge to fire a faster projectile.",
    "Feather Swipe\nFires a sweep of feathers. Opponents close enough get slashed.",
    "",
    False,
    "Call of the Earth\nAfter some startup, does a leap forwards. Landing spawns a melee hitbox and spread of rocks.",
    "", "", 0, 0
);
Define_ClassGuide("ColtonClass", "Colton", "temp description",
    "Desert Rattler\nFires a bullet.\nThese do headshot damage.",
    "Bullet Barrage\nUses all of the available ammo to rapid-fire weaker bullets. These do not do headshot damage.",
    "Flashbang Grenade\nThrows a grenade.\nIf it bounces, it stops and blinds nearby opponents after some time.",
    True,
    "Combat Roll\nDoes a quick dodge roll. This gives you invulnerability and a slight speed boost.",
    "", "", 0, 0
);

# MM7
Define_ClassGuide("BurstmanClass", "Burstman", "temp description",
    "Danger Wrap / Bubble Blower\nDanger Wrap: Fires the copywep Danger Wrap that can be used to rocket jump.\nBubble Blower: Rapid-Fires smaller Danger Wraps that just explode upon impact.",
    "Bubble Trap\nHold to move a bubble that can be shot.\nIf it hits opponents, it lifts them upwards.\nIf two bubbles were placed, use altfire again to reset them.\nHas a 3 second cooldown between uses.",
    "Detonates Bubbles.",
    False,
    "Float Mix\nPuts the player into a bubble, moving them up then down. Use again to disable it.",
    "", "", 0, 0
);
Define_ClassGuide("CloudmanClass", "Cloudman", "temp description",
    "Thunder Bolt\nUncharged: Fire a fast bolt which stuns enemies on hit.\nCharged: Unleash a faster and stronger bolt with more stun that drops bolts in the area it landed shortly after.\nFree flight is given during the charge, and rain drops fall below Cloud Man for damage.",
    "Thunder/Lightning Cloud\nFires a cloud that spawns raindrops while moving forwards.\nHit the cloud with mainfire to stop it in place.\nWhen supercharged, the cloud spawns lightning.",
    "Cloud Redirect\nRedirects any clouds that were hit with mainfire.",
    False,
    "Thunder Charge\nHold still for a moment while you charge up static energy, allowing you to drop bolts all around you during mainfire charge.\nIf altfire is used in this state, a cloud is spawned. This spawns more powerful rain drops.",
    "","", 0, 0
);

# MM8
Define_ClassGuide("FrostmanClass", "Frostman", "temp description",
    "Ice Wave\nIce Wave: Can be charged. At mid-charge, Ice Wave is summoned in a two-way spread. At full charge, the projectiles freeze opponents.",
    "Frost Punch / Frost Dash Punch\nCan be charged. Uncharged, does a punch that knocks back foes. Charged, does a ripper dash.",
    "Ice Block\nSummons an Ice Block. This can be punched with the Frost Punch.",
    False,
    "Frost Leap\nDoes a leap forwards.",
    "", "", 0, 0
);
Define_ClassGuide("GrenademanClass", "Grenademan", "temp description",
    "Flash Grenade / Flash Bomb\nUncharged: fires a spread of grenades.\nCharged: fires a Flash Bomb projectile that summons debris once it hits a ceiling.",
    "Rush\nDoes a damaging dash.",
    "",
    False,
    "",
    "", "", 2, 0
);

# MM8.5
Define_ClassGuide("BurnermanClass", "Burnerman", "temp description",
    "Wave Burner\nRapidly fires a variant of Wave Burner that blocks shots.\nIf pressed while dashing, summons spikes around the player.",
    "Extinguisher Grenade / Big Telly Bomb\nCan be charged.\nNo Charge: A small bomb.\nFull Charge: Spawns a Telly Bomb that spawns a huge firey explosion around the area where it explodes.\nIf pressed while dashing, rapidly summons grenades around the player.",
    "",
    False,
    "Burner Dash\nMakes you constantly dash in the air, using up all ammo built up.",
    "", "Hitting opponents gives ammo for User1.", 0, 0
);

# MM9
Define_ClassGuide("PlugmanClass", "Plugman", "temp description",
    "Plug Ball\nActs like Plug Ball, but the projectile doesn't have any gravity until it hits a wall. It then acts like Plug Ball.",
    "Plug Taser / Smaplar\nCan be charged.\nUncharged: fires a three-way spread of stunning projectiles.\nCharged: rapid-fires a barrage of Smaplars.",
    "Shadow Clone\nSummons 5 shadow clones, one at a time. They only walk around, running into oppoments eventually.",
    False,
    "",
    "", "", 0, 0
);
Define_ClassGuide("FakemanClass", "Fakeman", "temp description",
    "Fake Buster\nFires a bouncing, ripping projectile.",
    "Fake Shield\nPuts up a shield. Press mainfire while it's up to fire the shield.",
    "",
    True,
    "",
    "", "", 3, 0
);

# no mm10 :);

# MM11
Define_ClassGuide("FusemanClass", "Fuseman", "temp description",
    "Scramble Thunder / Scramble Melee\nFires a wallcrawling projectile or melee attack. Both of these use ammo.\nIf used during Voltekker, cancels Voltekker.",
    "Scramble Dash / Speed Gear\nWithout enough ammo:\nDoes a short vertical+horizontal dash. This cannot be used as well underwater.\nWith enough ammo: \nWeapon 1 activates Voltekker. If used during Voltekker, activates the Speed Gear attack.\nWeapon 2 Does a dash where you aim if used with half ammo.",
    "Mainfire Toggle\nToggle between mainfire firing a projectile and melee.",
    False,
    "",
    "", "", 0, 0
);

# Misc
Define_ClassGuide("DrWilyClass", "Dr. Wily", "temp description",
    "Wrench\nThrows a wrench that can be picked up after hitting a surface.\nGravity-affected wrenches are faster.\nHitting opponents with this spawns screws.",
    "Charge Rush\nCharge to run forwards upon release. Requires mainfire or altfire to be used again after ammo drains.\nIf mainfire is used, throws multiple wrenches and moves forwards.\nIf altfire is used, gives a speed boost.",
    "",
    False,
    "Disrepair/Repair\nIf used, starts a grab attack. If used on an opponent, they are damaged.\nIf used on an ally, they are slowly healed until ammo is drained or user1 is pressed again, but can be interrupted if hit.",
    "Magnet Gun\nActivates a Magnet Gun, pulling in screws and wrenches.",
    "", 0, 0
);
from class_guides import class_guides

def Define_ClassGuide(actor, name, desc, main, alt, item, reloadBool, user1, user2, passive, wallJumps, airJumps):
    class_guide = {
        "name": name,
        "desc": desc,
        "main": main,
        "alt": alt,
        "item": item,
        "reload": bool(reloadBool),
        "user1": user1,
        "user2": user2,
        "passive": passive,
        "wallJumps": int(wallJumps),
        "airJumps": int(airJumps),
    }
    class_guides.append(class_guide)
    return class_guide

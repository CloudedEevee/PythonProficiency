import pet, ninja

lisa = pet.Cat("Lisa", ["sit", "stand tall"])
ninja_1 = ninja.Ninja("Maia", "Corg", ["Tuna", "Chicken", "Beef"], "Kibble", lisa)

ninja_1.feed().walk().bathe()
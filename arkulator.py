def make_flint(flint2make):
    multiplier = 1
    flint2make = int(flint2make/multiplier+1)*multiplier if flint2make%multiplier != 0 else flint2make
    flint2make = flint2make/multiplier
    required_stone = flint2make*2
    return int(required_stone)

def make_sparkpowder(sparkpowder2make):
    multiplier = 12
    sparkpowder2make = int(sparkpowder2make/multiplier+1)*multiplier if sparkpowder2make%multiplier != 0 else sparkpowder2make
    sparkpowder2make = sparkpowder2make/multiplier
    required_stone = sparkpowder2make*4
    required_flint = sparkpowder2make*8
    return [int(required_stone), int(required_flint)]

def make_gunpowder(gunpowder2make): #amount of gunpowder
    multiplier = 6
    gunpowder2make = int(gunpowder2make/multiplier+1)*multiplier if gunpowder2make%multiplier != 0 else gunpowder2make
    gunpowder2make = gunpowder2make/multiplier
    required_spark = int(gunpowder2make*4)
    required_charcoal = int(gunpowder2make*4)

    ingredients_spark =  make_sparkpowder(required_spark)
    ingredients_flint = make_flint(ingredients_spark[1])
    return [required_charcoal, required_spark, ingredients_spark, ingredients_flint]
    
def make_ammo(ammo2make):
    """
    For calculating final ammo
    """
    multiplier = 2
    ammo2make = int(ammo2make/multiplier+1)*multiplier if ammo2make%multiplier != 0 else ammo2make
    ammo2make = ammo2make/multiplier
    required_metal = int(ammo2make*1)
    required_gunpowder = int(ammo2make*9)
    ingredients_gunpowder = make_gunpowder(required_gunpowder)

    return (f"<=== To make {int(ammo2make*multiplier)} Advanced Rifle Bullet ===>\n\
    Required Metal Ingot: {required_metal}\n\
    Required Gunpowder: {required_gunpowder}:\n\
    \tRequired Sparkpowder: {ingredients_gunpowder[1]}:\n\
    \t\tStone: {ingredients_gunpowder[2][0]}\n\
    \t\tFlint: {ingredients_gunpowder[2][1]}:\n\
    \t\t\tStone: {ingredients_gunpowder[3]}\n\
    \tRequired Charcoal: {ingredients_gunpowder[0]}\
    \n\n\
    Totalling Stone ({ingredients_gunpowder[3]}) to put into Grinder\n\
    Totalling Flint ({ingredients_gunpowder[2][1]}) and Stone ({ingredients_gunpowder[2][0]}) and Charcoal ({ingredients_gunpowder[0]}) to put into Laboratory\n\
    Tottaling Metal Ingot ({required_metal}) and Gunpowder ({required_gunpowder}) to put into Fabricator\n\
    \n\
    Total Stone to be collected:\t{ingredients_gunpowder[3] + ingredients_gunpowder[2][0]}\n\
    Total Charcoal to be collected:\t{ingredients_gunpowder[0]}\n\
    Total Metal Ingot to be collected:\t{required_metal}")

print(make_ammo(1003))


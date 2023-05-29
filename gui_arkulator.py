import PySimpleGUI as sg

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

def make_gunpowder(gunpowder2make,amount_of_flint): #amount of gunpowder
    multiplier = 6
    gunpowder2make = int(gunpowder2make/multiplier+1)*multiplier if gunpowder2make%multiplier != 0 else gunpowder2make
    gunpowder2make = gunpowder2make/multiplier
    required_spark = int(gunpowder2make*4)
    required_charcoal = int(gunpowder2make*4)

    ingredients_spark =  make_sparkpowder(required_spark)
    ingredients_flint = make_flint(ingredients_spark[1]- amount_of_flint )
    return [required_charcoal, required_spark, ingredients_spark, ingredients_flint]
    
def make_ammo(ammo2make, amount_of_flint):
    """
    For calculating final ammo
    """
    multiplier = 2
    ammo2make = int(ammo2make/multiplier+1)*multiplier if ammo2make%multiplier != 0 else ammo2make
    ammo2make = ammo2make/multiplier
    required_metal = int(ammo2make*1)
    required_gunpowder = int(ammo2make*9)
    ingredients_gunpowder = make_gunpowder(required_gunpowder,amount_of_flint)

    return (f"\
Required Metal Ingot: {required_metal}\n\
Required Gunpowder: {required_gunpowder}:\n\
\tRequired Sparkpowder: {ingredients_gunpowder[1]}:\n\
\t\tStone: {ingredients_gunpowder[2][0]}\n\
\t\tFlint: {ingredients_gunpowder[2][1] - amount_of_flint if ingredients_gunpowder[2][1] >= amount_of_flint else 0}:\n\
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

horizontal_size = 60
layout = [
    [   sg.Text("How much ammo:\t"),
        sg.In(size=(int(horizontal_size/2), 1), enable_events=True, key="_AMMO_AMOUNT_", default_text='0')],
    [   sg.Text("How much Flint:\t"),
        sg.In(size=(int(horizontal_size/2), 1), enable_events=True, key="_FLINT_AMOUNT_", default_text='0')],
    [   sg.Button("Apply", enable_events=True, key="_APPLY_BUTTON_")    ],
    [   sg.Text("<=== Advanced Rifle Bullet ===>")],


    # [   sg.Text("bla", size = (25,20), enable_events=True,key="_OUTPUT_TEXT_")  ],
    [   sg.Multiline("Provide number of ammo demanded ^", size = (horizontal_size,20), enable_events=True,key="_OUTPUT_TEXT_")  ],

    # [   sg.HSeparator() ],

    [   sg.Text("To exit:"),
        sg.VSeparator( pad=(50,0) ),
        sg.Button("Do not exit", enable_events = True, key = "_EXIT_BUTTON_") ]

]
window = sg.Window("ARKalculator for Ammo", layout,
                auto_size_text=True,
                auto_size_buttons=True,
                resizable=True,
                grab_anywhere=False,
                border_depth=5,
                finalize=True,
                element_justification='left',
                )

while True:
    event, values = window.read()
    if event == "_EXIT_BUTTON_" or event == sg.WIN_CLOSED:
        break

    if event in ["_AMMO_AMOUNT_", "_FLINT_AMOUNT_", "_APPLY_BUTTON_"]:
        try:
            amount_of_flint = int(values['_FLINT_AMOUNT_'])
        except:
            amount_of_flint = 0
            window['_FLINT_AMOUNT_'].update(0)

        try:
            amount_of_ammo = int(values["_AMMO_AMOUNT_"])
        except:
            amount_of_ammo = 0
            window['_AMMO_AMOUNT_'].update(0)
        try:
            window["_OUTPUT_TEXT_"].update(f'{make_ammo(amount_of_ammo, amount_of_flint)}\nAmount of flint{amount_of_flint}')

        except:
            window["_OUTPUT_TEXT_"].update(f'Provided value is not a number, lol\
                \nHow much ammo do you think is: {amount_of_ammo} ammo?')
            amount_of_ammo = -1

window.close()
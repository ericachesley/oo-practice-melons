############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType('musk', 1998, 'green', True, True, "Muskmelon")
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, "Casaba")
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, False, "Crenshaw")
    cren.add_pairing('prosciutto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, "Yellow Watermelon")
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon_type in melon_types:
        print(f'{melon_type.name} pairs with')

        for pairing in melon_type.pairings:
            print(f'- {pairing}')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dict = {}
    for melon_type in melon_types:
        melon_dict[melon_type.code] = melon_type

    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        self.type = melon_type
        self.shape_rating = shape_rating
        self. color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        return self.shape_rating > 5 and self.color_rating > 5 \
        and self.field != 3

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melon_lookup = make_melon_type_lookup(melon_types)
    melons = []

    melon1 = Melon(melon_lookup['yw'], 8, 7, 2, 'Sheila')
    melons.append(melon1)

    melon2 = Melon(melon_lookup['yw'], 3, 4, 2, 'Sheila')
    melons.append(melon2)

    melon3 = Melon(melon_lookup['yw'], 9, 8, 3, 'Sheila')
    melons.append(melon3)

    melon4 = Melon(melon_lookup['cas'], 10, 6, 35, 'Sheila')
    melons.append(melon4)

    melon5 = Melon(melon_lookup['cren'], 8, 9, 35, 'Michael')
    melons.append(melon5)

    melon6 = Melon(melon_lookup['cren'], 8, 2, 35, 'Michael')
    melons.append(melon6)

    melon7 = Melon(melon_lookup['cren'], 2, 3, 4, 'Michael')
    melons.append(melon7)

    melon8 = Melon(melon_lookup['musk'], 6, 7, 4, 'Michael')
    melons.append(melon8)

    melon9 = Melon(melon_lookup['yw'], 7, 10, 3, 'Sheila')
    melons.append(melon9)

    return melons
    

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        if melon.is_sellable():
            sellability = '(CAN BE SOLD)'
        else:
            sellability = '(NOT SELLABLE)'
        print(f'Harvested by {melon.harvester} from Field {melon.field} {sellability}')




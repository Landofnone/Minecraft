from blocks import *
# items and blocks share a common id table
# ids of items should be >= ITEM_ID_MIN
ITEM_ID_MIN = 256

# From MinecraftWiki
# Items are objects which do not exist outside of the player's inventory and hands 
# i.e., they cannot be placed in the game world. 
# Some items simply place blocks or entities into the game world when used.
# Type
# * Materials: iron ingot, gold ingot, etc.
# * Food: found or crafted by the player and eaten to regain hunger points
# * Poitions
# * Tools
# * Informative items: map, compass and clock
# * Weapons
# * Armor

ITEMS_DIR = {}

class Item(object):
    id = None
    max_stack_size = 0
    amount_label_color = 255, 255, 255, 255
    name = "Item"

    def __init__(self):
        ITEMS_DIR[self.id] = self

    def on_right_click(self):
        pass

class ItemStack(object):
    def __init__(self, type = 0, amount = 1, durability = -1, data = 0):
        if amount < 1:
            amount = 1
        self.type = type
        self.amount = amount
        self.durability = durability
        self.data = data
        if type >= ITEM_ID_MIN:
            self.max_stack_size = ITEMS_DIR[type].max_stack_size
        else:
            self.max_stack_size = BLOCKS_DIR[type].max_stack_size

    # for debugging
    def __repr__(self):
        return '{ Item stack with type = ' + str(self.type) + ' }'

    def change_amount(self, change=0):
        overflow = 0
        if change != 0:
            self.amount += change
            if self.amount < 0:
                self.amount = 0
            elif self.amount > self.max_stack_size:
                overflow = self.amount - self.max_stack_size
                self.amount -= overflow

        return overflow

    # compatible with blocks
    @property
    def id(self):
        return self.type

    # compatible with blocks
    @property
    def name(self):
        if self.id >= ITEM_ID_MIN:
            return ITEMS_DIR[self.id].name
        else:
            return BLOCKS_DIR[self.id].name


class Tool(Item):
    material = None
    multiplier = 0
    tool_type = None

    def __init__(self):
        multiplier = 2 * (material + 1)

class WoodAxe(Item):
    material = WOODEN_TOOL
    tool_type = AXE
    max_stack_size = 1
    id = 271
    name = "Wooden Axe"

class StoneAxe(Item):
    material = STONE_TOOL
    tool_type = AXE
    max_stack_size = 1
    id = 275
    name = "Stone Axe"

class IronAxe(Item):
    material = IRON_TOOL
    tool_type = AXE
    max_stack_size = 1
    id = 258
    name = "Iron Axe"

class DiamondAxe(Item):
    material = DIAMOND_TOOL
    tool_type = AXE
    max_stack_size = 1
    id = 279
    name = "Diamond Axe"

class GoldenAxe(Item):
    material = GOLDEN_TOOL
    tool_type = AXE
    max_stack_size = 1
    id = 286
    name = "Golden Axe"

class WoodPickaxe(Item):
    material = WOODEN_TOOL
    tool_type = PICKAXE
    max_stack_size = 1
    id = 270
    name = "Wooden Pickaxe"

class StonePickaxe(Item):
    material = STONE_TOOL
    tool_type = PICKAXE
    max_stack_size = 1
    id = 274
    name = "Stone Pickaxe"

class IronPickaxe(Item):
    material = IRON_TOOL
    tool_type = PICKAXE
    max_stack_size = 1
    id = 257
    name = "Iron Pickaxe"

class DiamondPickaxe(Item):
    material = DIAMOND_TOOL
    tool_type = PICKAXE
    max_stack_size = 1
    id = 278
    name = "Diamond Pickaxe"

class GoldenPickaxe(Item):
    material = GOLDEN_TOOL
    tool_type = PICKAXE
    max_stack_size = 1
    id = 285
    name = "Golden Pickaxe"

wood_axe = WoodAxe()
stone_axe = StoneAxe()
iron_axe = IronAxe()
diamond_axe = DiamondAxe()
golden_axe = GoldenAxe()
wood_pickaxe = WoodPickaxe()
stone_pickaxe = StonePickaxe()
iron_pickaxe = IronPickaxe()
diamond_pickaxe = DiamondPickaxe()
golden_pickaxe = GoldenPickaxe()
import random


class Ship:
    def __init__(self, ship_id, position):
        self.ship_id = ship_id
        self.position = position


class OffensiveCraft(Ship):
    def __init__(self, ship_id, position, cannons):
        super().__init__(ship_id, position)
        self.cannons = cannons
        self.shields_up = False

    def attack(self):
        # Perform attack logic here
        pass

    def raise_shields(self):
        self.shields_up = True


class SupportCraft(Ship):
    def __init__(self, ship_id, position, support_type):
        super().__init__(ship_id, position)
        self.support_type = support_type

    def perform_support_task(self):
        # Perform support task logic here
        pass


class CommandShip(OffensiveCraft):
    def __init__(self, ship_id, position, cannons):
        super().__init__(ship_id, position, cannons)


class Fleet:
    def __init__(self):
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def generate_random_positions(self, size, num_ships):
        positions = set()
        while len(positions) < num_ships:
            x = random.randint(0, size)
            y = random.randint(0, size)
            positions.add((x, y))
        return list(positions)

    def pair_support_with_offensive(self):
        support_ships = [ship for ship in self.ships if isinstance(ship, SupportCraft)]
        offensive_ships = [ship for ship in self.ships if isinstance(ship, OffensiveCraft)]

        random.shuffle(support_ships)
        random.shuffle(offensive_ships)

        num_pairs = min(len(support_ships), len(offensive_ships))
        pairs = []

        for i in range(num_pairs):
            pair = (support_ships[i], offensive_ships[i])
            pairs.append(pair)

        return pairs


# Usage example:
fleet = Fleet()

# Generate 50 ships with random positions
ship_positions = fleet.generate_random_positions(100, 50)

for i in range(50):
    if i == 0:
        ship = CommandShip(i, ship_positions[i], cannons=24)
    elif i % 2 == 0:
        ship = OffensiveCraft(i, ship_positions[i], cannons=12)
    else:
        ship = SupportCraft(i, ship_positions[i], support_type="refueling")

    fleet.add_ship(ship)

# Pair support ships with offensive ships
pairs = fleet.pair_support_with_offensive()

# Print ship pairs
for pair in pairs:
    print(f"Support Ship {pair[0].ship_id} paired with Offensive Ship {pair[1].ship_id}")
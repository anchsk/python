class House:
    """ 

    """
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost


house = House()
print(House.num_rooms)  # 5
print(house.num_rooms)  # 5

House.num_rooms = 7

print(House.num_rooms)  # 7
print(house.num_rooms)  # 7

house.num_rooms = 9

print(House.num_rooms)  # 7
print(house.num_rooms)  # 9

print(House.cost_evaluation(8))
print(house.cost_evaluation(6))

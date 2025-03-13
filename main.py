# Architecture Simulation - Initial Implementation
class Building:
    def __init__(self, name, height, floors):
        self.name = name
        self.height = height
        self.floors = floors

    def display_info(self):
        print(f"Building Name: {self.name}, Height: {self.height}m, Floors: {self.floors}")

# Main function
def main():
    building = Building("Eco Tower", 120, 30)
    building.display_info()

if __name__ == "__main__":
    main()

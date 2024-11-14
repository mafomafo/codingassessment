import dockingBays as db

# Function to print docking bays information


def print_docking_bays():
    print("Docking Bays:")
    for bay in db.docking_bays:
        print(
            f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information


def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in db.incoming_ships:
        print(
            f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")


# Main function
def main():
    print_docking_bays()
    print_incoming_ships()
    available()

    # TODO: Implement the docking scheduler logic here
    # Levels 1 to 4 and the bonus can be implemented below

# db.docking_bays[]['schedule'][0]                 Arrive
# db.print_docking_bays[]['schedule'][1]                 Depart
# f"{num%24}:00"                    Time formatter
# db.incoming_ships[]['arrival_time']
# db.incoming_ships[]['departure_time']


def available(ship_ind):
    total_time = 0
    check = false
    for ind, bay in db.docking_bays:
        if check:
            break
        for ship in db.incoming_ships:
            if bay['schedule'] == [] and bay['size'] == ship['size']:
                db.docking_bays[ind]['schedule'].append(ship['arrival_time'],ship[departure_time], f"taken by {ship['ship_name']}")
                check = true
                break
            for bay2 in db.docking_bays:
                total_time = 
                if 


if __name__ == "__main__":
    main()

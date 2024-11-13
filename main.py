import dockingBays as db

# Function to print docking bays information
def print_docking_bays():
    print("Docking Bays:")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information
def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in db.incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")


        

    
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


def find_slot():
    temp_sizes = []
    for i, bay in enumerate(db.docking_bays):
        if bay['size'] not in temp_sizes:
            temp_sizes.append(bay['size'])
    temp_ship_sched = []
    for ind, bay in enumerate(db.incoming_ships):
        temp_ship_sched.append((bay['arrival_time'], bay['departure_time'], 'taken'))
    temp_bay_sched = []
    for ind, bay in enumerate(db.docking_bays):
        for i, sched in enumerate(bay['schedule']):
            temp_bay_sched.append(sched)
        temp_bay_sched.append(())
    arr = ""
    dep = ""
    temp_bay = db.docking_bays
    temp_ship = db.incoming_ships
    ship_ind_ref = 0
    time_occupied = 0
    for i, bay in enumerate(temp_bay):
        for j, ship in enumerate(temp_ship):
            time_occupied = abs(int(bay['schedule'][0][0:2]) - int(bay['schedule'][1][0:2]))
            

    
        




if __name__ == "__main__":
    main()


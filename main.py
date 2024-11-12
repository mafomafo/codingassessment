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
    for time in range(10,18):
        scheduler(time, db.docking_bays, db.incoming_ships)
    print_docking_bays()
    print_incoming_ships()
    
    # TODO: Implement the docking scheduler logic here
    # Levels 1 to 4 and the bonus can be implemented below

# dock_bay[]['schedule'][0]                 Arrive
# dock_bay[]['schedule'][1]                 Depart
# f"{num%24}:00"                    Time formatter
# inc_ships[]['arrival_time']
# inc_ships[]['departure_time']
def slot_filler(time, ind):
        if db.docking_bays[ind]["schedule"] == []:
            for i in range (len(db.incoming_ships)):
                if db.incoming_ships[i]['arrival_time'] == time:
                    db.docking_bays[ind]['schedule'] = [(db.incoming_ships[i]['arrival_time'], db.incoming_ships[i]['departure_time'], "taken")]
                    print(f"Bay {db.docking_bays[ind]['bay_id']} is taken.")
                    break
def available(time, ind):
    temp = []
    if not(db.docking_bays[ind]["schedule"] == []):
        for ele in db.docking_bays[ind]["schedule"]:
            temp.append(ele)
    for ele in temp:
        if int(ele[0][0:2]) >= time and int(ele[1][0:2]) <= time:
            
    
def scheduler(time, dock_bay, inc_ships):
    for i in range (len(db.docking_bays)):
        slot_filler(time, i)


if __name__ == "__main__":
    main()


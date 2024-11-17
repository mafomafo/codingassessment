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
    print(available(0))

    # TODO: Implement the docking scheduler logic here
    # Levels 1 to 4 and the bonus can be implemented below

# db.docking_bays[]['schedule'][0]                 Arrive
# db.docking_bays[]['schedule'][1]                 Depart
# f"{num%24}:00"                    Time formatter
# db.incoming_ships[]['arrival_time']
# db.incoming_ships[]['departure_time']


def available(ship_ind):
    temp = []
    start = 0
    end = 0
    total_time = 0
    start_s = int(db.incoming_ships[ship_ind]['arrival_time'][0:2])
    end_s = int(db.incoming_ships[ship_ind]['departure_time'][0:2])
    total_time_s = abs(start_s - end_s)
    ind_to_insert = 0
    for bay in db.docking_bays:
        if not(bay['size'] == db.incoming_ships[ship_ind]['size']):
            continue
        if bay['schedule'] == []:
            bay['schedule'].append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}"))
            temp.append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}"))
            return f"Bay {bay['bay_id']} is taken by {db.incoming_ships[ship_ind]['ship_name']} during the time of {db.incoming_ships[ship_ind]['arrival_time']} and {db.incoming_ships[ship_ind]['departure_time']}."
        start = int(bay['schedule'][0][0][0:2])
        end = int(bay['schedule'][0][1][0:2])
        total_time = abs(start - end)
        if len(bay['schedule']) == 1:
            if abs(10 + total_time_s) <= start:
                bay['schedule'].insert(0, (db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}"))
                temp.append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}"))
                break
            if end <= abs(18 - total_time_s):
                bay['schedule'].append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}"))
                temp.append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}"))
                break
    return f"Bay {bay['bay_id']} is taken by {db.incoming_ships[ship_ind]['ship_name']} during the time of {db.incoming_ships[ship_ind]['arrival_time']} and {db.incoming_ships[ship_ind]['departure_time']}."
if __name__ == "__main__":
    main()

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
    start_s = int(db.incoming_ships[ship_ind]['arrival_time'][0:2])
    end_s = int(db.incoming_ships[ship_ind]['departure_time'][0:2])
    total_time_s = abs(start_s - end_s)
    for ind, bay in enumerate(db.docking_bays):
        if not(bay['size'] == db.incoming_ships[ship_ind]['size']):
            continue
        if bay['schedule'] == []:
            bay['schedule'].append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}"))
            temp.append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}", bay['bay_id'] + 1))
            break
        start = int(bay['schedule'][0][0][0:2])
        end = int(bay['schedule'][0][1][0:2])
        if len(bay['schedule']) == 1:
            if abs(10 + total_time_s) <= start:
                bay['schedule'].insert(0, (db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}"))
                temp.append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}", bay['bay_id'] + 1))
                break
            if end <= abs(18 - total_time_s):
                bay['schedule'].append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}"))
                temp.append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}", bay['bay_id'] + 1))
                break
        sched_len = 0
        sched_ind_ahead = 1
        check = True
        if len(bay['schedule']) >= 2:
            while sched_ind_ahead < len(bay['schedule']):
                start = int(bay['schedule'][sched_len][0][0:2])
                end = int(bay['schedule'][sched_len][1][0:2])
                start_ahead = int(bay['schedule'][sched_ind_ahead][0][0:2])
                end_ahaed = int(bay['schedule'][sched_ind_ahead][1][0:2])
                total_time_ahead = abs(start_ahead - end)
                if abs(start - 10) >= total_time_s and check:
                    check = False
                    bay['schedule'].insert(sched_len, (db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}"))
                    temp.append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}", bay['bay_id'] + 1))
                    break
                if total_time_ahead >= total_time_s:
                    bay['schedule'].insert(sched_len, (db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}"))
                    temp.append((db.incoming_ships[ship_ind]['arrival_time'], db.incoming_ships[ship_ind]['departure_time'], f"Taken by {db.incoming_ships[ship_ind]['ship_name']}", bay['bay_id'] + 1))
                    break
    return f"Bay {temp[0][3]} is taken by {temp[0][2]} during the time of {temp[0][0]} and {temp[0][1]}."
if __name__ == "__main__":
    main()

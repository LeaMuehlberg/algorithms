states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) # set = menge
stations = {}
stations["reins"] = set(["id", "nv", "ut"])
stations["rzwei"] = set(["wa", "id", "mt"])
stations["rdrei"] = set(["or", "nv", "ca"])
stations["rvier"] = set(["nv", "ut"])
stations["rfünf"] = set(["ca", "az"])
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states # vereinigungsmenge
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered
    
print(final_stations)
def autonomous_driving_agent(distance_metres,traffic_light):
    if distance_metres<5:
        return "Emergence Brake!"
    elif traffic_light=="Yellow":
        return "Slow down and prepare to stop"
    elif traffic_light=="Red":
        return "Stop"
    elif traffic_light==" Green" and distance_metres>=15:
        return "Drive Forware"
    else:
        return "Drive slowly"
print(autonomous_driving_agent(3,"Yellow"))
print(autonomous_driving_agent(10,"Green"))
print(autonomous_driving_agent(20,"Red"))

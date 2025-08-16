def make_driving_decision(distance_to_obstacle_meters, braking_threshold_meters=50):
    """
    A simple AI agent that decides whether to brake based on distance to an obstacle.
    """
    print(f"Current distance to obstacle: {distance_to_obstacle_meters} meters")
    if distance_to_obstacle_meters < braking_threshold_meters:
        return "BRAKE"
    else:
        return "CONTINUE"

# Simulate various sensor readings (mock data)
print(f"Decision for 100m: {make_driving_decision(100)}")
print(f"Decision for 60m: {make_driving_decision(60)}")
print(f"Decision for 40m: {make_driving_decision(40)}")
print(f"Decision for 10m: {make_driving_decision(10)}")
"""
    The ball usually pitches at a distance of 
        about 1 feet to 33 feet from the batsman
    A distance of 18 feet from the batsman is considered at the Best point

    A delivery is considered a Short Length delivery, 
        If Ball pitches more than 6 feet from the Best point towards bowler

    A delivery is considered a Good Length delivery, 
        If Ball pitches within 6 feet on either side of the Best point

    A delivery is considered a Full Length delivery, 
        If Ball pitches more than 6 feet from the Best point towards batsman

    33-----------------|----------18-----------|-----------------1
    -------------------|-----------|-----------|-----------------|
                       |          Best         |              Batsman
       Short Length -->|<--   Good Length   -->|<-- Full Length

    Given the distance from the batsman that the ball pitches, 
    find out the type of delivery bowled by the bowler.
"""

table = {
        -1 : "Full Length",
         0 : "Good Length",
         1 : "Short Length",
       }

def validate(actual, best):
    span = 6
    if actual > best - span or actual < best + span:
        return 0
    elif actual =< best - span:
        return 1
    elif actual => best + span:
        return -1

def delivery_type(lgt):
    mid_point = 18
    return table[validate(lgt, mid_point)]

# Main
print(delivery_type(1)) # Should print Full Length

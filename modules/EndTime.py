import math

# Define constants
bowlWidth = 26
flatBottom = 0.4  # Height of the removed segment
volume_tolerance = 0.5 # seems to correlate to 7~14 steps

R = bowlWidth / 2
effective_R = R - flatBottom  # Adjusted radius due to flat bottom

def segment_volume(h):
    """Calculate volume of a spherical segment with a flat bottom."""
    return math.pi * h**2 * (effective_R - (h / 3))

def find_new_height(target_v):
    """Solve for new segment height h using numerical methods."""
    max_h = effective_R
    max_v = segment_volume(max_h)
    guess = max_h/2
    error = max_h/2
    #print(f"\ttarget: {target_v}, tolerance: {volume_tolerance} cm³")
    steps = 0
    while True:
        steps += 1
        v = segment_volume(guess)
        d = target_v-v
        #print(f"\tguess={guess} +/- {error}, v={v}, d={d}")
        if d > volume_tolerance:
            #print("\t\tlow guess, trying higher")
            error /= 2
            guess += error
        elif d < -volume_tolerance:
            #print("\t\thigh guess, trying lower")
            error /= 2
            guess -= error
        else:
            #print("\t\twithin tolerance")
            break
    #print(f"\t(steps: {steps})");
    return guess

def test_height():
    scale = segment_volume(effective_R)/255
    for i in range(256):
        h = find_new_height(i*scale)
        print(f"{i*scale} -> {h}\n{segment_volume(h)}")
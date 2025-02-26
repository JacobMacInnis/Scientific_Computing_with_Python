import copy
import random

class Hat:
    def __init__(self, **kwargs):
        """Initialize the Hat with a dictionary of colors and their counts."""
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)  # Create a list with multiple instances of each color

    def draw(self, num_balls):
        """Draws num_balls randomly from the hat without replacement."""
        if num_balls >= len(self.contents):  # If requested more than available, return all balls
            return_value =  self.contents[:]
            self.contents = []
            return return_value 
        
        drawn_balls = random.sample(self.contents, num_balls)  # Randomly pick without replacement
        for ball in drawn_balls:
            self.contents.remove(ball)  # Remove drawn balls from the hat
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Performs the probability experiment by running num_experiments trials."""
    success_count = 0  # Count of successful experiments

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)  # Create a fresh copy of the hat for each experiment
        drawn_balls = hat_copy.draw(num_balls_drawn)  # Draw balls from the copied hat

        # Count occurrences of drawn balls
        drawn_counts = {color: drawn_balls.count(color) for color in set(drawn_balls)}

        # Check if the drawn balls satisfy the expected condition
        success = all(drawn_counts.get(color, 0) >= count for color, count in expected_balls.items())

        if success:
            success_count += 1

    return success_count / num_experiments  # Calculate probability

# ✅ Example Usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={'red': 2, 'green': 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print(probability)  # Output: Approx. 0.356 (varies with random draws)

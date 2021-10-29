import random
import copy


class Hat:
    def __init__(self, **kwargs):
        self.items = kwargs
        self.contents = []
        for ball, number in self.items.items():
            for i in range(number):
                self.contents.append(ball)


    def draw(self, times_drawn):
        drawed_balls = []
        if times_drawn <= len(self.contents):
            for i in range(times_drawn):
                random_index= random.randint(0, len(self.contents)-1)
                drawed_balls.append(self.contents[random_index])
                self.contents.pop(random_index)
        else: return self.contents
        return drawed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    ball_drawn = num_balls_drawn
    expect = 0

    for i in range(num_experiments):
        hats = copy.deepcopy(hat)
        expected= copy.deepcopy(expected_balls)
        ans = hats.draw(ball_drawn)
        for color in ans:
            if color in expected_balls:
                expected[color] -= 1
        
        if (all(value <= 0 for value in expected.values())):
            expect += 1
        else: pass

    return expect /num_experiments
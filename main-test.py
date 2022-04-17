# Import the min_cost function, and assert that it works correctly.
from main import min_cost

def test_min_cost():
    cost = [[10, 20, 30, 40],
            [60, 50, 20, 80],
            [20, 20, 20, 20],
            [60, 50, 20, 80]]
    m = len(cost)
    n = len(cost[0])
    min_cost_path = min_cost(cost, m-1, n-1)
    assert (1000 - min(min_cost_path[n-1])) == 920
    print("min_cost Function works correctly")

if __name__ == '__main__':
        test_min_cost()

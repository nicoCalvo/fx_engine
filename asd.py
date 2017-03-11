from simpleai.search import SearchProblem, astar


GOAL = 'HELLO WORLD'

class HelloProblem(SearchProblem):
    def actions(self, state):
        if len(state) < len(GOAL):
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        # how far are we from the goal?
        wrong = sum([1 if state[i] != GOAL[i] else 0
                    for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing


def initialize(context):
    context.i = 4
    context.days = 0
    context.months = 0
    context.problem = HelloProblem(initial_state='')


def handle_data(context, data):
    pass


def before_new_day(context, data):
    context.days += 1
    result = astar(problem)
    f = open('resultado.log','w')
    f.write(result.state)
    f.write('      ')
    f.write(str(result.path()))
    f.close()

def before_new_month(context, data):
    context.months += 1

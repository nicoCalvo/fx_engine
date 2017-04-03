from string import Template
# import json
import yaml

class TemplateStrategy(object):

    def __init__(self, strategy, simulation_type):
        self.strategy = strategy
        self.simulation_type = simulation_type

    def build_strategy(self):
        template = Template('$logger$ordermanager$simulationdate$strategy')
        return template.substitute(self.__get_imports())

    def __get_imports(self):
        fname = './fxEngine/strategy/' + self.simulation_type + '_imports.yaml'
        with open(fname) as file:
            imports = yaml.load(file)
        imports['strategy'] = self.strategy
        return imports

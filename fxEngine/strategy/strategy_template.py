from string import Template
# import json
import yaml

class TemplateStrategy(object):

    def __init__(self, strategy, simulation_type, _id):
        self.strategy = strategy
        self.simulation_type = simulation_type
        self._id = _id

    def build_strategy(self):
        template = Template('$logger$ordermanager$simulationdate$strategy')
        return template.substitute(self.__get_imports())

    def __get_imports(self):
        fname = './fxEngine/strategy/' + self.simulation_type + '_imports.yaml'
        with open(fname) as file:
            imports = yaml.load(file)
        imports['strategy'] = self.strategy
        imports['logger'] = imports['logger'].format(id=self._id)
        imports['ordermanager'] = imports['ordermanager'].format(id=self._id)
        return imports

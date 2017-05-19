#
# Copyright 2017 Atakama
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from fxEngine.trading_simulator import TradingSimulator
from fxEngine.tests.helper import RandomStrategy

import pdb
pdb.set_trace()
dto_strategy = RandomStrategy.get_strategy('current')

'''
Attach to rabbit Q listening for incoming strategies,
get payload and instantiate new TradingSimulator and then run it

'''
trading_simulator = TradingSimulator(dto_strategy)
trading_simulator.run_simulation('limited')


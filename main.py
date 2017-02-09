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
from data.data_portal import DataPortal
from trading.trading_simulator import TradingSimulator
import sys
import json



j_strategy = json.loads(sys.argv[1])

symbols = j_strategy.get('pairs')
trading_simulator = TradingSimulator(str_strategy, symbols, id_strategy)


## MAIN SIMULATION PROOF





dp = DataPortal()

dp.ingest()
dp.get_slice('bol_yen', 30)




Feature: The Data Portal plays the role of access point to
current and history data to be consumed by a strategy


#Scenario: The ingest process is done correctly #
	#Given a data portal
	#When we ingest the history
	#And we ingest backtest data
	#We see a bunch of crap

Scenario: The current data is returned for a currency pair
	Given a data with ['EURUSD','ARSMEX'] pairs
	And we ingest the history
	And we ask for current tick with pair EURUSD and value ask
	Then we see a single float value


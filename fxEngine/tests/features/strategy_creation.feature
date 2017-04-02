Feature: This feature aims to demonstrate how to create a strategy
with different values and validate  its expected response on each
scenario...

Scenario: Loading a strategy with an invalid pair
	Given a "current" strategy
	And we set -1 as capital base
	When we run it
	Then we see a InvalidCapitalBase exception
	And "Initial capital must be > 0" message


Scenario: Loading a strategy with invalid script
	Given a "invalid script" strategy
	When we run it
	Then we see a CompileMethodException exception
	And the message is like "Unable to compile code: invalid syntax"


Scenario: Loading a strategy with scheduled functions
	Given a "scheduled" strategy
	When we run it
	Then we find there are daily and monthly scheduled functions

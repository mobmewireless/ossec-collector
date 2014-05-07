Feature: OSSEC logs collector
  Scenario: Calling collect method
      Given collect method is called
       Then returns all alerts

  Scenario: OSSEC isn't installed
      Given collect method is called for non-existent log file
       Then returns entry indicating absence of log file
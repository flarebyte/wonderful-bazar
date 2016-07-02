Feature: Limit the learning curve for the front end development
  In order to limit the cost of new developers joining the company
  As a developer
  I want to limit the knowledges needed to do development work
  So that even a junior developer can learn the job quickly

  Scenario: Limit the learning curve
    Given that I explore all the projects
    When I take into account everything in the front-end projects
    Then I should be confident that it will take less than "5" weeks to learn

  Scenario: The front end should be written in JavaScript or CoffeeScript
    Given that I explore all the projects
    When I check any front-end project
    Then I should only see JavaScript or CoffeeScript

  Scenario: Limit the number of domain specific languages
    Given that I explore all the projects
    When I take into account all the "DSL" in the front-end projects
    Then I should be confident that it will take less than "2" weeks to learn

  Scenario: Limit the number of concepts
    Given that I explore all the projects
    When I take into account all the "concepts" in the front-end projects
    Then I should be confident that it will take less than "1" weeks to learn

  Scenario: Limit the number of public libraries
    Given that I explore all the projects
    When I take into account all the "public libraries" in the front-end projects
    Then I should be confident that it will take less than "2" weeks to learn
    
  Scenario: Limit the number of private libraries
    Given that I explore all the projects
    When I take into account all the "private libraries" in the front-end projects
    Then I should be confident that it will take less than "2" weeks to learn


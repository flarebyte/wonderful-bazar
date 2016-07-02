Feature: {{Verb}} a {{domain}}
  In order to improve {{quality}}
  As a {{role}} with the permission {{permission}}
  I want to {{verb}} a {{domain}}
  So that {{objective}}

  Scenario: {{Verb}} a {{domain}}
    Given that I am logged as "{{role}}" with the permission "{{permission}}"
    When I choose to {{verb}} this "{{domain}}"
    Then the application should display the "{{draft}}" page for this "{{domain}}"

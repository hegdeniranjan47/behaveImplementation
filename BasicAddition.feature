Feature:Basic features
  The basic addition of two integers is tested

  Scenario Outline: Valid inputs
    Given specified <op>
    When inputs <l> and <m> are passed
    Then output is <n>

    Examples:
      | l | m | n     | op |
      | 4 | 5 | 9     | +    |
      | 6 | 0 | 6     | -    |
      | 1 | 1 | 1     | *    |
      | 5 | 2 | 2     | /    |
      | 6 | 0 | 0     | /    |
      | 6 | 2 | 0     | %    |
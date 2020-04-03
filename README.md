# IN104-2020


## Rappels : la PEP-8

PEP 8 (https://www.python.org/dev/peps/pep-0008/) conventions are followed. In short:


------------ | -------------
classes      |  UpperCamelCase
functions    |  lower_case_with_underscores()
attributes   |  lower_case_with_underscores
@properties  |  lower_case_with_underscores; should have no side-effect, and no (or cheap) computation
constants    |  ALL_CAPS (although avoiding global constants is a much better idea)
indentation  |  use 4 spaces per indentation level (no tabs).


Run periodically /usr/bin/pep8 to check if your code is correct (or activate "pep-8 validation" in your editor).

To avoid encoding problems (windows <-> Linux <-> Mac), use only pure ASCII (no accents).


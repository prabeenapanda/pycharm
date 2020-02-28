*** Test Cases ***
tc1
    [Documentation]    my 1st test case
    log    welcome
    log    to my
    log    first test case

tc2
    ${a}    10
    ${b}    20
    ${c}    ${a}+${b}
    log    ${c}

*** Settings ***
Library       OperatingSystem

*** Variables ***
${expression}=  ${EMPTY}

*** Test Cases ***
My Test
    Push button  4
    Push button  +
    Push button  6
    Result should be  10

My Test2
    Push button  5
    Push button  +
    Push button  6
    Result should be  11

*** Keywords ***
Push button
    [Arguments]   ${var1}
    ${expression}=  Catenate  ${expression}${var1}
    Set test variable  ${expression}

Result should be
    [Arguments]  ${expected_val}
    ${result}=   Evaluate  ${expression}
    ${flag}=  Evaluate  ${expected_val}==${result}
    Should Be True  ${flag}
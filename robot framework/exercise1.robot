*** Settings ***
Library       OperatingSystem

*** Variables ***
${VAR1}    AAAAA
${VAR2}    BBBBB
${VAR3}    AAAAB

*** Test Cases ***
Strings equals Test
    Should Be Equal As Strings   ${VAR1}    AAAAA
    Should Be Equal As Strings   ${VAR2}    BBBBB
    Should Not Be Equal As Strings   ${VAR3}    AAAAA

Random int Test
    ${random}=   Evaluate  random.randint(0, 10)  sys,random
    Log  ${inputvar}
    ${inputint}=  Convert To Integer  ${inputvar}
    Should Be Equal As Integers  ${random}  ${inputint}

Current date Test
    @{time} =  Get Time    year month day
    Should Be Equal As Integers  ${time[0]}  2018  #year test
    Should Be Equal As Integers  ${time[1]}  02    #month test
    Should Be Equal As Integers  ${time[2]}  02    #day test

*** Keywords ***
My Keyword
    [Arguments]    ${path}
    Directory Should Exist    ${path}
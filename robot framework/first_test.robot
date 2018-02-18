*** Settings ***
Documentation    Suite description

*** Variables ***
${scalar}=  jakis string
@{lista} =  jeden   2   4   4   siedem
&{slownik}=  klucz=wartosc  imie=Jacek

*** Test Cases ***
Pierwszy Test case
    Log  ${lista}
    Log  ${lista[0]}
    Log  &{slownik}[imie]
    ${zmienna}=  Set variable  jakas wartosc
    Log  ${MARKA}
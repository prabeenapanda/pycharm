*** Settings ***
#Library  SeleniumLibrary
Library  ../robo.py

*** Test Cases ***
Robot fetch data
    Create folder
    #Concat name

*** Keywords ***
Create folder
   #[Arguments] ${sub}
   create
  # createe ${sub}

#Concat name
#   [Arguments] ${name} ${sur}
#   ${result} = concate ${name} ${sur}
#   log ${result}



# WileyQATechnicalTest
Repository for the QA Assessment in Wiley.

## Requirements
- Python 3.9.0b3;
- Chromedriver;
- Selenium;
- unittest;

## The scenario:
**Feature:** Login  
  
**Scenario:** Login at TeamSHIFT  
  
 **Given** I am on the https://teamshift-qa.crossknowledge.com/ page  
 **And** I have a valid login  
 **When** I click the Enter button;  
 **And** I type "allan@sklarow.blog.br" in the email field  
 **And** I click the Next button;  
 **And** I type "Testing123" in the password field  
 **And** I press the "Submit" button  
 **And** I see "Allan Sklarow" on the main page  
  
## The approach:
I could used RobotFramework to do this, but I made a very simple code using Python and the POM pattern, that I think is more suitable for the assessment!  
- The **locators** are at Resources/Locators
- The **Test Data** (login, URL, etc) are at Resoures/TestData
- For simplicity, I put all the 3 **Page Objects** in one file Resources/PO/Pages

## To-do / improvements
- Logs
- Separate the Pages in one file for each page

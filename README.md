# EnrollmentAutomation

This script was created to check user information on a data file  ".XLSX" from a Human Resources Department and use this information to synchronize user credentials for  Active Directory. Once there is a new user on the HR sheet, this new user will be created, once the user is deleted from the sheet, it will be also deleted on the AD System. The script runs every 5 minutes.
The basic code uses only 3 fields from the whole sheet in order to create the login on AD. As follow below

UserName,
Email,
CPF,

Password - the first password is made up using the social security field (CPF)  

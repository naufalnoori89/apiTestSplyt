# Splyt QA Test

This pythons script is to automate Spylt API testing: https://qa-interview-test.splytech.dev/api
This script is tested using Python 3.8 and above.

## Script Setup

1. Please run the requirement.txt for neccesary python libraries.
2. Run the main python script "python apiTester.py"
3. The list of test cases are available in ./template/qaApi.csv
4. Adjust the key parameters in the csv file to run the intended test cased:
   1. column 1: testId (mandatory: Please follow the sequence for easy tracking)
   2.  column 2: testName (mandatory: Please follow the sequence for easy tracking)
   3. column 3: testDescription (mandatory: Explain in details what is the test case about)
   4. column 4: pickup (mandatory: Insert Y or N ONLY)
   5. column 5: latitude (Optiional)
   6. column 6: longitude (Optiional)
   7. column 7: passenger (mandatory: Insert Y or N ONLY)
   8. column 8: name (Optiional)
   9. column 9: surname (Optiional)
   10. column 10: phone_number (Optiional)
   11. column 11: departure_date (Optiional)

5. The test results are recorded in ./log directory. The test logs are generated based on the time the test was run.


## OUTPUT RESULT

From the the script, test_10 seems to be a bug when passenger.phone_number is not listed in body json.

1. BUG: Record is saved even though mandatory key is not provided (phone_number).
2. STEP TO REPRODUCE: Dont include key and params for phone number in json body
3. OUTCOME: record_id is generated eventhough record is not stored. GET record API failed to generate response:
         
         
         {
         "name": "ApiError",
         "code": "INTERNAL_SERVER_ERROR"
         }

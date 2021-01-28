# Test

Correct behavior of the Integration for each Log Level:

- Error

  - Integration Log contains 3 records

- Warning

  - Integration Log contains 6 records

- Info

  - Integration Log contains 9 records 

- Debug

  - Integration Log contains 12 records

Read From STDOUT

  - +3 records if Read From STDOUT is enabled

**For example**:

If Log Level is Debug and Read From STDOUT is enabled then there will be 15 records in the Integration Log

## Automated testing

You can use a Rule from the components.xml to automaticly test this Integration.

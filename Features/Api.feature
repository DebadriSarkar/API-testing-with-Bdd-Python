Feature: API Automation


  @TEST_REGISTRATION_SUCCESS
  Scenario: Successfull Member Registration
    When : We call "POST" method for Member Registration with endpoint "member"
       | MemberName     | MemberEmail                 | MemberMobile | Password     | ConfirmPassword | Gender |
       | Debadri Sarkar | debadrisarkar2017@gmail.com | 8697672001   | ^&85Fhg?)(&^ | ^&85Fhg?)(&^    | M      |
    Then : Member verifies the status code is "200"
    And : Member verifies POST response body contains following information
      | Status| Message                 |
      | 1     | Successfully Registered |


  @TEST_REGISTRATION_FAILURE
  Scenario: Failure Member Registration
    When : We call "POST" method for Member Registration with endpoint "member"
       | MemberName     | MemberEmail                 | MemberMobile | Password     | ConfirmPassword | Gender |
       | Debadri Sarkar | debadrisarkar2017@gmail.com | 8697672001   | ^&85Fhg?)(&^ | ^&85Fhg?)(&1    | M      |
    Then : Member verifies the status code is "200"
    And : Member verifies POST response body contains following information
      | Status| Message                                    |
      | 0     | Password and confirm password are not same |


  @TEST_UPDATE_SUCCESS
  Scenario: Member updated successfully
    When : We call "PUT" method for Member Update with endpoint "memberupdate/?memberid=35"
       | MemberName     | MemberEmail                      | MemberMobile | Password       | Gender |
       | Debadri Sarkar | debadrisarkar2017@rediffmail.com | 8697672001   | ^&85Fhg?)(&^   | M      |
    Then : Member verifies the status code is "200"
    And : Member verifies PUT response body contains following information
      | Status| Message              |
      | 1     | Updated successfully |


  @TEST_UPDATE_FAILURE
  Scenario: Member not exist
    When : We call "PUT" method for Member Update with endpoint "memberupdate/?memberid=6"
       | MemberName     | MemberEmail                      | MemberMobile | Password       | Gender |
       | Debadri Sarkar | debadrisarkar2017@rediffmail.com | 8697672001   | ^&85Fhg?)(&^   | M      |
    Then : Member verifies the status code is "404"
    And : Member verifies PUT response body contains following information
      | Status| Message                                      |
      | 0     | Wrong Credentials or Member does not exist!! |


  @TEST_FIND_ALL_MEMBER_SUCCESS
  Scenario: We can see the all members
    When : We call "GET" method for see all members with endpoint "memberall"
    Then : Member verifies the status code is "200"
    And : Member verifies GET response body contains following information
      | Status| Message |
      | 1     | Success |

  @TEST_FIND_ALL_MEMBER_FAILURE
  Scenario: We can see the empty list
    When : We call "GET" method for see all members with endpoint "memberall"
    Then : Member verifies the status code is "200"
    And : Member verifies GET response body contains following information
      | Status| Message    |
      | 0     | Empty List |

  @TEST_DELETE_MEMBER_BY_ID_SUCCESS
  Scenario: We can delete member by id
    When : We call "DELETE" method for delete a member by id with endpoint "memberdelete/35"
    Then : Member verifies the status code is "200"
    And : Member verifies DELETE response body contains following information
      | Status| Message              |
      | 1     | Deleted Successfully |

  @TEST_DELETE_MEMBER_BY_ID_FAILURE
  Scenario: We can't delete member by id
    When : We call "DELETE" method for delete a member by id with endpoint "memberdelete/29"
    Then : Member verifies the status code is "404"
    And : Member verifies DELETE response body contains following information
      | Status| Message                                      |
      | 0     | Wrong Credentials or Member does not exist!! |
Feature: google task

    Scenario: open the Google task application
        Given veryfy_next batton
        When click on npr_allow_button
        And click on permission_deny_button



    Scenario: Create a New Task
        When I Create new task
        When I Create new task tittle
        When I click details on task
        And I click add_task_details on task
        And I add date/time on task
        And I add dtp_time_label
        And I add material_timepicker_ok_button
        And I save the task

    Scenario: View Task List
        When Log in with valid credentials if not already logged in

    Scenario: edit Task
        When Select the task
        When Edit the task Tittel
        When goto back

    Scenario: Add Subtasks to Task
        When Select the task
        And I add subtasks to a task
        And I add subtasks tittel task
        And goto back

    Scenario: Mark Task as Complete task
        When Select the task
        And I click mark complate

    Scenario: UnMark Task as Complete and mark with chackmarks
        When I click view complate task
        And I click unmark complate task
    

    Scenario:  Sort Tasks
         When Log in with valid credentials if not already logged in
         And I find the sort options
         And I click on Date options

    Scenario:  Delete Completed task
        When I click view complate task
        Then I select more options
        And I click on Delete all complated tasks
        And I click on Delete

    Scenario: DELETE Task all task
        When Select the task
        And Go to more options
        And Click on delete

    Scenario:  New list
         When I FOUND the NEW LIST options
         And I enter tittel for new list

    Scenario:  rename list
         When I select the list
         Then I select more options
         When I select rename option
         And I enter tittle

    Scenario:  Delete list
         When I select the list for delete
         Then I select more options
         When I select delete option
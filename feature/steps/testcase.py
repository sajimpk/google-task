from setting import *
import time
from behave import *
from selenium.webdriver.common.by import By
driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
time.sleep(3)
@Given(U'veryfy_next batton')
def veryfy_next(contex):
    if driver.find_element(By.XPATH,'//android.widget.ImageButton[@content-desc="Next page"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.ImageButton[@content-desc="Next page"]').click()
        time.sleep(3)
    else:
        assert False
@When(U'click on npr_allow_button')
def npr_allow_button(contex):
    if driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.google.android.apps.tasks:id/npr_allow_button"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.google.android.apps.tasks:id/npr_allow_button"]').click()
        time.sleep(3)
    else:
        assert False
@When(U'click on permission_deny_button')
def permission_deny_button(contex):
    if driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]').click()
        time.sleep(3)
    else:
        assert False

#sinario 2################################
@When(U'I Create new task')
def Create_new_task(context):
    if driver.find_element(By.XPATH,'//android.widget.ImageButton[@content-desc="Create new task"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.ImageButton[@content-desc="Create new task"]').click()
        time.sleep(5)
    else:
        assert False
@When(U'I Create new task tittle')
def Create_new_task(context):
        ele = driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/add_task_title"]')
        if ele:
            assert True
            ele.send_keys('task 1')
            time.sleep(1)
        else:
            assert False
@When(U'I click details on task')
def add_details(context):
    if driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Add details"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Add details"]').click()
        time.sleep(3)
    else:
        assert False

@When(U'I click add_task_details on task')
def add_task_details(context):
    if driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/add_task_details"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/add_task_details"]').send_keys('this is task 1')
        time.sleep(2)
    else:
        assert False
@when(U'I add date/time on task')
def add_date(context):
    if driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Set date/time"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Set date/time"]').click()
        time.sleep(3)
@when(U'I add dtp_time_label')
def dtp_time_label(context):
        if driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/dtp_time_label"]'):
            assert True
            driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/dtp_time_label"]').click()
            time.sleep(3)
        else:
            assert False
@when(U'I add material_timepicker_ok_button')
def material_timepicker_ok_button(context):
    if driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.google.android.apps.tasks:id/material_timepicker_ok_button"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.google.android.apps.tasks:id/material_timepicker_ok_button"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.google.android.apps.tasks:id/dtp_done"]').click()
        time.sleep(3)
@when(U'I save the task')
def save_task(context):
    if driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.google.android.apps.tasks:id/add_task_done"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.google.android.apps.tasks:id/add_task_done"]').click()
        time.sleep(3)
    else:
        assert False



#sinario 3 #################################
@when(U'Log in with valid credentials if not already logged in')
def chack_google(context):
    if driver.find_element(By.XPATH,'//android.widget.ImageView[@resource-id="com.google.android.apps.tasks:id/og_apd_internal_image_view"]'):
            assert True
            driver.find_element(By.XPATH,'//android.widget.ImageView[@resource-id="com.google.android.apps.tasks:id/og_apd_internal_image_view"]').click()
            time.sleep(3)
            driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="Close"]').click()
            time.sleep(3)
    else:
        assert False


#sinario 3 #################################
@when(U'Select the task')
def edit_task(context):
    try:
        driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/task_name"]').click()
        time.sleep(3)
    except:
        assert False

@when(U'Edit the task Tittel')
def edit1_task(context):
    try:
        if driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/edit_title"]'):
            assert True
            driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/edit_title"]').click()
            time.sleep(1)
        else:
            assert False
        if driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/edit_title"]'):
            assert True
            driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/edit_title"]').clear()
            time.sleep(1)
        else:
            assert False
        driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/edit_title"]').send_keys('Edited task')
        time.sleep(1)
    except:
        assert False
@when(U'goto back')
def edit_back(context):
    try:
        driver.find_element(By.XPATH,'//android.widget.ImageButton[@content-desc="Back"]').click()
        time.sleep(3)
    except:
        assert False
#sinario 4 #################################
@when(U'Go to more options')
def more_opt(context):
    try:
        if driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="More options"]'):
            driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="More options"]').click()
            time.sleep(3)
        else:
            assert False
    except:
        assert False

@when(U'Click on delete')
def delete_tsk(context):
    try:
        driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/title"]').click()
        time.sleep(3)
    except:
        assert False

#sinario 5 #################################

@when(U'I add subtasks to a task')
def sub_task(context):
    try:
        if driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/edit_subtasks_add_label"]'):
            assert True
            driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/edit_subtasks_add_label"]').click()
            time.sleep(3)
    except:
        assert False
@when(U'I add subtasks tittel task')
def sub_tittle(context):
    try:
        if driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/subtask_title"]'):
            assert True
            driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/subtask_title"]').click()
            time.sleep(3)
            driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/subtask_title"]').send_keys('this is sub task')
            time.sleep(3)
        else:
            assert False
    except:
        assert False

#sinario 6 #################################
@when(U'I click mark complate')
def mark_complate(context):
    driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.google.android.apps.tasks:id/edit_task_complete_button"]').click()
    time.sleep(3)
@when(U'I click view complate task')
def view_complate(context):
    if driver.find_element(By.XPATH,'//android.widget.ImageView[@resource-id="com.google.android.apps.tasks:id/expand"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.ImageView[@resource-id="com.google.android.apps.tasks:id/expand"]').click()
        time.sleep(3)
    else:
        assert False
@when(U'I click unmark complate task')
def unmark_complate(context):
    if driver.find_element(By.XPATH,'//android.view.View[@content-desc="Mark as not complete"]'):
        assert True
        driver.find_element(By.XPATH,'//android.view.View[@content-desc="Mark as not complete"]').click()
        time.sleep(5)
    else:
        assert False

@when(U'I select delete option')
def delete_list_opt(context):
    try:
        if driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/delete_list_option_title"]'):
            assert True
            driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/delete_list_option_title"]').click()
            time.sleep(3)
        else:
            assert False
    except:
        assert False


@Then(U'I click on Delete all complated tasks')
def delete_com_task(context):
    if driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/delete_all_completed_tasks_option"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/delete_all_completed_tasks_option"]').click()
        time.sleep(3)
    else:
        assert False
@Then(U'I click on Delete')
def delete_conf_task(context):
    try:
        driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="android:id/button1"]').click()
        time.sleep(3)
    except:
        assert False


#sinario 7 #################################
@when(U'I find the sort options')
def sort_opt(context):
    if driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Change sort order"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Change sort order"]').click()
        time.sleep(3)
    else:
        assert False
@when(U'I click on Date options')
def date_opt(context):
    try:
        driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/task_list_menu_item_text" and @text="Date"]').click()
        time.sleep(3)
    except:
        assert False
#sinario 9 ################################
@when(U'I FOUND the NEW LIST options')
def list_opt(context):
    try:    
        driver.find_element(By.XPATH,'//android.widget.TextView[@text="New list"]').click()
        time.sleep(2)
    except:
        assert False
   

@when(U'I enter tittel for new list')
def list_tittle(context):
    try:
        driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/edit_list_title"]').send_keys('list')
        time.sleep(3)
        driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/done_button"]').click()
        time.sleep(3)
    except:
        assert False

#sinario 10 ################################
@when(U'I select the list')
def rename1_list(context):
    try:
        driver.find_element(By.XPATH,'//android.widget.TextView[@text="list"]').click()
        time.sleep(3)
    except:
        assert False

@Then(U'I select more options')
def select_more_opt(context):
    try:
        driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="More options"]').click()
        time.sleep(3)
    except:
        assert False

@when(U'I select rename option')
def rename_opt(context):
    try:
        driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/rename_list_option"]').click()
        time.sleep(3)
    except:
        assert False
@when(U'I enter tittle')
def renamed_tittle(context):
    if driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/edit_list_title"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.tasks:id/edit_list_title"]').send_keys('list_edited')
        time.sleep(3)
    else:
        assert False
    if driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/done_button"]'):
        assert True
        driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.google.android.apps.tasks:id/done_button"]').click()
        time.sleep(3)
    else:
        assert False

@when(U'I select the list for delete')
def rename1_list(context):
    try:
        driver.find_element(By.XPATH,'//android.widget.TextView[@text="list_edited"]').click()
        time.sleep(3)
    except:
        assert False



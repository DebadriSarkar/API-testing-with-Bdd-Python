from behave import when, then, step

from Utility.API_Utility import API_Utility

api_utility = API_Utility()

@when(u': We call "{method}" method for Member Registration with endpoint "{endpoint}"')
def step_impl(context, method, endpoint):
    global response
    response = api_utility.Method_Call(context.table,method, endpoint)


@then(u': Member verifies the status code is "{status_code}"')
def step_impl(context, status_code):
    actual_status_code = response.status_code
    assert actual_status_code == int(status_code)


@when(u': We call "{method}" method for Member Update with endpoint "{endpoint}"')
def step_impl(context, method, endpoint):
    global response
    response = api_utility.Method_Call_Update(context.table, method, endpoint)


@when(u': We call "{method}" method for see all members with endpoint "{endpoint}"')
def step_impl(context, method, endpoint):
    global response
    response = api_utility.Method_Call_FIND_ALL(context, method, endpoint)

@when(u': We call "{method}" method for delete a member by id with endpoint "{endpoint}"')
def step_impl(context, method, endpoint):
    global response
    response = api_utility.Method_Call_DELETE_BY_ID(context, method, endpoint)

@step(u': Member verifies POST response body contains following information')
def step_impl(context):
    api_utility.Verify_POST(context.table)
    response_body = response.json()
    assert response_body['status'] == context.table[0][0]
    assert response_body['message'] == context.table[0][1]

@step(u': Member verifies PUT response body contains following information')
def step_impl(context):
    api_utility.Verify_PUT(context.table)
    response_body = response.json()
    assert response_body['status'] == context.table[0][0]
    assert response_body['message'] == context.table[0][1]

@step(u': Member verifies GET response body contains following information')
def step_impl(context):
    api_utility.Verify_GET(context.table)
    response_body = response.json()
    assert response_body['status'] == context.table[0][0]
    assert response_body['message'] == context.table[0][1]


@step(u': Member verifies DELETE response body contains following information')
def step_impl(context):
    api_utility.Verify_DELETE(context.table)
    response_body = response.json()
    assert response_body['status'] == context.table[0][0]
    assert response_body['message'] == context.table[0][1]
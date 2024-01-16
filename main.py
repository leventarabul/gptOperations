import gptOperation

from openai import OpenAI

client = OpenAI()

menu_action = input("menu: \n 1. delete all assistants \n 2. create assistant \n 3. Exit \n input: ")

print(f'menu_action {menu_action}')

if menu_action == '1':
    print("deleting started")
    try:
        gptOperation.GPTOperations.delete_all_assistants()

    except:
        print('no assistants to delete')

    finally:
        print('deleting finished')

if menu_action == '2':

    print("creating assistant started")

    assistant_id = gptOperation.GPTOperations.create_assistant('travel guru').id

    thread_id = gptOperation.GPTOperations.create_thread().id
    print(f'thread_id: {thread_id}')
    text_input = input("text: ")
    message_id = gptOperation.GPTOperations.create_message(thread_id, 'user', text_input).id
    run_id = gptOperation.GPTOperations.run_message(thread_id, assistant_id).id

    while gptOperation.GPTOperations.get_run_state(thread_id, run_id) != 'completed':
        run_state = gptOperation.GPTOperations.get_run_state(thread_id, run_id)
        print(f'run state: {run_state}')

    print(gptOperation.GPTOperations.get_run_state(thread_id, run_id))
    print('creating assistant finished')

    run_result = gptOperation.GPTOperations.get_answer(thread_id, run_id)
    print(run_result)
    print('run result printed')

if menu_action == '3':
    none = None
    print(none)
    print('none printed')

# using for testing
if menu_action == '4':
    run_id = 'run_eX3iVVm1fMChHcBANtI8SSht'
    thread_id = 'thread_SW5mQ0Xy3TzjUTMnxK0BB8Xb'
    run_state = client.beta.threads.runs.steps.list(run_id=run_id, thread_id=thread_id).last_id
    print(f'run state: {run_state}')
    last_run_step_id = run_state
    message_id = client.beta.threads.runs.steps.retrieve(run_id=run_id, thread_id=thread_id,
                                                         step_id=last_run_step_id).step_details.message_creation.message_id
    print(f'message id: {message_id}')
    message = client.beta.threads.messages.retrieve(thread_id=thread_id, message_id=message_id).content
    print(f'message: {message}')
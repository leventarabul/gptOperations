import gptOperation

from openai import OpenAI

client = OpenAI()

menu_action = '0'

while menu_action != 'E':

    menu_action = input("menu: \n 1. assistants \n 2. threads \n 3. messages \n E. Exit \n input: ")

    print(f'menu_action {menu_action}')

    if menu_action == '1':
        menu_action = input("menu: \n 1. create an assistant \n 2. list assistant \n 3. delete an assistant 4. delete "
                            "all assistants  \n E. Exit \n input: ")

        print(f'menu_action {menu_action}')

        if menu_action == '1':
            assistant_name = input("assistant name: ")
            assistant_description = input("assistant description: ")
            assistant = gptOperation.GPTOperations.create_assistant(name=assistant_name, instructions=assistant_description)
            print('creating assistant finished')

        if menu_action == '2':
            assistants = gptOperation.GPTOperations.get_assistant_list()
            print(assistants)
        if menu_action == '3':
            try:
                assistant_id = input("assistant id: ")
                gptOperation.GPTOperations.delete_assistant(assistant_id)
                print('deleting assistant finished')
            except:
                print('no assistant to delete')
            finally:
                print('deleting finished')
        if menu_action == '4':
            try:
                gptOperation.GPTOperations.delete_all_assistants()
                print('deleting all assistants finished')
            except:
                print('no assistants to delete')
            finally:
                print('deleting finished')

    if menu_action == '2':
        menu_action = input("menu: \n 1. create a thread \n 2. list threads \n 3. delete a thread \n E. Exit \n input: ")

        print(f'menu_action {menu_action}')

        if menu_action == '1':
            thread = gptOperation.GPTOperations.create_thread()
            print(f'thread_id: {thread.id}')

        if menu_action == '2':
            threads = gptOperation.GPTOperations.get_thread_list()
            print(threads)

    if menu_action == '3':
        assistant_id = input("assistant id: ")
        thread_id = input("thread id: ")
        while menu_action != 'E':
            text_input = input("send a message : ")
            message_id = gptOperation.GPTOperations.create_message(thread_id, 'user', text_input).id
            run_id = gptOperation.GPTOperations.run_message(thread_id, assistant_id).id

            while gptOperation.GPTOperations.get_run_state(thread_id, run_id) != 'completed':
                run_state = gptOperation.GPTOperations.get_run_state(thread_id, run_id)

            print(gptOperation.GPTOperations.get_run_state(thread_id, run_id))

            run_result = gptOperation.GPTOperations.get_answer(thread_id, run_id)
            print(run_result)
            print('run result printed')
            menu_action = input("menu: \n C. Continue \n E. Exit \n input:")
            print(f'menu_action {menu_action}')

    if menu_action == 'E':
        none = None
        print(none)
        print('none printed')
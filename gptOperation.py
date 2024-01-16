from openai import OpenAI

client = OpenAI()





class GPTOperations:
    client = OpenAI()

    @staticmethod
    def create_assistant(name='default', instructions='no aim', model="gpt-4-1106-preview"):
        assistant = client.beta.assistants.create(
            name=name,
            instructions=instructions,
            model=model,
            tools=[{"type": "code_interpreter"}]
        )
        return assistant

    @staticmethod
    def create_thread():
        thread = client.beta.threads.create()
        return thread

    @staticmethod
    def create_message(thread_id, role, content):
        message = client.beta.threads.messages.create(
            thread_id=thread_id,
            role=role,
            content=content
        )
        return message

    @staticmethod
    def run_message(thread_id, assistant_id):
        gpt_run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
        )
        return gpt_run

    @staticmethod
    def get_run_state(thread_id, run_id):
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        return run.status

    @staticmethod
    def get_run_result(thread_id, run_id):
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        return run

    @staticmethod
    def get_assistant_list():
        assistants = client.beta.assistants.list()
        return assistants

    @staticmethod
    def delete_assistant(assistant_id):
        client.beta.assistants.delete(assistant_id=assistant_id)
        return True

    @staticmethod
    def delete_all_assistants():
        assistants = GPTOperations.get_assistant_list()
        for assistant in assistants:
            GPTOperations.delete_assistant(assistant.id)
        return True

    @staticmethod
    def get_answer(thread_id, run_id):
        last_run_step_id = client.beta.threads.runs.steps.list(run_id=run_id, thread_id=thread_id).last_id
        message_id = client.beta.threads.runs.steps.retrieve(run_id=run_id, thread_id=thread_id,
                                                             step_id=last_run_step_id).step_details.message_creation.message_id
        message = client.beta.threads.messages.retrieve(thread_id=thread_id, message_id=message_id).content
        return message
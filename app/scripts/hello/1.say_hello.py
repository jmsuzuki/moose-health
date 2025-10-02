from moose_lib import task


@task
def say_hello():
    """Minimal hello world task for a workflow."""
    message = "Hello, World!"
    print(message)
    return {
        "task": "say_hello",
        "data": {"message": message},
    }



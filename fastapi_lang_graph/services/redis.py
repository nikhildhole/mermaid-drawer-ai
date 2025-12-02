code = """
graph TD
    A[Start] --> B{Is it working?}
    B -- Yes --> C[Great!]
    B -- No --> D[Check logs]
    D --> B
"""
def get_current_code() -> str:
    global code
    return code

def write_code(new_code: str) -> bool:
    global code
    code = new_code
    return True
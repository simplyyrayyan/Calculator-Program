import time
import sys

def slow_print(*args, speed=0.08, sep=" ", end="\n", file=None, flush=True):
    """
    Prints text slowly to the terminal. Fully compatible with native print features.
    Automatically prints instantly if text is too long or writing to a file.
    """
    # Use system default stdout if no file is specified
    target_file = file if file is not None else sys.stdout
    
    # Merge all arguments into one single string
    text = sep.join(map(str, args)) + end
    
    # SAFETY: If writing to an external file or text is huge (>300 chars), print instantly
    if file is not None or len(text) > 300 or speed <= 0:
        target_file.write(text)
        if flush:
            target_file.flush()
        return

    # Slow print loop for standard terminal output
    for char in text:
        target_file.write(char)
        if flush:
            target_file.flush() 
        time.sleep(speed)


def slow_input(*args, speed=0.05, sep=" "):
    """
    Prompts the user slowly and returns input.
    Keeps full GNU Readline compatibility (working arrow keys/history).
    """
    # Merge all arguments into one single prompt string
    prompt = sep.join(map(str, args))
    
    # SAFETY: If prompt is massive, print it instantly to prevent freezing
    if len(prompt) > 300 or speed <= 0:
        return input(prompt)

    # Slow print the prompt character by character
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    
    # Pass an empty string to native input() to capture user typing.
    # This keeps your terminal arrow keys, backspaces, and history working perfectly!
    return input("")
"""
Hello Everyone do you know what GOOS PAPER it stands for well it stands for 
G = Good 
O = On 
O = One
S = Side
"""

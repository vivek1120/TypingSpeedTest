import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getch()  # Changed from getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(0, 0, target)  # Display target text
    stdscr.addstr(1,0 ,"Press Esc to leave the terminal")
    stdscr.addstr(2, 0, f"WPM: {wpm}")  # Display WPM

    for i, (char, correct_char) in enumerate(zip(current, target)):
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addch(0, i, char, color)  # Display user's input

    stdscr.refresh()


def load_text():
    try:
        with open("text.txt", "r") as f:
            lines = f.readlines()
            return random.choice(lines).strip()
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise e

    # Return a default value in case of an error
    return "Default text for the typing test."



def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
            stdscr.refresh()
            stdscr.getch()
            break


        key = stdscr.getch() 

        if key == 27:  # Escape key
            break

        if key in (curses.KEY_BACKSPACE, 127):
            if current_text:
                current_text.pop()
        elif 32 <= key <= 126:
            current_text.append(chr(key))

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(2, 0, "Press any key to start again, or press 'q' to quit.")
        key = stdscr.getch() 

        if key == ord('q'):  
            break

wrapper(main)

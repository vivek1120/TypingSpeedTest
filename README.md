# Speed Typing Test Command Line Tool

This is a simple command-line tool for testing typing speed. It presents the user with a random line of text from the file `text.txt` and measures the typing speed in words per minute (WPM).

## How to Use

1. Make sure you have Python installed on your system.
2. Run the script using the command `python speed_typing_test.py`.
3. Follow the on-screen instructions.

## Instructions

1. The program will start by displaying a welcome message. Press any key to begin.
2. You will be presented with a line of text. Start typing it as accurately and quickly as possible.
3. The WPM (words per minute) will be displayed on the screen.
4. To exit the test at any time, press the 'Esc' key.
5. Once you complete the text, a message will indicate that you've finished. Press any key to continue.

## Comments on the Code

1. `start_screen`: This function displays the welcome message and waits for user input before starting the test.

2. `display_text`: This function displays the target text, user input, and WPM on the screen.

3. `load_text`: Loads a random line of text from the file `text.txt`.

4. `wpm_test`: This is the main function that manages the typing test. It tracks the time, updates the display, and checks for completion or exit.

5. `main`: Initializes curses color pairs, displays the start screen and controls the flow of the program.

6. The script uses `curses` for terminal handling, providing a simple UI for the typing test.

7. The color pairs are set up to highlight correct and incorrect characters.

## How to Customize the Text

1. Replace the content in `text.txt` with your own set of lines for testing.

## How to Quit

1. During the test, press the 'Esc' key to exit.
2. After completing a test, press any key to start a new test. Press 'q' to quit the program.

## Note

- Ensure that the `text.txt` file is in the same directory as the script.
- Make sure you have the required libraries (`curses`) installed in your Python environment.

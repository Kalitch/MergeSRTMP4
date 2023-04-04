## Explanation of Code

The code is a Python script that adds subtitles to an MP4 video file. It uses the `PySimpleGUI` library for creating a GUI interface for the user to input the necessary files and settings.

The script imports several functions and classes from the `moviepy` library, which is used for working with videos and subtitles. These include `VideoFileClip`, `SubtitlesClip`, `CompositeVideoClip`, and `concatenate_videoclips`, among others.

The script creates a GUI window with input fields for the MP4 file, SRT subtitle file, output file name, font size, and font family. When the user clicks the "Submit" button, the script reads the values from the input fields and checks that the necessary files exist. If any of the files are missing, an error message is displayed to the user.

The script then creates a subtitle clip from the SRT file, using a lambda function to generate a `TextClip` object for each subtitle line. It positions the subtitle clip at the bottom center of the video, and adjusts its duration if necessary to match the length of the video clip.

Finally, the script combines the video clip and subtitle clip into a new video clip, and writes it to the output file using the `write_videofile` function.

## Dependencies

In order to run this script, you will need to have the following installed:

- Python 3.x
- `PySimpleGUI` library
- `moviepy` library

You can install these dependencies using `pip`, the Python package manager. Here are the commands to install the required libraries:

pip install PySimpleGUI
pip install moviepy

PS: Feel free to fork and modify with your own needs

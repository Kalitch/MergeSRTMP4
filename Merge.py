# THIS CODE WAS CREATED SPECIFICALLY FOR THE MERGE SRT FILES ON MP4 VIDEOS (I WROTE THIS CODE TO MERGE SUBTITLES IN PARKS AND RECREATION SEASON 2)
import os
import re
import PySimpleGUI as sg
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.VideoClip import TextClip
sg.theme('DarkBlue3')


layout = [[sg.Text('MP4 Video File', size=(15, 1)), sg.Input(key='-MP4-'), sg.FileBrowse()],
          [sg.Text('SRT Subtitle File', size=(15, 1)),
           sg.Input(key='-SRT-'), sg.FileBrowse()],
          [sg.Text('Output File', size=(15, 1)), sg.Input(
              key='-OUTPUT-'), sg.FileSaveAs()],
          [sg.Text('Font Size', size=(15, 1)), sg.Input(
              key='-FONT_SIZE-', default_text='12')],
          [sg.Text('Font Family', size=(15, 1)), sg.Input(
              key='-FONT_FAMILY-', default_text='Times New Roman')],
          [sg.Submit(), sg.Cancel()]
          ]

window = sg.Window('Add Subtitles to MP4', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    if event == 'Submit':
        mp4_file = values['-MP4-']
        srt_file = values['-SRT-']
        output_file = values['-OUTPUT-']
        font_size = int(values['-FONT_SIZE-'])
        font_family = values['-FONT_FAMILY-']

        if not output_file.endswith('.mp4'):
            output_file = output_file + '.mp4'

        if not mp4_file or not srt_file or not output_file:
            sg.popup_error('All fields are required.')
            continue

        if not os.path.isfile(mp4_file):
            sg.popup_error('MP4 file does not exist.')
            continue

        if not os.path.isfile(srt_file):
            sg.popup_error('SRT file does not exist.')
            continue

        def generator(text): return TextClip(text, font=font_family,
                                             fontsize=font_size, color='white')
        video_clip = VideoFileClip(mp4_file)
        subtitle_clip = SubtitlesClip(srt_file, generator)
        subtitle_clip = subtitle_clip.set_position(lambda t: ('center', video_clip.size[1]-50))

        # Adjust subtitle duration if necessary
        if subtitle_clip.duration > video_clip.duration:
            subtitle_clip = subtitle_clip.set_duration(video_clip.duration)

        # Set the FPS to 23.98 THIS IS DO THE SUBTITLE SPECIFIED IN THE SRT FILE ON opensubtitles.com
        video_clip = video_clip.set_fps(23.98)
        subtitle_clip = subtitle_clip.set_fps(23.98)

        # Add subtitles to the video
        subtitle_clip = subtitle_clip.set_position(
            lambda t: ('center', 50))
        video_with_subtitles = CompositeVideoClip(
            [video_clip, subtitle_clip.set_duration(video_clip.duration)])
        final_clip = concatenate_videoclips([video_with_subtitles])

        # Write the output file
        final_clip.write_videofile(output_file, codec='libx264')

        sg.popup('Subtitle has been added successfully!', title='Success')

window.close()

import os
import json
import subprocess
from os.path import join

def extract_frames(input_path, output_path):
    os.makedirs(output_path, exist_ok=True)
    subprocess.check_output(f'ffmpeg -i {input_path} -start_number 0 {join(output_path, "%04d.png")}', shell=True, stderr=subprocess.STDOUT)

def create_fps_dict(data_path):
    with open(join(data_path, 'misc', 'conversion_list.json'), 'r') as f:
        conversion_dict = json.load(f)

    fps_dict = {}
    for key, value in conversion_dict.items():
        video_id, num = value.split(' ')
        with open(join(data_path, 'downloaded_videos', video_id, f'{video_id}.json'), 'r') as f:
            info_dict = json.load(f)
        fps_dict[key] = info_dict['fps']
    return fps_dict

def make_video_from_images(input_path, output_path, crf=0, fps=30):
    codec = 'libx264' if crf != 0 else 'libx264rgb'
    subprocess.check_output(f'ffmpeg -r {fps} -i {join(input_path, "%04d.png")} -crf {crf} -c:v {codec} -vf "fps={fps}" {output_path}', shell=True, stderr=subprocess.STDOUT)

def compress_folder(input_path, output_path, crf, fps, **kwargs):
    for folder in os.listdir(input_path):
        make_video_from_images(join(input_path, folder), join(output_path, f'{folder}.mp4'), crf=crf, fps=fps)

def compress_video_folder(input_path, output_path, crf, fps, **kwargs):
    codec = 'libx264' if crf != 0 else 'libx264rgb'
    os.makedirs(output_path, exist_ok=True)
    for video in os.listdir(input_path):
        subprocess.check_output(f'ffmpeg -r {fps} -i {join(input_path, video)} -crf {crf} -c:v {codec} -vf "fps={fps}" {join(output_path, video)}', shell=True, stderr=subprocess.STDOUT)

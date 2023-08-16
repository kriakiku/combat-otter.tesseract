import os
import shutil
import random
import pathlib
import subprocess
import shutil
import platform
import argparse

# Args
default_fonts_dir = os.path.join(os.path.expanduser('~'), '.fonts', 'tessfont')
argParser = argparse.ArgumentParser()
argParser.add_argument("--training_text", help="example: ./langdata_lstm/eng/eng.training_text", default="./langdata_lstm/eng/eng.training_text")
argParser.add_argument("--fonts_dir", help="example: ./fonts", default="./fonts")
argParser.add_argument("--font", help="example: Stratum2 Bold")
argParser.add_argument("--lang", help="example: eng", default="eng")
argParser.add_argument("--langdata_dir", help="example: ./langdata_lstm", default="./langdata_lstm")
argParser.add_argument("--output_dir", help="example: ./train", default="./train")
argParser.add_argument("--fonts_install", help=f"example: {default_fonts_dir}", default=default_fonts_dir)


args = argParser.parse_args()


# Magic / source: https://youtu.be/KE4xEzFGSU8


# Prepare
output_directory = pathlib.Path(os.path.join(args.output_dir, f'{args.font}-GT'))
unicharset_file = pathlib.Path(os.path.join(args.langdata_dir, args.lang, 'eng.unicharset'))

# shutil.rmtree(output_directory, ignore_errors=True)
output_directory.mkdir(parents=True, exist_ok=True)
fonts_dir = args.fonts_dir;

# Install font
if args.fonts_install:
    shutil.rmtree(args.fonts_install, ignore_errors=True)
    shutil.copytree(args.fonts_dir, args.fonts_install)
    subprocess.run(['fc-cache', '-f', '-v'], stdout = subprocess.DEVNULL)
    fonts_dir = args.fonts_install
    


lines = []
continueCheck = True

with open(args.training_text, 'r', encoding="utf8") as input_file:
    raw_line = input_file.readline()
    line_count = 0
    while raw_line:
        outputbase = os.path.join(output_directory, f'{args.lang}_{line_count}')

        # Continue
        continueCheckPath = pathlib.Path(f'{outputbase}.tif')
        if continueCheck and continueCheckPath.is_file() and continueCheckPath.stat().st_size > 0:
            print(f'Skipping {line_count} line (exists)')
            raw_line = input_file.readline()
            line_count += 1
            continue
        if continueCheck == True:
            print(f'Continue from {line_count} line')
            continueCheck = False

        line = raw_line.strip()
        line_training_text = f'{outputbase}.gt.txt'

        with open(line_training_text, 'w', encoding="utf8") as output_file:
            output_file.writelines([line])

        subprocess.run([
            'text2image',
            f'--fonts_dir={fonts_dir}',
            f'--font={args.font}',

            '--tlog_level=-1',

            f'--text={line_training_text}',
            f'--outputbase={outputbase}',
            '--max_pages=1',
            '--strip_unrenderable_words',
            '--leading=32',
            '--xsize=3600',
            '--ysize=480',
            '--char_spacing=1.0',
            '--exposure=0',
            f'--unicharset_file={unicharset_file}'
        ])

        raw_line = input_file.readline()
        line_count += 1

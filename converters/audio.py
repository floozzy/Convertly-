import subprocess


def convert_audio(input_file, output_format):

    output = f"converted.{output_format}"


    subprocess.run([
        "ffmpeg",
        "-i",
        input_file,
        output,
        "-y"
    ])


    return output

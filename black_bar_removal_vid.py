import os
import subprocess


def main():
    file_list = get_file_list(target_ext = ".mp4")
    auto_crop(file_list)
    

def get_file_list(target_ext):
    file_list = []
    for file in os.listdir():
        if os.path.splitext(file)[1] == target_ext:
            file_list.append(file)
    return file_list


def auto_crop(file_list):
    for file in file_list:
        black_box_detect_cmd = ['ffmpeg', '-ss', str(10), '-i',
                                file, '-vframes', str(10), '-vf',
                                'cropdetect', '-f', 'null', '-']
        output = subprocess.run(black_box_detect_cmd,
                                capture_output=True, text=True)
        ratio_idx_start = str(output).find("crop=")
        ratio_idx_length = str(output)[ratio_idx_start:].find(r"\n")
        ratio_arg = str(output)[ratio_idx_start:ratio_idx_start+ratio_idx_length]

        out_file = file[:-4] + "_cropped.mp4"
        print(out_file)
        black_box_crop_cmd = ['ffmpeg', '-i', file, '-vf',
                              ratio_arg, '-c:a', 'copy', out_file]
        subprocess.call(black_box_crop_cmd)


if __name__=="__main__":
    main()

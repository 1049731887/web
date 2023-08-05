import os
import json

def list_video_folders(directory):
    # 创建一个空列表用于存储找到的文件夹
    folders = []
    
    # 遍历目录中的所有文件夹
    for entry in os.scandir(directory):
        if entry.is_dir():  # 如果是文件夹
            folders.append(entry.name)
    
    return folders

if __name__ == "__main__":
    video_directory = "video"  # 替换为实际的目录名
    video_folders = list_video_folders(video_directory)

    if video_folders:
        print("找到以下视频文件夹：")
        for idx, folder in enumerate(video_folders, start=1):
            print(f"{idx}: {folder}")
    else:
        print("在目录 {} 下未找到任何视频文件夹。".format(video_directory))

    # 构建带编号的字典
    video_dict = {idx: folder for idx, folder in enumerate(video_folders, start=1)}
    BV_dict = {idx + 1000: "BV" for idx, folder in enumerate(video_folders, start=1)}
    # 将结果写入 list.json 文件
    with open("list.json", "w") as json_file:
        json.dump({**video_dict, **BV_dict}, json_file, indent=4)



    input("按下回车键继续...")


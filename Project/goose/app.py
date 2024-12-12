import ctypes
import os
import platform
import random
import shutil
from pathlib import Path

import winshell


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def run():
    system = platform.system()

    if system == "Windows":
        windows()
    elif system == "Darwin":
        print(
            f"{bcolors.WARNING}This is script is being developed for Mac{bcolors.ENDC}"
        )
    elif system == "Linux":
        print(
            f"{bcolors.FAIL}This script couldn't be used in Linux systems{bcolors.ENDC}"
        )


def windows():
    if os.path.exists(os.path.join(Path(__file__).parent, "assets", "windows.zip")):

        startup_folder = winshell.startup()

        print(startup_folder)

        app_data_path = os.getenv("APPDATA")
        goose_path = os.path.join(app_data_path, "Goose")
        goose_exe_path = os.path.join(goose_path, "windows", "GooseDesktop.exe")
        ini_file_path = os.path.join(goose_path, "windows", "config.ini")

        try:
            create_hidden_folder(os.path.join(app_data_path, "Goose"))
            shutil.unpack_archive(
                os.path.join(Path(__file__).parent, "assets", "windows.zip"),
                goose_path,
            )
            print(f"{bcolors.OKGREEN}Goose installed successfully{bcolors.ENDC}")

            goose_colors(ini_file_path)

            shortcut_path = os.path.join(startup_folder, "Goose.lnk")
            with winshell.shortcut(shortcut_path) as s:
                s.path = goose_exe_path
                s.description = "Goose"
                s.working_directory = goose_path

            print(f"{bcolors.OKGREEN}Shortcut created successfully{bcolors.ENDC}")

            [os.startfile(shortcut_path) for _ in range(random.randint(1, 6))]

            os.system("cls")

        except Exception as e:
            print(f"{bcolors.FAIL}Error creating hidden folder: {e}{bcolors.ENDC}")

    else:
        print(f"{bcolors.FAIL}Assets not found{bcolors.ENDC}")


def macos(): ...


def create_hidden_folder(path: str):
    if not os.path.exists(path):
        os.makedirs(path)

    FILE_ATTRIBUTE_HIDDEN = 0x02

    if not ctypes.windll.kernel32.SetFileAttributesW(path, FILE_ATTRIBUTE_HIDDEN):
        raise ctypes.WinError()


def goose_colors(file_path: str):
    with open(file_path, "r") as file:
        data = file.readlines()

    data[6] = f"GooseDefaultWhite={random_color()}\n"
    data[7] = f"GooseDefaultOrange={random_color()}\n"
    data[8] = f"GooseDefaultOutline={random_color()}\n"

    with open(file_path, "w") as file:
        file.writelines(data)


def random_color():
    return ["#" + "".join([random.choice("abcdef0123456789") for _ in range(6)])][0]


if __name__ == "__main__":
    run()

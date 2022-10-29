import os
import subprocess
import sys
import webbrowser
import FungibilityMatrixGen_STL
import Product_File
import Product_Init


def main():

    # Getting path to python executable (full path of deployed python on Windows)
    executable = sys.executable

    # Open browser tab. May temporarily display error until streamlit server is started.
    webbrowser.open("http://localhost:8501")

    filename = "FungibilityMatrixGen_STL.py"
    # Run streamlit server
    path_to_pre = sys.path[0]
    #prework = subprocess.run("cd " + path_to_pre)
    print("cd " + path_to_pre + filename)
    os.chdir(path_to_pre)
    result = subprocess.run(
        f"{executable} -m streamlit run {filename} --server.headless=true --global.developmentMode=false",
        shell=True,
        capture_output=True,
        text=True,
    )

    # These are printed only when server is stopped.
    # NOTE: you have to manually stop streamlit server killing process.
    print(result.stdout)
    print(result.stderr)


if __name__ == "__main__":
    main()
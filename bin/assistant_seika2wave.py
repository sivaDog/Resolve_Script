import sys
import os

lib_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../library/python')
)
sys.path.append(lib_path)

if __name__ == "__main__":
    from rs.tool.text2wave.assistant_seika2wave import run
    run()
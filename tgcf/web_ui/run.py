import os
from importlib import resources

import tgcf.web_ui as wu
from tgcf.config import CONFIG

package_dir = resources.path(package=wu, resource="").__enter__()

# Entry Point
def main():
    print(package_dir)
    path = os.path.join(package_dir, "0_👋_Hello.py")
    os.environ["STREAMLIT_THEME_BASE"] = CONFIG.theme
    os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
    os.system(f"streamlit run --server.port {os.environ.get('PORT')} {path}")


if __name__ == "__main__":
    main()

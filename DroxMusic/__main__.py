


import glob
from pathlib import Path
from DroxMusic.utils import load_plugins
import logging
from DroxMusic import DroxMusic

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "DroxMusic/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("تم تنصيب السورس بنجاح")
print("قناة السورس @DroxTeAm")

if __name__ == "__main__":
    DroxMusic.run_until_disconnected()

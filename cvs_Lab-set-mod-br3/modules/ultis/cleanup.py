import os
import glob

def cleanup_parts(parts_dir):
    if not os.path.exists(parts_dir):
        return

    for file in glob.glob(os.path.join(parts_dir, "p*.csv")):
        try:
            os.remove(file)
        except Exception as e:
            print(f"⚠️ Δεν μπόρεσα να διαγράψω {file}: {e}")
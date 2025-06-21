import ffmpeg
import os

def convert_mp4_for_resolve(input_path):
    base, _ = os.path.splitext(input_path)
    output_path = f"{base}_resolve_prores.mov"

    print(f"\nConverting: {input_path} → {output_path}")
    
    (
        ffmpeg
        .input(input_path)
        .output(
            output_path,
            vcodec='prores_ks',          # High-quality ProRes codec
            profile='3',                 # '3' = ProRes 422 HQ
            acodec='pcm_s16le',
            format='mov'
        )
        .run(overwrite_output=True)
    )
    
    print(f"✔ Done: {output_path}")


def list_mp4_files():
    return [f for f in os.listdir('.') if f.lower().endswith('.mp4')]

def select_files(files):
    print("Found the following MP4 files:")
    for i, f in enumerate(files, start=1):
        print(f"{i}: {f}")
    
    selected = input("\nEnter numbers of files to convert (e.g. 1 3 4), or 'a' for all: ").strip()
    
    if selected.lower() == 'a':
        return files
    else:
        try:
            indices = [int(x)-1 for x in selected.split()]
            return [files[i] for i in indices if 0 <= i < len(files)]
        except ValueError:
            print("Invalid input. Aborting.")
            return []

def main():
    mp4_files = list_mp4_files()
    if not mp4_files:
        print("No MP4 files found in this folder.")
        return

    to_convert = select_files(mp4_files)
    if not to_convert:
        return

    for f in to_convert:
        convert_mp4_for_resolve(f)

if __name__ == "__main__":
    main()


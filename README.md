#  DaVinci Resolve MP4 Compatibility Fix (Linux)

This Python script converts `.mp4` video files into a format fully compatible with **DaVinci Resolve on Linux**, which often struggles with AAC audio and certain compressed video formats.

## Features

- Converts **AAC audio** to **uncompressed PCM** (`pcm_s16le`)
- Rewraps video into a **`.mov` container** (preferred by Resolve)
- Offers:
  - Fast rewrap: copy video, fix audio only
  - Full re-encode: optional ProRes video for maximum compatibility
- Simple **command-line interface** with file selection
- Outputs new files with `_resolve.mov` or `_resolve_prores.mov` suffixes

---

##  Why

DaVinci Resolve on Linux **does not support AAC audio in MP4 files** by default. It may also have trouble decoding some compressed video formats (like HEVC/H.265).

This script ensures your video files are formatted in a way that Resolve can import and play back without issues.

---

## Requirements

- Python 3.x
- [`ffmpeg`](https://ffmpeg.org/) installed and in your system PATH
- Python module: `ffmpeg-python`  

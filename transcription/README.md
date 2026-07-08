# Multilingual audio → English transcript (Whisper)

Turn a **mixed German + English** audio file into **one clean English transcript**,
running entirely on your own computer. This uses OpenAI's open-source **Whisper**
model in *translate* mode, which automatically detects the language being spoken
(even when the speaker switches back and forth mid-sentence) and translates
everything to English in a single pass.

You run this **once** to set it up; after that it's a single command per file.

---

## Why this instead of Microsoft Word

Word's Transcribe feature assumes the **whole file is one language** and does **not**
translate. When it hears German, it guesses which English words the German *sounds*
like — that's why you got gibberish. Whisper is built for exactly this mixed-language
job.

---

## What you'll end up with

For an input `meeting.mp3`, you get two files next to it:

- `meeting.en.txt` — the plain English transcript
- `meeting.en.srt` — the same text with timestamps (subtitle format)

---

## Setup (one time)

You need two things: **ffmpeg** (reads the audio) and **Python + Whisper**.

### Step 1 — Install ffmpeg

**macOS** (needs [Homebrew](https://brew.sh)):

```bash
brew install ffmpeg
```

**Windows** (needs [Chocolatey](https://chocolatey.org/install), run in an
Administrator PowerShell):

```powershell
choco install ffmpeg
```

*(No package manager? Download ffmpeg from https://ffmpeg.org/download.html and add
its `bin` folder to your PATH.)*

### Step 2 — Install Python

If `python3 --version` (macOS) or `python --version` (Windows) prints a version of
3.9 or newer, you're set. Otherwise install it from https://www.python.org/downloads/
(on Windows, tick **"Add Python to PATH"** in the installer).

### Step 3 — Install Whisper

```bash
pip install -r requirements.txt
```

*(If you're on macOS and `pip` isn't found, use `pip3`.)*

---

## Run it

From inside this `transcription/` folder:

```bash
python transcribe_translate.py "/full/path/to/your_audio.mp3"
```

- **First run only:** it downloads the large model (~1.5–3 GB). This is a one-time
  download; later runs reuse it and start immediately.
- It prints each line as it goes, then writes the `.txt` and `.srt` files.

### How long will it take?

The `large-v3` model is the most accurate for mixed languages, but on a CPU it runs
roughly at (or a bit slower than) real time — a 30-minute recording can take ~30–90
minutes depending on your machine. If you have a lot of audio and want speed over a
little accuracy, use a smaller model:

```bash
python transcribe_translate.py "your_audio.mp3" --model medium
```

`medium` is noticeably faster and usually still good for translation; `small` is
faster still but weaker on heavy code-switching.

---

## Options

| Flag | Default | What it does |
|------|---------|--------------|
| `--model` | `large-v3` | Model size. Try `medium` or `small` for speed. |
| `--outdir` | next to the audio | Folder to write the `.txt` / `.srt` into. |

Example:

```bash
python transcribe_translate.py "interview.m4a" --model large-v3 --outdir ./transcripts
```

---

## Command-line alternative (no script)

If you install the reference package (`pip install -U openai-whisper`), you can skip
the script entirely and run:

```bash
whisper "your_audio.mp3" --model large --task translate
```

`--task translate` is the key part — it produces English output from mixed-language
audio. Whisper writes `.txt`, `.srt`, and `.vtt` files into the current folder.

---

## Troubleshooting

- **"ffmpeg not found"** — ffmpeg isn't installed or isn't on your PATH. Redo Step 1
  and open a new terminal window.
- **Download fails / very slow** — you're on a restricted network that blocks the
  model host (`huggingface.co`). Run this on a normal connection; the model only
  needs to download once.
- **Output still looks off** — make sure you did *not* pass a tiny model. Use
  `large-v3` (default) or at least `medium` for mixed German/English.

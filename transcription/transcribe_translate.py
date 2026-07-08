#!/usr/bin/env python3
"""
Transcribe a mixed-language (e.g. German + English) audio file and translate
everything into English, in one pass.

It uses OpenAI's open-source Whisper model in "translate" mode, which:
  - automatically handles code-switching (jumping between languages), and
  - outputs a single, unified English transcript.

By default it uses `faster-whisper` (much quicker on a normal laptop CPU).
If that isn't installed, it falls back to the reference `openai-whisper`.

USAGE
-----
    python transcribe_translate.py "my_audio.mp3"
    python transcribe_translate.py "my_audio.mp3" --model large-v3 --outdir ./out

The first run downloads the model (~1.5-3 GB) once; later runs reuse it.

OUTPUT
------
Two files next to the audio (or in --outdir):
    <name>.en.txt   plain English transcript
    <name>.en.srt   English subtitles with timestamps
"""

import argparse
import os
import sys
import time


def fmt_ts(seconds: float) -> str:
    """Seconds -> SRT timestamp 'HH:MM:SS,mmm'."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def write_outputs(segments, out_txt, out_srt):
    """segments: iterable of (start, end, text). Writes .txt and .srt."""
    txt_lines, srt_blocks = [], []
    for i, (start, end, text) in enumerate(segments, 1):
        text = text.strip()
        print(f"[{start:8.1f} -> {end:8.1f}]  {text}", flush=True)
        txt_lines.append(text)
        srt_blocks.append(f"{i}\n{fmt_ts(start)} --> {fmt_ts(end)}\n{text}\n")
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(txt_lines) + "\n")
    with open(out_srt, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_blocks))


def run_faster_whisper(audio, model_name, out_txt, out_srt):
    from faster_whisper import WhisperModel

    print(f"[faster-whisper] loading model '{model_name}' (cpu, int8)...", flush=True)
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    # task="translate" -> English out, regardless of the spoken language(s).
    segments, info = model.transcribe(
        audio, task="translate", beam_size=5, vad_filter=True
    )
    print(
        f"[faster-whisper] base language guess: {info.language} "
        f"(p={info.language_probability:.2f}), duration={info.duration:.0f}s",
        flush=True,
    )
    write_outputs(((s.start, s.end, s.text) for s in segments), out_txt, out_srt)


def run_openai_whisper(audio, model_name, out_txt, out_srt):
    import whisper

    # faster-whisper uses 'large-v3'; openai-whisper calls the same weights 'large'.
    if model_name == "large-v3":
        model_name = "large"
    print(f"[openai-whisper] loading model '{model_name}'...", flush=True)
    model = whisper.load_model(model_name)
    result = model.transcribe(audio, task="translate", verbose=False)
    segments = ((s["start"], s["end"], s["text"]) for s in result["segments"])
    write_outputs(segments, out_txt, out_srt)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("audio", help="path to the audio file (mp3, wav, m4a, ...)")
    p.add_argument("--model", default="large-v3",
                   help="model size (default: large-v3; best for mixed languages). "
                        "smaller/faster: medium, small")
    p.add_argument("--outdir", default=None,
                   help="where to write outputs (default: next to the audio file)")
    args = p.parse_args()

    if not os.path.isfile(args.audio):
        sys.exit(f"ERROR: file not found: {args.audio}")

    outdir = args.outdir or os.path.dirname(os.path.abspath(args.audio))
    os.makedirs(outdir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(args.audio))[0]
    out_txt = os.path.join(outdir, f"{stem}.en.txt")
    out_srt = os.path.join(outdir, f"{stem}.en.srt")

    t0 = time.time()
    try:
        run_faster_whisper(args.audio, args.model, out_txt, out_srt)
    except ImportError:
        print("faster-whisper not installed; using openai-whisper instead.", flush=True)
        run_openai_whisper(args.audio, args.model, out_txt, out_srt)

    print(f"\nDONE in {time.time() - t0:.0f}s")
    print(f"  transcript : {out_txt}")
    print(f"  subtitles  : {out_srt}")


if __name__ == "__main__":
    main()

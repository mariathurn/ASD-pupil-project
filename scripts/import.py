import pandas as pd
import numpy as np

# Example: one session's continuous stream (one row per sample)
# Required cols: subject_id, session_id, t (ms), pupil (or gaze_x/y), blink_flag (0/1)
stream = pd.read_csv("data/session01_stream.csv")

# Example: events log for the same session (one row per event)
# Required cols: subject_id, session_id, event, t (ms), and optionally trial_id or stimulus_id
events = pd.read_csv("data/session01_events.csv")

# 1) Ensure integer millisecond timestamps (or float seconds—just be consistent)
for df in (stream, events):
    # if your timestamps are seconds as float, convert to ms:
    if df['t'].max() < 1e6:  # heuristic: probably seconds
        df['t'] = (df['t'] * 1000).round().astype(int)

# 2) Sort
stream = stream.sort_values(['subject_id', 'session_id', 't']).reset_index(drop=True)
events = events.sort_values(['subject_id', 'session_id', 't']).reset_index(drop=True)

# 3) Optional: resample to uniform rate (e.g., 120 Hz => 8.33 ms) if your device is jittery.
# Often you can skip this and slice by timestamps directly.
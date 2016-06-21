import pandas as pd

def Excel(io, sheetname=None, header=0):
    frames = pd.read_excel(io, sheetname=sheetname, header=header)
    frames = [(sheetname, frame) for sheetname, frame in frames.items()]
    return frames[0][1] if len(frames) == 1 else frames

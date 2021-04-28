from pydub import AudioSegment
import math
from glob import glob


class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename.split('./')[1].split('/')[1]
        self.filepath = filename

        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 1000
        t2 = to_min * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(f'chunks/{split_filename}', format="wav")

    def multiple_split(self, sec_per_split):
        total_sec = math.ceil(self.get_duration())
        for i in range(0, total_sec, sec_per_split):
            split_fn = (f'_{str(i)}.').join(self.filename.split('.'))
            self.single_split(i, i + sec_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_sec - sec_per_split:
                print('All splited successfully')


folder = './ljud_1/'
files = glob(folder + '*.wav')
for file in files:
    split_wav = SplitWavAudioMubin(folder, file)
    split_wav.multiple_split(sec_per_split=5)
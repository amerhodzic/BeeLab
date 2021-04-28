import librosa, time, numpy as np, sys
from glob import glob


data_dir = './chunks/'
audio_files = glob(data_dir + '*.wav')

start = time.time()
mfcc_list = []
for file in range(0, len(audio_files), 1):
    X, sample_rate = librosa.load(audio_files[file], sr=8000)
    stft = np.abs(librosa.stft(X))
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40, hop_length=200).T,axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
    mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate, fmin=30).T, axis=0)
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X),sr=sample_rate,
                                             chroma=librosa.feature.chroma_stft(S=stft, sr=sample_rate)).T, axis=0)
    mfcc_list.append(np.hstack([mfccs, chroma, mel, contrast, tonnetz]))
    #mfcc_list.append(np.mean(librosa.feature.spectral_centroid(X, sr=sample_rate)[0].T,axis=0))
end = time.time()
tid = end - start
print(f'Time: {tid} seconds')

np.set_printoptions(threshold=sys.maxsize)
mfcc_arr = np.array(mfcc_list)
np.savetxt('test.out', mfcc_arr)
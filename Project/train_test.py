import numpy as np
import scipy


def train(path, n, feature_type='FFT', k=16):
    """ Speaker Recognition: Training Stage

    Parameters
    ----------
        path : string
            Path of training sound files.
        n : int
            number of training files in `path`
        feature_type : string
            Type of the features to be extracted. default = 'FFT'
        k : int
            number of centroids, default = 16.

    Returns
    -------
        codebook : list
            centroids (for FFT) or codebooks (for STFT and MFCC)

    """
    for i in range(n):
        filename = '{:s}s{}.wav'.format(path, i)
        print('Current training file is: {}'.format(filename))
 
        # You will write an audio reading utility here.
        [s, fs] = audioread(filename);  # An example line to read audio file

        # You will develop a code that will compute FFT, STFT or MFCC of the input here.
        v = scipy.fft.fft(s, fs) # An example line to preprocess data

        # You will develop a function that will generate VQ codebook when `feature_type` is STFT or MFCC, or centroids when the feature type is FFT.
        
    return codebook


def test(path, n, codebook, feature_type='FFT'):
    """ Speaker Recognition: Testing Stage

    Parameters
    ----------
    path : string
        string name of directory contains all test sound files
    n : int
        number of training files in `path`
    codebook : list
        centroids (for FFT) or codebooks (for STFT and MFCC)
    feature_type : string
        Type of the features to be extracted. default = 'FFT'

    Returns
    -------
    accuracy: float
        accuracy of the trained algorithm
    """

    for i in range(n):
        filename = '{:s}s{}.wav'.format(path, i)
        print('Current test file is: {}'.format(filename))

        # You will need the audio reading and preprocessing utilities from training here.
        [s, fs] = audioread(filename);  # An example line to read audio file
        v = scipy.fft.fft(s, fs) # An example line to preprocess data

        distmin = np.inf
        match_speaker_ind = 0
        len_code = len(codebook)

        for l in range(len_code):
            # Compute the distance of the current test feature to the a codebook element. Hint: You will need a pairwise distance computation as a codebook includes many vectors with which you will need to compare your test feature. See `scipy.spatial.distance.cdist`.
            d = pairwise_distance(v, codebook[l]) # An example line to get distance
            dist = sum(d.min(dim=1))/d.shape[0] # An example to get the total distortion 

            # Check if the total distortion of the current codebook is smaller than all the previous ones. If so, current speakers codebook is a better match than all previous speakers' codebooks.
            if dist < distmin:
                distmin = dist
                match_speaker_ind = l

        print('Speaker {} matches with speaker {}', i, match_speaker_ind)

        # Update your accuracy here, comparing the ground truth to estimation.

    return accuracy
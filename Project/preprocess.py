
## Bear in mind that this is a draft for you to have an idea on how to write this part. This code will not work unless you complete it. You do not have to use this format.

def preprocess(data, feature_type):
    """_summary_

    Parameters
    ----------
    data : _type_
        _description_
    feature_type : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """    

    # Create an if-else or switch-case statement here to check feature type
    if feature_type == 'FFT':
        return fft(data)
    elif feature_type == 'STFT':
        return stft(data)
    else feature_type == 'MFCC':
        return mfcc(data)

def mfcc(data):
    """_summary_

    Parameters
    ----------
    data : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """    

    spectrum = stft(data)
    mel_spec = melfilter(spectrum)
    mfcc = dct(mel_spec)

    return mfcc
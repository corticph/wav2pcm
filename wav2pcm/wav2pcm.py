def _get_field(wav, offset, lent):
    """

    Get values for filed. This is only working for fields with byteorder little

    Args :
      wav : the wave file
      offset : which position to start at.
      lent : length of field

    Return :
      Int of the desired field.

    """
    wav.seek(0)
    wav.seek(offset, 0)
    return int.from_bytes(wav.read(lent), byteorder='little')


def convert(wav_in):
    """
    Get the sample rate, bit rate and PCM raw bytes from a wav.

    Args :
      wav_in : wave file, or string with path to wave file.

    Return :
      sample_rate : int representing the wave file sample rate
      bit_rate : int repesenting the wave file bit rate
      pcm : bytes representing the raw sound.

    """
    if type(wav_in) is str:
        wav_file = open(wav_in, 'rb')
    else:
        wav_file = wav_in
    header_size = _get_field(wav_file, 16, 4)
    sample_rate = _get_field(wav_file, 24, 4)
    bit_rate = _get_field(wav_file, 34, 2)
    wav_file.seek(0)
    if header_size == 16:
        data = wav_file.read()[44:]
    elif header_size == 18:
        data = wav_file.read()[46:]
    else:
        print("WAV format unknown")
        exit(1)
    wav_file.close()
    return sample_rate, bit_rate, data


if __name__=='__main__':
    samp, bit, test = convert('../test/test8000.wav')
    print(samp, bit, len(test))

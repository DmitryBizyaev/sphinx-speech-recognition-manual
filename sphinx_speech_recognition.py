from pocketsphinx import Decoder
import wave


def decode_audio_file(audio_file_path):
    with wave.open(audio_file_path, "rb") as audio:
        decoder = Decoder(samprate=audio.getframerate())
        decoder.start_utt()
        decoder.process_raw(audio.getfp().read(), full_utt=True)
        decoder.end_utt()

    return decoder.hyp().hypstr    

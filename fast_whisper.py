from faster_whisper import WhisperModel



def whisper(audio_file_name):
    model_size = "tiny"
    
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    
    segments, info = model.transcribe(audio_file_name, beam_size=5)

    text = ''.join(segment.text for segment in segments)
    print(text)
    return text

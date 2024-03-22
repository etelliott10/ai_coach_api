from faster_whisper import WhisperModel



def whisper(audio_file_name):
    model_size = "tiny"
    # model_size = "large-v3"


# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    
    segments, info = model.transcribe(audio_file_name, beam_size=5)
    

    # segments, info = model.transcribe("myrecording.wav", beam_size=5)

# segments, info = model.transcribe("audio.mp3", beam_size=5)

    text = ''.join(segment.text for segment in segments)
    print(text)
    return text
# print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

# for segment in segments:
#     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
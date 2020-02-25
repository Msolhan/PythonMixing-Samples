from pydub import AudioSegment

AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe" #windows kullanılmıyorsan bu kodu yoruma al. 
melody = AudioSegment.from_mp3("sound1.wav")
bass = AudioSegment.from_mp3("sound2.wav")
drum = AudioSegment.from_mp3("sound3.wav")
melody2 = AudioSegment.from_mp3("sound4.wav")
#listedeki sesler ve ayarladığın pozisyonlar aynı sırada olmak zorunda
sound_list = [melody,bass,drum,melody2] # sound eklersen buraya variable nı eklemeyi unutma!
sound_position = [0000,3000,2000,6000] # sound eklersen buraya pozisyonunu eklemeyi unutma!
sound_bass = [1,2,3,4] # sound eklersen buraya bass ını eklemeyi unutma!
def main(list,sound_pos,bass):
    soundbass = list[0] - bass[0]
    output = soundbass
    for i in range(0,len(list)-1):
        soundf = list[i+1] - bass[i+1]
        output = output.overlay(soundf, position= sound_pos[i+1])
        if i+1 == len(list)-1:
            break
        else:
            pass

    output.export("output.wav", format="wav")

# save the result
main(sound_list,sound_position,sound_bass)
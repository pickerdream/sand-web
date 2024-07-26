from spleeter.separator import Separator
import os

# environment 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = ''

for i in (2,4,5):
    outdir_path = "./temp/output/" + str(i) + "stems"
    os.makedirs(outdir_path,exist_ok=True)

# information
input_audio = "./sample/0.wav"

# borcal or other(2 sounds)
separator_2stem = Separator('spleeter:2stems')
separator_2stem.separate_to_file(input_audio, "./temp/output/2stems.wav")

# borcal,base and dram or other(3 sounds)
separator_4stem = Separator('spleeter:4stems')
separator_4stem.separate_to_file(input_audio, "./temp/output/4stems.wav")

# borcal,base,dram and piano or other(4 sounds)
separator_5stem = Separator('spleeter:5stems')
separator_5stem.separate_to_file(input_audio, "./temp/output/5stems.wav")

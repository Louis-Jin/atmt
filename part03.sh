max=10
beamsize=20
echo "max $max"

for alpha in {0..10}
do
echo "at $alpha time"
python translate_beam.py --beam-size=$beamsize --alpha-i=$alpha --alpha-max=$max --output="./output_asg4_part3_k$beamsize/translated/model_translations_$alpha.txt"
bash postprocess.sh ./output_asg4_part3_k$beamsize/translated/model_translations_$alpha.txt ./output_asg4_part3_k$beamsize/postprocessed/model_translations_$alpha.out en
done

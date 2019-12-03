#for k in {1..50}
#do
#echo "at $k time"
#python translate_beam.py --beam-size=$k --output="./output_asg4/translated/model_translations_$k.txt"
#bash postprocess.sh ./output_asg4/translated/model_translations_$k.txt ./output_asg4/postprocessed/model_translations_$k.out en
#done

k=7

echo "at $k time"
python translate_beam.py --beam-size=$k --output="./output_asg4/translated/model_translations_$k.txt"
bash postprocess_asg4.sh ./output_asg4/translated/model_translations_$k.txt ./output_asg4/postprocessed/model_translations_$k.out en


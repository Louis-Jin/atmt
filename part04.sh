alphamax=10
gammamax=10
beamsize=20
for beamsize in {3,5,7,8,9,10,11,20,30,50,100}
    do
    echo "beamsize $beamsize"
    mkdir -p ./output_asg4_part4/k$beamsize/translated
    mkdir -p ./output_asg4_part4/k$beamsize/postprocessed

    for alpha in {0..10}
        do
        echo "alpha $alpha"

        for gamma in {0..10}
            do
            echo "gamma $gamma"

            python translate_beam.py --beam-size=$beamsize --alpha-i=$alpha --alpha-max=$alphamax --gamma-i=$gamma --gamma-max=$gammamax  --output="./output_asg4_part4/k$beamsize/translated/model_translations_alpha$alpha-gamma$gamma.txt"
            bash postprocess_asg4.sh ./output_asg4_part4/k$beamsize/translated/model_translations_alpha$alpha-gamma$gamma.txt ./output_asg4_part4/k$beamsize/postprocessed/model_translations_alpha$alpha-gamma$gamma.out en

            if [ $beamsize -gt 15 ];
            then
            break
            fi

            done

        if [ $beamsize -gt 15 ];
        then
        break
        fi

        done
    done

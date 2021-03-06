# Home of rafComputing Tool

The process of automatically tailoring a suitable rComplexity Class is provided on-demand, using rafComputing Tool.

## Description

A ML-based system is used for estimating rComplexity in the case when the theoretical mapping between the algorithm's function and the rComplexity Class is not known. For better performances, it should be inputted with the classic Big-Theta(for asymptotic behavior) Class or a acceptable classic Big-O Class approximation. However, this platform can approximate a good fitting for algorithms with unknown classic asymptotic behavior.

## Useful

#### Running MLdriver

`python3 ./rafComputing/ML/MLdriver.py rComplexity/samples/matrix_multiplication/results/fsri5/results_20200227181601`

#### Running MLAutoDriver

`python3 rafComputing/ML/MLAutoDriver.py rComplexity/samples/matrix_multiplication/results/fsri5/results_20200309165609`

#### FFmpeg.

A complete, cross-platform solution to record, convert and stream audio and video.

`ffmpeg -r 5 -n -i "result_%02d.png" output.m4v`

`ffmpeg -r 5 -n -i "result_%02d.png" -vcodec h264 output.mp4`

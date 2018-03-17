## Word Similarity Section:
> *Where the real fun's at*.

#### Loading words, and creating the neural network:
1. Make a file where each line has a comma seperated word pair, name it words. 
  2. Eg: line1: one, two ; line2: two, three
2. Make another file where each line has a similarity of the word pair in the same line as above mentioned file. Name it sims.
3. On the command line, run (from folder WordSimilarity) `python wordSim/wordSimCalc.py --create-df`.
4. After running wordSimCalc, the neural network (I'll also call it a model) will be exported to the file 'wordsim.pkl'.

#### Tuning the neural network:
Just run `python wordSim/tune.py` and enter the feedback requested, until you feel like you've done enough feedback.
* This will retrain the neural network, and export the new version to the file 'tunedwordsim.pkl'

#### Enjoying the results:
* Run `python wordSim/useNeuralNetwork.py`
  * By default, the model create from the plain Word Similarity network will be used. 
    * To use the 'tuned' one, run `python wordSim/useNeuralNetwork.py --use-tuned`.
  * To use some other model file (which isn't created by default), run `python wordSim/useNeuralNetwork.py --custom <filename>`.


<dl>
<br></br>
<br></br>
<p style="font-size:13px">This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.</p>
<p style="font-size:13px">To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.</p>
</dl>
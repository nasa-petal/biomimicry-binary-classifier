# SVM Binary Classifier
[AllenAI](https://allenai.org) gave us the code for this project. 

The purpose of this program is to classify various scientific papers into categories based on whether they are related to biomimicry or not.


We used the [golden.json](https://github.com/nasa-petal/data-collection-and-prep/blob/main/golden.json) file as training data and ran the program on Google Colab.

In the first attempt, we used only the first 500 rows in the data file, and the resulting f1 scores were very low (). We then used the first 1000 rows to gain more data. We realized that all of the data points we collected from only using the first rows were marked as "Y" for isBiomimicry, and therefore our data sets were skewed. So, we then used the first 500 of both the rows marked as "Y" and the rows marked as "N" to have a balanced collection of data.  



|                       | Fold 1     | Fold 2     | Fold 3     | Fold 4     |
|-----------------------|------------|------------|------------|------------|
| 500                   | 0.08695652 | 0.23076923 | 0.15384615 | 0.         |
| 1000                  | 0.35555556 | 0.23809524 | 0.04878049 | 0.15       |
| 500 of each | 0.85920578 | 0.83397683 | 0.84046693 | 0.86486486 |

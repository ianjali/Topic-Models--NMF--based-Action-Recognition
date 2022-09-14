{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.svm import SVC\n",
    "import numpy as np\n",
    "from sklearn.pipeline import Pipeline\n",
    "#def evaluate(Xtrain, Ytrain, Xval, Yval):\n",
    "#    print(\"Training with SVM\")\n",
    "#    clf = SVC(1,kernel=\"linear\",verbose=True)\n",
    "#    clf.fit(Xtrain, Ytrain)\n",
    "#    confusion_matrix = np.zeros((6,6))\n",
    "#    \n",
    "#    pred = clf.predict(Xval)\n",
    "#    \n",
    "#    correct = 0\n",
    "#    \n",
    "#    for i in range(len(Yval)):\n",
    "#        if pred[i] == Yval[i]:\n",
    "#            correct +=1\n",
    "#        confusion_matrix[pred[i],Yval[i]] +=1\n",
    "#    print(\"%d/%d Correct\" % (correct, len(pred)))\n",
    "#    print(\"Accuracy =\", correct / len(pred))\n",
    "#\n",
    "#    print(\"Confusion matrix\")\n",
    "#    print(confusion_matrix)\n",
    "\n",
    "# function to make predictions on the validation set and evaluate the results\n",
    "# Xval is the features dataframe (nvideos, 50), Yval is the labels dataframe \n",
    "def evaluate(clf, Xval, Yval):\n",
    "    print(\"Evaluate on validation set\")\n",
    "    confusion_matrix = np.zeros((6,6))\n",
    "    pred = clf.predict(Xval)\n",
    "    #pipeline=Pipeline([('classifier',MultinomialNB())])\n",
    "    #pipeline.fit()\n",
    "    correct = 0\n",
    "    \n",
    "    for i in range(len(Yval)):\n",
    "        if pred[i] == int(Yval.iloc[i]):\n",
    "            correct +=1\n",
    "        confusion_matrix[pred[i],int(Yval.iloc[i])] +=1\n",
    "    print(\"%d/%d Correct\" % (correct, len(pred)))\n",
    "    print(\"Accuracy = {} \".format( float(correct) / len(pred) ))\n",
    "    print(\"Confusion matrix\")\n",
    "    print(confusion_matrix)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

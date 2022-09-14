{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import os\n",
    "import pickle\n",
    "import csv\n",
    "\n",
    "from sklearn.svm import SVC\n",
    "\n",
    "# function to read the kth_sequences.txt file and return the dictionary of \n",
    "# frame sequences where actions occur.\n",
    "# returns d: dictionary eg {'filename': '1-10, 20-30, 50-100'}\n",
    "def read_seq(filePath):\n",
    "    d = {}\n",
    "    with open(filePath,'r') as tsvin:\n",
    "        tsvin = csv.reader(tsvin, delimiter='\\t')\n",
    "        #csvout = csv.writer(csvout)\n",
    "        for row in tsvin:\n",
    "            # if row is not and empty list then add the\n",
    "            if len(row)>0:\n",
    "                key = row[0].strip()\n",
    "                value = row[-1].strip()\n",
    "                d[key] = value\n",
    "    print(len(d))\n",
    "    return (d)\n",
    "\n",
    "\n",
    "# function to return the label (int) given the name of the video\n",
    "def get_video_label(srcVid):\n",
    "    if \"boxing\" in srcVid:\n",
    "        return 0\n",
    "    elif \"handclapping\" in srcVid:\n",
    "        return 1\n",
    "    elif \"handwaving\" in srcVid:\n",
    "        return 2\n",
    "    elif \"jogging\" in srcVid:\n",
    "        return 3\n",
    "    elif \"running\" in srcVid:\n",
    "        return 4\n",
    "    elif \"walking\" in srcVid:\n",
    "        return 5\n",
    "\n",
    "# load the data given the path of the pkl file.\n",
    "def create_labels(dataset_path):\n",
    "    dataset = pickle.load(open(dataset_path,\"rb\"))\n",
    "    X = []\n",
    "    Y = []\n",
    "    for video in dataset:\n",
    "        X.append(video[\"features\"])\n",
    "    for video in dataset:\n",
    "        label = get_video_label(video[\"filename\"])\n",
    "        Y.append(label)\n",
    "    return X, Y\n"
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

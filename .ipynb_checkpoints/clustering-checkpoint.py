{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pickle\n",
    "from sklearn.cluster import KMeans\n",
    "\n",
    "# function to extract magnitude space vectors and angle space vectors\n",
    "# It does not return any labeling information. Hence used only for finding \n",
    "# cluster centres.\n",
    "# optical_flow_data_path: \n",
    "def extract_vec_points(optical_flow_data_path):\n",
    "    # Convert into magnitude space points and angle space points.\n",
    "    mag_vecs = []\n",
    "    ang_vecs = []\n",
    "    data = pickle.load(open(optical_flow_data_path,\"rb\"))\n",
    "    # Iterate over the videos contained in the dictionary\n",
    "    for k, v in data.items():\n",
    "        # Iterate over the 2x16x12 dimensional matrices, for each flow feature\n",
    "        for flow_feature in v:\n",
    "            mag_vecs.append(flow_feature[0,...].ravel())\n",
    "            ang_vecs.append(flow_feature[1,...].ravel())\n",
    "        print(\"Video {} : Size_mag : {}\".format(k, len(mag_vecs)))\n",
    "    print(\"Done for {}\".format(optical_flow_data_path))\n",
    "    return np.array(mag_vecs), np.array(ang_vecs)\n",
    "\n",
    "\n",
    "# function to find the clusters using KMeans\n",
    "# vecs: any dataframe representing the input space points\n",
    "# nclusters: No. of clusters to be formed\n",
    "# returns the KMeans object, containing the \n",
    "def make_codebook(vecs, nclusters):\n",
    "#    pickle.dump(train_keypoints, open(os.path.join('data',target_file), \"wb\"))\n",
    "    print(\"Clustering using KMeans: Input size -> {} :: n_clusters -> {}\"\\\n",
    "          .format(vecs.shape, nclusters))   \n",
    "    \n",
    "    #train_features = pickle.load(open(keypoints_path, \"rb\"))\n",
    "    #clustering with k-means\n",
    "    #kmeans = KMeans(init='k-means++', n_clusters=200, n_init=10, n_jobs=2, verbose=1)\n",
    "    kmeans = KMeans(n_clusters=nclusters, n_init=10, n_jobs=2)\n",
    "    kmeans.fit(vecs)\n",
    "    print(\"Done Clustering!\")\n",
    "    return kmeans\n",
    "    \n"
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

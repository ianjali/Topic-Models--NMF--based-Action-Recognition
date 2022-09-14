{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import cv2\n",
    "import sys\n",
    "import numpy as np\n",
    "from utils import read_seq\n",
    "\n",
    "# function to extract optical flow based grid features from training set\n",
    "# and save the features in a dictionary on disk.\n",
    "# applicable only for the training set\n",
    "def extract_flow_seq_train(dataset_base, grid_size=10):\n",
    "    seq_path = os.path.join(dataset_base,'kth_sequences.txt')\n",
    "    dataset_path = os.path.join(dataset_base, 'kth_actions_train')\n",
    "    filenames = os.listdir(dataset_path)\n",
    "        \n",
    "    #farneback_params = dict(winsize = 20, iterations=1,\n",
    "    #    flags=cv2.OPTFLOW_FARNEBACK_GAUSSIAN, levels=1,\n",
    "    #    pyr_scale=0.5, poly_n=5, poly_sigma=1.1, flow=None)\n",
    "    n_processed_files = 0\n",
    "    seq = read_seq(seq_path)\n",
    "    features = {}  # save features in this dictionary\n",
    "    for filename in filenames:\n",
    "        filepath = os.path.join(dataset_path, filename)\n",
    "        ##print(filepath)\n",
    "        cap = cv2.VideoCapture(filepath)\n",
    "        if not cap.isOpened():\n",
    "            continue\n",
    "        dimensions = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))\n",
    "        fps = cap.get(cv2.CAP_PROP_FPS)\n",
    "        nframes = cap.get(cv2.CAP_PROP_FRAME_COUNT)\n",
    "        #ret,prev_frame = cap.read()\n",
    "        #prev_frame = cv2.cvtColor(prev_frame,cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "        # Store features in current file.\n",
    "        features_current_file = []\n",
    "        start_frames = []\n",
    "        end_frames = []\n",
    "        # Get the action sequences from the sequences dictionary.\n",
    "        key = filename.rsplit('_',1)[0]\n",
    "#        action_seq_str = seq[filename]\n",
    "        action_seq_str = seq[key]\n",
    "        for marker in action_seq_str.split(','):\n",
    "            temp = marker.split('-')        # ' 120-190'\n",
    "            start_frames.append(int(temp[0]))   # 120\n",
    "            end_frames.append(int(temp[1]))\n",
    "        \n",
    "        # Iterate over the sequences to get the optical flow features.\n",
    "        for i, stime in enumerate(start_frames):\n",
    "            cap.set(cv2.CAP_PROP_POS_FRAMES, stime)\n",
    "            ret, prev_frame = cap.read()\n",
    "\n",
    "            prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)\n",
    "            stime += 1\n",
    "       \n",
    "            while(cap.isOpened() and stime <= end_frames[i]):\n",
    "                ret, frame = cap.read()\n",
    "                if not ret:\n",
    "                    break\n",
    "                curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "        \n",
    "                flow = cv2.calcOpticalFlowFarneback(prev_frame,curr_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)\n",
    "                mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])\n",
    "                # stack sliced arrays along the first axis (2, 12, 16)\n",
    "                sliced_flow = np.stack(( mag[::grid_size, ::grid_size], \\\n",
    "                                        ang[::grid_size, ::grid_size]), axis=0)\n",
    "                \n",
    "                #feature.append(sliced_flow[..., 0].ravel())\n",
    "                #feature.append(sliced_flow[..., 1].ravel())\n",
    "                #feature = np.array(feature)\n",
    "                features_current_file.append(sliced_flow)\n",
    "                stime +=1\n",
    "                prev_frame = curr_frame\n",
    "        cap.release()\n",
    "        cv2.destroyAllWindows()\n",
    "        features[filename] = features_current_file\n",
    "        n_processed_files += 1\n",
    "        print(\"Done {} files : {}\".format( str(n_processed_files), filename))\n",
    "    \n",
    "    return features\n",
    "            \n",
    "# function to extract optical flow based grid features from validation/test set\n",
    "# Consider Background subtraction, using BGThreshold\n",
    "def extract_flow_val(dataset_base, bgThresh, grid_size=10, partition=\"validation\"):\n",
    "    if partition == 'validation':\n",
    "        dataset_path = os.path.join(dataset_base, 'kth_actions_validation')\n",
    "    elif partition == 'testing':\n",
    "        dataset_path = os.path.join(dataset_base, 'kth_actions_test')\n",
    "    else:\n",
    "        print(\"Invalid partition name! Abort! \")\n",
    "        sys.exit(0)\n",
    "        \n",
    "    filenames = os.listdir(dataset_path)\n",
    "        \n",
    "    #farneback_params = dict(winsize = 20, iterations=1,\n",
    "    #    flags=cv2.OPTFLOW_FARNEBACK_GAUSSIAN, levels=1,\n",
    "    #    pyr_scale=0.5, poly_n=5, poly_sigma=1.1, flow=None)\n",
    "    n_processed_files = 0\n",
    "    \n",
    "    features = {}\n",
    "    for filename in filenames:\n",
    "        filepath = os.path.join(dataset_path, filename)\n",
    "        ##print(filepath)\n",
    "        cap = cv2.VideoCapture(filepath)\n",
    "        if not cap.isOpened():\n",
    "            continue\n",
    "        dimensions = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))\n",
    "        fps = cap.get(cv2.CAP_PROP_FPS)\n",
    "        nframes = cap.get(cv2.CAP_PROP_FRAME_COUNT)\n",
    "        #ret,prev_frame = cap.read()\n",
    "        #prev_frame = cv2.cvtColor(prev_frame,cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "        # Store features in current file.\n",
    "        features_current_file = []\n",
    "        start_frames = [0]\n",
    "        end_frames = [nframes]\n",
    "        \n",
    "        for i, stime in enumerate(start_frames):\n",
    "            fgbg = cv2.createBackgroundSubtractorMOG2()\n",
    "            cap.set(cv2.CAP_PROP_POS_FRAMES, stime)\n",
    "            ret, prev_frame = cap.read()\n",
    "            fgmask = fgbg.apply(prev_frame)\n",
    "\n",
    "            prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)\n",
    "            stime = stime + 1\n",
    "            while(cap.isOpened() and stime <= end_frames[i]):\n",
    "                ret, frame = cap.read()\n",
    "                if not ret:\n",
    "                    break\n",
    "                curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "                    \n",
    "                # To find the background mask and skip the frame if foreground is absent\n",
    "                fgmask = fgbg.apply(frame)\n",
    "                if np.sum(fgmask)<bgThresh:\n",
    "                    #print (\"BG frame skipped !!\")\n",
    "                    prev_frame = curr_frame\n",
    "                    stime += 1\n",
    "                    continue\n",
    "        \n",
    "                flow = cv2.calcOpticalFlowFarneback(prev_frame,curr_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)\n",
    "                mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])\n",
    "                #feature = []\n",
    "                # stack sliced arrays along the first axis (2, 12, 16)\n",
    "                sliced_flow = np.stack(( mag[::grid_size, ::grid_size], \\\n",
    "                                        ang[::grid_size, ::grid_size]), axis=0)\n",
    "                \n",
    "                features_current_file.append(sliced_flow)\n",
    "                stime = stime + 1\n",
    "                prev_frame = curr_frame\n",
    "        cap.release()\n",
    "        cv2.destroyAllWindows()\n",
    "        features[filename] = features_current_file\n",
    "\n",
    "        n_processed_files += 1\n",
    "        #if n_processed_files % 30 == 0:\n",
    "        print(\"Done {} files : {}\".format( str(n_processed_files), filename))\n",
    "    \n",
    "    return features\n"
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

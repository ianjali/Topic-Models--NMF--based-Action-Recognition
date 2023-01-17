# Topic Models (NMF) based Action Recognition
  Applying topic models for unsupervised action recognition in videos.
  
  * cal_optical_flow_seq.py : python file to extract training, validation and testing set features 
    *  ***extract_flow_seq_train*** 
       * Extract the labelled frames of action using kth_sequences file 
       * From the start to end frame compute the dense optical flow using the Gunnar Farneback's algorithm based on the specified grid size.
       *   return the feature vector containing magnitude and angle of the action   

* clustering.py
  * ***extract_vec_points*** 
      * extract optical flow vectors i.e magnitude and angle of consecutive frames for all videos in training dataset
      *   

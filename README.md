## Introduction

The widespread availability of social media content and advanced technology has enabled the rapid proliferation of deepfakes, contributing to the dissemination of disinformation and hoaxes. This project aims to develop a robust system capable of distinguishing between authentic and fabricated content in the age of social media.

The proposed approach follows a multi-step process to enhance classification accuracy:

1. **Metadata Retrieval**: The system first retrieves the metadata associated with the input image, including information such as the compression level, image dimensions, and other relevant details.

2. **Error Level Analysis (ELA)**: An Error Level Analysis is conducted to detect potential modifications in the image and determine the compression ratio disparity between the original and fake images. This step is crucial because the compression methods used for original and fake images typically differ.

3. **Feature Extraction using Convolutional Neural Networks (CNNs)**: Convolutional Neural Networks (CNNs) are employed to extract high-level features from the images. These deep learning models are capable of automatically learning and capturing intricate patterns and details that may not be easily discernible using conventional methods.

4. **Classification using Support Vector Machines (SVMs) and K-Nearest Neighbors (KNN)**: The deep features extracted by the CNNs are then fed into Support Vector Machines (SVMs) and K-Nearest Neighbors (KNN) classifiers for the final classification. These machine learning algorithms are trained on datasets comprising both fake and original images, enabling them to discern manipulations within images effectively.

5. **Hyper-parameter Optimization**: Rigorous hyper-parameter optimization is performed to ensure optimal performance of the classifiers, further enhancing the system's accuracy.

By integrating these components, the proposed framework offers a comprehensive solution to the challenge of deepfake detection in social media content. It leverages both traditional techniques like Error Level Analysis and advanced deep learning algorithms to effectively counter the growing sophistication of deepfake generation techniques and safeguard against the dissemination of deceptive audiovisual content.

## Usage

To run this project, you'll need to have an NVIDIA CUDA-enabled GPU installed on your system. Once you have the required hardware, follow these steps:

1. Clone the repository: 
2.  Navigate to the project directory:
3.  Create a new virtual environment (optional but recommended):
4.  Install the required dependencies:

 Make sure you have the latest NVIDIA drivers and CUDA toolkit installed on your system before running the scripts.

5. Preprocess the data:

This script will preprocess the dataset, including retrieving metadata and performing Error Level Analysis.

7. Train the model:
8. Evaluate the trained model on a test dataset and provide performance metrics.

Note: Depending on the size of your dataset and the complexity of the models, the training and evaluation processes may take a significant amount of time. It's recommended to use a powerful GPU with sufficient VRAM for optimal performance.

## Contributors

This project is the result of a collaborative effort by a group of six members, each contributing to specific aspects of the development process. The contributions of each member are as follows:

- **Shubham Attri**: Shubham was responsible for implementing the Error Level Analysis (ELA) component of the project. He developed the code for detecting potential modifications in images and determining the compression ratio disparity between original and fake images.

- **Trilok Singh**: Trilok's focus was on the feature extraction process using Convolutional Neural Networks (CNNs). He implemented and fine-tuned various CNN architectures, such as ResNet, SqueezeNet, and GoogLeNet, to extract high-level features from the images effectively.

- **Adish Jain**: Adish worked on the classification phase of the project. He implemented and optimized the Support Vector Machine (SVM) and K-Nearest Neighbors (KNN) classifiers, ensuring accurate classification of the deep features extracted by the CNNs.

- **Dhruv Garg**: Dhruv's contribution was in the area of data preprocessing and augmentation. He developed scripts to preprocess the dataset, including retrieving metadata, and implemented various data augmentation techniques to improve the model's generalization performance.

- **Archit Garg**: Archit was responsible for the overall integration and deployment of the project. He coordinated the efforts of the team members, ensuring seamless integration of the different components, and set up the deployment pipeline for the final system.

- **Raj Gupta**: Raj focused on the evaluation and testing phase of the project. He designed and implemented the evaluation metrics, conducted rigorous testing on various datasets, and documented the performance results and comparisons with existing state-of-the-art methods.

The collaborative effort of this group, with each member contributing their expertise in specific areas, has resulted in a comprehensive and robust deepfake detection system that leverages advanced machine learning and deep learning techniques.

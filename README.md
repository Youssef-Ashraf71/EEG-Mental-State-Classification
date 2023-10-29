# EEG Signal Processing and Mental State Classification Web Application

This project focuses on the processing of raw EEG (Electroencephalogram) brain signals, extracting relevant features, and using deep learning to classify a user's mental state or intention. The project is divided into two main parts: signal preprocessing and model development, with the added capability of actuator control and a bonus mobile application for visualizing user intentions.

## Part 1: Signal Preprocessing and Feature Extraction

### EEG Data Acquisition
In the initial phase of the project, raw EEG data is collected or obtained from suitable sources. This data serves as the foundation for understanding the user's brain activity.

### Signal Preprocessing
- **Standerization**
- **Bandpass Filtering**: Unwanted frequency components are filtered out using bandpass filters, focusing on the frequency range relevant to the study(Alpha Waves from 8-->12 HZ.


### Signal Visualization
A user-friendly graphical user interface (GUI) is implemented to visualize and compare the filtered EEG signals with unfiltered ones. This helps users gain insights into the impact of preprocessing on signal quality.
![image](https://github.com/Youssef-Ashraf71/Task2_Medical/assets/83988379/aca5f826-388f-45d6-949f-4dd847a515dc)



## Part 2: Model Development and Actuator Control
### Model and Deep Learning Algorithm

The provided code snippet demonstrates the use of a deep learning model to classify eye states based on the EEG data. The model architecture and training process are as follows:

### Data Splitting

The dataset is divided into training and testing sets using an 80-20 ratio, ensuring a suitable separation for model training and evaluation.

### Data Reshaping

The EEG data is reshaped to have dimensions of (samples, 14, 1). This indicates that there are 14 channels (electrodes) and 1 feature for each channel, preparing the data for deep learning model processing.

### Model Architecture

The deep learning model for classifying eye states follows a specific architecture:

- **Input Layer**: The model begins with an input layer that accepts data with a shape of (14, 1).

- **Dense Layer 1**: A dense layer with 64 units and ReLU activation is applied. L2 regularization is incorporated to enhance model generalization.

- **Bidirectional LSTM Layers**: Two Bidirectional Long Short-Term Memory (LSTM) layers are utilized for capturing temporal dependencies in the EEG data. The first LSTM layer consists of 256 units, and the second has 128 units. Both layers return sequences, enabling them to effectively process sequential data.

- **Dropout Layers**: Dropout layers with a dropout rate of 0.2 are strategically inserted after the LSTM layers. This regularization technique helps mitigate overfitting, enhancing the model's robustness.

- **Flatten Layer**: A flatten layer is introduced to transform the output from the LSTM layers into a format suitable for the subsequent dense layers.

- **Dense Layer 2**: The model includes a dense layer with 128 units and ReLU activation. This layer is designed to capture intricate patterns in the data.

- **Output Layer**: The final layer is a dense layer with a single unit and sigmoid activation function. This configuration is well-suited for binary classification tasks, as it produces a probability output, allowing the model to predict eye states.

### Model Training

The model is trained with the following settings:

- **Loss Function**: Binary cross-entropy is employed as the loss function, which is standard for binary classification tasks.

- **Evaluation Metric**: The model's performance is evaluated using accuracy, which measures the fraction of correctly classified instances.

- **Optimizer**: The Adam optimizer is selected as the optimization algorithm, with a learning rate set to 0.001. This optimizer efficiently adjusts model weights during training.

- **Callbacks**:
  - **Early Stopping**: Early stopping is implemented to monitor the validation loss and stop training if it ceases to improve. This is important for preventing overfitting.
  - **Model Checkpointing**: Model checkpointing saves the best model based on validation accuracy.
  - **Learning Rate Scheduler**: A learning rate scheduler is used to adjust the learning rate during training. It gradually reduces the learning rate, which can lead to better convergence.

- **Training Duration**: The model is trained for 100 epochs, allowing it to learn and adapt to the patterns present in the EEG data.

This robust deep learning model architecture and training process ensure effective classification of eye states based on EEG data, making it a valuable tool for various applications.

### Real-time Classification
- The trained model is implemented to classify the user's ongoing EEG signals in real-time.
- Continuous processing of incoming EEG data allows for the prediction of the user's current Eye state .
![image](https://github.com/Youssef-Ashraf71/Task2_Medical/assets/83988379/004ba914-7125-4e69-bef7-9524d6e181f7)

### Actuator Control
- An actuator control mechanism is put in place to translate the model's output into appropriate actions. These actions include controlling external servo.


## Web Application Deployment

A web application is built using Flask to deploy the model. Users can input EEG data, and the application displays the user's current eye state or protection level. This web app serves as a practical demonstration of the project's capabilities.

---

By combining signal processing, Deep learning, and actuator control, this project provides a comprehensive solution for understanding and utilizing EEG data to classify a user's eye state and take corresponding actions. The web application offers a practical and user-friendly interface for real-world applications.

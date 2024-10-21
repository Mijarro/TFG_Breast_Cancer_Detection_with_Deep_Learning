# Breast Cancer Detection with Deep Learning

This project explores the use of Deep Learning and machine learning techniques for the detection and categorization of breast cancer, utilizing digital mammograms and digital breast tomosynthesis as data sources. The research aims to demonstrate how neural networks can be applied to address critical societal issues, moving beyond conventional uses of technology.

## Project Description

The project presents and analyzes four different neural network architectures designed to classify a dataset of digital mammograms into three categories: cancer cases, benign tumors, and healthy patients. Various techniques were employed throughout the development to enhance model performance, including:

- *Transfer learning*
- *Fine-tuning*
- Data augmentation
- Cross-validation
- Custom loss functions
- *Dropout*, among others

The objective was to achieve the highest possible accuracy in image detection and classification.

## Results and Conclusions

The results show that two of the proposed architectures outperformed existing CAD (computer-aided detection) systems currently used by radiologists for breast cancer detection. This demonstrates the potential of Deep Learning techniques to make a significant contribution to medical diagnosis.

### Performance Comparison of Neural Networks

| **Neural Network**       | **Base Data**                                | **Data Augmentation**                          | **Normal Precision (%)** | **Benign & Cancer Precision (%)** |
|--------------------------|----------------------------------------------|------------------------------------------------|--------------------------|-----------------------------------|
| **Dense UNet3D**         | Loss: 0.0345 <br> Accuracy: 97.02            | Loss: 0.0945 <br> Accuracy: 94.43              | Base: 99.69 <br> DA: 99.67 | Base: 86.18 <br> DA: 65.96         |
| **Parallel UNet**        | Loss: 0.0385 <br> Accuracy: 96.76            | Loss: 0.0641 <br> Accuracy: 94.56              | Base: 99.72 <br> DA: 99.44 | Base: 72.68 <br> DA: 73.26         |
| **Parallel InceptionV3** | Loss: 0.0286 <br> Accuracy: 98.87            | Loss: 0.0238 <br> Accuracy: 98.83              | Base: 99.97 <br> DA: 99.87 | Base: 91.75 <br> DA: 94.81         |
| **Parallel ResNetV2**    | Loss: 0.0272 <br> Accuracy: 98.33            | Loss: 0.0350 <br> Accuracy: 98.08              | Base: 99.94 <br> DA: 99.87 | Base: 91.25 <br> DA: 92.31         |

*Table 1: Performance comparison of different neural networks on two datasets, showing precision for the normal class and precision for the benign and cancer classes.*

## Keywords

Breast cancer detection, Deep Learning, machine learning, *fine-tuning*.

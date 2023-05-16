# Arrhythmia Detection using IoT

## Introduction

According to the Indian Rhythm Society, Arrhythmia turns out to be a significant health concern in India, being prevalent in around 10-15% of the adult population in the country. Out of the 5 Major types of Arrhythmia including Atrial Fibrillation, Ventricular tachycardia, Atrial Flutter, Bradycardia and Premature Ventricular Contractions, atrial fibrillation and ventricular arrhythmias are the most common types found in the Indian Population. 

The proposed approach acts as the solution to this issue by using ECG Signals as the input as these can identify abnormal heartbeats, help in assessing the severity and monitor the effectiveness of treatment provided after diagnosis. The system can also detect the possibility of Arrhythmia with high accuracy and provide a reasonable time interval to diagnose the patient along with alerts provided to the concerned caretakers.

## Objectives and Goals

The main objective of this project is to incorporate the concept of the Internet of Things to predict the chances of conditions of Arrhythmia along with its classification using ECG Signals as input. The proposed approach automates the process of detection, making it more feasible and affordable without any discrepancies in the accuracy of results. The system is designed to perform early detection with significant confidence levels to provide alerts and avoid further complications.

## Applications

The proposed approach could be used to obtain ECG Signals from the commonly used equipment and use the same for early prediction of the possibility of Arrhythmic conditions. In the case of detecting arrhythmia with a significant confidence rate, alerts could be provided for timely diagnosis. The hardware setup is feasible and easy to use. The overall design has been framed to work from remote locations in the worst cases. In case of requiring a second opinion, the data can also be displayed in a professional dashboard and availed to doctors for efficient remedies.

## Features

- Early prediction of Arrhythmic conditions with confidence levels is enabled
- Classification of the type of Arrhythmia is also provided based on confidence levels
- Real-time data collection, processing and storage in the cloud
- Ease of use, feasible and affordable (relative to the products in the market)
- Alerts are provided when detected, data dashboard is available with necessary signal details

## Design

### Components Used

#### BioAmp-EXG-Pill

BioAmp EXG Pill is an Analog Front End board for acquiring Biopotential Signals with any MicroController Unit in presence of an ADC. It can record publication-grade Biopotential Signals including ECG, EMG, EOG and EEG without any dedicated filters in Hardware or Software Mode.

![BioAmp-EXG-Pill](./images/bioamp_exg_pill.jpg)

#### ESP8266 (NodeMCU)

ESP8266 is a Wi-Fi microchip built with TCP/IP networking software and microcontroller capabilities. It is generally used as the WiFi module because of its low cost and small size. It is capable of being interfaced with microcontroller boards through Serial Port. It is widely used in autonomous projects due to its compact features. Since ESP8266 supports APSD, it is the ideal choice for VoIP applications and Bluetooth interfaces.

![ESP8266 (NodeMCU)](./images/nodemcu.jpg)

#### Gel electrodes

Due to the minute nature of Electrical signals produced by Electrocardiogram electrodes, capturing the same, a high level of accuracy is required. These Gel electrodes carry electric current from the skin to the measuring instrument and are held by sticky patches to the skin to measure the electrical activity.

![Gel Electrodes](./images/gel_electrodes.jpg)


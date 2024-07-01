# Attention Detection Buzzer

By- Rhythm

## Contents

1. [Introduction](#introduction)
2. [Model Training & Downloading (Teachable Machines)](#model-training--downloading-teachable-machines)
3. [Making Arduino Sketch](#making-arduino-sketch)
4. [Writing Python Script](#writing-python-script)
5. [Collecting & Assembling Hardware](#collecting--assembling-hardware)
6. [Loading The Code to Arduino & Testing](#loading-the-code-to-arduino--testing)
7. [Conclusion](#conclusion)

## Introduction

### 1.1 Intro to Project

The system utilizes a machine learning model trained with a Teachable Machine to analyze live video feeds from a laptop camera. By interpreting facial expressions and eye movement patterns, the model determines whether the student is attentive. The Arduino microcontroller interfaces with the model's predictions and controls hardware components. Upon detecting inattentiveness, the system triggers a buzzer to alert the student or the instructor, serving as a gentle reminder. Conversely, when the student is deemed attentive, an LED is activated, providing positive reinforcement. This documentation will guide you through the setup process, explain the necessary components, and offer insights into the software and hardware integration. Whether you're a student, educator, or hobbyist, this project is an engaging exploration of machine learning and hardware interfacing.

### 1.2 Intro to Software Used

#### a) Visual Studio Code
Visual Studio Code is a free, lightweight code editor with powerful writing and debugging features. It supports various programming languages and extensions, making it a popular choice among developers.

#### b) Teachable Machines
Teachable Machines is a simple online tool by Google that helps you train your computer to recognize and respond to different sounds, images, or poses without coding.

#### c) Arduino IDE
Arduino IDE is a software platform that allows you to write, upload, and run code on Arduino microcontrollers, enabling you to create interactive electronic projects without advanced programming knowledge.

## Model Training & Downloading (Teachable Machines)

We will use the following steps to build a model:

1. Go to the [Teachable Machines website](https://teachablemachine.withgoogle.com).
2. Select the type of project you want to create: Image.
3. Collect images for each class you want to recognize and upload them.
4. Label each class or category in your dataset.
5. Click on the "Train Model" button to let Teachable Machines train a model based on your data.
6. After training, you can test your model using the built-in testing interface to see how well it recognizes new examples.
7. Once satisfied with the performance, export your model. Teachable Machines provides options to export models for TensorFlow.js, TensorFlow Lite, or as a link to use in your projects.

## Making Arduino Sketch

After making the model, our next step will be writing an Arduino script for our Arduino Uno which can take serial commands and move motors accordingly.

## Writing Python Script

Now our next step is making a Python script. Below is the script and its explanations:


![Screenshot 2024-07-02 035731](https://github.com/Rhythmbellic/Attention-Detection-Buzzer/assets/92723976/d0539d3e-32a6-427c-86d9-d6aed60c46b5)



## Collecting & Assembling Hardware

### Hardware Requirements
- Arduino Uno
- Breadboard
- Jumper Wires
- LED
- Buzzer

### Assembling
1. First, put an LED & buzzer on the breadboard.
2. Then connect wire with GND of Arduino to straightly connected breadboard pins.
3. Connect 2 jumper wires to the line and connect to the negative terminal of both LED and buzzer.
4. Connect LED positive to Arduino pin 4 & buzzer to Arduino pin 5.

## Loading The Code to Arduino & Testing


Now all the important parts are done. Just connect the cable to Arduino and load the Arduino sketch into the Uno, then start the Python script and test.


https://github.com/Rhythmbellic/Attention-Detection-Buzzer/assets/92723976/90e1d666-5274-4f88-8715-b97e5197087b




## Conclusion

Now you can make this Attention Detection Buzzer by yourself. Try adding more things to it, play with it, and discover where you can use it.

Thank You,

Rhythm

# Stanford Solar Forecasting Dataset

![sunnygif](/sample%20images/sunny_day_demo_1.gif)
![cloudygif](/sample%20images/cloudy_day_demo_1.gif)
![sunnygif](/sample%20images/sunny_day_demo_2.gif)
![cloudygif](/sample%20images/cloudy_day_demo_2.gif)
![sunnygif](/sample%20images/sunny_day_demo_3.gif)
![cloudygif](/sample%20images/cloudy_day_demo_3.gif)
![sunnygif](/sample%20images/sunny_day_demo_4.gif)
![cloudygif](/sample%20images/cloudy_day_demo_4.gif)
![sunnygif](/sample%20images/sunny_day_demo_5.gif)
![cloudygif](/sample%20images/cloudy_day_demo_5.gif)
![sunnygif](/sample%20images/sunny_day_demo_6.gif)
![cloudygif](/sample%20images/cloudy_day_demo_6.gif)

This repo describes the solar forecasting dataset collected at Stanford University. 

## Dataset Description

This dataset is a collection of sky images and PV power output for solar forecasting from Stanford University. The data consist of three years (2017–2019) of quality-controlled, 1-min resolution in sky images taken from a ground-based fish-eye camera and power output measurement from a 30 kW rooftop PV array ~125 m away from the camera at Stanford Campus. We hope that the dataset will enable researchers to tackle the problem of short-term local ground camera-based solar power prediction.

- **Homepage:**
[Environmental Assessment and Optimization (EAO) Group]( https://eao.stanford.edu/short-term-solar-forecasting)

- **Repository:**
[EAO Group](https://github.com/Stanford-EAO);
[SUNSET Model](https://github.com/YuchiSun/SUNSET)

- **Publications:**
[Solar Nowcast](https://pubs.rsc.org/en/content/articlehtml/2018/ee/c7ee03420b);
[Solar Forecast](https://www.sciencedirect.com/science/article/pii/S0038092X19306164);
[Data Fusion for Solar Forecasting](https://aip.scitation.org/doi/full/10.1063/1.5122796);
[Sky Condition Submodels](https://aip.scitation.org/doi/full/10.1063/5.0014016);
[Resampling and Data Augmentation](https://www.sciencedirect.com/science/article/pii/S0038092X21004795)

### Dataset Summary

#### Sky Images

The sky images are frames from a video recorded by a ground-based 6-megapixel 360-degree fish-eye camera (Hikvision model DS-2CD6362F-IV) installed on the roof of the Green Earth Sciences Building (GESB) at Stanford University. Camera aperture, white balance and dynamic range are held constant. Fig.1 gives examples of sky images in different weather conditions, and shows the camera and PV panels used for the dataset. 

<div align=center><image src="https://ars.els-cdn.com/content/image/1-s2.0-S0038092X19306164-gr1.jpg"></div>
  
<p align=center>
Fig.1.1. Photos of sky images and research equipment. 
(A. Sky image captured on a clear day at 12:51:00, Mar.14.2017. 
B. Sky image of a cloudy day captured at 10:50:00 Mar.16.2017. 
C. Fish-eye camera used for sky imaging. 
D. PV panels used in this study.)
</p>

Videos are captured in a resolution of 1536 × 1536 pixels at 20 frames per second (fps). It is compressed with the h.264 standard to a bit rate of 2 Mbps. Images (.jpg) are extracted at a chosen sampling frequency, and down-sampled to a resolution of 64 × 64 pixels, which was previously shown to be acceptable for PV output forecast, while retaining a reasonable training time. Images are retained between the hours of 6:00 AM and 8:00 PM local time (PST).

#### PV Output 

The PV output data are collected from solar panel arrays ∼125 m away from the camera, on the top of the Jen-Hsun Huang Engineering Center at Stanford University. The poly-crystalline panels are rated at 30.1 kW-DC, with an elevation and azimuth angle at 22.5° and 195° respectively.


## Demonstration of Use Cases

### Sun and Clouds Identification

We develop a physics-based non-parametric classifier based on the threshold of the fractional cloudiness in a sky. We utilize a modified NRBR threshold with the background subtraction method to classify input images into different sky conditions as showed in fig. 2.1.

![sunnygif](/sample%20images/sunny_day_demo_1.gif)
![cloudygif](/sample%20images/cloudy_day_demo_1.gif)

### Nowcast and Forecast Using SUNSET Model

Images of the sky provide information on current and future cloud coverage, and are potentially useful in inferring PV generation. Our group has developed a specialized convolutional neural network model named SUNSET (Stanford University Neural Network for Solar Electricity Trend) for PV output forecast. The following two projects have been published, with more research projects going on.

#### Solar Power Nowcast

We explore convolutional neural networks (CNN) to correlate PV output to contemporaneous images of the sky (a “now-cast”). We demonstrate that sky images are useful in inferring PV panel output, and CNN is a suitable structure in this application. Parts of the results are showed in fig.2.2 and fig.2.3 for sunny and cloudy days respectively.

![nowcast sunny](https://github.com/yuhao-nie/Stanford-solar-forecasting-dataset/blob/main/sample%20images/sunset_nowcast_sunny_days.gif)
<p align=center>
Fig. 2.2 Nowcast in Sunny Days 
</p>

![nowcast cloudy](https://github.com/yuhao-nie/Stanford-solar-forecasting-dataset/blob/main/sample%20images/sunset_nowcast_cloudy_days.gif)
<p align=center>
Fig.2.3 Nowcast in Cloudy Days
</p>

#### Short-term Solar Power Forecast

We extend the “now-cast” work and proposed a specialized convolutional neural network (CNN) “SUNSET” to predict 15-min ahead minutely-averaged PV output. The model is characterized by its usage of hybrid input, temporal history and strong regularization. Parts of the results are showed in fig.2.4 and fig.2.5 for sunny and cloudy days respectively.

![forecast sunny](https://github.com/yuhao-nie/Stanford-solar-forecasting-dataset/blob/main/sample%20images/sunset_forecast_sunny_days.gif)
<p align=center>
Fig. 2.4 Forecast in Sunny Days
</p>

![forecast cloudy](https://github.com/yuhao-nie/Stanford-solar-forecasting-dataset/blob/main/sample%20images/sunset_forecast_cloudy_days.gif)
<p align=center>
Fig. Forecast in Cloudy Days
</p>

## Additional Information
  
### Request of access

To request access to the dataset please send a enquiry to Yuhao Nie (ynie@stanford.edu).


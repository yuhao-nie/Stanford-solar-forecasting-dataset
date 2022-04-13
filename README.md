# Stanford Solar Forecasting Dataset

This repo describes the solar forecasting dataset collected at Stanford University. 

## Dataset Description
![skycamgif]()

This dataset is a collection of sky images and PV power output for solar forecasting from Stanford University. The data consist of three years (2017–2019) of quality-controlled, 1-min [not sure?] resolution in sky images taken from a ground-based fish-eye camera and power output measurement from a 30 kW rooftop PV array ~125 m away from the camera at Stanford Campus. We hope that the dataset will enable researchers to tackle the problem of short-term local ground camera-based solar power prediction. [We also include models?]

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

![image](https://ars.els-cdn.com/content/image/1-s2.0-S0038092X19306164-gr1.jpg)

Fig.1. Photos of sky images and research equipment. 
(A. Sky image captured on a clear day at 12:51:00, Mar.14.2017. 
B. Sky image of a cloudy day captured at 10:50:00 Mar.16.2017. 
C. Fish-eye camera used for sky imaging. 
D. PV panels used in this study.)

Videos are captured in a resolution of 1536 × 1536 pixels at 20 frames per second (fps). It is compressed with the h.264 standard to a bit rate of 2 Mbps. Images (.jpg) are extracted at a chosen sampling frequency, and down-sampled to a resolution of 64 × 64 pixels, which was previously shown to be acceptable for PV output forecast, while retaining a reasonable training time. Images are retained between the hours of 6:00 AM and 8:00 PM local time (PST).

#### PV Output 
[should we include the Y2E2 solar PV arrays as well?]

The PV output data are collected from solar panel arrays ∼125 m away from the camera, on the top of the Jen-Hsun Huang Engineering Center at Stanford University. The poly-crystalline panels are rated at 30.1 kW-DC, with an elevation and azimuth angle at 22.5° and 195° respectively.


### Demonstration of use cases




### Request of access

To request access to the dataset please send a enquiry to Yuhao Nie (ynie@stanford.edu).

## Additional Information



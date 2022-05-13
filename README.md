# Stanford Solar Forecasting Dataset

![sunnygif_1](/sample%20images/sunny_day_demo_1.gif)
![cloudygif_1](/sample%20images/cloudy_day_demo_1.gif)
![sunnygif_2](/sample%20images/sunny_day_demo_2.gif)
![cloudygif_2](/sample%20images/cloudy_day_demo_2.gif)
![sunnygif_3](/sample%20images/sunny_day_demo_3.gif)
![cloudygif_3](/sample%20images/cloudy_day_demo_3.gif)
![sunnygif_4](/sample%20images/sunny_day_demo_4.gif)
![cloudygif_4](/sample%20images/cloudy_day_demo_4.gif)
![sunnygif_5](/sample%20images/sunny_day_demo_5.gif)
![cloudygif_5](/sample%20images/cloudy_day_demo_5.gif)
![sunnygif_6](/sample%20images/sunny_day_demo_6.gif)
![cloudygif_6](/sample%20images/cloudy_day_demo_6.gif)

Large-scale integration of photovoltaics (PV) into electricity grids is challenged by the intermittent nature of solar power. Sky image-based solar forecasting has been recognized as a promising approach to predicting the short-term fluctuations. 

Here, we present Stanford solar forecasting dataset (SSFD), a curated dataset collected and compiled by the [Environment Assessment and Optimization (EAO) Group](https://eao.stanford.edu/) at Stanford University. We hope that this dataset will facilitate the research of image-based solar forecasting and we also encourage the users to explore on other related areas with this dataset, such as sky image segmentation, cloud type classification and cloud movement forecasting.

## Dataset Description

The dataset consists of two major categories of data: sky images and PV power output, both of which are logged with 1-min frequency. To support the flexibility of research, we also open source the concurrent sky video footage and users can thus tailor their data extraction. The data collection started from 2017 March and has continued through now[^1]. However, we've only open-sourced the data from 2017 March to 2019 October so far, and work to compile the data beyond is going on, so stay tuned!

[^1]: The dataset suffer from some interruptions adue to the water intrusion, wiring and/or electrical failure of the camera as well as daylight-saving adjustment failure in 2017 and 2018, which is back to normal for 2019 and beyond.

### Sky Images

Video recordings of the daytime sky (6:00 AM ~ 8:00 PM PST) are shot with a 6-megapixel 360-degree fish-eye camera (Hikvision DS-2CD6362F-IV[^2]), which is located on top of the Green Earth Sciences Building at Stanford University and oriented towards 14&deg; south by west. Camera aperture, white balance and dynamic range are held constant. Videos are captured in a resolution of 2048 × 2048 pixels at 20 frames per second (fps) and images (.jpg) are extracted from the video at 1-min sampling frequency. Figure 1 gives examples of sky images in different weather conditions, and shows the camera and PV panels used in this study.

[^2]: The camera model Hikvision DS-2CD6362F-IV is discontinued and is replaced by a new model Hikvision DS-2CD6365GOE-IVS. We replace the old model with the new model on April 29, 2022 due to aging.

User can extract higher frequency image samples and down-size the samples to a lower resolution based on their needs. For your reference, our previous research work [[1]](#1) shows 1-min frequency and 64 x 64 resolution to be acceptable for PV output forecast, while retaining reasonable training time.

<div align=center><image src="./sample%20images/sky_camera_and_panel_photos.jpg"></div>
  
<p align=justify>
Figure 1: Photos of sky images and research equipment. 
(A. Sky image captured on a clear day at 12:51:00, Mar.14.2017. 
B. Sky image of a cloudy day captured at 10:50:00 Mar.16.2017. 
C. Fish-eye camera used for sky imaging. 
D. Studied PV panels.
E. Locations of the camera and studied solar panels)
</p>

### PV Output 

The PV output data are collected from solar panel arrays ∼125 m away from the camera, on the top of the Jen-Hsun Huang Engineering Center at Stanford University. The poly-crystalline panels are rated at 30.1 kW-DC, with an elevation and azimuth angle at 22.5° and 195° respectively. The raw PV output power data are originally logged by Stanford Utility and the miuntely averaged data are shared with us.

## Data Processing
We expect the users of this dataset to process the data based on their own needs, while we provide some reference codes for data processing used in our previous publications in our [SUNSET Model](https://github.com/YuchiSun/SUNSET) GitHub repository. One can refer to the main context and supplementary material of this paper [[1]](#1) for detailed instructions.

## Demonstration of Use Cases
Here, we demontrates a few use cases of this dataset based on our published works. Images of the sky provide information on current and future cloud coverage, and are potentially useful in inferring PV generation. Our group has developed a specialized convolutional neural network model named SUNSET (Stanford University Neural Network for Solar Electricity Trend) for PV output forecast.

### Solar Power Nowcast
We explore convolutional neural networks (CNN) to correlate PV output to contemporaneous images of the sky (a “now-cast”). We demonstrate that sky images are useful in inferring PV panel output, and CNN is a suitable structure in this application. Parts of the results are shown in Figure 2 and Figure 3 and you can refer to [[2]](#2) for the detailed work. 

![nowcast sunny](/sample%20images/sunset_nowcast_sunny_days.gif)
<p align=center>
Figure 2: Sample results for solar nowcasting on sunny days 
</p>

![nowcast cloudy](/sample%20images/sunset_nowcast_cloudy_days.gif)
<p align=center>
Figure 3: Sample results for solar nowcasting on cloudy days
</p>

### Short-term Solar Power Forecast
We extend the “now-cast” work and proposed a specialized convolutional neural network (CNN) “SUNSET” to predict 15-min ahead minutely-averaged PV output. The model is characterized by its usage of hybrid input, temporal history and strong regularization. Parts of the results are showed in Figure 4 and Figure 5 and you can refer to [[1]](#1) for the detailed work.

![forecast sunny](/sample%20images/sunset_forecast_sunny_days.gif)
<p align=center>
Figure 4: Sample results for solar forecasting on sunny days
</p>

![forecast cloudy](/sample%20images/sunset_forecast_cloudy_days.gif)
<p align=center>
Figure 5: Sample results for solar forecasting on cloudy days
</p>

### Sun Tracking and Clouds Detection

We utlize a camera projection model to correlate the sun position in a sky image with solar azimuth and zenith angle in the real world, and we develop a modified NRBR threshold with the background subtraction method to determine whether a pixel in the sky image is cloud pixel. In Figure 6, we demonstrate the sun tracking and cloud detection algorithms we developed. You can refer to [[3]](#3) for the details.

<div align=center>
  <image src="./sample%20images/sun_identification_demo_1.gif">
  <image src="./sample%20images/sun_identification_demo_4.gif">
  <image src="./sample%20images/sun_identification_demo_6.gif">
</div> 
  
<div align=center>
  <image src="./sample%20images/cloud_identification_demo_1.gif">
  <image src="./sample%20images/cloud_identification_demo_2.gif">
  <image src="./sample%20images/cloud_identification_demo_6.gif">
</div> 
  
<p align=justify>
Figure 6: Sample results for sun tracking and clouds detection (red spots in the 1st row of images represent the sun location, and green shades in the 2nd row of images represent the identified cloud pixels)
</p>

## Summary of Relevant Publications

So far, we have published the following 5 papers based on the dataset, and more research works are going on.

1. Solar Nowcasting [[2]](#2)

2. Short-term Solar Forecasting [[1]](#1)

3. Data Fusion [[4]](#4)

4. Sky-condition-specific Sub-models for Solar Forecasting [[3]](#3)

5. Resampling and Data Augmentation for Solar Forecasting with an Imbalanced Sky Image Dataset [[5]](#5)

## Access Instruction

We are working on generating a permanent URL (PURL) for users to access our dataset without hassle. For now, please send the enquiry directly to Yuhao Nie (ynie@stanford.edu).

## Citation
If you find the Stanford Solar Forecasting Dataset useful to your research/work please cite:

```

```

## License


## Collaboration on the Dataset
Our utlimate goal is to build a centralized large-scale sky image and PV output/irradiance measurements dataset for solar forecasting, just like ImageNet for computer vision research. This large-scale dataset is expected to include data streams coming from all over the world and cover a wide range of climate conditions, thus calling on a joint effort from the community. If you would like to collaborate on building such a dataset, please reach out directly to the PI Adam Brandt (abrandt@stanford.edu).

Some of our ongoing efforts include: (1) continuing the data collection at Stanford Campus; (2) having a new data stream from Oregon (Stanford North) with the same camera set up; and (3) webscraping 1-min high-res sky images from NREL which are open-sourced but have not been archived [^3] (Stanford East). 

[^3]: NREL only archives sky images in 10-min frequency and open sources to the public.

## Acknowledgements
We thank Stanford Utility for giving us permission to accessing the PV output history and Jacques Chalendar from Stanford University who help us access the data.

## References
<a id="1">[1]</a> 
Sun, Y., Venugopal, V., Brandt, A.R., 2019. Short-term solar power forecast with deep learning: Exploring optimal input and output configuration. Sol. Energy 188, 730–741.

<a id="2">[2]</a> 
Sun, Y., Szűcs, G., Brandt, A.R., 2018. Solar PV output prediction from video streams using convolutional neural networks. Energy Environ. Sci. 11, 1811–1818.

<a id="3">[3]</a> 
Nie, Y., Sun, Y., Chen, Y., Orsini, R., Brandt, A., 2020. PV power output prediction from sky images using convolutional neural network: The comparison of sky-condition-specific sub-models and an end-to-end model. J. Renew. Sustain. Energy 12, 046101.

<a id="4">[4]</a> 
Venugopal, V., Sun, Y., Brandt, A.R., 2019. Short-term solar PV forecasting using computer vision: The search for optimal CNN architectures for incorporating sky images and PV generation history. J. Renew. Sustain. Energy 11, 066102.

<a id="5">[5]</a> 
Nie, Y., Zamzam, A.S., Brandt, A., 2021. Resampling and data augmentation for short-term PV output prediction based on an imbalanced sky images dataset using convolutional neural networks. Sol. Energy 224, 341–354.

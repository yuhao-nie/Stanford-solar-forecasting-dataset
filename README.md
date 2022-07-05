# SKIPP'D — a SKy Images and Photovoltaic Power Generation Dataset for Short-term Solar Forecasting

Note: This *README* file is for demonstration purpose. For details of the dataset please refer to our dataset paper. All datasets are licensed under a
[Creative Commons Attribution 4.0 International License][cc-by]. All code files are licensed under the MIT license (see ``LICENSE``).

[cc-by]: http://creativecommons.org/licenses/by/4.0/

---

[**Dataset Paper**](https://arxiv.org/abs/2207.00913) | [**Benchmark Dataset**](https://purl.stanford.edu/dj417rh1007) | [**Raw Dataset**](https://purl.stanford.edu/sm043zf7254)

![sunnygif_1](/sample_images/sunny_day_demo_1.gif)
![cloudygif_1](/sample_images/cloudy_day_demo_1.gif)
![sunnygif_2](/sample_images/sunny_day_demo_2.gif)
![cloudygif_2](/sample_images/cloudy_day_demo_2.gif)
![sunnygif_3](/sample_images/sunny_day_demo_3.gif)
![cloudygif_3](/sample_images/cloudy_day_demo_3.gif)
![sunnygif_4](/sample_images/sunny_day_demo_4.gif)
![cloudygif_4](/sample_images/cloudy_day_demo_4.gif)
![sunnygif_5](/sample_images/sunny_day_demo_5.gif)
![cloudygif_5](/sample_images/cloudy_day_demo_5.gif)
![sunnygif_6](/sample_images/sunny_day_demo_6.gif)
![cloudygif_6](/sample_images/cloudy_day_demo_6.gif)

Large-scale integration of photovoltaics (PV) into electricity grids is challenged by the intermittent nature of solar power. Sky image-based solar forecasting has been recognized as a promising approach to predicting the short-term fluctuations. 

Here, we present **SKIPP'D** — a **SK**y **I**mages and **P**hotovoltaic **P**ower Generation **D**ataset for short-term solar forecasting, collected and compiled by the [Environmental Assessment and Optimization (EAO) Group](https://eao.stanford.edu/) at Stanford University. We hope that this dataset will facilitate the research of image-based solar forecasting using deep learning and contribute to a standardized benchmark for evaluating and comparing different solar forecasting models. We also encourage the users to explore on other related areas with this dataset, such as sky image segmentation, cloud type classification and cloud movement forecasting.

Any questions regarding the dataset can be directed to Yuhao Nie (ynie@stanford.edu).

## Dataset Update Log
2022.07.01 SKIPP'D v1.0: Release 2017-2019 benchmark and raw datasets collected at Stanford campus.

## Code Base and Dependencies
All the codes are writen in Python 3.6.1. The deep learning models are implemented using deep learning framework TensorFlow 2.4.1 and trained on GPU cluster, with NVIDIA TESLA V100 32GB or A100 40GB card. TensorFlow 2.4.1 is compatible with CUDA 11.2.0 and cuDNN 8.1.1.33. All dependencies are listed in `requirements.txt`. 

| File | Description |
| ------------- | ------------- |
| `data_processing/data_preprocess_snapshot_only.ipynb` | Jupyter Notebook used to capture images from the video stream at designated frequency. |
| `data_processing/data_preprocess_pv.ipynb` | Jupyter Notebook used to process the raw PV power generation history.  |
| `data_processing/data_nowcast.ipynb` | Jupyter Notebook used to down-sample the image frames, filter out the invalid frames and match images with the concurrent PV data, and partition model development and testing sets.  |
| `data_processing/data_forecast.ipynb` | Jupyter Notebook used to generate valid samples for the forecast task. |
| `models/SUNSET_nowcast.ipynb` | Jupyter Notebook used to create the SUNSET nowcast model to correlate PV output to contemporaneous images of the sky, including model training, validation and testing. |
| `models/SUNSET_forecast.ipynb` | Jupyter Notebook used to create the SUNSET forecast model to predict 15-min ahead minutely-averaged PV output, including model training, validation and testing. |
| `models/Relative_op_func.py` | Helper functions for calculating theoretical PV power output under clear sky condition and the clear sky index. |

## Dataset Description

The dataset contains the following two levels of data which distinguishes it from most of the existing open-sourced solar forecasting datasets and makes it especially suitable for deep-learning-based solar forecasting research: 

1. Benchmark dataset: 3 years of processed sky images (64×64) and concurrent PV power generation data with
1-min interval that are ready-to-use for deep learning model development;

2. Raw dataset: Overlapping high resolution sky video footage (2048×2048) recorded at 20 frames
per second, sky image frames (2048×2048) and history PV power generation data logged in 1-min frequency
that suit various research purposes. 

In addition, we provide the code base of data processing and baseline model implementation for researchers to fast reproduce our previous work and accelerate solar forecasting research.

The benchmark data is available at https://purl.stanford.edu/dj417rh1007 and the raw data is deposit separately by each year given its large size. The 2017 raw data is available at https://purl.stanford.edu/sm043zf7254 and the links to 2018 and 2019 data can be found in the "Related items" elsewhere on the same web page. The data files are summarized below.

| File | Type | Description |
| ------------- | ------------- | ------------- |
| `2017_2019_images_pv_processed.hdf5` | Benchmark data | A file-directory like structure consisting of two groups: "trainval" and "test", for storing model development set and test set, respectively, with each group containing two datasets: "images\_log" and "pv\_log", which stores the processed images and PV generation data from all three years (2017-2019) in Python NumPy array format. |
| `times_trainval.npy` | Benchmark data | Python NumPy array of time stamps corresponding to development set in *.hdf5* file. |
| `times_test.npy ` | Benchmark data | Python NumPy array of time stamps corresponding to test set in *.hdf5* file.  |
| `{Year}_{Month}_videos.tar` | Raw data | Tar archives with daytime 2048x2048 sky videos (*.mp4*) recorded at 20 frames per second for each month from 2017/03 to 2019/12. |
| `{Year}_{Month}_images_raw.tar` | Raw data | Tar archives with daytime 2048 $\times$ 2048 sky images (*.jpg*) captured at 1-min intervals for each month from 2017/03 to 2019/12 (around 7 GB of each month). |
| `{Year}_pv_raw.csv` | Raw data | One-min PV generation data for the year 2017, 2018 and 2019. |

### Dataset Sources
Our research group started the data collection from March, 2017 at Stanford University campus, located in the center of the San Francisco Peninsula, in California. According to the Köppen climate classification system, Stanford  has a warm-summer Mediterranean climate, abbreviated Csb (C=temperate climate s=dry summer b=warm summer) on climate maps. In terms of cloud coverage, Stanford is featured by long summers with mostly clear sky and short winters with partly cloudy sky.

Two major categories of data are collected and logged: sky images and PV power generation. Data are recorded according to their internal clocks synchronized with the local time zone, which is Pacific Standard Time (PST), to ensure consistency. Over the past five years, our lab has collected over 3 terabytes of data. In this release, we open-source the data from 2017 March to 2019 December[^1]. Here, we provide two levels of data to suit the different needs of researchers: (1) A processed dataset consists of 1-min down-sampled sky images (64x64) and PV power generation pairs, which is intended for fast reproducing our previous work and accelerating the development and benchmarking of deep-learning-based solar forecasting models; (2) A raw dataset consists of high resolution sky images (2048x2048) and PV power generation data, as well as the source sky video footage, which is intended for customizing data extraction, and exploring other related areas of solar forecasting such as cloud segmentation and cloud movement forecasting. 

In a future release, we will open source the data from 2020 and beyond of the Stanford dataset and include two additional data sources: sky images and PV power generation data from a solar farm in Oregon collected by our research group and sky images from cameras set up by NREL which correspond to solar irradiance data collected by them. The update information will be released in this GitHub repository.

[^1]: The dataset suffer from some interruptions due to the water intrusion, wiring and/or electrical failure of the camera as well as daylight-saving adjustment failure in 2017 and 2018, which is back to normal for 2019 and beyond.

### Sky Images

Video recordings of the daytime sky (6:00 AM ~ 8:00 PM PST) are shot with a 6-megapixel 360-degree fish-eye camera (Hikvision DS-2CD6362F-IV[^2]), which is located on top of the Green Earth Sciences Building at Stanford University and oriented towards 14&deg; south by west. Camera aperture, white balance and dynamic range are held constant. Videos are captured in a resolution of 2048 × 2048 pixels at 20 frames per second (fps) and images (.jpg) are extracted from the video at 1-min sampling frequency. Figure 1 gives examples of sky images in different weather conditions, and shows the camera and PV panels used in this study.

[^2]: The camera model Hikvision DS-2CD6362F-IV is discontinued and is replaced by a new model Hikvision DS-2CD6365GOE-IVS. We replace the old model with the new model on April 29, 2022 due to aging.

User can extract higher frequency image samples and down-size the samples to a lower resolution based on their needs. For your reference, our previous research work [[1]](#1) shows 1-min frequency and 64 x 64 resolution to be acceptable for PV output forecast, while retaining reasonable training time.

<div align=center><image src="./sample_images/sky_camera_and_panel_photos_update.png"></div>
  
<p align=justify>
Figure 1: Photos of sky images and research equipment. 
(A. Sky image captured on a clear day at 12:18:20 pm, January 25, 2019. 
B. Sky image of a cloudy day captured at 12:32:10 pm May 27, 2019. 
C. Fish-eye camera used for sky imaging. 
D. Studied PV panels.
E. Locations of the camera and studied solar panels)
</p>

### PV power generation 

The PV power generation data are collected from solar panel arrays ∼125 m away from the camera, on the top of the Jen-Hsun Huang Engineering Center at Stanford University. The poly-crystalline panels are rated at 30.1 kW-DC, with an elevation and azimuth angle at 22.5° and 195°, respectively. The raw PV output power data are logged with 1-min frequency and representing the average power output within that minute[^3].

[^3]: It should be noted that this is different from the instaneous raw PV data that we used in our previous published works [[1]](#1), [[2]](#2), [[3]](#3) and [[4]](#4), so users do not need to take rolling average during data processing to get the minutely average data.

## Data Processing
For flexibility of research, we open source high-resolution, high-frequency raw data, and the users of this dataset can process the data based on their own needs. We provide some reference codes for data processing in directory `\data_processing`, which basically including the following steps:

1. Snapshotting the video footage at a designated frequency (`data_preprocess_snapshot_only.ipynb`)
2. Processing the raw PV output history (`data_preprocess_PV.ipynb`)
    - Interpolation of PV data to every 10 seconds (in preparation for matching with images with irregular time stamps, e.g., 08:20:40)
    - Filtering out the invalid PV data (missing record>1 hr or PV data<0)
3. Processing images and matching images with the concurrent PV data (`data_preprocess_nowcast.ipynb`)
    - Down-sizing the image frames
    - Filtering out repeating images caused by the occasional abnormal behavior of OpenCV video capture function  
4. Generating valid samples for the forecast task (which will be described in the second use case below) and partitioning training, validation and testing sets (`data_preprocess_forecast.ipynb`)

Users can either use the reference codes we provided here or customize their own data processing pipeline. For more details, please refer to the data processing section of this dissertation [[6]](#6). 

## Benchmark dataset
The benchmark dataset contains the model development set and test set obtained from the data processing Step 3 described in the above section. The samples of the benchmark dataset are organized as aligned pairs of sky images and PV power generation. Figure 2 shows the distribution of the PV power generation data for the development set and test set and the PV power generation profiles of the 20 days in the test set.

![benchmark data](/sample_images/combined_pv_distribution_test_set_PV_output_profile.jpg)
<p align=justify>
Figure 2:  The PV power generation data distribution of the benchmark dataset: A. development set PV data distribution; B. test set PV data distribution; and C. the PV power generation profiles of the 10 sunny days and 10 cloudy days used in the test set: upper panel shows for the sunny days, and the lower panel is for the cloudy days.
</p>

## Demonstration of Use Cases
Here, we demontrates a few use cases of the dataset based on our previously published works. Our group has developed a specialized convolutional neural network model named SUNSET (Stanford University Neural Network for Solar Electricity Trend) for PV output forecast. Two specific prediction tasks were investigated based on SUNSET, including (1) PV power generation nowcast [[2]](#2), i.e., given a sky image, predicting the contemporaneous PV output; and (2) PV power generation forecast [[1]](#1), given sky images and PV output for the past 15 minutes on 1-minute resolution, predicting PV output 15 minutes ahead into the future. The details of these two models can be found in the corresponding published papers. It should be noted that the results shown below are based on the results from our previous publications for demonstration purpose, for results based on the benchmark dataset, please refer to our [dataset paper](). As described in the paper, we implemented these two deep learning models using TensorFlow 2.x, which is an update from the TensorFlow 1.x code base used in our previous publications. The new code base can be found in the directory `\models`. The old code base can be found in our [SUNSET Model](https://github.com/YuchiSun/SUNSET) GitHub repository.

### Solar Power Nowcast
We explore convolutional neural networks (CNN) to correlate PV output to contemporaneous images of the sky (a “now-cast”). We demonstrate that sky images are useful in inferring PV panel output, and CNN is a suitable structure in this application. Parts of the results are shown in Figure 3 and Figure 4 and you can refer to [[2]](#2) for the detailed work. 

![nowcast sunny](/sample_images/sunset_nowcast_sunny_days.gif)
<p align=center>
Figure 3: Sample results for solar nowcasting on sunny days 
</p>

![nowcast cloudy](/sample_images/sunset_nowcast_cloudy_days.gif)
<p align=center>
Figure 4: Sample results for solar nowcasting on cloudy days
</p>

### Short-term Solar Power Forecast
We extend the “now-cast” work and proposed a specialized convolutional neural network (CNN) “SUNSET” to predict 15-min ahead minutely-averaged PV output. The model is characterized by its usage of hybrid input, temporal history and strong regularization. Parts of the results are showed in Figure 5 and Figure 6 and you can refer to [[1]](#1) for the detailed work.

![forecast sunny](/sample_images/sunset_forecast_sunny_days.gif)
<p align=center>
Figure 5: Sample results for solar forecasting on sunny days
</p>

![forecast cloudy](/sample_images/sunset_forecast_cloudy_days.gif)
<p align=center>
Figure 6: Sample results for solar forecasting on cloudy days
</p>

### Sun Tracking and Clouds Detection

We utlize a camera projection model to correlate the sun position in a sky image with solar azimuth and zenith angle in the real world, and we develop a modified NRBR threshold with the background subtraction method to determine whether a pixel in the sky image is cloud pixel. In Figure 7, we demonstrate the sun tracking and cloud detection algorithms we developed. You can refer to [[3]](#3) for the details.

<div align=center>
  <image src="./sample_images/sun_identification_demo_1.gif">
  <image src="./sample_images/sun_identification_demo_4.gif">
  <image src="./sample_images/sun_identification_demo_6.gif">
</div> 
  
<div align=center>
  <image src="./sample_images/cloud_identification_demo_1.gif">
  <image src="./sample_images/cloud_identification_demo_2.gif">
  <image src="./sample_images/cloud_identification_demo_6.gif">
</div> 
  
<p align=justify>
Figure 7: Sample results for sun tracking and clouds detection (red spots in the 1st row of images represent the sun location, and green shades in the 2nd row of images represent the identified cloud pixels)
</p>

## Summary of Relevant Publications

So far, we have published the following 5 papers based on the dataset, and more research works are going on.

1. Solar Nowcasting [[2]](#2)

2. Short-term Solar Forecasting [[1]](#1)

3. Data Fusion [[4]](#4)

4. Sky-condition-specific Sub-models for Solar Forecasting [[3]](#3)

5. Resampling and Data Augmentation for Solar Forecasting with an Imbalanced Sky Image Dataset [[5]](#5)

## Access Instruction

SKIPP'D can be accessed without hassle. The benchmark data is available at https://purl.stanford.edu/dj417rh1007 and the raw data is deposit separately by each year given its large size. The 2017 raw data is available at https://purl.stanford.edu/sm043zf7254 and the links to 2018 and 2019 data can be found in the "Related items" elsewhere on the same web page.

## Citation
If you find SKIPP'D useful to your research/work please cite (release soon):

```

```

## Collaboration on the Dataset
Our utlimate goal is to build a centralized large-scale sky image and PV output/irradiance measurements dataset for solar forecasting, just like ImageNet for computer vision research. This large-scale dataset is expected to include data streams coming from all over the world and cover a wide range of climate conditions, thus calling on a joint effort from the community. If you would like to collaborate on building such a dataset, please reach out directly to the PI Adam Brandt (abrandt@stanford.edu).

Some of our ongoing efforts include: (1) continuing the data collection at Stanford Campus; (2) having a new data stream from Oregon (Stanford North) with the same camera set up; and (3) webscraping 1-min high-res sky images from [NREL Solar Radiation Research Laboratory](https://midcdmz.nrel.gov/apps/sitehome.pl?site=SRRLASI) which are open-sourced but not archived [^4] (Stanford East). 

[^4]: NREL only archives sky images in 10-min frequency and open sources to the public.

## Acknowledgements
The authors thank Stanford Utility for giving us permission to accessing the PV power generation history and Jacques de Chalendar from Stanford University who help us access the data. The authors would also like to acknowledge the Stanford Research Computing Center for providing the computational resources for conducting the experiments in this study. The authors are also grateful to Amy Hodge from Science and Engineering Resource Group at Stanford Libraries for facilitating the datasets depositing.

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

<a id="6">[6]</a> 
Sun, Y., 2019. Short-term Solar Forecast Using Convolutional Neural Networks with Sky Images. Stanford University.

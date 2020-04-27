---
title: 'ESDaP: A Python package for Epileptic Seizure Detection and Prediction from EEG data'
tags:
  - Python
  - epilepsy
  - seizure detection
  - seizure prediction
  - neural networks
  - EEG
authors:
  - name: Fabian Egli
    affiliation: 1
  - name: Nick Pullen
    affiliation: 1
  - name: Thomas Frick
    affiliation: "1, 2"
  - name: Alessio Quercia
    affiliation: 2
  - name: Isabelle Dupanloup
    orcid: 0000-0002-9258-6963
    affiliation: 1
affiliations:
 - name: Swiss Institute of Bioinformatics, CH-1015 Lausanne, Switzerland
   index: 1
 - name: IBM Research ZÃ¼rich, CH-8803 RÃ¼schlikon, Switzerland
   index: 2
date: 24 April 2020
bibliography: paper.bib

---

# Summary

Epilepsy is a chronic neurological disorder characterized by recurrent 
seizures [@Beghi:2020]. Epilepsy affects approximately 1% of the population 
worldwide, and for 30% of the patients, there is no effective therapeutic 
strategy [@Meisel:2019].
Epileptic seizures correspond to sudden alterations in consciousness, 
movement, sensation or behaviour. They can vary from brief and nearly 
undetectable episodes to long periods of vigorous shaking. Seizures are 
difficult to detect and predict, which worsens the quality of life for 
patients, families and caregivers.
Efficient detection systems would provide useful data for the management 
of epilepsy and for promoting efficient therapies. Seizure prediction 
systems would be even more valuable, by allowing more tailored therapies 
for seizure abortion and by preventing accidents and SUDEP (sudden unexpected 
death in epilepsy) [@Acharya:2018].
Epileptic seizures occur as a result of a malfunctioning of the 
electrophysiological system of the brain. Electroencephalogram (EEG) 
provides a direct measurement of electrical brain activity, with electrodes 
placed along the scalp, or directly on the surface of the brain. 
Experienced neurologists can recognize ictal (during a seizure), 
and also preictal (before a seizure), activities by visually scanning 
EEG signals. But EEG reading is a complex task. Although accepted 
definitions and terminologies are available, a gold standard is lacking 
and the final interpretation of EEG is prone to inter-observer 
variabilities and subjectivity [@Grant:2014].
More than 20 years of international effort have been devoted to develop 
algorithms for the detection and prediction of seizures from EEG data 
[@Acharya:2018]. These algorithms use generally, either traditional machine 
learning models or deep learning models to classify EEG data in either 
ictal, preictal, or interictal (i.e. normal) state 
[@Baumgartner:2018; @Meisel:2019]. But models still need further improvement 
to achieve better performance and several alternatives should be compared 
in a common framework. Performance metrics from different models cannot, 
indeed, be directly compared, if estimated on different datasets, patients, 
and using distinct data processing techniques.

`ESDaP` is an open-source Python package for detecting and predicting 
epileptic seizures from EEG data, using a large variety of options across the 
data analysis pipeline. It allows the extraction of features from 
segments, or short time windows, of the original EEG data. Various types of 
features can be extracted from the original data, in the time domain, the 
frequency domain and the time frequency domain. Also univariate, as well as 
multivariate features can be computed. Our choice of features was motivated 
by previous studies showing the predictive potential of these features 
[@Gadhoumi:2016; @Boonyakitanont:2020].
`ESDaP` reads EEG data in the edf format which is a standard file format 
designed for the exchange and storage of medical time series. `ESDaP` reads 
seizure information from summary files as used in the CHB-MIT Scalp EEG 
Database [@Shoeb:2009].
`ESDaP` allows to run different types of neural networks to classify 
the original segments, using the extracted features, in ictal, preictal, 
postictal (after a seizure) or interictal state. The networks that are 
currently implemented in `ESDaP` are: a fully connected neural network (FCN) 
[@Abbasi:2019], a Long Short-Term Memory (LSTM) neural network 
[@Tsiouris:2018], a one-dimensional convolutional neural network (CNN) 
[@Truong:2018]. The architecture of the neural networks and their 
hyperparameters can be modulated upon the choice of the users. 
`ESDaP` measures the classification performance of the models, using 
cross-validation and a variety of standard metrics.

`ESDaP` has a series of dependencies, namely: joblib, a set of tools to 
provide lightweight pipelining in Python; matplotlib [@Hunter:2007], a library 
for creating static, animated, and interactive visualizations in Python; 
mlflow, a platform to streamline machine learning development, including 
tracking experiments, packaging code into reproducible runs, and sharing 
and deploying models; mne [@Gramfort:2013], a package for exploring, 
visualizing, and analyzing human neurophysiological data such as EEG; 
numba [@Lam:2015], an open source optimizing compiler for Python; numpy 
[@numpy:2011], a package for scientific computing; pandas [@pandas:2020], 
a package providing fast, flexible, and expressive data structures 
designed to make working with structured (tabular, multidimensional, 
potentially heterogeneous) and time series data both easy and intuitive; 
pywavelets [@Lee:2019], a package for wavelet analysis; scikit-learn 
[@Pedregosa:2011], a module for predictive data analysis using machine 
learning; scipy [@Virtanen:2020], a package providing efficient numerical 
routines for numerical integration, interpolation, optimization, linear 
algebra, and statistics; seaborn, a library for making statistical graphics 
in Python; tensorflow [@Abadi:2015], an open source machine learning 
framework; xgboost [@Chen:2016], a library which implements machine learning 
algorithms under the Gradient Boosting framework.

`ESDaP` can be used to perform a systematic comparison of the performance of 
several algorithms for seizure detection and/or prediction, in the exact same 
conditions. It can also allow users to quantify the effect of various options 
(segment length, extracted features, deep learning models, architecture of 
the neural networks, etc.) on the algorithms performance.
To our knowledge, `ESDaP` is the only open-source solution which allows to 
achieve the tasks described here. In the future, we plan to continue 
contributing to the `ESDaP` code by implementing other models to propose 
to the users an extensive choice of architecture and predictive potential. 
We also invite external contributions to the `ESDaP` code and provide 
guidelines for new implementations.
In the long run, we hope that `ESDaP` could ultimately be used to 
identify efficient, patient-specific algorithms, that could be 
integrated into devices for alarming patients and caregivers of an 
impending seizure.

# Acknowledgements

This work was supported by the Novartis Foundation through the FreeNovation 
2018 program.

# References

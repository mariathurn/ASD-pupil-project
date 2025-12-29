
Using Pupil Responses in Video-Viewing to Classify ASD

This repository contains the code used for the course project “Using Pupil Responses in Video-Viewing to Classify Autism Spectrum Disorder”, completed as part of Computational Cognitive Science 3 (MSc IT & Cognition, University of Copenhagen).

The project investigates whether participant-level pupil features provide additional discriminative value beyond gaze-based features when classifying children with Autism Spectrum Disorder (ASD) versus typically developing (TD) controls using eye-tracking data.

⸻

Overview

The analysis focuses on:
	•	Participant-level aggregation of eye-tracking data
	•	Comparison of gaze-only, pupil-only, and combined feature sets
	•	Evaluation using interpretable machine-learning models (logistic regression, linear SVM) and a non-linear baseline (XGBoost)
	•	Careful handling of noisy pupil data and missing samples

The accompanying report describes the methodological choices and results in detail.

⸻

Dataset

Source

This project uses the publicly available eye-tracking dataset published by:

Cilia et al. (2022)
Eye-Tracking Dataset to Support the Research on Autism Spectrum Disorder
Figshare
https://doi.org/10.6084/m9.figshare.20113592.v1

Description
	•	Participants: 57 children (ASD and TD)
	•	Task: Free viewing of naturalistic visual stimuli (videos and images)
	•	Data:
	•	Pupil diameter (left and right eye)
	•	Gaze coordinates
	•	Fixation and saccade annotations
	•	Tracking quality metrics
	•	Metadata: Age, gender, diagnostic group, CARS scores (ASD group)

The dataset is released in anonymised form and may be used for research purposes under the terms specified by the original authors.

How to obtain the data
	1.	Visit the Figshare page:
https://doi.org/10.6084/m9.figshare.20113592.v1
	2.	Download the dataset files
	3.	Extract the data locally
	4.	Place the data in the directory expected by the scripts (see below)

Note: The dataset is not included in this repository.


Preprocessing and Feature Extraction
	•	Pupil diameter values are screened for invalid and physiologically implausible samples
	•	Short gaps in the pupil signal are linearly interpolated; longer gaps are retained
	•	Pupil signals are median-centred at the participant level
	•	Participant-level pupil features summarise:
	•	Tonic pupil level
	•	Variability
	•	Temporal dynamics (velocity-based features)
	•	Gaze features are derived from fixation and saccade annotations and aggregated across trials

All features are computed at the participant level, not the trial level.

⸻

Models and Evaluation

The following classifiers are implemented:
	•	Logistic regression
	•	L1-regularised logistic regression
	•	Linear Support Vector Machine (SVM)
	•	Gradient-boosted decision trees (XGBoost)

Evaluation is performed using participant-level stratified cross-validation, and performance is assessed using accuracy, balanced accuracy, F1-score, and ROC–AUC.

⸻

Requirements

The code was developed using Python. Main dependencies include:
	•	numpy
	•	pandas
	•	scikit-learn
	•	xgboost
	•	matplotlib / seaborn (for visualisation)

Exact versions are not fixed; standard recent versions should work.

⸻

Ethical Considerations

The dataset contains eye-tracking data from children and should be handled with care. All analyses in this repository are conducted on anonymised data collected with informed consent. Results are intended for research purposes only and should not be interpreted as diagnostic.

⸻

Citation

If you use this dataset or code, please cite the original dataset publication:

Cilia, F., Carette, R., Elbattah, M., Guérin, J.-L., & Dequen, G. (2022). Eye-Tracking Dataset to Support the Research on Autism Spectrum Disorder. Figshare. https://doi.org/10.6084/m9.figshare.20113592.v1

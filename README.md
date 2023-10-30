# signatures-hand-synergies

Check the write-up [here](https://github.com/alizma/signatures-hand-synergies/blob/main/Signatures_for_Hand_Kinematic_Synergies-3.pdf). This project was done under Professor Kavita Ramanan and William Salkeld at Brown under the Spring 2023 UTRA Award. 

## File Organization
`classify_stim.ipynb` - Initial testing of classification algorithms

`exploratory_data_analysis.ipynb` - Initial plotting, analysis, etc. of data

`main.ipynb` - main results from writeup

`deepmlp_classif.ipynb` - similar results to `main.ipynb` but using MLP

### Scripts:
`normalizers.py` - simple normalizers

`paths.py` - `Path` objects for different databases

## Database Annotations 

### DB1 
[Associated paper](http://publications.hevs.ch/index.php/publications/show/1172 )

* **Aquisition Setup** 
    + **Kinematic Data**
        + 22-sensor Cyberglove II representing 22 joint angles as 8-bit values at a resolution < 1 degree
        + 2-axis inclinometer fixed onto wrist to collect wrist orientation 
        + 25Hz sampling frequency 
    + **Surface EMG**
        + Double-differential MyoBock 13E200
        + 100Hz sampling frequency  


* **Stimulus**: 52 movements divided into 4 main classes:
    + 12 movements of fingers (flexions and extensions)
    + 8 isometric, isotonic hand configurations/postures 
    + 9 wrist movements (adduction/abduction, flexion/extension, pronation/supination)
    + 23 grasping and functional movements 

* 27 subjects
* 10 repetitions of each class of movements
* 5 seconds of motion, 3 seconds of rest in-between 

### DB3 
[Associated paper](https://www.nature.com/articles/sdata201453)

Collection of phantom limb electrical signals along forearm from hand-amputated subjects

* **Aquisition Setup** 
    + **Surface EMG**
        + Double-differential MyoBock 13E200-50
        + 12 electrodes in total along different parts of forearm 
        + 100Hz sampling frequency  
        + Columns 1-8 are electrode signals around forearm 
        + Columns 9 & 10 are signal along two activity spots of Flexor and Extensor Digitorum Superficialis 
        + Columns 11 & 12 (partially -- "when available") are from electrodes on actiity spots of muscle Biceps Brachii and of the muscle Triceps Brachii


* 11 hand-amputated subjects 
* 10 repetitions of each class of movements
* 5 seconds of motion, 3 seconds of rest in-between 

* Contains 36 columns of data about (x, y, z) acceleration of 12 sEMG electrodes
* 2 columns of (roll, pitch) inclination values 

* 6 columns of force values 
* 2x6 columns of extremal force values (minimal and maximal force values for each sensor) 

### DB5 
[Associated paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0186132)

* **Aquisition Setup** 
    + **Kinematic Data**
        + 22-sensor Cyberglove II representing 22 joint angles as 8-bit values at a resolution < 1 degree
        + 2-axis inclinometer fixed onto wrist to collect wrist orientation 
        + 25Hz sampling frequency 
    + **Surface EMG**
        + 2 Thalmic Myo bands, one tilted at 22.5 degrees above first
        + 16 electrodes 
        + 200Hz sampling frequency  
        + Columns 1-8 are the electrodes equally spaced around the forearm at the height of the radio humeral joint
        + Columns 9-16 represent the second Myo, tilted by 22.5 degrees clockwise.
        + 3 columns for accelerometer from first Myo 
        + 200Hz sampling frequency 

* **Stimulus**: 52 movements divided into 4 main classes:
    + 12 movements of fingers (flexions and extensions)
    + 8 isometric, isotonic hand configurations/postures 
    + 9 wrist movements (adduction/abduction, flexion/extension, pronation/supination)
    + 23 grasping and functional movements 

* 10 intact subjects
* 6 repetitions of each class of movements
* 5 seconds of motion, 3 seconds of rest in-between 

* DB5 - For feature extraction and classification, "Repetitions 1, 3, 4 and 6 were used to train the classifiers, repetitions 2 and 5 were used for validating them. The classification was performed on all movements (rest included)" in DB5, according to [this](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0186132) associated paper. 

* DB5 sampling frequency is 200 Hz, so windowing into 200 sample-sized windows (with an overlap of 50%) involves 1 second of data in each window 

### DB7 
[Associated paper](https://jneuroengrehab.biomedcentral.com/articles/10.1186/s12984-017-0284-4)

Includes offline analysis of a real-time prosthetic hand control experiment with 12 subjects (11 intact, 1 amputee)

* **Aquisition Setup** 
    + Does not collect any kinematic data 
    + **Surface EMG**
        + Delsys Trigno IM Wireless EMG 
        + 12 electrodes and 9-axes inertial measurement units (9 degrees of freedom: 3-axial accelerometer, gyroscope and magnetometer)
        + 100Hz sampling frequency  

* **Stimulus**: 40 movements divided into 4 main classes:
    + 12 movements of fingers (flexions and extensions)
    + 8 isometric, isotonic hand configurations/postures 
    + 9 wrist movements (adduction/abduction, flexion/extension, pronation/supination)
    + 23 grasping and functional movements 

* 20 intact subjects, 2 amputees
* 6 repetitions of each class of movements
* 5 seconds of rest between movement trials

### DB9 
[Associated paper](https://www.nature.com/articles/s41597-019-0349-2)

* **Aquisition Setup** 
    + **Kinematic Data**
        + 22-sensor Cyberglove II representing 22 joint angles as 8-bit values at a resolution < 1 degree
        + 2-axis inclinometer fixed onto wrist to collect wrist orientation 
        + 25Hz sampling frequency 

* **Stimulus**: 40 movements divided into 4 main classes:
    + 8 isometric, isotonic hand configurations/postures 
    + 9 wrist movements (adduction/abduction, flexion/extension, pronation/supination)
    + 23 grasping and functional movements 

* 77 subjects
* 5 repetitions of each class of movements
* 5 seconds of motion, 3 seconds of rest in-between 
* 22 columns of order of angles : name of the angles corresponding to variable “angles”

[Zenodo Download](https://doi.org/10.5281/ZENODO.3480074)


## Evens DB Notes
- All have a stimulus, restimulus, repetition, rerepetition (re- is corrected for what acc happened,
data can be ragged)
- EMG usually recorded with something attached to forearm
- If you wanted to combine databases, you would need to determine which exercises match across different databases since they all have a different ordering

### DB2:
- 12 EMG columns, 2kHz
- 6 reps, 49 movements, 40 subjects (intact)
- Movements include hand positions (1-8), basic movements of wrists (9-17), grasps and functional movements (18-40), force patterns (41-49)
- 5 seconds + 3 seconds rest
- Glove is 22 dof version

* Sampling frequency is 2000 Hz 

### DB4:
Same paper as DB5, different instrument (Cometa vs. Double Myo) 
- 12 EMG rather than 16 compared to DB5 
- 3 exercises: (1) basic movements (2) wrist movements (3) grasping + functional movements
- 6 repetitions, 52 movements, 10 subjects (intact)
- 5 seconds + 3 seconds rest

* Sampling frequency is 2000 Hz 

- eSMG dim is $10$ 

### DB6
- "Repetability"
- unique thing is multiple days of acquisition - made participants do the movements twice a day for 5 days (larger dataset...)
- EMG - 16 dims (2 are empty though), 2 kHz
- 12 repetitions of 7 *grasps* only, 10 intact subjects
- 4 seconds + 4 seconds rest

### DB8:
- 10 intacts, 2 amputees
- EMG - orig 1111 hz, then upsampled to 2khz, 16 dims
- Glove - 18 DoF
- 6-9 seconds + 3 seconds rest
- Each exercise is more like a "grip"/finger movement rather tahn an involved action
- Explicitly states that this database is meant for estimation/reconstruction of finger movement rather than movement/grip classification, since the data is meant to be slow finger movements and there is a lack of extended hold period). Though, that *shouldn't* affect using signatures, since its still tree-like equivalent to a properly timed movement...

### DB10:
Newest but seemingly most involved (more details later, but I don't think it's that useful for the purposes of this project)

A lot of data that I probably can't store locally

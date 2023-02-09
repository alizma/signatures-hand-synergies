# signatures-hand-synergies

## Notes

* DB5 - For feature extraction and classification, "Repetitions 1, 3, 4 and 6 were used to train the classifiers, repetitions 2 and 5 were used for validating them. The classification was performed on all movements (rest included)" in DB5, according to [this](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0186132) associated paper. 

* DB1 sampling frequency is 100 Hz 
- eSMG dim is $10$ 

* DB2 sampling frequency is 2000 Hz

* DB4 sampling frequency is 2000 Hz

* DB5 sampling frequency is 200 Hz, so windowing into 200 sample-sized windows (with an overlap of 50%) involves 1 second of data in each window 


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

### DB4:
Same paper as DB5, different instrument (Cometa vs. Double Myo) 
- 12 EMG rather than 16 compared to DB5 
- 3 exercises: (1) basic movements (2) wrist movements (3) grasping + functional movements
- 6 repetitions, 52 movements, 10 subjects (intact)
- 5 seconds + 3 seconds rest

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

## Questions 

### January 30th Meeting 

* 
*

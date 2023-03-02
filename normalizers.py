import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# TODO: DB5 specific right now, change so extracts by last column in general 
def normalize(data : pd.DataFrame, train_reps : list) -> pd.DataFrame:
    """
    Given sEMG data and exercise repetitions, extracts the subset of data from specification,
    which is centered and scaled to unit variance. 
    
    Parameters
    ----------
    data : pd.Dataframe 
        Collection of sensor data from which repetitions are to be extracted 
    train_reps : list 
        Specified exercise repetitions to extract by 
        
    Returns 
    -------
    pd.DataFrame
        Centered and unit-variance scaled sensor data for specified exercise repetitions

    """
    x = [np.where(data.values[:,17] == rep) for rep in train_reps]
    indices = np.squeeze(np.concatenate(x, axis = -1))
    train_data = data.iloc[indices, :].reset_index(drop=True)
    
    scaler = StandardScaler(with_mean=True,
                                with_std=True,
                                copy=False).fit(train_data.iloc[:, :16])
    
    scaled = scaler.transform(data.iloc[:,:16])
    normalized = pd.DataFrame(scaled)
    normalized['stimulus'], normalized['repetition'] = data['stimulus'], data['repetition']

    return normalized

def better_normalize(data : pd.DataFrame, train_reps : list, dims : int) -> pd.DataFrame:
    """
    Given sEMG data and exercise repetitions, extracts the subset of data from specification,
    which is centered and scaled to unit variance. 
    
    Parameters
    ----------
    data : pd.Dataframe 
        Collection of sensor data from which repetitions are to be extracted 
    train_reps : list 
        Specified exercise repetitions to extract by 
        
    Returns 
    -------
    pd.DataFrame
        Centered and unit-variance scaled sensor data for specified exercise repetitions

    """
    x = [np.where(data.repetition.values == rep) for rep in train_reps]
    indices = np.squeeze(np.concatenate(x, axis = -1))
    train_data = data.iloc[indices, :].reset_index(drop=True)
    
    scaler = StandardScaler(with_mean=True,
                                with_std=True,
                                copy=False).fit(train_data.iloc[:, :dims])
    
    scaled = scaler.transform(data.iloc[:,:dims])
    normalized = pd.DataFrame(scaled)
    normalized['stimulus'], normalized['repetition'] = data['stimulus'], data['repetition']

    return normalized
    
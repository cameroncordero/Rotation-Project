import pandas as pd
import sys
import scipy
import statsmodels.api as sm
def RegressionAnalysis(OutputFile: str):
    with open('Normalized_Linear_Regression_'+OutputFile, 'r') as data:
        df = pd.read_csv(data)
        countDict = {}
        xdf = df.drop(columns=['context','frequency'])
        ydf = df.frequency
        for column in xdf:
            rValue, _ = scipy.stats.pearsonr(xdf[column], df.frequency)
            countDict[column] = rValue
        i = 0
        fivePrimeDict = {}
        threePrimeDict = {}
        for key, value in countDict.items():
            if i < 4:
                fivePrimeDict[key] = value
                i += 1
            else:
                threePrimeDict[key] = value
        threeDrop = (min(threePrimeDict, key = lambda dictionaryKey: abs(threePrimeDict.get(dictionaryKey))))
        fiveDrop = (min(fivePrimeDict, key = lambda dictionaryKey: abs(fivePrimeDict.get(dictionaryKey))))
        Adi = df.drop(columns=['context', 'frequency', str(threeDrop), str(fiveDrop)])
        X2 = sm.add_constant(Adi)
        est = sm.OLS(ydf,X2).fit()
        with open ('Regression_Results_'+OutputFile[:-3]+'.txt', 'w') as file:
            sys.stdout = file
            print(est.summary())
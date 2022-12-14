import pandas as pd
import numpy as np
def load_and_process(csv):
    data=pd.read_csv(csv)
#Drop Unwanted Columns
    df1 = (pd.DataFrame(data)
           .drop('DemoCount',axis=1)
           .drop('Reviews',axis=1)
           .drop('Website',axis=1)
           .drop('HeaderImage',axis=1)
           .drop('DRMNotice',axis=1)
           .drop('DLCCount',axis=1)
           .drop('DeveloperCount',axis=1)
           .drop('LegalNotice',axis=1)
           .drop('ExtUserAcctNotice',axis=1)
           .drop('MovieCount',axis=1)
           .drop('RequiredAge',axis=1)
           .drop('PublisherCount',axis=1)
           .drop('ScreenshotCount',axis=1)
           .drop('Background',axis=1)
           .drop('AboutText',axis=1)
           .drop('ShortDescrip',axis=1)
           .drop('DetailedDescrip',axis=1)
           .drop('SupportEmail',axis=1)
           .drop('SupportURL',axis=1)
           .drop('SupportedLanguages',axis=1)
           .drop('PriceCurrency',axis=1)
           .drop('LinuxMinReqsText',axis=1)
           .drop('LinuxRecReqsText',axis=1)
           .drop('PCRecReqsText',axis=1)
           .drop('PCMinReqsText',axis=1)
           .drop('MacMinReqsText',axis=1)
           .drop('MacRecReqsText',axis=1)
           .drop('PackageCount',axis=1)
           .drop('SteamSpyOwnersVariance',axis=1)
           .drop('SteamSpyPlayersVariance',axis=1)
           .drop('AchievementCount',axis=1)
           .drop('AchievementHighlightedCount',axis=1)
           .drop('ControllerSupport',axis=1)
           .drop('SteamSpyPlayersEstimate',axis=1)
           .drop('FreeVerAvail',axis=1)
           .drop('PurchaseAvail',axis=1)
           .drop('SubscriptionAvail',axis=1)
           .drop('PlatformWindows',axis=1)
           .drop('PlatformLinux',axis=1)
           .drop('PlatformMac',axis=1)
           .drop('PCReqsHaveMin',axis=1)
           .drop('PCReqsHaveRec',axis=1)
           .drop('LinuxReqsHaveMin',axis=1)
           .drop('LinuxReqsHaveRec',axis=1)
           .drop('MacReqsHaveMin',axis=1)
           .drop('MacReqsHaveRec',axis=1)
           .drop('CategorySinglePlayer',axis=1)
           .drop('CategoryMultiplayer',axis=1)
           .drop('CategoryCoop',axis=1)
           .drop('CategoryMMO',axis=1)
           .drop('CategoryInAppPurchase',axis=1)
           .drop('CategoryIncludeSrcSDK',axis=1)
           .drop('CategoryIncludeLevelEditor',axis=1)
           .drop('CategoryVRSupport',axis=1)
           .drop('GenreIsNonGame',axis=1)
           .drop('QueryName',axis=1)
           .drop('QueryID',axis=1)
           .drop('ResponseID',axis=1)
           .drop('IsFree',axis=1))
    #Rename
    df2=(df1.rename(columns={"Metacritic":"Rating"}).rename(columns={"SteamSpyOwners":"Owners"}).rename(columns={"RecommendationCount":"Recommendations"}).rename(columns={"ResponseName":"Games"}))
    
    return df2
def Column_var_sort(df,col,up_down):
    df1=(df.sort_values(col,ascending=up_down))
    return df1
def Rating_Sort(df,val):
    d2=df.loc[lambda x: x['Rating']>val]
    return d2
def boolean_to_inta(df):
    df=df*1
    return df

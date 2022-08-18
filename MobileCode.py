import pandas as pd
c1= pd.read_csv('mobile_price_train.csv')              #to read the dataset file

c1 = c1.drop(columns = ['blue','fc','m_dep','sc_w','sc_h','pc','clock_speed','mobile_wt','px_height','px_width','talk_time'])    #to drop columns


x = c1.iloc[:,:-1]      #dividing dependent and independnt variable
y = c1['price_range']    


from sklearn.preprocessing import StandardScaler
sc = StandardScaler() 
x = sc.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state= 0)

from sklearn.ensemble import RandomForestClassifier   
reg = RandomForestClassifier()
reg.fit(x_train,y_train)

y_pred= reg.predict(x_test)

#to calculate accuracy
from sklearn.metrics import r2_score
print (r2_score(y_test,y_pred))


#to dump and load
from joblib import dump,load
dump(sc,"scaler.joblib")
dump(reg,"regress.joblib")

    
    
    

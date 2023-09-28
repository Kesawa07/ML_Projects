from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def SmokerPrediction(req):
    data=pd.read_csv("C:\\Users\\kcrkr\\Desktop\\K C Rushi Kesawa Reddy_HKBKCollege\\Project1_SmokerStatusPrediction(Machine Learning)\\SmokerStatusPrediction_CODE\\train_dataset.csv")
    inputs = data.drop(['smoking'],'columns')
    output = data.drop(['age','height(cm)','weight(kg)','waist(cm)','eyesight(left)','eyesight(right)','hearing(left)','hearing(right)','systolic','relaxation','fasting blood sugar','Cholesterol','triglyceride','HDL','LDL','hemoglobin','Urine protein','serum creatinine','AST','ALT','Gtp','dental caries'],'columns')
    x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.75)
    sc=StandardScaler()
    x_train=sc.fit_transform(x_train)
    x_test=sc.transform(x_test)
    if(req.method=="POST"):
        data=req.POST
        age=data.get('age')
        height=data.get('height')
        weight=data.get('weight')
        waist=data.get('waist')
        eyeleft=data.get('eyeleft')
        eyeright=data.get('eyeright')
        hearleft=data.get('hearleft')
        hearright=data.get('hearright')
        systolic=data.get('systolic')
        relax=data.get('relaxation')
        fbs=data.get('fbs')
        choles=data.get('cholesterol')
        trigly=data.get('triglyceride')
        hdl=data.get('hdl')
        ldl=data.get('ldl')
        hemo=data.get('hemoglobin')
        uprotein=data.get('uprotein')
        serum=data.get('serum')
        ast=data.get('ast')
        alt=data.get('alt')
        gtp=data.get('gtp')
        dental=data.get('dental')
        if len(age) < 1 or len(height) < 1 or len(weight) < 1 or len(waist) < 1 or len(eyeleft) < 1 or len(eyeright) < 1 or len(hearleft) < 1 or len(hearright) < 1 or len(systolic) < 1 or len(relax) < 1 or len(fbs) < 1 or len(choles) < 1 or len(trigly) < 1 or len(hdl) < 1 or len(ldl) < 1 or len(hemo) < 1 or len(uprotein) < 1 or len(serum) < 1 or len(ast) < 1 or len(alt) < 1 or len(gtp) < 1 or len(dental) < 1 :
            res="Plaease Enter data In All Fields"
            return render(req,'SmokerPrediction.html',context={'result':res})
        if('prdct' in req.POST):
            model=LogisticRegression()
            model.fit(x_train,y_train)
            res=model.predict([[int(age),int(height),int(weight),float(waist),float(eyeleft),float(eyeright),int(hearleft),int(hearright),int(systolic),int(relax),int(fbs),int(choles),int(trigly),int(hdl),int(ldl),float(hemo),int(uprotein),float(serum),int(ast),int(alt),int(gtp),int(dental)]])
            if(res==1):
                result="Smoker"
            else:
                result="Not A Smoker"
            return render(req,'SmokerPrediction.html',context={'result':result})
    return render(req,'SmokerPrediction.html')
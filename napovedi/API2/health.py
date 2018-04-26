max_age = 13

#ta bo napovedal trebusnjake

def csv_to_DataFrame(path):
    import pandas as pd
    return pd.read_csv(path, sep=",", encoding="utf_8", na_values=" ")


def prepare_data(df, age, target_year, columns,T):
    """Filters DataFrame by columns specificated untill age as X and ATT_18 as Y."""
    columns_yr = [col + '_' + str(i) for col in columns for i in range(6, age + 1)]
    X = df[columns_yr]
    Y = df[T + str(target_year)]
    return X, Y


def prepare_data_multi_y(df, max_age, target_year, columns,T):
    """Filters DataFrame by columns specificated untill age as X and ATT_18 as Y."""
    columns_x = [col + '_' + str(i) for col in columns for i in range(6, max_age + 1)]
    X = df[columns_x].copy()
    columns_y = [T+'_' + str(i) for i in range(max_age + 1, target_year + 1)]
    Y = df[columns_y].copy()
    return X, Y


#########################
def prepare_data_multiX(df, max_age,columns):
    """Filters DataFrame by columns specificated untill age as X and ATT_18 as Y."""
    columns_x = [col +'_' + str(i) for col in columns for i in range(6, max_age + 1)]
    X = df[columns_x].copy()
    from sklearn.preprocessing import StandardScaler
    return StandardScaler().fit(X)



def linreg_multi_GUI(df, max_age, target_year, columns,T):
    X, y = prepare_data_multi_y(df, max_age, target_year, columns,T)
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler().fit(X)
    X_scaled = scaler.transform(X)

    # makes linear regression model
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_scaled, y)

    return (model, scaler)


def predict_GUI(model, scaler, person, max_age, target_year, columns, T,multi=True):
    if multi:
        X_person, y_person = prepare_data_multi_y(person, max_age, target_year, columns,T)
        y_predicted = model.predict(scaler.transform(X_person))
        return (y_predicted[0], y_person.values[0])  # returns predicted value and the real value of att at age of 18
    else:
        X_person, y_person = prepare_data(person, max_age, target_year, [T])
        y_predicted = model.predict(scaler.transform(X_person))

        return (
        float(y_predicted), float(y_person.values))  # returns predicted value and the real value of att at age of 18
def izpisi2(T="DT",identiteta=""):

    path_train = "GUI_train_set.csv"
    path_test = "GUI_test_set.csv"
    data_train = csv_to_DataFrame(path_train)
    data_test = csv_to_DataFrame(path_test)
    person = data_test.sample()
    model, scalar = linreg_multi_GUI(data_train, max_age, 18, [T],T)
    if identiteta=="":
        person = data_test.sample()
    else:

        for x in data_test['index'].keys():
            a = int(data_test['index'][x])
            b = int(identiteta)
            if a==b:
                person=data_test.loc[data_test['index'] == data_test['index'][x]]
    predicted_y, real_y = predict_GUI(model, scalar, person, max_age, 18, [T],T, multi=True)

    dataa=[]
    X=[]
    Y=[]
    Z=[]
    for age in range(6,max_age+1):
        att=T+"_"
        real=int(person[att+str(age)])
        Z.append(age)
        X.append(real)
        Y.append(real)

    for age, predicted, real in list(zip(list(range(max_age + 1, 19)), predicted_y, real_y)):
        Z.append(age)
        X.append(predicted)
        Y.append(real)


    return [X,Y,Z]

def izpisi(T="DT",identiteta=""):
    if len(T)==0:
        T="DT"
    [X,Y,Z]=izpisi2(T,identiteta)
    A=[]
    if T=="ATT" or T=="ATV":
        for i in range(len(X)):
            X[i]=X[i]/10
            Y[i]=Y[i]/10
    for i in range(len(X)):
        A.append([X[i],Y[i]])
    return A


def izpisi_bmi(identiteta=""):
    visina=izpisi("ATT",identiteta)
    teza=izpisi("ATV",identiteta)
    bmi=[]
    for i in range(len(visina)):
        bmi.append([100*teza[i][0]/(visina[i][0]**2),100*teza[i][1]/(visina[i][1]**2)])

    return bmi


def bmi_risk(bmi):

    if 15<=bmi and bmi <18.5:
        # prvo je tvegajnje za moske  drugo za zenske
        return 82

    elif 18.5<=bmi and bmi <20:
        # prvo je tvegajnje za moske  drugo za zenske
        return 44
    elif 20<=bmi and bmi <22.5:
        # prvo je tvegajnje za moske  drugo za zenske
        return 2
    elif 22.5<=bmi and bmi <25:
        # prvo je tvegajnje za moske  drugo za zenske
        return 0
    elif 25<=bmi and bmi <27.5:
        # prvo je tvegajnje za moske  drugo za zenske
        return 7
    elif 27.5<=bmi and bmi <30:
        # prvo je tvegajnje za moske  drugo za zenske
        return 27
    elif 30<=bmi and bmi <35:
        # prvo je tvegajnje za moske  drugo za zenske
        return 66
    else:
        return 100


def sit_up_risk(trebusnjaki):
    if 75 < trebusnjaki and trebusnjaki <= 100:
        return 0,

    elif 50 < trebusnjaki and trebusnjaki <= 75:
        return 13

    elif 25 < trebusnjaki and trebusnjaki <= 75:
        return 0
    elif 0 < trebusnjaki and trebusnjaki <= 25:
        return 172
    else:
        return -1



def running_percentil(x):
    path_train = "GUI_train_set.csv"
    path_test = "GUI_train_set.csv"

    data_train = csv_to_DataFrame(path_train)
    data_test = csv_to_DataFrame(path_test)

    manjsi=0
    vsi=0

    #data_test['T600_18']

    for y in data_test['T600_18']:
        if x<int(y):
            manjsi+=1
        vsi+=1
    print("tek")
    print(x)
    print(manjsi)
    print(vsi)
    print(100*(manjsi/vsi))
    print("hoja")

    return 100*(manjsi/vsi)




def running_risk2(tek):
    if 80 < tek and tek <= 100:
        return 0

    elif 60 < tek and tek <= 80:
        return 28

    elif 40 < tek and tek <= 60:
        return 59
    elif 20 < tek and tek <= 40:
        return 78
    elif 0 < tek and tek <= 20:
        return 85
    else:
        return 100

def running_risk(tek):
    percentil=running_percentil(tek)
    return running_risk2(percentil)




def risk_index(indeks='1902'):

    data=[]

    bmi=izpisi_bmi(indeks)

    bmi=bmi[-1][1]
    bmi=bmi*10

    bmi=bmi_risk(bmi)
    tek=izpisi("T600",indeks)[-1][1]
    tek=running_risk(tek)

    sit=izpisi("DT",indeks)[-1][1]
    sit=sit_up_risk(sit)


    data.append(["obescity",bmi])
    data.append(["Cardiorespioatory fitness",tek])
    data.append(["Muscle fitness",sit])


    return data
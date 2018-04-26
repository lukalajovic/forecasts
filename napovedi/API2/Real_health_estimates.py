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


####################
# Test







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
        for x in data_test['identity'].keys():
            if data_test['identity'][x]==identiteta:
                person=data_test.loc[data_test['identity']==identiteta]
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
    [X,Y,Z]=izpisi2(T,identiteta)
    A=[]
    if T=="ATT":
        for i in range(len(X)):
            X[i]=X[i]/10
            Y[i]=Y[i]/10
    for i in range(len(X)):
        A.append([X[i],Y[i]])
    return A


def izpisi_vse(identiteta=""):
    vse=["ATV","ATT","AKG","DPR","SDM","PON","DT","PRE","VZG","T60","T600"]
    if identiteta=="":
        path_test = "GUI_test_set.csv"
        data_test = csv_to_DataFrame(path_test)
        per = data_test.sample()
        identiteta=str(per['identity'])

    slovar = {}
    for x in vse:
        slovar[x]=izpisi(x,identiteta)

    return slovar

def izpisi_bmi(identiteta=""):
    visina=izpisi("ATT",identiteta)
    teza=izpisi("ATV",identiteta)
    bmi=[]
    for i in range(len(visina)):
        bmi.append([100*teza[i][0]/(visina[i][0]**2),100*teza[i][1]/(visina[i][1]**2)])

    return bmi

def izpisi_test2():
    path_train = "GUI_train_set.csv"
    path_test = "GUI_test_set.csv"

    data_train = csv_to_DataFrame(path_train)
    data_test = csv_to_DataFrame(path_test)


    return data_test



def izpisiPoljubno(T,rand_person,data_train):
    model, scalar = linreg_multi_GUI(data_train, max_age, 18, [T], T)

    #rand_person = data_test.sample()
    predicted_y, real_y = predict_GUI(model, scalar, rand_person, max_age, 18, [T], T, multi=True)
    dataa = []
    X = []
    Y = []
    Z = []

    for age in range(6, max_age + 1):
        att = T + "_"
        real = int(rand_person[att + str(age)])
        Z.append(age)
        X.append(real)
        Y.append(real)

    for age, predicted, real in list(zip(list(range(max_age + 1, 19)), predicted_y, real_y)):

        Z.append(age)
        X.append(predicted)
        Y.append(real)

    return [X, Y, Z]














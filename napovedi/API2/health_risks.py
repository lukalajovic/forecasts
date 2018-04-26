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


    return 100*(manjsi/vsi)

#print(running_percentil()


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
        return -1

def running_risk(tek):
    percentil=running_percentil(tek)
    return running_risk2(percentil)


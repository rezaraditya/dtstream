# NAMA : REZA RADITYA
# NIM : 231352004

<body>



# Link Data
<div class = "linkdata">

link file keseluruhan: https://github.com/rezaraditya/dtstream/tree/main/Industrial-Copper-Modeling-Project-main/Industrial-Copper-Modeling-Project-main
<br>

link ipynb: https://github.com/rezaraditya/dtstream/blob/main/Industrial-Copper-Modeling-Project-main/Industrial-Copper-Modeling-Project-main/EDA_COPPER.ipynb
</div>

## 1. Pendahuluan
<h4>Proyek ini bertujuan untuk mengembangkan dua model pembelajaran mesin untuk industri tembaga guna mengatasi tantangan dalam memprediksi harga jual dan klasifikasi timbal. Prediksi manual dapat memakan waktu dan mungkin tidak menghasilkan keputusan penetapan harga yang optimal atau menangkap prospek secara akurat. Model-model tersebut akan menggunakan teknik-teknik canggih seperti normalisasi data, deteksi dan penanganan outlier, penanganan data dalam format yang salah, identifikasi distribusi fitur, dan pemanfaatan model berbasis pohon, khususnya algoritma pohon keputusan, untuk memprediksi harga jual dan prospek secara akurat. .
</h4>

## 2. Data Exploration
<h4>Adapun EDA decision tree ditampilkan sebagai berikut : </h4>

<div class = "hasil">
Accuracy: 0.912118593365685
Confusion Matrix:
[[ 5692  1310]
 [ 1334 21750]]

Confusion Matrix:
[[ 5692  1310]
 [ 1334 21750]]
<br>


<div class = "classification">

<h3> Classification Report : </h3>

</div>

<br>

              precision    recall  f1-score   support

           0       0.81      0.81      0.81      7002
           1       0.94      0.94      0.94     23084

    accuracy                           0.91     30086
   macro avg       0.88      0.88      0.88     30086
weighted avg       0.91      0.91      0.91     30086
<br><br><br>
=![image](image.png)

</div>

## 3. Data_Preprocessing

###  IMPORT LIBRARY

 
<div class = "kata">
<p>import warnings</p>
<p >warnings.filterwarnings("ignore")</p> 

<p>import pandas as pd</p>
</div>

###  Read the CSV file into a pandas dataframe
<h5>df = pd.read_csv</h5> 
<br><p class = "hasil">(r"C:\Users\91939\OneDrive\Desktop\Copper_P4\DATASET\INDUSTRY_COPPER.csv")
df.head(2) 
</p>

<div>
<style scoped>
    .dataframe{
        border-collapse: collapse;
    }
    .dataframe  tr th {
        background : yellow;
       }
    .dataframe tr td{
        background : blue;
    }
    .dataframe tbody tr th {
        vertical-align: middle;
        background: blue;
        }
    .dataframe tbody tr th  {
        vertical-align: top;
        background: "yellow";
        }
    .dataframe thead tr th td {
        text-align: center;
        background: "blue";   
    }
</style>
<table  class="dataframe">
  <thead border=4>
    <tr style="text-align: center;">
      <th></th>
      <th>id</th>
      <th>item_date</th>
      <th>quantity tons</th>
      <th>customer</th>
      <th>country</th>
      <th>status</th>
      <th>item type</th>
      <th>application</th>
      <th>thickness</th>
      <th>width</th>
      <th>material_ref</th>
      <th>product_ref</th>
      <th>delivery date</th>
      <th>selling_price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>EC06F063-9DF0-440C-8764-0B0C05A4F6AE</td>
      <td>20210401.0</td>
      <td>54.151139</td>
      <td>30156308.0</td>
      <td>28.0</td>
      <td>Won</td>
      <td>W</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>1500.0</td>
      <td>DEQ1 S460MC</td>
      <td>1670798778</td>
      <td>20210701.0</td>
      <td>854.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4E5F4B3D-DDDF-499D-AFDE-A3227EC49425</td>
      <td>20210401.0</td>
      <td>768.024839</td>
      <td>30202938.0</td>
      <td>25.0</td>
      <td>Won</td>
      <td>W</td>
      <td>41.0</td>
      <td>0.8</td>
      <td>1210.0</td>
      <td>0000000000000000000000000000000000104991</td>
      <td>1668701718</td>
      <td>20210401.0</td>
      <td>1047.0</td>
    </tr>
  </tbody>
</table>
</div>
<div>

### print len
![print](image-1.png)

### null values, shape and data types before dealing with incorrect data 
![null value](image-2.png)
### liat info
![liat info](image-3.png)

## Dealing with data in wrong format
<h4> 

![dealing with data in wrong data format](image-4.png)

</h4>
### Nan values and shape after dealing with data in wrong format
<h4>

![nan value and shape 1](image-5.png)
<br>
</h4>

<h4>

![nan value and shape 2](image-6.png)
</h4>

### Dealing with Missing Values
<h4>

![Dealing with Missing Values](image-7.png)

</h4>

![copy](image-8.png)

### PLOTTING
![plt1](image-9.png)
<br>

![qt](image-10.png)

<br>
<div class = "deret">

![ct](image-11.png)
![app](image-12.png)
![thick](image-13.png)
![wid](image-14.png)
![sp](image-15.png)

</div>

![np](image-16.png)
<br>

![dfp](image-17.png)

<br>

![dropna](image-18.png)

<br>

![distplot](image-19.png)

<br>

![splog](image-20.png)

<br>

![qtlog](image-21.png)

<br>

![thlog](image-22.png)

<br>

![dfhead](image-23.png)

<br>

![dfsns](image-24.png)

<br>

![subplotaxes](image-25.png)

<br>

## DECISION TREE REGRESSOR 

   #### 1 Encode categorical features
   #### 2 Test and Train split
   #### 3 Define Hyperparameters for GridSearchCV
   #### 4 Train the DecisionTreeRegressor with best parameters
   #### 5 Evalution metrics
   #### 6 Predict the selling price for new values
   #### 7 Save the DecisionTreeRegressor model

   ![eef1](image-26.png)
   ![eef2](image-27.png)
  ![hsl](image-28.png)
   <br>

   ![srch](image-29.png)
   <br>

   ![src2](image-30.png)

   <br>

  ### saving model

   ![svmodel](image-31.png)
  
  <br>

  ![printlen](image-32.png)
  
  <br>

  ![dfc](image-33.png)

## DECISION TREE CLASSIFIER
<br>

![dtc1](image-34.png)

<br>

![dtc2](image-35.png)

<br>

![dtc3](image-36.png)

<br>

![dtc4](image-37.png)

<br>

#### save model

![svmod](image-38.png)

# STREAMLIT
link : https://dtstream-6rczlw6dreju4mvcuosj5x.streamlit.app/

</body>
<style>
body{
  background : #4329;
  }

.kata{
    background-color : purple;
    border-radius : 3px solid white;
}
p{
    color : yellow;
    font-size: 10pt;
    font-weight: 2rem;
    border-radius : 2px solid black;
    -color: blue;
}
.hasil{
    color: yellow;
    background: black;
    border-radius: 3px solid white;
    padding: 10px 10px;
}
.deret{
  margin: 10px;
}
.classification h3{
  color: white;
  text-transform: uppercase;
}
.linkdata{
  font-size: 14pt;
  color: blue;
}
</style>

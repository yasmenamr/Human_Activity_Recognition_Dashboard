# Human Activity Recognition Dashboard


![dashboard](https://images.unsplash.com/photo-1520895653685-c739b6db8fce?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=4800')


A dashboard that recognize the human activity based on readings from sensor data.

## Usage and installation

1.Create and activate a virtual environment

```bash
$python -m venv venv
$source venv/bin/activate
```

2.Install all the requirements

```bash
$pip install -r requirements.txt
```

3.If you want to retrain our model
```bash
$train app.py
```

4.Run the app

```bash
$python app.py
```

##How o use Dashboard:

the Dashboard view:
![dashbroad2](Human_Activity_Recognition/Images/DashboardJPG.JPG)

Enter your data :

1.the length of data must be = 562 like the dataset

2.the data must be seperated by comma ','.

-Example of data you can Enter => 0.9253,0.3256,.....,0.256,'1' 

![walking](Human_Activity_Recognition/Images/walking.JPG)


##How to use my Dashboard with a gif:

![walking](Human_Activity_Recognition/Images/my-project-gif.gif)
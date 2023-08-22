## Reatil Store Object Detection Using Deep Learning Algorithm (YOLO) and IOT

This program allows you to read item count within a specific boundary in real time , if the item count is zero for a set amount of time , a simple notification pops up in the form of a html file.

![Within redbox counts items](image.png)

![Notification](image-1.png)


The model used here to train the data is YOLOv8. We have used a pretrained model that identifies all items, but if you need to add your own model that identifies specific items you can do so by changing "items.pt"  in line 56 within main.py. you can try so by by replacing "items.pt" using our candp.pt,candp2.pt or colddrinks.pt which identifies cold beverages.

![in main.py ->  Line56 : change .ptfile](image-4.png)

## Flowchart


![IMG_1912 (2)](https://github.com/FozanAzhar/InventoryYOLO-IOT/assets/95569589/8779a280-19bb-4c84-a7b6-1b7d886faee4)


Before running main.py be sure to install all the necessary libraries in your terminal , you can run the following commands in the termnal to install the necessary libraries. 

pip install numpy

pip install supervision

pip install ultralytics

pip install cv 

You also need to change the address to the relevant address for "manager.html"

![in main.py -> Line 14: change address of manager.html of your directory](image-3.png)

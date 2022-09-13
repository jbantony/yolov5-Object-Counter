### Notes for Running this detection

##### Use the flags

--nosave            : Not to save the recorded video while feeding from Webcam
--line-thickness    : Keep clean bounding boxes use 1
--source 0          : To read from WEbCam

##### Optional for Good results
--imgsz             : To get more accurate results, use imgsz 800

--print_class       : To print the number of detected objects in the frame for the given class
--print_all         : To print all the detected classes in the image, default false


Example Usage

python detect.py --source 0 --imgsz 800 --line-thickness 1 --print_class person --nosave

or

python detect.py --source 0 --line-thickness 1 --print_all --nosave

###### Quit the running

Quit using STRG + C while running.
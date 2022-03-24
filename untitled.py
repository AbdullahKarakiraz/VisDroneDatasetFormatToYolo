import os
import glob
import cv2
# index0: x coordinat, index1: y coordinat, index2: widht, index3: height, index5: category 
annotations_path = glob.glob("path*.txt")

imageFileName = "images"
jpg = "jpg"

def convert_x(bbox_left,image_width,box_xmax):
	image_width = 1.0 * int(image_width)
	absolute_x = int(bbox_left) + 0.5 * (int(box_xmax) - int(bbox_left))
	x = absolute_x / image_width
	return str(round(x,6))

	

def convert_y(image_height,box_ymax,bbox_top):
	image_height = 1.0 * int(image_height)
	absolute_y = int(bbox_top) + 0.5 * (int(box_ymax) - int(bbox_top))
	y = absolute_y / image_height
	return str(round(y,6))

def convert_width(box_xmax,bbox_left,image_width): 
	absolute_width = int(box_xmax) - int(bbox_left)
	image_width = 1.0 * int(image_width)
	width = absolute_width / image_width 
	return str(round(width,6))


def convert_height(bbox_top,box_ymax,image_height):
	absolute_height = int(box_ymax) - int(bbox_top)
	image_height = 1.0 * int(image_height)
	height = absolute_height / image_height
	return str(round(height,6))

for path in annotations_path[0:548]:
    
    temp_path = path.replace("annotations",imageFileName)
    temp_path = temp_path.replace("txt",jpg)
    (h,w) = cv2.imread(temp_path).shape[:2]
    k = path
    fileName = os.path.split(path)[1]
    
    with open(path,"r") as f:
        temp = [line.strip().strip() for line in f.readlines()]
        annotions_yolo_format = []
        
        writeYoloFormat = []
        for bbox in temp:
            
            temp2 = list(map(int,bbox.split(",")))
            annotions_yolo_format.append(temp2)
        for element in annotions_yolo_format:
            writeLine = []
            bbox_left = element[0]
            bbox_top = element[1]
            bbox_width = element[2]
            bbox_height = element[3]
            box_xmax = int(element[0]) + int(element[2])
            box_ymax = int(element[1]) + int(element[3])
            writeLine.append(element[5])
            writeLine.append(convert_x(bbox_left,w,box_xmax))
            writeLine.append(convert_y(h,box_ymax,bbox_top))
            writeLine.append(convert_width(box_xmax,bbox_left,w))
            writeLine.append(convert_height(bbox_top,box_ymax,h))
            writeYoloFormat.append(writeLine)
        with open(fileName,"w") as f:
            for bbox in writeYoloFormat:
                f.write(" ".join(str(i) for i in bbox)+"\n")

          
            
    

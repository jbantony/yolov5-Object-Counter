"""
visualising the results as text
"""


import cv2

def visualiseCountSpecific(found_classes, image, object_class):
    """
    To print the total number of detected "object_class" in the visualising image
    """
    aligns = image.shape
    align_bottom = aligns[0]-10
    align_right= (aligns[1]/1.7)

    for i, (k, v) in enumerate(found_classes.items()):
        #a=f" {k} = {v}"
        #align_bottom= align_bottom - 35
        #cv2.putText(image, str(a), (int(align_right), align_bottom), cv2.FONT_HERSHEY_SIMPLEX, 1, (45,255,255), 1, cv2.LINE_AA)
        if k == object_class:
            a = f"{object_class}s = {v}"
            #align_bottom= align_bottom - 35
            cv2.putText(image, str(a), (int(align_right), align_bottom), cv2.FONT_HERSHEY_SIMPLEX, 1, (45,255,255), 1, cv2.LINE_AA)



def printAllClasses(found_classes, image):
    """
    To print all the detected classes in the image
    """
    aligns = image.shape
    align_bottom = aligns[0]-5
    align_right= (aligns[1]/1.7)

    for i, (k, v) in enumerate(found_classes.items()):
        a=f" {k} = {v}"
        align_bottom= align_bottom - 35
        cv2.putText(image, str(a), (int(align_right), align_bottom), cv2.FONT_HERSHEY_SIMPLEX, 1, (45,255,255), 1, cv2.LINE_AA)
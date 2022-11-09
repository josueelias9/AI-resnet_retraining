
# https://detectron2.readthedocs.io/en/latest/modules/structures.html#detectron2.structures.Boxes.area
objects_area = outputs["instances"].pred_boxes.area()

# https://detectron2.readthedocs.io/en/latest/modules/structures.html#detectron2.structures.Boxes.tensor
objects_coor = outputs["instances"].pred_boxes.tensor

# https://pytorch.org/docs/stable/generated/torch.Tensor.tolist.html#torch.Tensor.tolist
objects_coor_list = objects_coor.tolist()
objects_area_list = objects_area.tolist()
max_value = max(objects_area_list)
index = objects_area_list.index(max_value)
eee=objects_coor_list[index]

# https://learnopencv.com/cropping-an-image-using-opencv/ 
cv2.imwrite("Cropped_Image.jpg", im[
    int(eee[1]):int(eee[3]), 
    int(eee[0]):int(eee[2])])

im_2 = cv2.imread("./Cropped_Image.jpg")
cv2_imshow(im_2)

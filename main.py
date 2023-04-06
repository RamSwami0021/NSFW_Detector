from nsfw_detector import predict
import openpyxl
import urllib.request

workbook = openpyxl.Workbook()
worksheet = workbook.active

model = predict.load_model("./models/keras_nsfw_mobilenet2.224x224.h5")

# this code for online test data use
# number = int(input("Enter the no of img (1 to 1000) :- "))
# for i in range(1, number):
#     urllib.request.urlretrieve("https://github.com/RamSwami0021/NSFW_Detector/blob/main/test_data/{i}.jpg", "image_{i}.jpg")
#     result = predict.classify(model, "image_{i}.jpg")
#     worksheet.append(result)

# this code for offline test data use

for i in range(1, 1000):
    result = predict.classify(model, "./test_data/{i}.jpg")
    worksheet.append(result)

workbook.save('Final_Result.xlsx')

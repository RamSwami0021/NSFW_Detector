from nsfw_detector import predict
import openpyxl

workbook = openpyxl.Workbook()
worksheet = workbook.active

model = predict.load_model("./models/keras_nsfw_mobilenet2.224x224.h5")


# this code for offline test data use

for i in range(1, 1000):
    result = predict.classify(model, "./test_data/{i}.jpg")
    worksheet.append(result)

workbook.save('Final_Result.xlsx')

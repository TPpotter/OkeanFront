import cv2
from roboflow import Roboflow
import matplotlib.pyplot as plt
data = {
    '0' : 'Леонид Филинов. Доcтуп разрешён',
    '1' : 'Александр Евдокимов. Доступ разрешён',
    '2' : 'Нет в базе данных. Доступ запреещён'
}
rf = Roboflow(api_key="gvepPIkiLWgbCS9hAFWP")
project = rf.workspace("kpop10007").project("faces-2guh1")
model = project.version(5).model
def handel(img_path: str):
    try:
        img = cv2.imread(img_path)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        face = face_classifier.detectMultiScale(
            gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100)
        )
        for (x, y, w, h) in face:
            #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            img = img[y : y + h, x : x+ w]

        res_img = cv2.resize(img, (224, 224))
        res_img = cv2.cvtColor(res_img, cv2.COLOR_BGR2RGB)
        return res_img
    except:
        print('Error')
        return False
def predict(img_path):
    img = handel(img_path)
    if type(img) == bool:
        return 'bad image'
    cv2.imwrite('to_model.jpg', img)
    json_result = model.predict(r'to_model.jpg').json()
    cof = list()
    names = list()
    for i in json_result['predictions'][0]['predictions']:
        names.append(i)
        cof.append(json_result['predictions'][0]['predictions'][i]['confidence'])
    ind = cof.index(max(cof))
    result = data[names[ind]]
    return result
print(*predict(r'oooo.jpg'), sep='\n')
import face_recognition

known_image = face_recognition.load_image_file("imagens/vitinho.jpg")
unknown_image = face_recognition.load_image_file("imagens/unknown.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
arq = open('lista_verificacao.txt','w')
arq.write(str(results))
arq.close()

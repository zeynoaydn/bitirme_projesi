import 'package:bitirme_projesi/background.dart';
import 'package:bitirme_projesi/page_to_edit.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

class imagePicker extends StatefulWidget {
  const imagePicker({Key? key}) : super(key: key);

  @override
  State<imagePicker> createState() => _imagePickerState();
}

class _imagePickerState extends State<imagePicker> {

  void pickImage(BuildContext context) async {
    final XFile? pickedFile = await ImagePicker().pickImage(
      source: ImageSource.gallery,
    );
    if (pickedFile == null) return;
    Navigator.of(context)
        .push(MaterialPageRoute(builder: (_) => PageToEdit(image: pickedFile,camera:pickedFile,))); 
  }

  void pickImageCamera(BuildContext context) async {
    final XFile? pickedFileCamera = await ImagePicker().pickImage(
      source: ImageSource.camera,
    );
    if (pickedFileCamera == null) return;
    Navigator.of(context)
        .push(MaterialPageRoute(builder: (_) => PageToEdit(camera: pickedFileCamera,image: pickedFileCamera,)));
  }
  

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Background(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          InkWell(
            onTap: () {
              pickImage(context);
            },
            child: Container(
              // constraints: BoxConstraints(
              //   minWidth: MediaQuery.of(context).size.width - 125,
              //   minHeight: 50,
              // ),
              width: MediaQuery.of(context).size.width - 125,
              height: 50,
              decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(21),
            boxShadow: const [
              BoxShadow(
                  color: Colors.black26, offset: Offset(0, 4), blurRadius: 5.0)
            ],
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              stops: [0.0, 1.0],
              colors: [
                Colors.purple.shade400,
                Colors.purple.shade200,
              ],
            ),
            color: Colors.deepPurple.shade300,
          ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: const [
                  Icon(
                    Icons.file_open_outlined,
                  ),
                  SizedBox(
                    width: 9,
                  ),
                  Text(
                    'Fotoğraf Arşivi',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                        color: Colors.white,
                        fontSize: 21,
                        fontWeight: FontWeight.w300),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(
            height: 13,
          ),
          InkWell(
            onTap: () {
              pickImageCamera(context);
            },
            child: Container(
              // constraints: BoxConstraints(
              //   minWidth: MediaQuery.of(context).size.width - 125,
              //   minHeight: 50,
              // ),
              width: MediaQuery.of(context).size.width - 125,
              height: 50,
              decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(21),
            boxShadow: const [
              BoxShadow(
                  color: Colors.black26, offset: Offset(0, 4), blurRadius: 5.0)
            ],
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              stops: [0.0, 1.0],
              colors: [
                Colors.purple.shade400,
                Colors.purple.shade200,
              ],
            ),
            color: Colors.deepPurple.shade300,
          ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: const [
                  Icon(
                    Icons.camera_alt_outlined,
                  ),
                  SizedBox(
                    width: 9,
                  ),
                  Text(
                    'Kamera',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                        color: Colors.white,
                        fontSize: 21,
                        fontWeight: FontWeight.w300),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(
            height: 20,
          ),
        ],
      ),
    ));
  }
}


import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:gallery_saver/gallery_saver.dart';
import 'package:http/http.dart' as http;
import 'package:dio/dio.dart';

class PageToEdit extends StatefulWidget {
  PageToEdit({
    Key? key,
    required this.image, required XFile camera, 
  }) : super(key: key);
  late final XFile image;
  late final XFile camera;

  @override
  State<PageToEdit> createState() => _PageToEditState();
}

class _PageToEditState extends State<PageToEdit> {
  bool loading = false;

  void saveImage() async {
    await GallerySaver.saveImage(widget.image.path,
        toDcim: true, albumName: 'Flutter');
    Future.delayed(const Duration(seconds: 2), (() {
      setState(() {
        loading = false;
      });
    }));
  }
  void saveImageCamera() async {
    await GallerySaver.saveImage(widget.camera.path,
        toDcim: true, albumName: 'Flutter');
    Future.delayed(const Duration(seconds: 2), (() {
      setState(() {
        loading = false;
      });
    }));
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: const Color.fromARGB(255, 81, 81, 81),
          elevation: 2,
          actions: [
            InkWell(
              child: button(),
              onTap: () async {
                setState(() {
                  loading = true;
                });
                saveImage();
              },
            ),
          ],
        ),
        body: 
        Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Stack(
              children: [
                Container(
                  height: MediaQuery.of(context).size.height - 140,
                  ),
                Positioned(
                  top: 76.7,
                  left: 70.7,
                  child: SizedBox(
                    height: 390,
                    width: 270,
                    child: Image.file(File(widget.image.path)),
                  ),
                ),
                Positioned(
                    top: 181,
                    left: 115,
                    child: loading
                        ? loadingMethod()
                        : const SizedBox(
                            width: 1,
                            height: 1,
                          ))
              ]),
            Container(
              decoration: const BoxDecoration(
                color: Color.fromARGB(255, 81, 81, 81),
                // gradient: LinearGradient(
                //   colors: [
                //   ]
                // ),
              ),
              child: SizedBox(
                width: double.infinity,
                height: 60,
                child: ListView(
                  scrollDirection: Axis.horizontal,
                  children: [
                    InkWell(
                      onTap: () {
                        debugPrint('deneme');
                      },
                      child: SizedBox(
                          width: 90,
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            crossAxisAlignment: CrossAxisAlignment.center,
                            children: const [
                              // SizedBox(child: Icon(Icons.add,color: Colors.red,)),
                              SizedBox(child: Icon(Icons.add)),
                              SizedBox(child: Text('deneme')),
                            ],
                          )),
                    ),
                  ],
                ),
              ),
            )
          ],
        ));
  }

  Container loadingMethod() {
    return Container(
        padding: EdgeInsets.all(5),
        width: 120,
        height: 80,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(13),
          color: Colors.white.withOpacity(0.5),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: [
            CircularProgressIndicator(
              color: Colors.purple.shade200,
              backgroundColor: Colors.purple.shade400,
              strokeWidth: 4,
            ),
            const Text('Başarıyla İndiriliyor',textAlign:TextAlign.center,),
          ],
        ));
  }

  void _alerDialog() {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text('Download'),
          content: const SingleChildScrollView(
              child: Text('Resim başarıyla indirildi')),
          actions: [
            TextButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                child: const Text('Kapat')),
          ],
        );
      },
    );
  }

  Column button() {
    return Column(
      children: [
        Container(
          alignment: Alignment.center,
          width: 80,
          height: 40,
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(10),
            boxShadow: const [
              BoxShadow(
                  color: Colors.black26, offset: Offset(0, 4), blurRadius: 5.0)
            ],
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              stops: [0.0, 1.0],
              colors: [
                Colors.deepPurple.shade400,
                Colors.deepPurple.shade200,
              ],
            ),
            color: Colors.deepPurple.shade300,
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: const [
              Text(
                'Save',
                textAlign: TextAlign.center,
                style: TextStyle(
                    color: Colors.white,
                    fontSize: 21,
                    fontWeight: FontWeight.w300),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

import 'package:bitirme_projesi/image_picker.dart';
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});
 
  @override
  Widget build(BuildContext context) {
    return  const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: imagePicker(),
    );
  }
}
// class MyApp extends StatelessWidget {
//   const MyApp({super.key});
 
//   @override
//   Widget build(BuildContext context) {
//     return  MaterialApp(
//       debugShowCheckedModeBanner: false,
//       home: Scaffold(
//         body: Center(
//           child: Container(
//             child: Image.network('http://10.0.2.2:5000/getImage/kedi.jpg',
//             width: 270,
//             height: 390,
//             fit: BoxFit.cover,
//             loadingBuilder: (BuildContext context, Widget child, ImageChunkEvent? loadingProgress) {
//               if (loadingProgress == null)
//                 return child;
//               return CircularProgressIndicator(
//                 value: loadingProgress.expectedTotalBytes != null
//                     ? loadingProgress.cumulativeBytesLoaded / loadingProgress.expectedTotalBytes!
//                     : null,
//               );
//             },)
//             ,),),
//       ) ,
//     );
//   }
// }
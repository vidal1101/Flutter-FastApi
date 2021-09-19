import 'package:flutter/material.dart';
import 'package:userapp/src/pages/login.dart';

class MyApp extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home:LoginApp(),
    );
  }
}
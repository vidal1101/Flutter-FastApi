import 'dart:async';
import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:userapp/src/models/model_user.dart';
import 'package:http/http.dart' as http;

class UserProviders{

  String urlApi = "http://192.168.1.100:8000/user/fetchall-usuarios";

  Future<List<UserModel>>  getUser() async {
   /*final url = Uri.https(urlApi , "user/fetchall-usuarios");
    final resp = await http.get(url);*/
    http.Response resp = await http.get(urlApi);
    print("status Code");
    debugPrint(resp.body);
    return [];
  }

}

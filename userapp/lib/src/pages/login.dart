import 'package:flutter/material.dart';
import 'package:userapp/src/widget/color.dart';

class LoginApp extends StatefulWidget {
  @override
  _LoginAppState createState() => _LoginAppState();
}

class _LoginAppState extends State<LoginApp> {
  String _username = "";
  String _password = "";
  Color color1 = HexColor("b74093");

  @override
  Widget build(BuildContext context) {
    var mediaquery = MediaQuery.of(context).size;
    return Scaffold(
      body: loginHead(mediaquery),
    );
  }

  /**
   * 
   */
  Widget loginHead(media) {
    return SingleChildScrollView(
      child: Stack(
        children: <Widget>[
          headColor(),
          Container(
            padding: EdgeInsets.only(left: 40, top: 180, right: 40),
            child: Column(
              children: [
                avatarCircle(),
                textfieldUser(),
                textfielPassword(),
                buttonSession(),
                textRegister()
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget headColor() {
    return Container(
      width: 400,
      height: 240,
      color: color1,
      child: Center(
        child: Text("API Python", 
        style: TextStyle(fontWeight: FontWeight.bold ),),
      ),
    );
  }

  Widget avatarCircle() {
    return Opacity(
      opacity: 0.9,
      alwaysIncludeSemantics: true,
      child: CircleAvatar(
        radius: 60.0,
        backgroundImage: NetworkImage(
            "https://scontent.fsyq1-1.fna.fbcdn.net/v/t1.6435-9/55835972_1809531029153050_4345148121928433664_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=gm9VL0ImbNYAX-IjMSM&tn=RVYM4y5IvA_BjXe4&_nc_ht=scontent.fsyq1-1.fna&oh=4e32215fe8e551d519868d3a49324bec&oe=616D246B"),
      ),
    );
  }

  Widget textfieldUser() {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 15),
      child: TextField(
        keyboardType: TextInputType.text,
        decoration: InputDecoration(
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(25.0),
          ),
          suffixIcon: Icon(Icons.person),
          prefixIcon: Icon(Icons.person_pin),
          labelText: "Usuario",
        ),
        onChanged: (user) {
          setState(() {
            _username = user;
          });
        },
      ),
    );
  }

  Widget textfielPassword() {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 15),
      child: TextField(
        obscureText: true,
        keyboardType: TextInputType.visiblePassword,
        decoration: InputDecoration(
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(25.0),
          ),
          suffixIcon: Icon(Icons.lock_open),
          prefixIcon: Icon(Icons.lock),
          labelText: "Contraseña",
        ),
        onChanged: (pass) {
          setState(() {
            _password = pass;
          });
        },
      ),
    );
  }

  Widget buttonSession() {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 15),
      child: OutlinedButton(
        child: Text("Iniciar"),
        style: OutlinedButton.styleFrom(
          primary: Colors.white,
          backgroundColor: Colors.blue,
          onSurface: Colors.blueAccent,
          side: BorderSide(color: Colors.purpleAccent, width: 1),
          elevation: 15,
          minimumSize: Size(150, 50),
          shadowColor: Colors.purpleAccent,
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
        ),
        onPressed: () {},
      ),
    );
  }

  Widget textRegister() {
    return GestureDetector(
      child: Padding(
        padding: const EdgeInsets.symmetric(vertical: 45),
        child: Center(
          child: Row(
            children: [
              SizedBox(width: 39,),
              Text("No tienes Cuenta?" , style: TextStyle(fontSize: 15),),
              SizedBox(width: 5,),
              Text("REGISTRARSE", style: TextStyle(fontWeight:  FontWeight.bold ),),
            ],
          ),
        ),
      ),
      onTap: (){},
    );
  }
}
